import tkinter as tk

root = tk.Tk()
output = tk.Label(root, text="", font=("Arial", 14))
output.pack(pady=10)

tk.Button(root, text="Привітати", command=lambda: output.config(text="Вітаю, користувач!")).pack()
tk.Button(root, text="Очистити", command=lambda: output.config(text="")).pack()
tk.Button(root, text="Вийти", command=root.quit).pack()

root.mainloop()
