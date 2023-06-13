import customtkinter
import json

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
        
        # Set settings file path
        self.settings_file_path = r"C:\Users\ondrej.rott\Documents\Python\MASO\PROJECT\settings\shop_quickbar_settings.json"
        
        # Load the last known buttons settings from saved JSON file
        self.quickbar_buttons_settings = self.load_quickbar_buttons_text(self.settings_file_path)
        
        # Set initial state to normal (normal / edit)
        self.state = "normal"

        # Configure grid resizing
        
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=0)
        self.grid_rowconfigure(1,weight=0)
        self.grid_rowconfigure(2,weight=1)
        
        # Quick bar label
        self.quick_bar_label = customtkinter.CTkLabel(self, fg_color="red", text="QUICK BAR")
        self.quick_bar_label.grid(row=0, column=0, sticky='nsew', padx=10, pady=20)

        # Edit button
        self.edit_quickbar_button = customtkinter.CTkButton(self, text="Edit", command=self.switch_state)
        self.edit_quickbar_button.grid(row=1, column=0, padx=20, sticky="w")

        # Button field
        self.buttons_grid = customtkinter.CTkFrame(self, fg_color="red")
        self.buttons_grid.grid(row=2, column=0, sticky='nsew', padx=10, pady=20)

        # TODO - connect to db items
        # Define the options for the selection widget - select from db Items
        self.options = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]



        # Initialize the grid of buttons
        self.buttons = []
        for row in range(4):
            btn_row = []
            self.buttons_grid.grid_rowconfigure(row, weight=1)
            for column in range(4):
                self.buttons_grid.grid_columnconfigure(column, weight=1)
                button_current_item = self.quickbar_buttons_settings[row][column]
                if button_current_item != " ": # If some saved value, load active button with that value
                    btn = customtkinter.CTkButton(self.buttons_grid, fg_color="orange", hover_color="white", text=button_current_item, text_color="black", state="normal", command=lambda i=row, j=column: self.on_button_click(i, j))
                    btn.grid(row=row, column=column, sticky='nsew', padx=2, pady=2)
                    btn_row.append(btn)
                else: # Else load default empty button
                    btn = customtkinter.CTkButton(self.buttons_grid, fg_color="dark grey", text=" ", state="disabled", command=lambda i=row, j=column: self.on_button_click(i, j))
                    btn.grid(row=row, column=column, sticky='nsew', padx=2, pady=2)
                    btn_row.append(btn)
            self.buttons.append(btn_row)

    def on_button_click(self, row, column):
        if self.state == "normal":
            # add to selling items logic
            print("adding item to cart")
            pass
        elif self.state == "edit":
            self.edit_field(row, column)

    def edit_field(self, row, column):
        # Create a new toplevel window
        self.toplevel = customtkinter.CTkToplevel(self)

        # Update idletasks to make sure we get the correct position
        self.toplevel.update_idletasks()

        # Make this new top level window to always stay on top and steal all focus on it.
        self.toplevel.attributes("-topmost", 1)
        self.toplevel.grab_set() # This makes focus on top level only, locking everything else until top level destroyed.

        # Make the top level window to appear an the locatino of clickd button
        x = self.buttons[row][column].winfo_rootx() # We can extract position info from button object in self.buttons list.
        y = self.buttons[row][column].winfo_rooty()

        # Move the toplevel window to the position of the button widget
        self.toplevel.geometry(f"{200}x{180}+{x}+{y}")

        ## Select new item section
        # Create select label
        self.select_label = customtkinter.CTkLabel(self.toplevel, text="Vyber polozku pro tuto pozici:", padx=5, pady=5)
        self.select_label.pack()

        # Create a Combobox
        self.combo = customtkinter.CTkComboBox(self.toplevel, values=self.options)
        self.combo.pack()
        # Create a "Select" button
        self.select_btn = customtkinter.CTkButton(self.toplevel, fg_color="dark green", hover_color="light green", text="Pridat", command=lambda: self.on_select_click(row, column))
        self.select_btn.pack(pady=5)

        ## Clear item section
        # Create clear label
        self.clear_label = customtkinter.CTkLabel(self.toplevel, text="NEBO\nOdebrat stavajici polozku:", padx=5, pady=5)
        self.clear_label.pack()
        # Create a "Clear" button
        self.clear_btn = customtkinter.CTkButton(self.toplevel, text="X", fg_color="dark red", hover_color="red", command=lambda: self.on_clear_click(row, column))
        self.clear_btn.pack(pady=5)

        # Bind Enter key to select button
        self.toplevel.bind("<Return>", lambda event: self.on_select_click(row, column))

        # Bind Delete key to clear button
        self.toplevel.bind("<Delete>", lambda event: self.on_clear_click(row, column))

    def on_select_click(self, row, column):
        # Update the button text
        self.buttons[row][column].configure(state="normal", fg_color="orange", hover_color="white", text=self.combo.get(), text_color="black")

        # Destroy the toplevel window
        self.toplevel.destroy()

    def on_clear_click(self, row, column):
        # Update the button text
        self.buttons[row][column].configure(fg_color="light grey", hover_color="dark grey", text="+", text_color="black")

        # Destroy the toplevel window
        self.toplevel.destroy()

    def switch_state(self):
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
            self.quickbar_buttons_state = [[button.cget("text") for button in row] for row in self.buttons]
            with open(self.settings_file_path, "w") as f:
                json.dump(self.quickbar_buttons_state, f)
    
    def load_quickbar_buttons_text(self, settings_file_path: str):
        default_settings = [
                            [" ", " ", " ", " "],
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


if __name__ == "__main__":
    root = customtkinter.CTk()
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")
    # Configure the shop tab grid
    root.grid_columnconfigure(0, weight=1)
    root.grid_rowconfigure(0, weight=1)

    app = QuickBar(root)
    app.grid(sticky="nsew")
    root.mainloop()
