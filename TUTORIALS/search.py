import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.combo = ttk.Combobox(self.root)
        self.combo['values'] = ('Option 1', 'Option 2', 'Option 3')
        self.combo.grid(column=0, row=0)
        self.combo.bind("<<ComboboxSelected>>", self.on_combobox_select)

    def on_combobox_select(self, event):
        print(f"User selected: {self.combo.get()}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()