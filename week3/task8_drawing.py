import tkinter as tk
from tkinter import colorchooser, filedialog

root = tk.Tk()
root.title("Графіка")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack(padx=5, pady=5)

color = tk.StringVar(value="black")
mode = tk.StringVar(value="line")
start_x, start_y = None, None
preview_tag = 'preview'

def on_press(e):
    global start_x, start_y
    canvas.delete(preview_tag)
    start_x, start_y = e.x, e.y

def on_drag(e):
    global start_x, start_y
    if start_x is None or start_y is None:
        return
    # remove previous preview
    canvas.delete(preview_tag)
    if mode.get() == "line":
        canvas.create_line(start_x, start_y, e.x, e.y, fill=color.get(), width=2, tags=preview_tag)
    else:
        r = ((e.x - start_x)**2 + (e.y - start_y)**2)**0.5
        canvas.create_oval(start_x-r, start_y-r, start_x+r, start_y+r, outline=color.get(), width=2, tags=preview_tag)

def choose_color():
    c = colorchooser.askcolor()[1]
    if c:
        color.set(c)

def clear():
    canvas.delete("all")

def save():
    file = filedialog.asksaveasfilename(defaultextension=".ps", filetypes=[("PostScript", "*.ps")])
    if file:
        canvas.postscript(file=file)

canvas.bind("<Button-1>", on_press)
canvas.bind("<B1-Motion>", on_drag)
canvas.bind("<ButtonRelease-1>", lambda e: on_release(e) if 'on_release' in globals() else None)

def on_release(e):
    global start_x, start_y
    if start_x is None or start_y is None:
        return
    # remove preview and draw permanent shape
    canvas.delete(preview_tag)
    if mode.get() == "line":
        canvas.create_line(start_x, start_y, e.x, e.y, fill=color.get(), width=2)
    else:
        r = ((e.x - start_x)**2 + (e.y - start_y)**2)**0.5
        canvas.create_oval(start_x-r, start_y-r, start_x+r, start_y+r, outline=color.get(), width=2)
    start_x, start_y = None, None

frame = tk.Frame(root)
frame.pack(pady=5)
tk.Button(frame, text="Колір", command=choose_color).pack(side="left", padx=2)
tk.Radiobutton(frame, text="Лінія", variable=mode, value="line").pack(side="left", padx=2)
tk.Radiobutton(frame, text="Коло", variable=mode, value="circle").pack(side="left", padx=2)
tk.Button(frame, text="Очистити", command=clear).pack(side="left", padx=2)
tk.Button(frame, text="Зберегти", command=save).pack(side="left", padx=2)

if __name__ == "__main__":
    root.mainloop()
