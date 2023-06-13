from customtkinter import CTk, CTkFrame



class shop(CTkFrame):
    
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.configure_app_resizing()

        # Create left side - items sold
        self.left_side = CTkFrame(self, fg_color="dark grey", height=400)
        self.grid(left_side, row=0, column=0, sticky='nsew', padx=10, pady=20)

        # Create headings items sold
        self.headings = ItemsHeadings(self.left_side)
        # Create list if sold items
        self.items = GuiItemList(self.left_side)
        # Create footer
        self.footer = GuiFooter(self.left_side)

    def configure_app_resizing(self):
        # Configure the shop tab grid
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)