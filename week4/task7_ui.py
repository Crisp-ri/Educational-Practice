import tkinter as tk
from task7_logic import greet, process_data

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Модульна програма")
        self.root.geometry("400x300")
        
        tk.Label(self.root, text="Ім'я:", font=("Arial", 12)).pack(pady=5)
        self.name_entry = tk.Entry(self.root, width=30)
        self.name_entry.pack(pady=5)
        
        self.result = tk.Label(self.root, text="", font=("Arial", 12), relief="sunken", height=5)
        self.result.pack(padx=10, pady=10, fill="both", expand=True)
        
        tk.Button(self.root, text="Привітати", command=self.on_greet).pack(pady=5)
        tk.Button(self.root, text="Обробити", command=self.on_process).pack(pady=5)
    
    def on_greet(self):
        name = self.name_entry.get()
        self.result.config(text=greet(name))
    
    def on_process(self):
        data = self.name_entry.get()
        self.result.config(text=process_data(data))
