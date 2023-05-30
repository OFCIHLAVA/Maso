Shop database

Tables:

1. Item table ("polozky_data"):
This table holds list of known items. When new items is created, it needs to be inserted into this table.

It contains Item data:
a. "carovy_kod" - integer, unique 4 digit number represention of given Item for its Barcode.
b. "nazev" - text, unique name for given item.
c. "druh" - text, type representation of given item. Example: nazev: Ovce, druh: maso.
d. "typ" - text, even more detailed subtype representation of given item. Example: nazev: "Ovce", druh: "maso", typ: "svickova".
e. "cena" - real, price information in CZK with 2 decimal point precision.
f. "units" - text, item units of measure information (ea, kg ...).

2. Warehouse table ("sklad"):
This table holds records for all items on stock. Each record represents one specific Item (optioanly of some type and subtype) added on stock with some quantity and date.

It contains records data:
a. "polozka_id" - integer, id of given item from "polozky_data" table.
b. "mnozstvi" - real, qty of given item in Warehouse in units of given item. Precision 2 decimal points.
c. "mnozstvi_carovy_kod" - integer, digits representation of barcode for given qty.
d. "datum" - text, optionaly can be provided date information for given record. Format "YYYY-MM-DD".
e. "datum_carovy_kod" - integer, digits representation of barcode for given date. Example: 2023-06-20 → 20230620.
TRANSAKCE?


