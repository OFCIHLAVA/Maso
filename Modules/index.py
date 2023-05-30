import tkinter as tk
from tkinter import ttk, filedialog
import os
import time
from SQL_update.Modules import queries, sqllite
import database_manager
import time
import sqlite3

### Setup files

# Nalezeni stavajiciho umisteni
current_folder_path = os.path.dirname(os.path.abspath(__file__))
# Nazev databaze, kam chceme vkladat zaznamy
database_name = 'programy.db'
# Sestaveni cesty databaze (predpoklada, ze se databaze nachazi v podslozce SQL_update ve slozce programu.)
database_path = f'{current_folder_path}\\SQL_update\\{database_name}'

# see all the indexes on all tables
tables = sqllite.get_all_tables_in_database(database_path) 

# Connect to the database
conn = sqlite3.connect(database_path)
    
# Create a cursor
cursor = conn.cursor()

for t in tables:
    # Show all indexes on given table
    print(t)
    cursor.execute(f'PRAGMA index_list("{t}")')
    r = cursor.fetchall()
    print(r)

# # Create index 
sqllite.create_index_on_column(database_path, t, "obsazen v")