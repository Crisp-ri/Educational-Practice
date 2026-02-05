import tkinter as tk

root = tk.Tk()
root.title("Калькулятор")

num1 = tk.Entry(root, width=15)
num1.pack(padx=5, pady=5)
num2 = tk.Entry(root, width=15)
num2.pack(padx=5, pady=5)

result = tk.Label(root, text="Результат", font=("Arial", 12), relief="sunken", width=20)
result.pack(padx=5, pady=5)

def calc(op):
    try:
        a, b = float(num1.get()), float(num2.get())
        res = {'+': a+b, '-': a-b, '*': a*b, '/': a/b if b != 0 else "Помилка: ділення на 0"}[op]
        result.config(text=f"Результат: {res}")
    except:
        result.config(text="Помилка: невірні дані")

frame = tk.Frame(root)
frame.pack(padx=5, pady=5)
tk.Button(frame, text="+", command=lambda: calc('+')).pack(side="left", padx=2)
tk.Button(frame, text="-", command=lambda: calc('-')).pack(side="left", padx=2)
tk.Button(frame, text="*", command=lambda: calc('*')).pack(side="left", padx=2)
tk.Button(frame, text="/", command=lambda: calc('/')).pack(side="left", padx=2)

root.mainloop()
