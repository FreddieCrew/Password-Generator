import tkinter as tk
from tkinter import ttk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x450")
        
        self.root.configure(bg="#333333")
        
        self.generate_button_style = ttk.Style()
        self.generate_button_style.configure("Generate.TButton", background="#4287f5", foreground="white")
        self.generate_button_style.map("Generate.TButton",
                                       background=[("active", "#3570d8")],
                                       foreground=[("active", "white")])
        
        self.length_label = ttk.Label(root, text="Password Length:", background="#333333", foreground="white")
        self.length_label.pack(pady=10)
        
        self.length_var = tk.IntVar()
        self.length_entry = ttk.Entry(root, textvariable=self.length_var)
        self.length_entry.pack()
        
        self.uppercase_var = tk.BooleanVar()
        self.uppercase_check = ttk.Checkbutton(root, text="Include uppercase letters", variable=self.uppercase_var,
                                               style="Dark.TCheckbutton")
        self.uppercase_check.pack(anchor="w")
        
        self.symbols_var = tk.BooleanVar()
        self.symbols_check = ttk.Checkbutton(root, text="Include symbols", variable=self.symbols_var,
                                             style="Dark.TCheckbutton")
        self.symbols_check.pack(anchor="w")
        
        self.numbers_var = tk.BooleanVar()
        self.numbers_check = ttk.Checkbutton(root, text="Include numbers", variable=self.numbers_var,
                                             style="Dark.TCheckbutton")
        self.numbers_check.pack(anchor="w")
        
        self.generate_button = ttk.Button(root, text="Generate Password", command=self.generate_password,
                                          style="Generate.TButton")
        self.generate_button.pack(pady=10)
        
        self.result_var = tk.StringVar()
        self.result_entry = ttk.Entry(root, textvariable=self.result_var, state="readonly")
        self.result_entry.pack(pady=10)
        
        self.result_label = ttk.Label(root, text="Result:", background="#333333", foreground="white")
        self.result_label.pack()
        self.result_label.pack_forget()
        
        self.result_entry.pack_forget()

    def generate_password(self):
        length = self.length_var.get()
        include_uppercase = self.uppercase_var.get()
        include_symbols = self.symbols_var.get()
        include_numbers = self.numbers_var.get()
        
        characters = string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_symbols:
            characters += string.punctuation
        if include_numbers:
            characters += string.digits
        
        password = ''.join(random.choice(characters) for _ in range(length))
        self.result_var.set(password)
        
        self.result_label.pack()
        self.result_entry.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
