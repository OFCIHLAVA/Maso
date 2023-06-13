from customtkinter import CTk, CTkFrame
from classes.tabs.shop.GuiHeadings import ItemsHeadings
from classes.tabs.shop.GuiItemList import ItemList
from classes.tabs.shop.GuiFooter import Footer
from classes.tabs.shop.QuickBar import QuickBar
from classes.tabs.shop.ItemSearch import ItemSearch
from classes.tabs.shop.SellBar import SellBar


class TabShop(CTkFrame):
    
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.configure_app_resizing()

        ## Create left side - items sold
        self.left_side = CTkFrame(self, fg_color="orange", height=400)
        self.left_side.grid(row=0, column=0, sticky='nsew', padx=10, pady=20)

        # Create headings items sold
        self.headings = ItemsHeadings(self.left_side)
        # Create list if sold items
        self.items = ItemList(self.left_side)
        # Create footer
        self.footer = Footer(self.left_side)

        ## Create right side - shop controls
        self.right_side = CTkFrame(self, fg_color="#2D2D2D")
        # Configure the right side
        self.right_side.grid_columnconfigure(0, weight=1)
        self.right_side.grid_rowconfigure(0, weight=1)
        self.right_side.grid_rowconfigure(1, weight=0)
        self.right_side.grid_rowconfigure(2, weight=1)
        self.right_side.grid(row=0, column=1, sticky='nsew', padx=10, pady=20)

        # Create Quick bar
        self.quick_bar = QuickBar(self.right_side)
        # Create item search element
        self.item_search = ItemSearch(self.right_side)
        # # Create sell bar
        self.sell_bar = SellBar(self.right_side)
        

    def configure_app_resizing(self):
        # Configure the shop tab grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=1)
    