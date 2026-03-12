import tkinter as tk

expression = ""

def press(key):
    global expression
    expression += str(key)
    entry_var.set(expression)

def calculate():
    global expression
    try:
        result = str(eval(expression))
        entry_var.set(result)
        expression = result
    except ZeroDivisionError:
        entry_var.set("Cannot divide by 0")
        expression = ""
    except Exception:
        entry_var.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    entry_var.set("")


root = tk.Tk()
root.title("Calculator")
root.geometry("330x410")
root.resizable(False, False)
root.configure(bg="white")

entry_var = tk.StringVar()


entry = tk.Entry(root, textvariable=entry_var, font=('Arial', 20), bd=10,
                 relief=tk.RIDGE, justify='right', bg="white", fg="black")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=5, ipady=10)


buttons = [
    ('7', 1, 0), ('8', 1, 1),  ('9', 1, 2),  ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1),  ('6', 2, 2),  ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1),  ('3', 3, 2),  ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1),  ('+', 4, 2),  ('//', 4, 3),
    ('**', 5, 0), ('=', 5, 1)
]


for (text, row, col) in buttons:
    if text == '=':
        tk.Button(root, text=text, width=22, height=2, font=("Arial", 12),
                  bg="black", fg="white", command=calculate)\
            .grid(row=row, column=col, columnspan=3, padx=5, pady=5)
    elif text == 'C':
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 12),
                  bg="black", fg="white", command=clear)\
            .grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=text, width=5, height=2, font=("Arial", 12),
                  bg="black", fg="white", command=lambda t=text: press(t))\
            .grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
