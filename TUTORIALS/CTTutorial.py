import tkinter as tk

root = tk.Tk()

# Create two frames
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

# Position frames using grid
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)

# Create widgets within frames
label1 = tk.Label(frame1, text="Frame 1")
label1.pack()

label2 = tk.Label(frame2, text="Frame 2")
label2.pack()

root.mainloop()