import tkinter as tk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Блокнот")
root.geometry("600x400")

text = tk.Text(root, font=("Arial", 12))
text.pack(fill="both", expand=True)

current_file = None
saved = True

def open_file():
    global current_file, saved
    file = filedialog.askopenfilename(filetypes=[("Text", "*.txt"), ("All", "*.*")])
    if file:
        current_file = file
        with open(file, 'r') as f:
            text.delete("1.0", "end")
            text.insert("1.0", f.read())
        saved = True
        root.title(f"Блокнот - {file}")

def save_file():
    global current_file, saved
    if not current_file:
        current_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text", "*.txt"), ("All", "*.*")])
    if current_file:
        with open(current_file, 'w') as f:
            f.write(text.get("1.0", "end-1c"))
        saved = True
        root.title(f"Блокнот - {current_file}")

def exit_app():
    global saved
    if not saved and messagebox.askyesno("Попередження", "Зберегти файл перед виходом?"):
        save_file()
    root.quit()

menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Відкрити", command=open_file)
file_menu.add_command(label="Зберегти", command=save_file)
file_menu.add_command(label="Вийти", command=exit_app)

text.bind("<KeyRelease>", lambda e: globals().__setitem__('saved', False))

root.mainloop()
