from customtkinter import CTkFrame, CTkLabel, CTkImage, CTkEntry, CTkButton

from tkinter import StringVar

from PIL import Image

class ItemLine(CTkFrame):
    
    active_item_lines = []
    total_of_all_active_lines = 0
    
    def __init__(self, master=None, item_data_dict=None, footer=None, **kwargs):
        super().__init__(master=master, **kwargs)
        
        self.id = item_data_dict.get("id")
        self.icon_url = item_data_dict.get("icon_url")
        self.name = item_data_dict.get("name")
        self.price = item_data_dict.get("price")
        self.units = item_data_dict.get("units")
        self.stock = item_data_dict.get("stock")
        self.subtotal = self.price*1
        self.footer = footer

        # Actions to execute during init
        ItemLine.active_item_lines.append(self)
        ItemLine.total_of_all_active_lines += self.subtotal


        # Plus and minus buttons to manipulate quantity, destrous line if quantity decreased bellow zero
        def decrease_quantity():
            try:
                quantity = float(self.quantity_value.get())
                if quantity > 1:
                    quantity -= 1
                    self.quantity_value.set(format_number(quantity))
                    calculate_subtotal()
                    self.footer.update_total()
                else:
                # elif quantity == 0:
                    destroy_line()
            except:
                pass

        def increase_quantity():
            try:
                quantity = float(self.quantity_value.get())
                on_stock = self.stock
                if quantity < on_stock:
                    quantity += 1
                    
                    self.quantity_value.set(format_number(quantity))
                    calculate_subtotal()
            except:
                pass

        # Function to validate quantiy value
        def validate_quantity(*args):
            try:
                value = float(self.quantity_value.get())
                if value < 0:
                    self.quantity_value.set("1")
                elif value > self.stock:
                    self.quantity_value.set(format_number(self.stock))
                else:
                    self.quantity_value.set(format_number(value))
                calculate_subtotal()   
            except:
                self.quantity_value.set("1")
                calculate_subtotal()

        # Function to update subtotal label
        def calculate_subtotal(*args):
            try:
                quantity = float(self.quantity_value.get())
                price = self.price
                old_subtotal = self.subtotal
                self.subtotal = quantity*price
                self.subtotal_value.set(format_number(quantity*price))
                ItemLine.total_of_all_active_lines += self.subtotal - old_subtotal
                self.footer.update_total()
            except ValueError:
                pass

        # Destroy self function
        def destroy_line():
            ItemLine.total_of_all_active_lines -= self.subtotal
            ItemLine.active_item_lines.remove(self) # TADY Skonceno
            self.footer.update_total()
            self.destroy()

        # Helper function to show numbers in more readable format
        def format_number(value):
            return format(value, ',').replace(',', ' ')    

        # pack line in Parrent frame
        self.pack(side="top", pady=1, padx=5, fill="x")

        # Now we want to have fields coresponding with headings

        self.id_label = CTkLabel(self, width=40, height=30, text=self.id, font=("roboto", 12, "bold"), pady=10, padx=10, corner_radius=3)
        self.id_label.pack(side="left", pady=5, padx=5, fill="x")

        self.sep_label = CTkLabel(self, width=1, text="", bg_color="yellow")
        self.sep_label.pack(side="left", pady=5, padx=5, fill="x")

        self.icon_image = CTkImage(light_image=Image.open(self.icon_url), size=(30,30))
        self.icon_label = CTkLabel(self, width=50, text="", image=self.icon_image, pady=10, padx=10)
        self.icon_label.pack(side="left", pady=5, padx=5, fill="x")

        self.sep_label = CTkLabel(self, width=1, text="", bg_color="yellow")
        self.sep_label.pack(side="left", pady=5, padx=5, fill="x")

        self.name_label = CTkLabel(self, text=self.name, font=("roboto", 12, "bold"), pady=10, padx=10)
        self.name_label.pack(side="left", pady=5, padx=5, fill="x", expand=True)

        self.sep_label = CTkLabel(self, width=1, text="", bg_color="yellow")
        self.sep_label.pack(side="left", pady=5, padx=5, fill="x")

        self.price_label = CTkLabel(self, width=54, text=self.price, font=("roboto", 12, "bold"), pady=10, padx=10)
        self.price_label.pack(side="left", pady=5, padx=5, fill="x")

        self.sep_label = CTkLabel(self, width=1, text="", bg_color="yellow")
        self.sep_label.pack(side="left", pady=5, padx=5, fill="x")

        self.units_label = CTkLabel(self, width=53, text=self.units, font=("roboto", 12, "bold"), pady=10, padx=10)
        self.units_label.pack(side="left", pady=5, padx=5, fill="x")

        self.sep_label = CTkLabel(self, width=1, text="", bg_color="yellow")
        self.sep_label.pack(side="left", pady=5, padx=5, fill="x")

        # minus qty button
        self.decrease_quantity_button = CTkButton(self, width=30, text="-", font=("roboto", 14, "bold"), fg_color="grey", hover=True, hover_color="red", command=decrease_quantity)
        self.decrease_quantity_button.pack(side="left", pady=5, fill="x")

        self.quantity_value = StringVar()
        self.quantity_value.set("1")
        self.quantity_value.trace("w", self.footer.update_total)
        #quantity_value.trace("w", validate_quantity)
        self.quantity_entry = CTkEntry(self, width=50, textvariable=self.quantity_value, font=("roboto", 12, "bold"), justify="center")
        self.quantity_entry.bind('<FocusOut>', validate_quantity)
        self.quantity_entry.bind('<Return>', validate_quantity)
        self.quantity_entry.pack(side="left", pady=5, padx=3, fill="x")

        # plus qty button
        self.increase_quantity_button = CTkButton(self, width=30, text="+", font=("roboto", 14, "bold"), fg_color="grey", hover=True, hover_color="green", command=increase_quantity)
        self.increase_quantity_button.pack(side="left", pady=5, fill="x")

        self.sep_label = CTkLabel(self, width=1, text="", bg_color="yellow")
        self.sep_label.pack(side="left", pady=5, padx=5, fill="x")

        self.on_stock_label = CTkLabel(self, width=81, text=self.stock, font=("roboto", 12, "bold", "bold"), pady=10, padx=10)
        self.on_stock_label.pack(side="left", pady=5, padx=5, fill="x")

        self.sep_label = CTkLabel(self, width=1, text="", bg_color="yellow")
        self.sep_label.pack(side="left", pady=5, padx=5, fill="x")

        self.subtotal_value = StringVar()
        self.subtotal_value.set(format_number(self.price))
        self.subtotal_label = CTkLabel(self, width=81, textvariable=self.subtotal_value, font=("roboto", 12, "bold", "bold"), pady=10, padx=10)
        self.subtotal_label.pack(side="left", pady=5, padx=5, fill="x")

        self.sep_label = CTkLabel(self, width=1, text="", bg_color="yellow")
        self.sep_label.pack(side="left", pady=5, padx=5, fill="x")

        self.destroy_line_button = CTkButton(self, width=30, text="X", font=("roboto", 14, "bold"), fg_color="black", hover=True, hover_color="orange", command=destroy_line)
        self.destroy_line_button.pack(side="left", pady=5, padx=5, fill="x")

