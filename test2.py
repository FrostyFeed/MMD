import tkinter as tk
from tkinter import messagebox
from scipy.optimize import linprog

def solve_lp():
    try:
        arg1 = -float(entry_protein.get())
        arg2 = -float(entry_fat.get())
        arg3 = -float(entry_carbs.get())
        print(arg1,arg2,arg3)
        # Коефіцієнти цільової функції
        c = [-5, -30]

        # Коефіцієнти обмежень (змінені на ≤)
        A = [
            [-0.1, -0.2],
            [0, -0.5],
            [-0.5, -0.2]
        ]

        # Вектор обмежень
        b = [arg1, arg2, arg3]

        # Обмеження змінних (x1, x2 >= 0)
        x0_bounds = (0, None)
        x1_bounds = (0, None)

        # Розв'язання задачі
        result = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='simplex')
        messagebox.showinfo("Результат", f"Оптимальна дієта включає {result.x[0]:.2f} одиниць хліба і {result.x[1]:.2f} одиниць сала з мінімальною вартістю {abs(result.fun):.2f} у.о.")
        
    except ValueError:
        messagebox.showerror("Помилка вводу", "Будь ласка, введіть коректні числові значення.")

# Створення головного вікна
root = tk.Tk()
root.title("Лінійне програмування")

# Створення і розміщення елементів інтерфейсу
label_protein = tk.Label(root, text="Мінімальна кількість білку:")
label_protein.grid(row=0, column=0, padx=10, pady=5)
entry_protein = tk.Entry(root)
entry_protein.grid(row=0, column=1, padx=10, pady=5)

label_fat = tk.Label(root, text="Мінімальна кількість жирів:")
label_fat.grid(row=1, column=0, padx=10, pady=5)
entry_fat = tk.Entry(root)
entry_fat.grid(row=1, column=1, padx=10, pady=5)

label_carbs = tk.Label(root, text="Мінімальна кількість вуглеводів:")
label_carbs.grid(row=2, column=0, padx=10, pady=5)
entry_carbs = tk.Entry(root)
entry_carbs.grid(row=2, column=1, padx=10, pady=5)

button_solve = tk.Button(root, text="Розв'язати", command=solve_lp)
button_solve.grid(row=3, column=0, columnspan=2, pady=10)

# Запуск головного циклу обробки подій
root.mainloop()
