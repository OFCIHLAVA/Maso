import os

from Modules.sqllite import get_specific_record 

from Classes.polozka import Polozka

# database name
database_name = "inventory.db"
# current directory
curr_directory = os.path.dirname(os.path.abspath(__file__))
# database name
database_name = "inventory.db"
# database path
database_path = os.path.join(curr_directory, database_name)


Polozka.instantiate_from_csv(r"C:\Users\ondrej.rott\Documents\Python\MASO\pridat_polozky.csv")


# Add Qty to sklad

# if polozka known, add qty of instace to total qty already on sklad.
# else create this polozka and then add qty of instace to total qty on sklad.


# 1. check if known item

for polozka in Polozka.all:
    known_polozka = get_specific_record(database_path, "polozky_data", ["nazev"], [polozka.name])
    print(known_polozka)
