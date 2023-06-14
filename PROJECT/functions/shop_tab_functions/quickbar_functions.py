import sqlite3

# Get list of available products from database
def get_available_products(produkt_ids: list=None): # Returns all produkts records in inventory database. (id + name), Optionly can be passed list of IDs to filter searched records.
    inventory_database_path = r"c:\Users\ondrej.rott\Documents\Python\MASO\inventory.db"

    conn = sqlite3.Connection(inventory_database_path)   
    cursor = conn.cursor()

    # If none id filter → get all records
    if produkt_ids is None:
        # Get all produkts # LEFT JOIN joins all rows to left (base table) even if theese have NONE in them. INNER JOIN only shows rows, with all values not=NONE.
        cursor.execute(f"""
                        SELECT produkty.id, polozky_data.nazev_polozky, druh_data.nazev_druh, typ_data.nazev_typ
                        FROM produkty
                        LEFT JOIN polozky_data
                        ON produkty.polozka_id = polozky_data.id
                        LEFT JOIN druh_data
                        ON produkty.druh_id = druh_data.id
                        LEFT JOIN typ_data
                        ON produkty.typ_id = typ_data.id
                        """)
    else:
       # Get records filtered by given IDs
        cursor.execute(f"""
                        SELECT produkty.id, polozky_data.nazev_polozky, druh_data.nazev_druh, typ_data.nazev_typ
                        FROM produkty
                        LEFT JOIN polozky_data
                        ON produkty.polozka_id = polozky_data.id
                        LEFT JOIN druh_data
                        ON produkty.druh_id = druh_data.id
                        LEFT JOIN typ_data
                        ON produkty.typ_id = typ_data.id
                        WHERE produkty.id IN ({", ".join("?" for _ in produkt_ids)})
                        """, tuple(produkt_ids))

    produkty_records = cursor.fetchall()    
    print(produkty_records)
    return produkty_records
    conn.commit()
    conn.close()
    

def get_product_data_for_item_line(produkt_id: int): # Returns database record for produkt based on its ID.
    inventory_database_path = r"c:\Users\ondrej.rott\Documents\Python\MASO\inventory.db"

    conn = sqlite3.Connection(inventory_database_path)   
    cursor = conn.cursor()

    # Get records filtered by given ID\
    cursor.execute(f"""
                    SELECT produkty.id, jednotky.jednotky, polozky_data.nazev_polozky, druh_data.nazev_druh, typ_data.nazev_typ, produkty.cena_czk
                    FROM produkty
                    LEFT JOIN jednotky
                    ON produkty.jednotky_id = jednotky.id
                    LEFT JOIN polozky_data
                    ON produkty.polozka_id = polozky_data.id
                    LEFT JOIN druh_data
                    ON produkty.druh_id = druh_data.id
                    LEFT JOIN typ_data
                    ON produkty.typ_id = typ_data.id
                    WHERE produkty.id = ?
                    """, (produkt_id,))

    produkt_record = cursor.fetchall()[0]
    print(produkt_record)
    return produkt_record
    conn.commit()
    conn.close()

if __name__ == "__main__":
    get_available_products()