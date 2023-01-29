from Modules import sqllite
import os

# Get current folder path

current_folder_path = os.path.dirname(os.path.abspath(__file__))

### Create database sklad

# Prepare file paths
database_name = 'stock.db'
database_path = f'{current_folder_path}\\{database_name}'

# Delete some table if needed
#sqllite.delete_table(database_path, "animal")
#sqllite.delete_table(database_path, "product")
#sqllite.delete_table(database_path, "units")
#sqllite.delete_table(database_path, "pricing")

# Create table "animal" in database
#sqllite.create_table(database_path, "animal", "name TEXT NOT NULL")

# Create table "product" in database
#sqllite.create_table(database_path, "product", "name TEXT NOT NULL")

# Create table "units" in database
#sqllite.create_table(database_path, "units", "name TEXT NOT NULL")

# Create table "pricing" in database
#sqllite.create_table(database_path, "pricing", "animal TEXT NOT NULL, product TEXT NOT NULL, price_per_unit FLOAT")

### Check the created tables in database

# Get all tables in db 
all_tables = sqllite.get_all_tables_in_database(database_path)
for i,t in enumerate(all_tables):
	print(f'Showing table nr: {i+1} in database: {database_name}, table name:{t}')
	# For each table show columns
	t_columns = sqllite.get_table_columns(database_path, t)
	t_columns.insert(0, "rowid")
	print("Columns in table: "+"\t".join(t_columns))
	# For each table show count of records in it and print all records in it.
	sqllite.get_count_records_in_table(database_path, t)
	sqllite.show_all_records_database_in_table(database_path, t)

### Insert new animal, product and unit of measure to database to table

# Insert 1 new animal:

# Take animal to add as list
animal_name = ["prase"]

# Check wheter provided animal name already in database
exists = sqllite.record_exists(database_path, "animal", sqllite.get_table_columns(database_path, "animal") , animal_name)
if not exists:
	print(f'Animal: {animal_name[0]} not yet in database.')

# Add to database if not already there
if not exists:
	sqllite.insert_record(database_path, "animal", sqllite.get_table_columns(database_path, "animal"), animal_name)
else:
	print(f'\nAnimal: "{animal_name[0]}" already exists in database. Nothing inserted.\n')

# Insert 1 new product:

# Take animal to add as list
product_name = ["kýta"]

# Check wheter provided product name already in database
exists = sqllite.record_exists(database_path, "product", sqllite.get_table_columns(database_path, "product") , product_name)
if not exists:
	print(f'product: {product_name[0]} not yet in database.')

# Add to database if not already there
if not exists:
	sqllite.insert_record(database_path, "product", sqllite.get_table_columns(database_path, "product"), product_name)
else:
	print(f'\nproduct: "{product_name[0]}" already exists in database. Nothing inserted.\n')

# Insert 1 new unit:

# Take animal to add as list
unit_name = ["kg"]

# Check wheter provided unit name already in database
exists = sqllite.record_exists(database_path, "units", sqllite.get_table_columns(database_path, "units") , unit_name)
if not exists:
	print(f'unit: {unit_name[0]} not yet in database.')

# Add to database if not already there
if not exists:
	sqllite.insert_record(database_path, "units", sqllite.get_table_columns(database_path, "units"), unit_name)
else:
	print(f'\nunit: "{unit_name[0]}" already exists in database. Nothing inserted.\n')


### Delete some record from table

# Delete prase from database from table animal

# Provide list of values to identify the record toi be deleted as list
animal_record_values = ["prase"]

# Delete record
# sqllite.delete_record(database_path, "animal", sqllite.get_table_columns(database_path, "animal"), animal_record_values)

