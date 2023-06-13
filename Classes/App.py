from tabshop import shop
from customtkinter import CTk, set_appearance_mode, set_default_color_theme
from tkinter import ttk


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
        self.notebook.pack(expand=True, fill='both')
        # Create shop tab
        self.shop_tab = shop(self.notebook)

        # Pack shop tab to app
        self.notebook.add(self.shop_tab, text="PRODEJ")




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