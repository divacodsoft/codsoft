import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password(length, use_digits, use_special_chars):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def on_generate():
    length = int(length_var.get())
    use_digits = digits_var.get()
    use_special_chars = special_var.get()
    
    password = generate_password(length, use_digits, use_special_chars)
    password_var.set(password)

app = tk.Tk()
app.title("Password Generator")

frame = ttk.Frame(app, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

length_var = tk.IntVar(value=12)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)
password_var = tk.StringVar(value="Your password will appear here.")

ttk.Label(frame, text="Password Length:").grid(row=0, column=0, sticky=tk.W, pady=5)
ttk.Spinbox(frame, from_=4, to=32, textvariable=length_var, width=5).grid(row=0, column=1, sticky=tk.W, pady=5)

ttk.Checkbutton(frame, text="Include digits", variable=digits_var).grid(row=1, column=0, sticky=tk.W, pady=5)
ttk.Checkbutton(frame, text="Include special characters", variable=special_var).grid(row=2, column=0, sticky=tk.W, pady=5)

ttk.Button(frame, text="Generate Password", command=on_generate).grid(row=3, column=0, columnspan=2, pady=20)

ttk.Label(frame, text="Generated Password:").grid(row=4, column=0, sticky=tk.W, pady=5)
ttk.Entry(frame, textvariable=password_var, width=35, state="readonly").grid(row=4, column=1, pady=5)

app.mainloop()

