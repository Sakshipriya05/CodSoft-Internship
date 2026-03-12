import tkinter as tk
import random
from tkinter import messagebox

choices = ["Rock", "Paper", "Scissors"]


def play_game(user):
    computer = random.choice(choices)

    user_choice_label.config(text="User choice is: " + user)
    comp_choice_label.config(text="Computer choice is: " + computer)

    if user == computer:
        result = "It's a tie."
    elif user == "Rock" and computer == "Scissors":
        result = "You win...\nHurrahh!"
    elif user == "Paper" and computer == "Rock":
        result = "You win...\nHurrah !"
    elif user == "Scissors" and computer == "Paper":
        result = "You win...\nHurrah!"
    else:
        result = "Computer wins!"

    result_label.config(text="Result: " + result)


def exit_game():
    if messagebox.askyesno("Exit", "Do you want to exit the game?"):
        root.destroy()

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("420x350")
root.config(bg="#e8f5e9")

tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 16, "bold"), bg="#e8f5e9").pack(pady=10)

button_frame = tk.Frame(root, bg="#e8f5e9")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Rock", width=10, font=("Arial", 12), command=lambda: play_game("Rock")).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Paper", width=10, font=("Arial", 12), command=lambda: play_game("Paper")).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Scissors", width=10, font=("Arial", 12), command=lambda: play_game("Scissors")).grid(row=0, column=2, padx=10)

user_choice_label = tk.Label(root, text="User choice is: ", font=("Arial", 12), bg="#e8f5e9")
user_choice_label.pack(pady=5)

comp_choice_label = tk.Label(root, text="Computer choice is: ", font=("Arial", 12), bg="#e8f5e9")
comp_choice_label.pack(pady=5)

result_label = tk.Label(root, text="Result: ", font=("Arial", 12, "bold"), fg="#1b5e20", bg="#e8f5e9")
result_label.pack(pady=10)
tk.Button(root, text="Exit", command=exit_game, bg="#c62828", fg="white", font=("Arial", 12)).pack(pady=10)

root.mainloop()









