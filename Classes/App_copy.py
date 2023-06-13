from Classes.GuiItemList import ItemList
from customtkinter import CTk, CTkFrame, set_appearance_mode, set_default_color_theme, CTkScrollableFrame, CTkLabel
from tkinter import ttk, StringVar


class App(CTk):
    def __init__(self):
        super().__init__()
        # Set app appearance
        self.geometry("1000x500")
        self.minsize(1000, 500)
        self.title("          AGROSHOP 3000")
        self.set_dark_theme()
        # Create notebook structure within app + appearance
        self.notebook = ttk.Notebook(self)
        self.set_tab_pages_style()

        # Create shop tab
        self.shop_tab = TabShop(self.notebook)

        # Pack shop tab to app
        self.notebook.add(self.shop_tab, text="PRODEJ")
        
        self.notebook.pack(expand=True, fill='both')

    def run(self):
        self.mainloop()
   
    def set_dark_theme(self):
        set_appearance_mode("dark")
        set_default_color_theme("blue")

    def set_tab_pages_style(self):
        tabs_style = ttk.Style()
        tabs_style.configure('TNotebook.Tab',
                font=('roboto', '12', 'bold'), 
                padding=[20, 5])
        # Change the selected tab color
        tabs_style.map('TNotebook.Tab',
                foreground=[('selected', 'orange')])
                
class TabShop(CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.configure_app_resizing()

        # Create left side - items sold
        self.left_side = CTkFrame(self, fg_color="orange", height=400)
        self.left_side.grid(row=0, column=0, sticky='nsew', padx=10, pady=20)

        # Create headings items sold
        self.headings = ItemsHeadings(self.left_side)
        # Create list if sold items
        self.items = ItemList(self.left_side)
        # Create footer
        self.footer = Footer(self.left_side)

    def configure_app_resizing(self):
        # Configure the shop tab grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

class ItemsHeadings(CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.pack(side="top", pady=10, padx=5, fill="both")

        # Follows all the labels with headings names, sepparated by sep. labels
        self.id_label = CTkLabel(self, width=50,height=70, text="ID", font=("roboto", 12, "bold"), pady=10, padx=10, corner_radius=3)
        self.id_label.pack(side="left", pady=5, padx=5, fill="x")

        self.sep_label = CTkLabel(self, width=1, text="", bg_color="yellow")
        self.sep_label.pack(side="left", pady=5, padx=5, fill="x")

        self.icon_label = CTkLabel(self, width=50, text="ICON", font=("roboto", 12, "bold"), pady=10, padx=10)
        self.icon_label.pack(side="left", pady=5, padx=5, fill="x")

        self.sep_label = CTkLabel(self, width=1, text="", bg_color="yellow")
        self.sep_label.pack(side="left", pady=5, padx=5, fill="x")

        self.name_label = CTkLabel(self, text="NAME", font=("roboto", 12, "bold"), pady=10, padx=10)
        self.name_label.pack(side="left", pady=5, padx=5, fill="x", expand=True)

        self.sep_label = CTkLabel(self, width=1, text="", bg_color="yellow")
        self.sep_label.pack(side="left", pady=5, padx=5, fill="x")

        self.price_label = CTkLabel(self, width=50, text="PRICE", font=("roboto", 12, "bold"), pady=10, padx=10)
        self.price_label.pack(side="left", pady=5, padx=5, fill="x")

        self.sep_label = CTkLabel(self, width=1, text="", bg_color="yellow")
        self.sep_label.pack(side="left", pady=5, padx=5, fill="x")

        self.units_label = CTkLabel(self, width=50, text="UNITS", font=("roboto", 12, "bold"), pady=10, padx=10)
        self.units_label.pack(side="left", pady=5, padx=5, fill="x")

        self.sep_label = CTkLabel(self, width=1, text="", bg_color="yellow")
        self.sep_label.pack(side="left", pady=5, padx=5, fill="x")

        self.quantity_label = CTkLabel(self, width=108, text="QTY", font=("roboto", 12, "bold"), pady=10, padx=10)
        self.quantity_label.pack(side="left", pady=5, padx=5, fill="x")

        self.sep_label = CTkLabel(self, width=1, text="", bg_color="yellow")
        self.sep_label.pack(side="left", pady=5, padx=5, fill="x")

        self.on_stock_label = CTkLabel(self, width=50, text="ON STOCK", font=("roboto", 12, "bold"), pady=10, padx=10)
        self.on_stock_label.pack(side="left", pady=5, padx=5, fill="x")

        self.sep_label = CTkLabel(self, width=1, text="", bg_color="yellow")
        self.sep_label.pack(side="left", pady=5, padx=5, fill="x")

        self.subtotal_label = CTkLabel(self, width=50, text="SUBTOTAL", font=("roboto", 12, "bold"), pady=10, padx=10)
        self.subtotal_label.pack(side="left", pady=5, padx=5, fill="x")

        self.sep_label = CTkLabel(self, width=1, text="", bg_color="yellow")
        self.sep_label.pack(side="left", pady=5, padx=5, fill="x")

        self.manage_qty_label = CTkLabel(self, width=30, text="", pady=10, padx=10)
        self.manage_qty_label.pack(side="left", pady=5, padx=5, fill="x")

        self.end_sep_label = CTkLabel(self, width=12, text="")
        self.end_sep_label.pack(side="left", pady=5, padx=5, fill="x")

#class ItemList(CTkScrollableFrame):
#    
#    def __init__(self, master=None, **kwargs):
#        super().__init__(master=master, **kwargs)
#        self.pack(side="top", pady=10, padx=5, fill="both", expand=True)

class Footer(CTkFrame):
    def __init__(self, master=None,  **kwargs):
        super().__init__(master=master, **kwargs)
        self.pack(side="bottom", pady=10, padx=5, fill="both")

        # Follows all the labels with headings names, sepparated by sep. labels

        self.footer_label = CTkLabel(self, height=70, text="© OFCIHLAVA 2023", font=("roboto", 12, "bold"), anchor="w", pady=10, padx=10)
        self.footer_label.pack(side="left", pady=5, padx=5, fill="x", expand=True)

        self.sep_label = CTkLabel(self, width=1, text="", bg_color="white")
        self.sep_label.pack(side="left", pady=5, padx=5, fill="x")

        self.total_label = CTkLabel(self, width=81, text="TOTAL", font=("roboto", 12, "bold"), pady=10, padx=10)
        self.total_label.pack(side="left", pady=5, padx=5, fill="x")

        self.sep_label = CTkLabel(self, width=1, text="", bg_color="white")
        self.sep_label.pack(side="left", pady=5, padx=5, fill="x")

        self.total_value = StringVar()
        self.total_value.set("0")
        self.total_value_label = CTkLabel(self, width=81, textvariable=self.total_value, font=("roboto", 12, "bold"), pady=10, padx=10)
        self.total_value_label.pack(side="left", pady=5, padx=5, fill="x")

        self.sep_label = CTkLabel(self, width=1, text="", bg_color="white")
        self.sep_label.pack(side="left", pady=5, padx=5, fill="x")

        self.manage_qty_label = CTkLabel(self, width=30, text="", pady=10, padx=10)
        self.manage_qty_label.pack(side="left", pady=5, padx=5, fill="x")

        self.end_sep_label = CTkLabel(self, width=10, text="")
        self.end_sep_label.pack(side="left", pady=5, padx=5, fill="x")

    # Helper function to show numbers in more readable format
    def format_number(value):
        return format(value, ',').replace(',', ' ') 

    def update_total(self, *args):
        total = ItemLine.total_of_all_active_lines
        print("updatuju total")
        print(total)
        self.total_value.set(self.format_number(total))

    @staticmethod
    def format_number(value):
        return format(value, ',').replace(',', ' ')