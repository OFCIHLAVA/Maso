import customtkinter


class SellBar(customtkinter.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master=master, **kwargs)
        self.grid(row=2, column=0, sticky="sew")

        # Storno button
        self.storno_button = customtkinter.CTkButton(self, height=70, text="STORNO", font=("roboto", 12, "bold"), fg_color="red")
        self.storno_button.pack(side="left", fill="x", padx=10, pady=10, expand=True)
        # K pokladne button
        self.to_checkout_button = customtkinter.CTkButton(self, height=70, text="TO CHECKOUT", font=("roboto", 12, "bold"), fg_color="green")
        self.to_checkout_button.pack(side="left", fill="x", padx=10, pady=10, expand=True)

if __name__ == "__main__":
    root = customtkinter.CTk()
    sb = SellBar(root)
    root.mainloop()
