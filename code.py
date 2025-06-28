import tkinter as tk
from tkinter import messagebox
import re
# Function to check password strength
def check_strength():
    password = entry.get()
    length_error = len(password) < 8
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    digit_error = not re.search(r"\d", password)
    special_char_error = not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    score = 5 - sum([length_error, uppercase_error, lowercase_error, digit_error, special_char_error])
    if score == 5:
        result = "Strong Password"
        color = "green"
    elif 3 <= score < 5:
        result = "Medium Password"
        color = "orange"
    else:
        result = "Weak Password"
        color = "red"
    result_label.config(text=result, fg=color)
# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")
root.config(bg="#f0f0f0")
title = tk.Label(root, text="Enter your password:", font=("Helvetica", 12), bg="#f0f0f0")
title.pack(pady=10)
entry = tk.Entry(root, show="*", font=("Helvetica", 12), width=30)
entry.pack()
check_btn = tk.Button(root, text="Check Strength", command=check_strength, font=("Helvetica", 11, "bold"), bg="#4CAF50", fg="white")
check_btn.pack(pady=10)
result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#f0f0f0")
result_label.pack()
root.mainloop()



