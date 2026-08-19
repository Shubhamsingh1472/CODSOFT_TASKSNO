"""
CODSOFT - Python Programming Internship
Task 4: Rock-Paper-Scissors Game

"""
import tkinter as tk
import random


choices = ["Rock", "Paper", "Scissors"]
user_score = 0
computer_score = 0
round_number = 0


def play_game(user_choice):
    global user_score, computer_score, round_number

    computer_choice = random.choice(choices)
    round_number += 1

 
    user_choice_label.config(text=f"You: {user_choice}")
    computer_choice_label.config(text=f"Computer: {computer_choice}")
    round_label.config(text=f"Round {round_number}")


    if user_choice == computer_choice:
        result_label.config(
            text="It's a Tie!",
            fg="#f59e0b"
        )

    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or
        (user_choice == "Paper" and computer_choice == "Rock")
        or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        user_score += 1
        result_label.config(
            text="You Win!",
            fg="#16a34a"
        )

    else:
        computer_score += 1
        result_label.config(
            text="Computer Wins!",
            fg="#dc2626"
        )

    
    score_label.config(
        text=f"You     {user_score}     :     {computer_score}     Computer"
    )


def reset_game():
    global user_score, computer_score, round_number

    user_score = 0
    computer_score = 0
    round_number = 0

    user_choice_label.config(text="You: -")
    computer_choice_label.config(text="Computer: -")
    result_label.config(
        text="Choose your move!",
        fg="#1f2937"
    )
    score_label.config(
        text="You     0     :     0     Computer"
    )
    round_label.config(text="Round 0")


window = tk.Tk()
window.title("Rock Paper Scissors")
window.geometry("600x650")
window.resizable(False, False)
window.configure(bg="#f3f4f6")


header = tk.Frame(
    window,
    bg="#1f2937",
    height=120
)
header.pack(fill="x")

title_label = tk.Label(
    header,
    text="ROCK  PAPER  SCISSORS",
    font=("Arial", 25, "bold"),
    bg="#1f2937",
    fg="white"
)
title_label.pack(pady=(25, 5))

subtitle_label = tk.Label(
    header,
    text="CODSOFT • Python Internship • Task 4",
    font=("Arial", 11),
    bg="#1f2937",
    fg="#d1d5db"
)
subtitle_label.pack()


round_label = tk.Label(
    window,
    text="Round 0",
    font=("Arial", 12, "bold"),
    bg="#f3f4f6",
    fg="#6b7280"
)
round_label.pack(pady=(25, 5))


result_label = tk.Label(
    window,
    text="Choose your move!",
    font=("Arial", 22, "bold"),
    bg="#f3f4f6",
    fg="#1f2937"
)
result_label.pack(pady=15)


choice_frame = tk.Frame(
    window,
    bg="#f3f4f6"
)
choice_frame.pack(pady=10)

user_choice_label = tk.Label(
    choice_frame,
    text="You: -",
    font=("Arial", 14, "bold"),
    bg="white",
    fg="#374151",
    width=18,
    height=2
)
user_choice_label.grid(row=0, column=0, padx=8)

computer_choice_label = tk.Label(
    choice_frame,
    text="Computer: -",
    font=("Arial", 14, "bold"),
    bg="white",
    fg="#374151",
    width=18,
    height=2
)
computer_choice_label.grid(row=0, column=1, padx=8)


instruction_label = tk.Label(
    window,
    text="Make your choice",
    font=("Arial", 13),
    bg="#f3f4f6",
    fg="#6b7280"
)
instruction_label.pack(pady=(25, 10))


button_frame = tk.Frame(
    window,
    bg="#f3f4f6"
)
button_frame.pack()

rock_button = tk.Button(
    button_frame,
    text="ROCK",
    font=("Arial", 13, "bold"),
    width=12,
    height=2,
    bg="#e5e7eb",
    fg="#111827",
    activebackground="#d1d5db",
    relief="flat",
    cursor="hand2",
    command=lambda: play_game("Rock")
)
rock_button.grid(row=0, column=0, padx=6)

paper_button = tk.Button(
    button_frame,
    text="PAPER",
    font=("Arial", 13, "bold"),
    width=12,
    height=2,
    bg="#e5e7eb",
    fg="#111827",
    activebackground="#d1d5db",
    relief="flat",
    cursor="hand2",
    command=lambda: play_game("Paper")
)
paper_button.grid(row=0, column=1, padx=6)

scissors_button = tk.Button(
    button_frame,
    text="SCISSORS",
    font=("Arial", 13, "bold"),
    width=12,
    height=2,
    bg="#e5e7eb",
    fg="#111827",
    activebackground="#d1d5db",
    relief="flat",
    cursor="hand2",
    command=lambda: play_game("Scissors")
)
scissors_button.grid(row=0, column=2, padx=6)

score_label = tk.Label(
    window,
    text="You     0     :     0     Computer",
    font=("Arial", 16, "bold"),
    bg="#1f2937",
    fg="white",
    width=35,
    height=2
)
score_label.pack(pady=35)

reset_button = tk.Button(
    window,
    text="RESET GAME",
    font=("Arial", 11, "bold"),
    width=18,
    height=2,
    bg="#ef4444",
    fg="white",
    activebackground="#dc2626",
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    command=reset_game
)
reset_button.pack()

footer_label = tk.Label(
    window,
    text="Made with Python & Tkinter",
    font=("Arial", 9),
    bg="#f3f4f6",
    fg="#9ca3af"
)
footer_label.pack(side="bottom", pady=15)


window.mainloop()
