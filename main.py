import tkinter as tk

# 80 мм при типичных 96 DPI ≈ 302 пикселя
# (1 дюйм = 25.4 мм, 80/25.4*96 ≈ 302)
SIZE_PX = 302

GREEN = "#00AA00"   # заливка основного окна
YELLOW = "#FFFF99"  # заливка полей ввода
BLUE = "#0000CC"    # цвет шрифта

FONT = ("Arial", 7, "bold")  # мелкий шрифт, чтобы всё поместилось

root = tk.Tk()
root.title("Умножение")
root.geometry(f"{SIZE_PX}x{SIZE_PX}")
root.configure(bg=GREEN)
root.resizable(False, False)

def multiply(*args):
    """Пересчитывает итог при любом изменении полей."""
    try:
        a = float(entry1.get())
    except ValueError:
        a = 0.0
    try:
        b = float(entry2.get())
    except ValueError:
        b = 0.0
    result_var.set(f"{a * b:g}")

# Переменные
result_var = tk.StringVar(value="0")
v1 = tk.StringVar()
v2 = tk.StringVar()
v1.trace_add("write", multiply)
v2.trace_add("write", multiply)

# Поле "аргумент 1"
tk.Label(root, text="аргумент 1", bg=GREEN, fg=BLUE,
         font=FONT).pack(pady=(8, 0))
entry1 = tk.Entry(root, width=5, bg=YELLOW, fg=BLUE,
                  font=FONT, justify="center", textvariable=v1)
entry1.pack()

# Поле "аргумент 2"
tk.Label(root, text="аргумент 2", bg=GREEN, fg=BLUE,
         font=FONT).pack(pady=(8, 0))
entry2 = tk.Entry(root, width=5, bg=YELLOW, fg=BLUE,
                  font=FONT, justify="center", textvariable=v2)
entry2.pack()

# Поле "итог"
tk.Label(root, text="итог", bg=GREEN, fg=BLUE,
         font=FONT).pack(pady=(8, 0))
result_entry = tk.Entry(root, width=5, bg=YELLOW, fg=BLUE,
                        font=FONT, justify="center",
                        textvariable=result_var, state="readonly")
result_entry.pack()

root.mainloop()
