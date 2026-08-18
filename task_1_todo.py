"""
CODSOFT - Python Programming Internship
Task 1: To-Do List Application

"""

import json
import os
import tkinter as tk
from tkinter import messagebox

DATA_FILE = "tasks.json"

BG_COLOR = "#0F6E7A"      
TITLE_COLOR = "white"
BTN_BG = "#E8F6F7"      
BTN_FG = "#0B4F58"
LIST_BG = "#F4FBFC"
LIST_SELECT_BG = "#1CA3B0"


class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Manager")
        self.root.geometry("560x420")
        self.root.configure(bg=BG_COLOR)
        self.root.resizable(False, False)

        self.tasks = []
        self.load_tasks()

        self._build_ui()
        self._refresh_listbox()

   
    def _build_ui(self):
        # Title
        tk.Label(
            self.root, text="To-Do List", bg=BG_COLOR, fg=TITLE_COLOR,
            font=("Segoe UI", 26, "bold")
        ).pack(pady=(20, 10))

        # Main content area: left = entry + buttons, right = listbox
        content = tk.Frame(self.root, bg=BG_COLOR)
        content.pack(fill="both", expand=True, padx=30, pady=10)

        left = tk.Frame(content, bg=BG_COLOR)
        left.pack(side="left", fill="y", padx=(0, 20))

        tk.Label(
            left, text="Enter the Task:", bg=BG_COLOR, fg=TITLE_COLOR,
            font=("Segoe UI", 11, "bold")
        ).pack(anchor="w", pady=(0, 4))

        self.task_entry = tk.Entry(left, width=22, font=("Segoe UI", 11))
        self.task_entry.pack(pady=(0, 14))
        self.task_entry.bind("<Return>", lambda e: self.add_task())

        tk.Button(
            left, text="Add Task", width=18, bg=BTN_BG, fg=BTN_FG,
            font=("Segoe UI", 10, "bold"), relief="raised", command=self.add_task
        ).pack(pady=6)

        tk.Button(
            left, text="Delete Task", width=18, bg=BTN_BG, fg=BTN_FG,
            font=("Segoe UI", 10, "bold"), relief="raised", command=self.delete_task
        ).pack(pady=6)

        tk.Button(
            left, text="Exit", width=18, bg=BTN_BG, fg=BTN_FG,
            font=("Segoe UI", 10, "bold"), relief="raised", command=self.root.destroy
        ).pack(pady=6)

        # Right: listbox with scrollbar
        right = tk.Frame(content, bg=BG_COLOR)
        right.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(right)
        scrollbar.pack(side="right", fill="y")

        self.task_listbox = tk.Listbox(
            right, width=30, height=13, font=("Segoe UI", 11),
            bg=LIST_BG, fg="#0B4F58", selectmode="single",
            selectbackground=LIST_SELECT_BG, selectforeground="white",
            yscrollcommand=scrollbar.set
        )
        self.task_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.task_listbox.yview)

    
    def load_tasks(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r", encoding="utf-8") as f:
                    self.tasks = json.load(f)
            except (json.JSONDecodeError, OSError):
                self.tasks = []

    def save_tasks(self):
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, indent=2)

    
    def add_task(self):
        task = self.task_entry.get().strip()
        if not task:
            messagebox.showwarning("Missing task", "Please enter a task.")
            return
        self.tasks.append(task)
        self.save_tasks()
        self._refresh_listbox()
        self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showinfo("No selection", "Select a task to delete.")
            return
        index = selection[0]
        removed = self.tasks.pop(index)
        self.save_tasks()
        self._refresh_listbox()

    def _refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
