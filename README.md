import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mul(x, y):
    return x * y
def div(x, y):
    if y == 0:
        raise ValueError("Denominator cannot be zero.")
    return x / y
def exp(x, y):
    return x ** y

def calculate():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        choice = int(option_var.get())

        if choice == 1:
            result = add(x, y)
            result_text = f"Addition: {result}"
        elif choice == 2:
            result = sub(x, y)
            result_text = f"Subtraction: {result}"
        elif choice == 3:
            result = mul(x, y)
            result_text = f"Multiplication: {result}"
        elif choice == 4:
            result = div(x, y)
            result_text = f"Division: {result}"
        elif choice == 5:
            result = exp(x, y)
            result_text = f"Exponent: {result}"
        else:
            result_text = "Invalid choice"

        messagebox.showinfo("Result", result_text)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

#Setting up the main window
root = tk.Tk()
root.title("Basic Arithmetic Calculator")
root.configure(bg="#ADD8E6")  # set the background color of window

#Input fields
tk.Label(root, text="Enter first number:", bg="#ADD8E6", font=("Calibri", 16)).grid(row=0, column=0)
entry_x = tk.Entry(root, bg="#ADD8E6", font=("Calibri", 16))
entry_x.grid(row=0, column=1)

tk.Label(root, text="Enter second number:", bg="#ADD8E6", font=("Calibri", 16)).grid(row=1, column=0)
entry_y = tk.Entry(root, bg="#ADD8E6", font=("Calibri", 16))
entry_y.grid(row=1, column=1)

#Choices for arithmetic operations
option_var = tk.StringVar(value="1")
operations = [
    ("Addition", 1),
    ("Subtraction", 2),
    ("Multiplication", 3),
    ("Division", 4),
    ("Exponent", 5)
]

tk.Label(root, text="Choose operation:", bg="#ADD8E6", font=("Calibri", 16)).grid(row=2, column=0)
for text, value in operations:
    tk.Radiobutton(root, text=text, variable=option_var, value=value, bg="#ADD8E6", font=("Calibri", 16)).grid(sticky=tk.W)

#Customise the Calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate, bg="#00FF00", font=("Calibri", 18))
calculate_button.grid(row=6, columnspan=2, pady=10)

root.mainloop()    # Run the application
