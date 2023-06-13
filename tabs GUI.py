import customtkinter

import tkinter

from Classes.GuiHeadings import ItemsHeading

from Classes.GuiItemList import GuiItemList

from Classes.GuiFooter import GuiFooter

from Classes.ItemLine import ItemLine


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

### Create app main window
app_window = customtkinter.CTk()
app_window.geometry("1000x500")
app_window.minsize(1000, 500)
app_window.title("          AGROSHOP 3000")

## Create notebook inside the app window plus its styles
style = tkinter.ttk.Style()

# Configure the Tab style
style.configure('TNotebook.Tab', 
                font=('roboto', '12', 'bold'), 
                padding=[20, 5])

# Change the selected tab color
style.map('TNotebook.Tab',
          foreground=[('selected', 'orange')])

# Create notebook
notebook = tkinter.ttk.Notebook(app_window)

## First tab insude the app will contain SHOP interface

#Configure the app window grid
#app_window.grid_rowconfigure(0, weight=1)
#app_window.grid_columnconfigure(0, weight=1)
#app_window.grid_columnconfigure(1, weight=1)

## Frame containing shop elements items interface
tab_shop = customtkinter.CTkFrame(master=notebook, fg_color="grey")

# Configure the shop tab grid
tab_shop.grid_rowconfigure(0, weight=1)
tab_shop.grid_columnconfigure(0, weight=1)
tab_shop.grid_columnconfigure(1, weight=1)

# Left side of the app window contains interface for displaying items being sold
sold_items = customtkinter.CTkFrame(master=tab_shop, fg_color="dark grey", height=400)
sold_items.grid(row=0, column=0, sticky='nsew', padx=10, pady=20)

# Headings Frame
items_headings = ItemsHeading(sold_items)

# List of items Frame
items_list = GuiItemList(sold_items)

# Footer Frame
items_footer =GuiFooter(sold_items)

## Right side of the app window contains interface for manipulate the orders
# Frame containing shop controls interface
shop_controls = customtkinter.CTkFrame(master=tab_shop, fg_color="dark grey", height=400)
shop_controls.grid(row=0, column=1, sticky='nsew', padx=10, pady=20)

# Add frames to notebook
notebook.add(tab_shop, text="PRODEJ")
#notebook.add(shop_controls, text="DRUHY TAB")

notebook.pack(expand=True, fill='both')

#sold_items.grid(row=0, column=0, sticky='nsew', padx=10, pady=20)

# sold_items.grid_rowconfigure(0, weight=1)
# sold_items.grid_columnconfigure(0, weight=1)
# sold_items.grid_columnconfigure(1, weight=1)

# Design item being sold line (frame with labels probably)
# Test item lines
for i in range(20):
    item_line = ItemLine(items_list, {"id": 1,
                                          "icon_url":r"C:\Users\ondrej.rott\Documents\Python\MASO\Images\icon.gif",
                                          "name":"ovce",
                                          "price":12.5,
                                          "units":"ea",
                                          "stock":250
                                          }, items_footer)

## Right side of the app contains user interface
# Frame containing shop controls interface

#shop_controls.grid(row=0, column=1, sticky='nsew', padx=10, pady=20)

# # Design item being sold line (frame with labels probably)
# # Test item lines
# for i in range(20):
#     item_line = ItemLine(items_list, {"id": 1,
#                                           "icon_url":r"C:\Users\ondrej.rott\Documents\Python\MASO\Images\icon.gif",
#                                           "name":"ovce",
#                                           "price":12.5,
#                                           "units":"ea",
#                                           "stock":250
#                                           }, items_footer)

app_window.mainloop()