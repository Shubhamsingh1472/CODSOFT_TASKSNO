"""
CODSOFT - Python Programming Internship
Task 3: Password Generator

Generates a random password based on the length
and character types the user wants (letters, numbers, symbols).
"""

import random
from tkinter import *
from tkinter.ttk import Combobox


def generate_password():
    entry.delete(0, END)

    length = int(var1.get())

    if var.get() == 1:
        characters = "abcdefghijklmnopqrstuvwxyz"

    elif var.get() == 2:
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    elif var.get() == 3:
        characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

    else:
        entry.insert(0, "Select a strength")
        return

    password = ""

    for i in range(length):
        password += random.choice(characters)

    entry.insert(0, password)


root = Tk()
root.title("Random Password Generator")
root.geometry("650x350")
root.resizable(False, False)

root.configure(bg="#1e1e2f")

var = IntVar(value=2)
var1 = IntVar(value=12)


title = Label(
    root,
    text=" Random Password Generator",
    font=("Arial", 22, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=(25, 5))

subtitle = Label(
    root,
    text="Create a strong and secure password",
    font=("Arial", 11),
    bg="#1e1e2f",
    fg="#b8b8c7"
)
subtitle.pack(pady=(0, 20))


password_frame = Frame(
    root,
    bg="#292943",
    padx=15,
    pady=15
)
password_frame.pack(pady=5)

password_label = Label(
    password_frame,
    text="Password",
    font=("Arial", 12, "bold"),
    bg="#292943",
    fg="white"
)
password_label.grid(row=0, column=0, padx=10)

entry = Entry(
    password_frame,
    width=35,
    font=("Arial", 13),
    bg="white",
    fg="#222222",
    relief=FLAT
)
entry.grid(row=0, column=1, padx=10, ipady=7)


generate_button = Button(
    password_frame,
    text="Generate",
    command=generate_password,
    font=("Arial", 10, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    activeforeground="white",
    relief=FLAT,
    cursor="hand2",
    padx=20,
    pady=8
)
generate_button.grid(row=0, column=2, padx=5)


options_frame = Frame(
    root,
    bg="#1e1e2f"
)
options_frame.pack(pady=25)


length_label = Label(
    options_frame,
    text="Password Length:",
    font=("Arial", 11, "bold"),
    bg="#1e1e2f",
    fg="white"
)
length_label.grid(row=0, column=0, padx=10)


combo = Combobox(
    options_frame,
    textvariable=var1,
    state="readonly",
    width=8,
    font=("Arial", 11)
)

combo["values"] = tuple(range(8, 33))
combo.current(4)
combo.grid(row=0, column=1, padx=10)


strength_label = Label(
    options_frame,
    text="Strength:",
    font=("Arial", 11, "bold"),
    bg="#1e1e2f",
    fg="white"
)
strength_label.grid(row=1, column=0, pady=20)


radio_low = Radiobutton(
    options_frame,
    text="Low",
    variable=var,
    value=1,
    bg="#1e1e2f",
    fg="#ffcc00",
    selectcolor="#292943",
    activebackground="#1e1e2f",
    activeforeground="#ffcc00",
    font=("Arial", 10)
)
radio_low.grid(row=1, column=1, padx=5)


radio_medium = Radiobutton(
    options_frame,
    text="Medium",
    variable=var,
    value=2,
    bg="#1e1e2f",
    fg="#00d4ff",
    selectcolor="#292943",
    activebackground="#1e1e2f",
    activeforeground="#00d4ff",
    font=("Arial", 10)
)
radio_medium.grid(row=1, column=2, padx=5)


radio_strong = Radiobutton(
    options_frame,
    text="Strong",
    variable=var,
    value=3,
    bg="#1e1e2f",
    fg="#4CAF50",
    selectcolor="#292943",
    activebackground="#1e1e2f",
    activeforeground="#4CAF50",
    font=("Arial", 10)
)
radio_strong.grid(row=1, column=3, padx=5)


status_label = Label(
    root,
    text="Choose password length and strength",
    font=("Arial", 10),
    bg="#1e1e2f",
    fg="#b8b8c7"
)
status_label.pack(pady=5)


root.mainloop()
