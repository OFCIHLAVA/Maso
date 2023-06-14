from customtkinter import CTkScrollableFrame, CTkLabel
from classes.tabs.shop.ItemLine import ItemLine


class ItemList(CTkScrollableFrame):
    
    def __init__(self, master=None, footer=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.pack(side="top", pady=10, padx=5, fill="both", expand=True)
        self.footer = footer

    def add_item_line(self, item_data_dict: dict): # Create Item Line in sell items list.
        ItemLine(self, item_data_dict, self.footer)
        self.footer.update_total()