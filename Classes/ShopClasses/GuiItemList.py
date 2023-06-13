from customtkinter import CTkScrollableFrame, CTkLabel

class ItemList(CTkScrollableFrame):
    
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.pack(side="top", pady=10, padx=5, fill="both", expand=True)