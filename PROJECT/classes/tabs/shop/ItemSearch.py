import tkinter
import customtkinter
import sqlite3

class ItemSearch(customtkinter.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, height=150, **kwargs)
        #self.pack(side="top", pady=10, padx=5, fill="both")
        self.grid(row=1, column=0, sticky="ew")
        self.grid_columnconfigure(0, weigh=1)
        
        
        # Set database path
        self.database_path = r"C:\Users\ondrej.rott\Documents\Python\MASO\inventory.db"
        # Dummy list database options
        self.options = ["ondra", "Ondra", " Martin", "ONdra Martin", "ho v no", "LOpata "]
        # Dummy list for items already selected for sell - these will not appear in options to select
        self.already_selected = []
        # Search results for autosuggestion when searching
        self.results = []
        
        # Quick bar label
        self.quick_bar_label = customtkinter.CTkLabel(self, text="↓ SEARCH PRODUKT ↓", font=("roboto", 12, "bold"))
        self.quick_bar_label.grid(row=0, column=0, sticky='nsew', padx=5, pady=10)
        
        # Create search window inside inner container Frame
        self.search_window = customtkinter.CTkEntry(self, text_color="grey")
        self.search_window.grid(row=1, column=0, sticky="ew")
         
        # Create results frame
        self.results_frame = customtkinter.CTkFrame(self, height=80,fg_color="#2D2D2D")
        self.results_frame.grid(row=2, column=0, sticky="ew")

        # Binding for placeholder to search window
        self.search_window.bind("<FocusIn>", self.clear_placeholder_text)
        self.search_window.bind("<FocusOut>", self.set_placeholder_text)
        # Binding the auto updating of options as you type into search window (auto suggestions)
        self.search_window.bind("<KeyRelease>", self.update_search_results)

        # Create ListBox for search results
        self.search_results_listbox = tkinter.Listbox(self.results_frame, height=5)
        # Create scrollbar for listbox
        #self.search_results_scrollbar = customtkinter.CTkScrollbar(self.results_frame)
        #self.search_results_scrollbar.pack(side=customtkinter.RIGHT, fill=customtkinter.Y)

        # Bind the ListBox selection event to a function
        self.search_results_listbox.bind('<<ListboxSelect>>', self.on_listbox_select)

        self.set_placeholder_text() 

    def clear_placeholder_text(self, event):
        print("focusuju in")
        self.search_window.delete(0, 'end')
        print(self.search_window.get())
        self.search_window.configure(text_color="white")
        self.update_search_results(event)
    
    def set_placeholder_text(self, *args):
        print("focusuju out a nastavuju placeholder")
        self.search_results_listbox.pack_forget()
        self.search_window.delete(0, "end")
        self.search_window.insert(0, "Hledat produkt...")
        self.search_window.configure(text_color="grey")        

    def on_listbox_select(self, event):
        # Get the currently selected item and set it as the Entry text
        try:
            selection = self.search_results_listbox.get(self.search_results_listbox.curselection())
            # TODO move selected item to list of items beeing sold ↓↓
            self.already_selected.append(selection)
        except tkinter.TclError:
            pass
        # Update options again to acount for newly selected item
        self.update_search_results(event)

    def update_search_results(self, event):
        # If nothing left to show → show info.
        if len(self.options) - len(self.already_selected) == 0:
            print("uz nezbylo nic k vybrani")
            self.search_window.delete(0, 'end')
            self.search_window.insert(0, f"There no other items to be selected")
            self.search_window.configure(text_color="grey")
            self.search_results_listbox.forget()      
        # Get current search text
        else:
            text_to_search_for = self.search_window.get().lower().strip()
            print(f'hledam text {text_to_search_for}')
            if text_to_search_for: # filtered search
                print("je tedxdt")
                self.results = [item for item in self.options if text_to_search_for in item.lower() and item not in self.already_selected]
                print("filtered non selected result")
                print(self.results)
            # If clicked into empty search window, show all the options without filtering
            else:
                print("neni tedxdt")
                self.results = [item for item in self.options if item not in self.already_selected]
                print("non selected result")
                print(self.results)
            if self.results:
                # Clear current search results
                self.search_results_listbox.delete(0, 'end')
                # Display results to listbox
                for result in sorted(self.results, key=lambda s: s.strip().lower()):
                    self.search_results_listbox.insert(tkinter.END, result)
                # Show the ListBox if it's not currently visible
                if not self.search_results_listbox.winfo_viewable():
                    self.search_results_listbox.pack(fill="x", expand=True)
            # If nothing else can be selected → hide options list
            else:
                if text_to_search_for:
                    self.search_results_listbox.forget()               


if __name__ == "__main__":
    root = customtkinter.CTk()
    search = ItemSearch(root)
    root.mainloop()