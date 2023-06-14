import customtkinter
import json
from classes.tabs.shop.ItemLine import ItemLine
from functions.shop_tab_functions.quickbar_functions import get_available_products, get_product_data_for_item_line
from functions.shop_tab_functions.Item_list_functions import ItemLine


class QuickBar(customtkinter.CTkFrame):
    """
    This class represents a Quick Bar widget. It is used to display a bar of
    buttons that the user can customize. The bar's state and button configurations 
    are saved in a JSON file and are loaded when the Quick Bar is initialized. 

    The Quick Bar has two states: 'normal' and 'edit'. In the 'normal' state,
    clicking a button will trigger an event (such as adding an item to a cart).
    In the 'edit' state, clicking a button allows the user to change its configuration.

    Attributes:
        settings_file_path (str): The path to the JSON file where the Quick Bar's settings are saved.
        state (str): The current state of the Quick Bar, can be either 'normal' or 'edit'.
        options (list): List of options that the user can choose from when configuring a button.
        quickbar_buttons_settings (list): A 2D list representing the button configurations in the Quick Bar.
        buttons (list): A 2D list of CTkButton objects representing the buttons in the Quick Bar.

    """

    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        
        self.selling_observers = []
        self.grid(row=0, column=0, sticky="nsew")

        self.master.grid_columnconfigure(0,weight=1)
        self.master.grid_rowconfigure(0,weight=1)
        # Set settings file path
        self.settings_file_path = r"C:\Users\ondrej.rott\Documents\Python\MASO\PROJECT\settings\shop_quickbar_settings.json"
        
        # Load the last known buttons settings from saved JSON file
        self.quickbar_buttons_settings = self.load_quickbar_buttons_text(self.settings_file_path)
        print(self.quickbar_buttons_settings)
        
        # Set initial state to normal (normal / edit)
        self.state = "normal"

        # Configure grid resizing
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=0)
        self.grid_rowconfigure(1,weight=1)
        
        # Quick bar label
        self.quick_bar_label = customtkinter.CTkLabel(self, text="↓ QUICK BAR ↓", font=("roboto", 12, "bold"))
        self.quick_bar_label.grid(row=0, column=0, sticky='nsew', padx=5, pady=10)

        # Edit button
        self.edit_quickbar_button = customtkinter.CTkButton(self, height=20, width=50, text="Edit", command=self.switch_quickbar_state)
        self.edit_quickbar_button.grid(row=0, column=0, padx=10, pady=5, sticky="e")

        # Button field
        self.buttons_grid = customtkinter.CTkFrame(self)
        self.buttons_grid.grid(row=1, column=0, sticky='nsew', pady=10)

        # Populate the button grid with actual buttons based on last saved settings. Grid 3rows x 4collumns buttons.
        self.buttons = []
        for row in range(3):
            btn_row = []
            self.buttons_grid.grid_rowconfigure(row, weight=1) # set resizing for rows
            for column in range(4):
                self.buttons_grid.grid_columnconfigure(column, weight=1) # set resizing for columns
                button_current_produkt_id = self.quickbar_buttons_settings[row][column] # Check if this position have some produkt ID saved for this button in settings.
                if button_current_produkt_id != " ": # If some saved produkt ID, populate button with Name for that produkt ID that value.
                    current_produkt_record = get_available_products([button_current_produkt_id])[0] # Returns list of tuples with 1 tuple in it.
                    current_produkt_name = " - ".join([str(field) for field in current_produkt_record if field is not None]) # Format as text to show on buttons
                    btn = customtkinter.CTkButton(self.buttons_grid, fg_color="orange", hover_color="white", text=current_produkt_name, text_color="black", state="normal", command=lambda i=row, j=column: self.on_button_click(i, j))
                    btn.grid(row=row, column=column, sticky='nsew', padx=2, pady=2)
                    btn_row.append(btn)
                else: # Else load default empty button
                    btn = customtkinter.CTkButton(self.buttons_grid, fg_color="dark grey", text=" ", state="disabled", command=lambda i=row, j=column: self.on_button_click(i, j))
                    btn.grid(row=row, column=column, sticky='nsew', padx=2, pady=2)
                    btn_row.append(btn)
            self.buttons.append(btn_row)

    def on_button_click(self, row, column): # Functionality when some quick bar button clicked.
        if self.state == "normal":
            # add to selling items logic
            print("adding item to cart")
            # Get item data_dict from database
            sell_item_id = self.quickbar_buttons_settings[row][column]
            sell_item_data = get_product_data_for_item_line(sell_item_id)
            print(f"retrivnuta data {sell_item_data}")
            item_data_dict = self.create_item_data_dict(sell_item_data)
            print(f"postaveny data dict {item_data_dict}")

            # Create Item line in relvant elements
            for observer in self.selling_observers:
                observer.add_item_line(item_data_dict)
                pass
        elif self.state == "edit":
            self.edit_button(row, column)

    def edit_button(self, row, column): # Lets select what item should be bound to this buttons or clears bound item from this button.
        # Create a new toplevel window
        self.toplevel = customtkinter.CTkToplevel(self)

        # Make this new top level window to always stay on top and steal all focus on it.
        self.toplevel.attributes("-topmost", 1)
        self.toplevel.grab_set() # This makes focus on top level only, locking everything else until top level destroyed.

        # Make the top level window to appear an the location of clicked button
        x = self.buttons[row][column].winfo_rootx() # We can extract position info from button object in self.buttons list.
        y = self.buttons[row][column].winfo_rooty()

        # Move the toplevel window to the position of the button widget + set fixed size for it.
        self.toplevel.geometry(f"{200}x{180}+{x}+{y}")

        ## Select new item section of top level.
        # Create select label
        self.select_label = customtkinter.CTkLabel(self.toplevel, text="Vyber PRODUKT pro tuto pozici:", padx=5, pady=5)
        self.select_label.pack()

        # Create a Combobox
        # Define the options for the selection widget - select from db Items
        self.options = get_available_products() # Get all products records from database as list of tupples [(id, Name, druh, typ),]
        self.available_items = [" - ".join([str(field) for field in record if field is not None]) for record in self.options] # Format as text to show on buttons

        self.combo = customtkinter.CTkComboBox(self.toplevel, values=self.available_items)
        self.combo.pack()

        # Create a "Select" button
        self.select_button = customtkinter.CTkButton(self.toplevel, fg_color="dark green", hover_color="light green", text="Pridat", command=lambda: self.select_item_for_button(row, column))
        self.select_button.pack(pady=5)

        ## Clear item section
        # Create clear label
        self.clear_label = customtkinter.CTkLabel(self.toplevel, text="NEBO\nOdebrat stavajici polozku:", padx=5, pady=5)
        self.clear_label.pack()
        # Create a "Clear" button
        self.clear_btn = customtkinter.CTkButton(self.toplevel, text="X", fg_color="dark red", hover_color="red", command=lambda: self.clear_item_from_button(row, column))
        self.clear_btn.pack(pady=5)

        # Bind Enter key to select button
        self.toplevel.bind("<Return>", lambda event: self.select_item_for_button(row, column))

        # Bind Delete key to clear button
        self.toplevel.bind("<Delete>", lambda event: self.clear_item_from_button(row, column))

    def select_item_for_button(self, row, column): # Function to udate the button text with name of selected product from Combobox and save that product ID to settings for this button.
        self.buttons[row][column].configure(state="normal", fg_color="orange", hover_color="white", text=self.combo.get(), text_color="black")
        self.quickbar_buttons_settings[row][column] = int(self.combo.get().split(" - ", 1)[0]) # this gets produkt ID from record and saves it to settings
        print(self.quickbar_buttons_settings)

        # Destroy the toplevel window
        self.toplevel.destroy()

    def clear_item_from_button(self, row, column): # Removes bound item from given button.
        # Reset the button text to "+" - none selected value.
        self.buttons[row][column].configure(fg_color="light grey", hover_color="dark grey", text="+", text_color="black")
        self.quickbar_buttons_settings[row][column] = " " # this resets the settings for this button to default
        print(self.quickbar_buttons_settings)

        # Destroy the toplevel window
        self.toplevel.destroy()

    def switch_quickbar_state(self): # Depending on state of Quick bar, lets user Edit, or Save Buttons settings for the Quick bar.
        if self.state == "normal":
            self.state = "edit"
            self.edit_quickbar_button.configure(text="Save")
            for button_row in self.buttons:
                for button in button_row:
                    if button.cget("text") == " ": 
                        button.configure(state="normal", fg_color="light grey", hover_color="dark grey", text="+", text_color="black")
                    else:
                        button.configure(state="normal")    
        elif self.state == "edit":
            self.state = "normal"
            self.edit_quickbar_button.configure(text="Edit")
            for button_row in self.buttons:
                for button in button_row:
                    if button.cget("text") == "+":
                        button.configure(state="disabled", fg_color="dark grey", text=" ",)
                    else:
                        button.configure(state="normal", fg_color="orange", hover_color="white", text_color="black")
            # Save current buttons settings into JSON file
            with open(self.settings_file_path, "w") as f:
                json.dump(self.quickbar_buttons_settings, f)
    
    def load_quickbar_buttons_text(self, settings_file_path: str): # Loads last known Quick bar buttons settings when starting the app.
        default_settings = [
                            [" ", " ", " ", " "],
                            [" ", " ", " ", " "],
                            [" ", " ", " ", " "]
                           ]
        try:
            with open(settings_file_path, "r") as f:
                buttons_texts = json.load(f)
            return buttons_texts    
        except FileNotFoundError:
            print(f"Warning: Quick bar settings file not found → initializing Quick bar with default settings.")
            return default_settings
        except json.JSONDecodeError:
            print(f"Warning: Quick bar settings file appears to have invalid data or no data in it. → initializing Quick bar with default settings.")
            return default_settings

    def register_observer(self, observer): # Registers instance of some other class as Observer of this Quickbar instance to achive visibility connection between them
        self.selling_observers.append(observer)

    def create_item_data_dict(self, item_data: list): # Takes Item data from database record and returns dictionary for Item line instance creation.
        item_data_dict = dict()

        print(item_data)

        item_data_dict["id"] = item_data[0]
        item_data_dict["units"] = item_data[1]
        item_data_dict["name"] = " - ".join([str(field) for field in [item_data[2], item_data[3], item_data[4]] if field is not None])
        item_data_dict["price"] = item_data[5]
        item_data_dict["stock"] = 250 # TO link produkt stock QTY from database
        item_data_dict["icon_url"] = r"C:\Users\ondrej.rott\Documents\Python\MASO\Images\icon.gif" # TO link produkt ICON from DB


        return item_data_dict
 
