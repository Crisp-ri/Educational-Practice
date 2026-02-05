import tkinter as tk
from tkinter import ttk, colorchooser, filedialog
import json
import os

root = tk.Tk()
root.title("Налаштування")

nb = ttk.Notebook(root)
nb.pack(fill="both", expand=True, padx=5, pady=5)

tab1 = ttk.Frame(nb)
tab2 = ttk.Frame(nb)
tab3 = ttk.Frame(nb)
nb.add(tab1, text="Головна")
nb.add(tab2, text="Налаштування")
nb.add(tab3, text="Про програму")

tk.Label(tab1, text="Форма введення", font=("Arial", 14)).pack(pady=10)
tk.Entry(tab1, width=30).pack(pady=5)
tk.Button(tab1, text="Зберегти").pack(pady=5)

color_var = tk.StringVar(value="#ffffff")
config_file = "config.json"

def load_config():
    if os.path.exists(config_file):
        with open(config_file, 'r') as f:
            data = json.load(f)
            color_var.set(data.get("color", "#ffffff"))
            root.config(bg=color_var.get())

def choose_color():
    color = colorchooser.askcolor()[1]
    if color:
        color_var.set(color)
        root.config(bg=color)
        with open(config_file, 'w') as f:
            json.dump({"color": color}, f)

tk.Label(tab2, text="Колір фону").pack(pady=10)
tk.Button(tab2, text="Вибрати колір", command=choose_color).pack(pady=5)

tk.Label(tab3, text="Про програму\nАвтор: Студент", font=("Arial", 12)).pack(pady=20)

load_config()
root.mainloop()
