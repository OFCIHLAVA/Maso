import os

from Modules.sqllite import delete_table, create_table

# database name
database_name = "inventory.db"
# current directory
curr_directory = os.path.dirname(os.path.abspath(__file__))
# database name
database_name = "inventory.db"
# database path
database_path = os.path.join(curr_directory, database_name)


### Database manupulation ↓

## Create new tables in database

# Table polozek
create_table(
    database_path,
    "polozky_data",
    """
    id INTEGER PRIMARY KEY,
    carovy_kod TEXT,
    nazev_polozky TEXT NOT NULL
    """
    )

# Table druhu
create_table(
    database_path,
    "druh_data",
    """
    id INTEGER PRIMARY KEY,
    carovy_kod TEXT,
    nazev_druh TEXT NOT NULL
    """
    )

# Table typu
create_table(
    database_path,
    "typ_data",
    """
    id INTEGER PRIMARY KEY,
    carovy_kod TEXT,
    nazev_typ TEXT NOT NULL
    """
    )    

# Table produktu
create_table(
    database_path,
    "produkty",
    """
    id INTEGER PRIMARY KEY,
    polozka_id INTEGER NOT NULL,
    jednotky_id INTEGER NOT NULL,
    druh_id INTEGER,
    typ_id INTEGER,
    cena_czk REAL
    """
    )  

# Table jednotek
create_table(
    database_path,
    "jednotky",
    """
    id INTEGER PRIMARY KEY,
    jednotky TEXT NOT NULL,
    popis TEXT
    """
    )

# Table price_history
create_table(
    database_path,
    "historie_cen",
    """
    id INTEGER PRIMARY KEY,
    produkt_id INTEGER NOT NULL,
    cena_czk REAL NOT NULL,
    datum_vytvoreni_zaznamu TEXT NOT NULL,
    datum_zneplatneni_zaznamu TEXT
    """
    )      



# Delete specific table from database

database_name = "inventory.db"
table_to_delete_name = "produkty1"
delete_table(database_path, table_to_delete_name)
