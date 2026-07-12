import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.expression = ""

        self.input_var = tk.StringVar()
        self.create_widgets()
        self.bind_keyboard()

    def create_widgets(self):
        entry = tk.Entry(
            self.root, textvariable=self.input_var, font=("Arial", 20),
            bd=10, relief=tk.RIDGE, justify="right"
        )
        entry.pack(fill=tk.BOTH, padx=10, pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill=tk.BOTH, padx=10, pady=(0, 10))
        button_frame.grid_rowconfigure(0, weight=1)
        button_frame.grid_columnconfigure(0, weight=1)

        buttons = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("C", "0", ".", "+"),
            ("=",)
        ]

        for r, row in enumerate(buttons):
            for c, text in enumerate(row):
                btn = tk.Button(
                    button_frame, text=text, font=("Arial", 14),
                    command=lambda t=text: self.on_button_click(t)
                )
                btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)
                button_frame.grid_columnconfigure(c, weight=1)

        button_frame.grid_rowconfigure(len(buttons) - 1, weight=1)

    def bind_keyboard(self):
        self.root.bind("<Key>", self.on_key_press)

    def on_key_press(self, event):
        key = event.char
        if key in "0123456789+-*/.=":
            self.on_button_click(key)
        elif key == "\r":
            self.on_button_click("=")
        elif key == "\x08":
            self.on_button_click("C")

    def on_button_click(self, text):
        if text == "C":
            self.expression = ""
            self.input_var.set("")
        elif text == "=":
            try:
                result = eval(self.expression)
                self.input_var.set(str(result))
                self.expression = str(result)
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                self.expression = ""
                self.input_var.set("")
            except Exception:
                messagebox.showerror("Error", "Invalid expression")
                self.expression = ""
                self.input_var.set("")
        else:
            self.expression += text
            self.input_var.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
