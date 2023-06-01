import sqlite3

from Modules import sqllite

from datetime import datetime

# Helper functions
def record_already_exists_check(table_name: str, column_names: list, record_data_for_columns: list): # Function to check, if record with specified values already exitst in table.
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    # 1. Potreba dynamicky poskladat SQL statement for select query both for columns with some value and for columns with None value.
    
    # Not-Null columns - vybrat pary sloupec:hodnota pro sloupce s nenulovaou hodnotou
    columns_with_values = [column_names[i] for i, value in enumerate(record_data_for_columns) if value is not None]
    not_null_values = [value for i, value in enumerate(record_data_for_columns) if value is not None]

    # Null columns 
    columns_with_null_values = [column_names[i] for i, value in enumerate(record_data_for_columns) if value is None]

    # cast SQL query kde existuje value pro sloupce
    where_sql_statement = "= ? AND ".join([column for column in columns_with_values])+ "= ?"

    if None in record_data_for_columns: # This applies only when there are some None values in columns.
    # cast SQL query pro NULL value sloupce
        null_values_sql_part = "IS NULL AND ".join([column for column in columns_with_null_values])+" IS NULL" # We use IS NULL statement to check for None values.
        where_sql_statement = where_sql_statement + " AND " + null_values_sql_part

    # 2. Overit jestli record odpovidajici bodu 1 je uz v tabulce
    print(f"SELECT * FROM '{table_name}' WHERE {where_sql_statement}")
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

## Warehouse backoffice
def create_new_polozka(polozka_name: str): # New "polozka_data" table record.
    table_name = "polozky_data"

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    
    # 1. Check if such "polozka" already in "polozky_data" table. If no, create new, otherwise show warning, that already exists.
    exists = record_already_exists_check(table_name, ["nazev_polozky"], [polozka_name])

    # 2. Create new record for this polozka.
    if not exists:
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
    else:
        print(f"Pozor, Polozka s takovymto nazvem - {polozka_name} - uz existuje. Nic nepridano.")

def edit_polozka_name(polozka_id: int, new_nazev: str): # Edits name for specifir polozka ID record.
    table_name = "polozky_data"

    conn = sqlite3.Connection(database_path)   
    cursor = conn.cursor()

    # Get old value to confirm changes
    cursor.execute(f"SELECT id, nazev_polozky FROM {table_name} WHERE id = ?", (polozka_id,))
    polozka_record = cursor.fetchall()
    print(polozka_record)
    polozka_id = polozka_record[0][0]
    puvodni_nazev = polozka_record[0][1]
    
    # Make update itself
    cursor.execute(f"UPDATE {table_name} SET nazev_polozky = ? WHERE id = ?", (new_nazev, polozka_id))

    # Check, if changes done correctly
    cursor.execute(f"SELECT id, nazev_polozky FROM {table_name} WHERE id = ?", (polozka_id,))
    polozka_record = cursor.fetchall()
    novy_nazev = polozka_record[0][1]

    print(f"U polozky ID - {polozka_id} - zmenen nazev z puvodniho - {puvodni_nazev} - na - {novy_nazev}")

    conn.commit()
    conn.close()

def create_new_druh(druh_name: str): # New "druh_data" table record.
    table_name = "druh_data"

    # 1. Check if such "druh" already in "druh_data" table. If no, create new, otherwise show warning, that already exists.
    exists = record_already_exists_check(table_name, ["nazev_druh"], [druh_name])

    # 2. Create new record for this druh.
    if not exists:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

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
    else:
        print(f"Pozor, Druh s takovymto nazvem - {druh_name} - uz existuje. Nic nepridano.")

def edit_druh_name(druh_id: int, new_nazev: str): # Edits name for specifir druh ID record.
    table_name = "druh_data"

    conn = sqlite3.Connection(database_path)   
    cursor = conn.cursor()

    # Get old value to confirm changes
    cursor.execute(f"SELECT id, nazev_druh FROM {table_name} WHERE id = ?", (druh_id,))
    druh_record = cursor.fetchall()
    druh_id = druh_record[0][0]
    puvodni_nazev = druh_record[0][1]
    
    # Make update itself
    cursor.execute(f"UPDATE {table_name} SET nazev_druh = ? WHERE id = ?", (new_nazev, druh_id))

    # Check, if changes done correctly
    cursor.execute(f"SELECT id, nazev_druh FROM {table_name} WHERE id = ?", (druh_id,))
    druh_record = cursor.fetchall()
    novy_nazev = druh_record[0][1]

    print(f"U druhu ID - {druh_id} - zmenen nazev z puvodniho - {puvodni_nazev} - na - {novy_nazev}")

    conn.commit()
    conn.close()

def create_new_typ(typ_name: str): # New "typ_data" table record.
    table_name = "typ_data"

    # 1. Check if such "typ" already in "typ_data" table. If no, create new, otherwise show warning, that already exists.
    exists = record_already_exists_check(table_name, ["nazev_typ"], [typ_name])

    # 2. Create new record for this typ.
    if not exists:
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
    else:
        print(f"Pozor, Typ s takovymto nazvem - {typ_name} - uz existuje. Nic nepridano.")        

def edit_typ_name(typ_id: int, new_nazev: str): # Edits name for specifir druh ID record.
    table_name = "typ_data"

    conn = sqlite3.Connection(database_path)   
    cursor = conn.cursor()

    # Get old value to confirm changes
    cursor.execute(f"SELECT id, nazev_typ FROM {table_name} WHERE id = ?", (typ_id,))
    typ_record = cursor.fetchall()
    typ_id = typ_record[0][0]
    puvodni_nazev = typ_record[0][1]
    
    # Make update itself
    cursor.execute(f"UPDATE {table_name} SET nazev_typ = ? WHERE id = ?", (new_nazev, typ_id))

    # Check, if changes done correctly
    cursor.execute(f"SELECT id, nazev_typ FROM {table_name} WHERE id = ?", (typ_id,))
    typ_record = cursor.fetchall()
    novy_nazev = typ_record[0][1]

    print(f"U typu ID - {typ_id} - zmenen nazev z puvodniho - {puvodni_nazev} - na - {novy_nazev}")

    conn.commit()
    conn.close()

def create_new_jednotka(jednotky_name: str, popis: str=None ): # New "jednotky" table record.
    table_name = "jednotky"

    # 1. Check if such "jednotka" already in "jednotky" table. If no, create new, otherwise show warning, that already exists.
    exists = record_already_exists_check(table_name, ["jednotky"], [jednotky_name])

    # 2. Create new record for this jednotky.
    if not exists:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute(f"INSERT INTO '{table_name}' (jednotky, popis) VALUES (?,?)", (jednotky_name, popis))

        # Commint changes to database
        conn.commit()
        conn.close()
    else:
        print(f"Pozor, jednotka s takovymto nazvem - {jednotky_name} - uz existuje. Nic nepridano.")  

def edit_jednotka_name(jednotka_id: int, new_nazev: str): # Edits name for specifir jednotka ID record.
    table_name = "jednotky"

    conn = sqlite3.Connection(database_path)   
    cursor = conn.cursor()

    # Get old value to confirm changes
    cursor.execute(f"SELECT id, jednotky FROM {table_name} WHERE id = ?", (jednotka_id,))
    jednotka_record = cursor.fetchall()
    jednotka_id = jednotka_record[0][0]
    puvodni_nazev = jednotka_record[0][1]
    
    # Make update itself
    cursor.execute(f"UPDATE {table_name} SET jednotky = ? WHERE id = ?", (new_nazev, jednotka_id))

    # Check, if changes done correctly
    cursor.execute(f"SELECT id, jednotky FROM {table_name} WHERE id = ?", (jednotka_id,))
    jednotka_record = cursor.fetchall()
    novy_nazev = jednotka_record[0][1]

    print(f"U jednotkay ID - {jednotka_id} - zmenen nazev z puvodniho - {puvodni_nazev} - na - {novy_nazev}")

    conn.commit()
    conn.close()

# Product
def updated_create_new_produkt(polozka_id: int, jednotky_id: int, druh_id: int=None, typ_id: int=None, cena_czk: float=0): 
    # Builds new product record by combining IDs of polozka + druh + typ. Combines ID so relevant data can be connected to it. Saves price to pricebook table if provided, else saves with price 0.00.    
    # 1st Build the product based on components selected by user.
    table_name = "produkty"

    cena_czk_2_decimals = round(cena_czk, 2)

    # 2. Check if such product already in "produkty" table. If no, create new, otherwise show warning, that already exists.
    exists = record_already_exists_check(table_name, ["polozka_id", "druh_id", "typ_id"], [polozka_id, druh_id, typ_id])

    # 3. Create new record for this product in database in table "produkty"
    if not exists:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        cursor.execute(f"INSERT INTO '{table_name}' (polozka_id, jednotky_id, druh_id, typ_id, cena_czk) VALUES (?,?,?,?,?)", (polozka_id, jednotky_id, druh_id, typ_id, cena_czk_2_decimals))
        
        # Also create initial price history record for this new produkt.
        # Get ID of last inserted record - our jus inserted record
        last_record_id = cursor.lastrowid
        # Commint changes to database
        conn.commit()
        conn.close()
        create_new_price_record(last_record_id, cena_czk_2_decimals)
    else:
        print(f"WARNING: Such record - polozka ID : {polozka_id}, druh ID: {druh_id} and typ ID: {typ_id} - already in database. Not inserting new record.")

def edit_produkt_cena_value(produkt_id: int, nova_cena_czk: float): # Edits cena_czk value for given id product in table "produkty".
    table_name = "produkty"
    nova_cena_czk_2_decimals = round(nova_cena_czk, 2)

    # 1. edit price value on product record
    conn = sqlite3.Connection(database_path)   
    cursor = conn.cursor()

    # Get old value to confirm changes
    cursor.execute(f"SELECT id, cena_czk FROM {table_name} WHERE id = ?", (produkt_id,))
    produkt_record = cursor.fetchall()
    print(produkt_record)
    produkt_id = produkt_record[0][0]
    puvodni_cena_czk = produkt_record[0][1]

    # Make update itself
    cursor.execute(f"UPDATE {table_name} SET cena_czk = ? WHERE id = ?", (nova_cena_czk_2_decimals, produkt_id))
    
    # Check, if changes done correctly
    cursor.execute(f"SELECT cena_czk FROM {table_name} WHERE id = ?", (produkt_id,))
    produkt_record = cursor.fetchall()
    nova_cena_czk = produkt_record[0][0]
    
    print(f"Cena updatovana u produktu ID - {produkt_id} - z puvodnich - {puvodni_cena_czk} CZK na - {nova_cena_czk} ")
    
    conn.commit()
    conn.close()

def change_produkt_jednotky(produkt_id: int, nove_jednotky_id: int): # Selects new value for product jednotky from existing jednotek
    produkty_table_name = "produkty"
    jednotky_table_name = "jednotky"

    conn = sqlite3.Connection(database_path)   
    cursor = conn.cursor()

    # Get old jednotky value to confirm changes
    cursor.execute(f"""
                    SELECT jednotky.id, jednotky.jednotky
                    FROM {produkty_table_name}
                    INNER JOIN {jednotky_table_name}
                    ON {produkty_table_name}.jednotky_id = {jednotky_table_name}.id
                    WHERE produkty.id = ?""", (produkt_id,))
    produkt_record = cursor.fetchall()
    puvodni_jednotky = produkt_record[0][1]

    # Make update itself
    cursor.execute(f"UPDATE {produkty_table_name} SET jednotky_id = ? WHERE id = ?", (nove_jednotky_id, produkt_id))
    
    # Check, if changes done correctly
    cursor.execute(f"""
                    SELECT jednotky.id, jednotky.jednotky
                    FROM {produkty_table_name}
                    INNER JOIN {jednotky_table_name}
                    ON {produkty_table_name}.jednotky_id = {jednotky_table_name}.id
                    WHERE produkty.id = ?""", (produkt_id,))
    produkt_record = cursor.fetchall()
    nove_jednotky = produkt_record[0][1]
    
    print(f"Jednotky u produktu ID - {produkt_id} - zmeneny z puvodnich - {puvodni_jednotky} - na - {nove_jednotky}.")
    
    conn.commit()
    conn.close()

def invalidate_current_price_history_line(produkt_id: int): # Updates column "datum_zneplatneni_zaznamu" for active produkt price line in table "historie_cen" with todays date. 
    table_name = "historie_cen"
    todays_date = datetime.today().date()

    # 1. fill the "datum_zneplatneni_zaznamu" value on price line record.
    conn = sqlite3.Connection(database_path)   
    cursor = conn.cursor()

    # Get id of current price line to confirm changes
    cursor.execute(f"SELECT id FROM {table_name} WHERE produkt_id = ? AND datum_zneplatneni_zaznamu IS NULL", (produkt_id,))
    old_record = cursor.fetchall()
    print(old_record)
    old_record_id = old_record[0][0]

    # Make update itself
    cursor.execute(f"UPDATE {table_name} SET datum_zneplatneni_zaznamu = ? WHERE produkt_id = ? AND datum_zneplatneni_zaznamu IS NULL", (str(todays_date), produkt_id))

    # Check updated record, if changes done correctly
    cursor.execute(f"SELECT datum_zneplatneni_zaznamu FROM {table_name} WHERE id = ?", (old_record_id,))
    updated_record = cursor.fetchall()
    datum_zneplatneni_zaznamu = updated_record[0][0]

    print(f"Price history Line ID - {old_record_id} - zneplatnena k datumu - {todays_date}.")

    conn.commit()
    conn.close()

# Pricing backoffice
def create_new_price_record(produkt_id: int, cena_czk: float): # creates new price history line in table "historie_cen".
    # creates new price history line in table "historie_cen".
    table_name = "historie_cen"

    todays_date = datetime.today().date()
    cena_czk_2_decimals = round(cena_czk, 2)

    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO '{table_name}' (produkt_id, cena_czk, datum_vytvoreni_zaznamu) VALUES (?,?,?)", (produkt_id, cena_czk_2_decimals, str(todays_date)))

    # Commint changes to database
    conn.commit()
    conn.close() 

def change_product_price(produkt_id: int, nova_cena_czk: float): # Allows user to change prices for existing products.
    table_name = "produkty"
    nova_cena_czk_2_decimals = round(nova_cena_czk, 2)

    # 1. Check if price needs to be updated, or is already same as we want it to be.
    conn = sqlite3.Connection(database_path)   
    cursor = conn.cursor()

    cursor.execute(f"SELECT id, cena_czk FROM {table_name} WHERE id = ?", (produkt_id,))
    produkt_record = cursor.fetchall()
    produkt_id = produkt_record[0][0]
    puvodni_cena_czk = produkt_record[0][1]

    # Pokud stavajici cena je stejna jako ta, na jakou se to snazime zmenit → nemenit at se nehlti databaze.
    if puvodni_cena_czk != nova_cena_czk_2_decimals:
    
        # 1. edit price value in "produkt" table
        edit_produkt_cena_value(produkt_id, nova_cena_czk)

        # 2. invalidate last price history line by updating it with todays date.
        invalidate_current_price_history_line(produkt_id)

        # 3. create new price history line
        create_new_price_record(produkt_id, nova_cena_czk)
    else:
        print(f"WARNING: Produkt ID - {produkt_id} - uz ma stavajici cenu - {puvodni_cena_czk} - CZK. Neni treba menit na novou cenu - {nova_cena_czk_2_decimals} CZK. Nic neupdatovano.")

if __name__ == "__main__":
    database_path = r"C:\Users\ondrej.rott\Documents\Python\MASO\inventory.db"

    # SHow record in table 
    # create_new_polozka("Ondra")
    # create_new_druh("kluk")
    # create_new_typ("zrzek")
    # create_new_jednotka("ea", "jednotka s popisem")
    create_new_jednotka("kg")

    sqllite.show_all_records_database_in_table(database_path, "polozky_data")
    sqllite.show_all_records_database_in_table(database_path, "druh_data")
    sqllite.show_all_records_database_in_table(database_path, "typ_data")
    sqllite.show_all_records_database_in_table(database_path, "jednotky")
    

    updated_create_new_produkt(1,1,typ_id=1, cena_czk=35.216546)

    sqllite.show_all_records_database_in_table(database_path, "produkty")
    change_product_price(1, 50.000)
    edit_jednotka_name(1, "hovno")
    change_produkt_jednotky(1, 2)

    sqllite.show_all_records_database_in_table(database_path, "produkty")
    sqllite.show_all_records_database_in_table(database_path, "historie_cen")