import tkinter as tk
from tkinter import ttk


def solve_quadratic():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        D = b ** 2 - 4 * a * c
        if D < 0:
            result_x1.set("Нет действительных корней")
            result_x2.set("")
        elif D == 0:
            x1 = -b / (2 * a)
            result_x1.set(f"{x1:.2f}")
            result_x2.set("")
        else:
            x1 = (-b + D ** 0.5) / (2 * a)
            x2 = (-b - D ** 0.5) / (2 * a)
            result_x1.set(f"{x1:.2f}")
            result_x2.set(f"{x2:.2f}")
    except ValueError:
        result_x1.set("Ошибка ввода")
        result_x2.set("")


root = tk.Tk()
root.title("Решение квадратного уравнения")

label_title = ttk.Label(root, text="Решение квадратного уравнения")
label_title.pack(pady=10)

label_title2 = ttk.Label(root, text="a * x^2 + b * x + c = 0")
label_title2.pack(pady=10)

frame_pattern = ttk.Frame(root)
frame_pattern.pack(pady=10)

label_a = ttk.Label(frame_pattern)
entry_a = ttk.Entry(frame_pattern, width=4)
label_x2 = ttk.Label(frame_pattern, text=" * x^2 + ")
label_b = ttk.Label(frame_pattern)
entry_b = ttk.Entry(frame_pattern, width=4)
label_x = ttk.Label(frame_pattern, text=" * x + ")
label_c = ttk.Label(frame_pattern)
entry_c = ttk.Entry(frame_pattern, width=4)
label_eq = ttk.Label(frame_pattern, text=" = 0")

label_a.grid(row=0, column=0)
entry_a.grid(row=0, column=1)
label_x2.grid(row=0, column=2)
label_b.grid(row=0, column=3)
entry_b.grid(row=0, column=4)
label_x.grid(row=0, column=5)
label_c.grid(row=0, column=6)
entry_c.grid(row=0, column=7)
label_eq.grid(row=0, column=8)

button_solve = ttk.Button(root, text="Решить", command=solve_quadratic)
button_solve.pack(pady=10)

frame_answer = ttk.Frame(root)
frame_answer.pack(pady=10)

result_x1 = tk.StringVar()
result_x2 = tk.StringVar()

label_x1 = ttk.Label(frame_answer, text="x1 = ")
label_result_x1 = ttk.Label(frame_answer, textvariable=result_x1, relief=tk.SUNKEN)
label_x2 = ttk.Label(frame_answer, text="x2 = ")
label_result_x2 = ttk.Label(frame_answer, textvariable=result_x2, relief=tk.SUNKEN)

label_x1.grid(row=0, column=0)
label_result_x1.grid(row=0, column=1)
label_x2.grid(row=1, column=0)
label_result_x2.grid(row=1, column=1)

root.mainloop()
