import tkinter as tk
import random
from tkinter import messagebox

def generate_password():
    try:
        length = int(entry.get())

        if length <= 0:
            messagebox.showwarning("Invalid Input", "Please enter a number greater than 0.")
            return

        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        symbols = "!~@#$%^&*><|\\/,"
        all_characters = letters + numbers + symbols

        password = ""
        for i in range(length):
            password += random.choice(all_characters)

        result_label.config(text="Generated Password:\n" + password)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")


root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.config(bg="#e0f7fa")


title = tk.Label(root, text="🔐 Password Generator", font=("Arial", 16, "bold"), bg="#e0f7fa")
title.pack(pady=10)

label = tk.Label(root, text="Enter Password Length:", font=("Arial", 12), bg="#e0f7fa")
label.pack()

entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=5)

button = tk.Button(root, text="Generate", font=("Arial", 12), bg="#26a69a", fg="white", command=generate_password)
button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="#e0f7fa")
result_label.pack(pady=10)

root.mainloop()
