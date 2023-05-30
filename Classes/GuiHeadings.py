from customtkinter import CTkFrame, CTkLabel

class ItemsHeading(CTkFrame):
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