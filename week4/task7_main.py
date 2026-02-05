import tkinter as tk
from task7_ui import MainWindow
from task7_logic import greet, process_data

if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
