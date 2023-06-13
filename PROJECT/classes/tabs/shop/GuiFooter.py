from classes.tabs.shop.ItemLine import ItemLine

from customtkinter import CTkFrame, CTkLabel

from tkinter import StringVar

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

    