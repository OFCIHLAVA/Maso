import customtkinter

from Classes.GuiHeadings import ItemsHeading

from Classes.GuiItemList import GuiItemList

from Classes.GuiFooter import GuiFooter

from Classes.ItemLine import ItemLine


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

### Create app main window
app_window = customtkinter.CTk()
app_window.geometry("1000x400")
app_window.minsize(1000, 400)
app_window.title("          AGROSHOP 3000")

# Configure the app window grid
app_window.grid_rowconfigure(0, weight=1)
app_window.grid_columnconfigure(0, weight=1)
app_window.grid_columnconfigure(1, weight=1)

## Left side of the app window contains interface for displaying items being sold
# Frame containing sold items interface
frame_items = customtkinter.CTkFrame(master=app_window, fg_color="grey", height=400)
frame_items.grid(row=0, column=0, sticky='nsew', padx=10, pady=20)

# Headings Frame
items_headings = ItemsHeading(frame_items)

# List of items Frame
items_list = GuiItemList(frame_items)

# Footer Frame
items_footer =GuiFooter(frame_items)

## Right side of the app contains user interface
# Frame containing shop controls interface
shop_controls = customtkinter.CTkFrame(master=app_window, fg_color="grey", height=400)
shop_controls.grid(row=0, column=1, sticky='nsew', padx=10, pady=20)





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