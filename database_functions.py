import sqlite3

from Modules import sqllite

from datetime import datetime


database_path = r"C:\Users\ondrej.rott\Documents\Python\MASO\inventory.db"

# Helper functions
def record_already_exists_check(table_name: str, column_names: list, record_data_for_columns: list):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    # 1. Potreba dynamicky poskladat SQL statement for select query both for columns with some value and for columns with None value.
    
    # Not-Null columns - vybrat pary sloupec:hodnota pro sloupce s nenulovaou hodnotou
    columns_with_values = [column_names[i] for i, value in enumerate(record_data_for_columns) if value is not None]
    not_null_values = [value for i, value in enumerate(record_data_for_columns) if value is not None]

    # Null columns 
    columns_with_null_values = [column_names[i] for i, value in enumerate(record_data_for_columns) if value is None]

    # cast SQL query kde existuje value pro sloupce
    where_sql_statement = "= ? AND ".join([column for column in columns_with_values])+"= ?"

    if None in record_data_for_columns: # This applies only when there are some None values in columns.
    # cast SQL query pro NULL value sloupce
        null_values_sql_part = "IS NULL AND ".join([column for column in columns_with_null_values])+"IS NULL" # We use IS NULL statement to check for None values.
        where_sql_statement = where_sql_statement + " AND " + null_values_sql_part

    # 2. Overit jestli record odpovidajici bodu 1 je uz v tabulce
    cursor.execute(f"SELECT * FROM '{table_name}' WHERE {where_sql_statement}", tuple(not_null_values)) # No need to provide values for None columns (We have IS NULL in statement)
    duplicate_record = cursor.fetchall()
    if duplicate_record:
        return True
    return False
    
# Barcode formatting functions
def format_polozka_id_to_barcode(id: int): # Used for "polozka", "druh" and "typ" tables.
    return str(id).zfill(4) # Item id barcode must be in format: "dddd" examlpe 0001 for id 1, 0014 for id 14. SAME FOR POLOZKA, DRUH AND TYP!

def none_barcode(len_digits: int): # Creates barcode for None value with given len of barcode string. Returns string. Barcode string for None value is "0".
    return str(0).zfill(len_digits) # Fills number of positions to match len digits with zeroes. Example: str(0).zfill(5) → "00000"

# Warehouse backoffice
def create_new_polozka(polozka_name: str): # New "polozka_data" table record.
    database_path = r"C:\Users\ondrej.rott\Documents\Python\MASO\inventory.db"
    table_name = "polozky_data"

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    # First we need to insert new record and only after that we can build id barcode 
    cursor.execute(f"INSERT INTO '{table_name}' (nazev_polozky) VALUES (?)", (polozka_name,))

    # register barcode_id method with SQL - this allows that function to be used with SQL query
    conn.create_function("ID_TO_BARCODE", 1, format_polozka_id_to_barcode)

    # Get id of last inserted record - our jus inserted record
    last_record_id = cursor.lastrowid

    # Build the barcode representation of record id and insert it into new record
    cursor.execute("UPDATE polozky_data SET carovy_kod = ID_TO_BARCODE(id) WHERE id = ?", (last_record_id,))

    # Commint changes to database
    conn.commit()
    conn.close()

def create_new_druh(druh_name: str): # New "druh_data" table record.
    database_path = r"C:\Users\ondrej.rott\Documents\Python\MASO\inventory.db"
    table_name = "druh_data"

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    # First we need to insert new record and only after that we can build id barcode 
    cursor.execute(f"INSERT INTO '{table_name}' (nazev_druh) VALUES (?)", (druh_name,))

    # register barcode_id method with SQL - this allows that function to be used with SQL query
    conn.create_function("ID_TO_BARCODE", 1, format_polozka_id_to_barcode)

    # Get id of last inserted record - our jus inserted record
    last_record_id = cursor.lastrowid

    # Build the barcode representation of record id and insert it into new record
    cursor.execute("UPDATE druh_data SET carovy_kod = ID_TO_BARCODE(id) WHERE id = ?", (last_record_id,))

    # Commint changes to database
    conn.commit()
    conn.close()

def create_new_typ(typ_name: str): # New "typ_data" table record.
    database_path = r"C:\Users\ondrej.rott\Documents\Python\MASO\inventory.db"
    table_name = "typ_data"

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    # First we need to insert new record and only after that we can build id barcode 
    cursor.execute(f"INSERT INTO '{table_name}' (nazev_typ) VALUES (?)", (typ_name,))

    # register barcode_id method with SQL - this allows that function to be used with SQL query
    conn.create_function("ID_TO_BARCODE", 1, format_polozka_id_to_barcode)

    # Get id of last inserted record - our jus inserted record
    last_record_id = cursor.lastrowid

    # Build the barcode representation of record id and insert it into new record
    cursor.execute("UPDATE typ_data SET carovy_kod = ID_TO_BARCODE(id) WHERE id = ?", (last_record_id,))

    # Commint changes to database
    conn.commit()
    conn.close()    

def create_new_jednotka(jednotky_name: str, popis: str=None ): # New "jednotky" table record.
    database_path = r"C:\Users\ondrej.rott\Documents\Python\MASO\inventory.db"
    table_name = "jednotky"

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO '{table_name}' (jednotky, popis) VALUES (?,?)", (jednotky_name, popis))

    # Commint changes to database
    conn.commit()
    conn.close() 

# Pricing backoffice
def create_new_price_record(produkt_id: int, cena_czk: float): # creates new price history line in table "historie_cen".
    # creates new price history line in table "historie_cen".
    database_path = r"C:\Users\ondrej.rott\Documents\Python\MASO\inventory.db"
    table_name = "historie_cen"

    todays_date = datetime.today().date()
    cena_czk_2_decimals = round(cena_czk, 2)

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO '{table_name}' (produkt_id, cena_czk, datum_vytvoreni_zaznamu) VALUES (?,?,?)", (produkt_id, cena_czk_2_decimals, str(todays_date)))

    # Commint changes to database
    conn.commit()
    conn.close() 


def create_new_product(polozka_id: int, jednotky_id: int, druh_id: int=None, typ_id: int=None, cena_czk: float=0): 
    # Builds new product record by combining polozka + druh + typ. Combines name + barcodes. Saves price to pricebook table if providesd
    
    # 1st Build the product based on components selected by user.
    database_path = r"C:\Users\ondrej.rott\Documents\Python\MASO\inventory.db"
    table_name = "produkty"

    # get relevant records for component
    polozka_record = sqllite.get_specific_record(database_path, "polozky_data", ["id"], [polozka_id])
    jednotky_record = sqllite.get_specific_record(database_path, "jednotky", ["id"], [jednotky_id])
    druh_record = sqllite.get_specific_record(database_path, "druh_data", ["id"], [druh_id])
    typ_record = sqllite.get_specific_record(database_path, "typ_data", ["id"], [typ_id])
    cena_czk_2_decimals = round(cena_czk, 2)

    # extract relevant data; returned record structure: [(rowid, id, barcode, name)] 
    polozka_name = polozka_record[0][3] 
    polozka_barcode = polozka_record[0][2]

    druh_name = druh_record[0][3] if druh_record else None
    druh_barcode = druh_record[0][2] if druh_record else none_barcode(4) # if no barcode → default = 0. 4 positions in this case →  "0000"

    typ_name = typ_record[0][3] if typ_record else None
    typ_barcode = typ_record[0][2] if typ_record else none_barcode(4) # if no barcode → default = 0. 4 positions in this case →  "0000"

    # New product name will be built from names of its components. Same princip for barcode.
    product_name = " ".join([name for name in [polozka_name, druh_name, typ_name] if name is not None]) # Only include the not None values in final product name
    
    product_barcode = "".join((polozka_barcode, druh_barcode, typ_barcode))

    # 2. Check if such product already in "produkty" table. If no, create new, otherwise show warning, that already exists.
    exists = record_already_exists_check(table_name, ["carovy_kod", "produkt"], [product_barcode, product_name])

    # 3. Create new record for this product in database in table "produkty"
    if not exists:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute(f"INSERT INTO '{table_name}' (produkt, carovy_kod, jednotky_id, cena_czk) VALUES (?,?,?,?)", (product_name, product_barcode, jednotky_id, cena_czk_2_decimals))
        
        # Also create initial price history record for this new produkt.
        # Get ID of last inserted record - our jus inserted record
        last_record_id = cursor.lastrowid
        # Commint changes to database
        conn.commit()
        conn.close()
        create_new_price_record(last_record_id, cena_czk_2_decimals)
    else:
        print(f"WARNING: Such record - NAME: {product_name}, BARCODE: {product_barcode} - already in database. Not inserting new record.")


if __name__ == "__main__":
    # SHow record in table 
    # create_new_polozka("Ondra")
    # create_new_druh("kluk")
    # create_new_typ("zrzek")
    # create_new_jednotka("ea", "jednotka s popisem")
    # create_new_jednotka("ea")

    sqllite.show_all_records_database_in_table(database_path, "polozky_data")
    sqllite.show_all_records_database_in_table(database_path, "druh_data")
    sqllite.show_all_records_database_in_table(database_path, "typ_data")
    sqllite.show_all_records_database_in_table(database_path, "jednotky")
    

    create_new_product(1,1,typ_id=1, cena_czk=35.216546)

    sqllite.show_all_records_database_in_table(database_path, "produkty")
    sqllite.show_all_records_database_in_table(database_path, "historie_cen")