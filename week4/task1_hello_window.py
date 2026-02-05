import tkinter as tk

root = tk.Tk()
root.geometry("1024x768")
root.title("Перша програма")
tk.Label(root, text="Hello, world!", font=("Arial", 20)).pack(pady=300)
root.mainloop()
