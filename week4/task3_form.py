import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Анкета користувача")

tk.Label(root, text="Ім'я:").grid(row=0, column=0, padx=5, pady=5)
name = tk.Entry(root)
name.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Стать:").grid(row=1, column=0, padx=5, pady=5)
gender = ttk.Combobox(root, values=["Чоловіча", "Жіноча"], state="readonly")
gender.grid(row=1, column=1, padx=5, pady=5)

agree = tk.BooleanVar()
tk.Checkbutton(root, text="Погоджуюсь із умовами", variable=agree).grid(row=2, column=0, columnspan=2, pady=5)

result = tk.Label(root, text="", relief="sunken", width=40)
result.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

def save():
    result.config(text=f"Ім'я: {name.get()}\nСтать: {gender.get()}\nПогоджено: {agree.get()}")

tk.Button(root, text="Зберегти", command=save).grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()
