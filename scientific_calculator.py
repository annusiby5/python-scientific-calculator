import tkinter as tk
from tkinter import messagebox
import math
from datetime import datetime

class ScientificCalculator:

    def __init__(self, root):
        self.root = root
        self.root.title("CalcMaster")
        self.root.geometry("700x600")

        self.memory = 0
        self.history = []

        # Display
        self.display = tk.Entry(
            root,
            font=("Arial", 20),
            justify="right"
        )
        self.display.pack(fill="x", padx=10, pady=10)

        # History
        self.history_box = tk.Text(
            root,
            height=10
        )
        self.history_box.pack(
            fill="both",
            padx=10,
            pady=5
        )

        self.create_buttons()

    def add_history(self, text):
        timestamp = datetime.now().strftime("%H:%M:%S")
        record = f"[{timestamp}] {text}\n"

        self.history.append(record)

        self.history_box.insert(tk.END, record)
        self.history_box.see(tk.END)

    def insert(self, value):
        self.display.insert(tk.END, value)

    def clear(self):
        self.display.delete(0, tk.END)

    def evaluate(self):
        try:
            expression = self.display.get()
            result = eval(expression)

            self.add_history(
                f"{expression} = {result}"
            )

            self.clear()
            self.insert(str(result))

        except Exception:
            messagebox.showerror(
                "Error",
                "Invalid Expression"
            )

    def scientific(self, operation):

        try:
            num = float(self.display.get())

            if operation == "sqrt":
                result = math.sqrt(num)

            elif operation == "sin":
                result = math.sin(math.radians(num))

            elif operation == "cos":
                result = math.cos(math.radians(num))

            elif operation == "tan":
                result = math.tan(math.radians(num))

            elif operation == "log":
                result = math.log10(num)

            elif operation == "fact":
                result = math.factorial(int(num))

            self.add_history(
                f"{operation}({num}) = {result}"
            )

            self.clear()
            self.insert(str(result))

        except Exception:
            messagebox.showerror(
                "Error",
                "Invalid Input"
            )

    # Memory Functions
    def memory_add(self):
        try:
            self.memory += float(self.display.get())
        except:
            pass

    def memory_subtract(self):
        try:
            self.memory -= float(self.display.get())
        except:
            pass

    def memory_recall(self):
        self.clear()
        self.insert(str(self.memory))

    def memory_clear(self):
        self.memory = 0

    # Save History
    def save_history(self):
        with open("history.txt", "w") as file:
            file.writelines(self.history)

        messagebox.showinfo(
            "Saved",
            "History saved to history.txt"
        )

    # UI 
    def create_buttons(self):

        frame = tk.Frame(self.root)
        frame.pack()

        buttons = [

            ['7', '8', '9', '/', 'sqrt'],
            ['4', '5', '6', '*', 'sin'],
            ['1', '2', '3', '-', 'cos'],
            ['0', '.', '=', '+', 'tan'],
            ['log', 'fact', 'C', '^', '%']
        ]

        for r, row in enumerate(buttons):

            for c, text in enumerate(row):

                if text == '=':

                    btn = tk.Button(
                        frame,
                        text=text,
                        width=10,
                        height=2,
                        command=self.evaluate
                    )

                elif text == 'C':

                    btn = tk.Button(
                        frame,
                        text=text,
                        width=10,
                        height=2,
                        command=self.clear
                    )

                elif text in [
                    'sqrt',
                    'sin',
                    'cos',
                    'tan',
                    'log',
                    'fact'
                ]:

                    btn = tk.Button(
                        frame,
                        text=text,
                        width=10,
                        height=2,
                        command=lambda t=text:
                        self.scientific(t)
                    )

                elif text == '^':

                    btn = tk.Button(
                        frame,
                        text=text,
                        width=10,
                        height=2,
                        command=lambda:
                        self.insert("**")
                    )

                else:

                    btn = tk.Button(
                        frame,
                        text=text,
                        width=10,
                        height=2,
                        command=lambda t=text:
                        self.insert(t)
                    )

                btn.grid(
                    row=r,
                    column=c,
                    padx=2,
                    pady=2
                )

        # Memory Buttons
        mem_frame = tk.Frame(self.root)
        mem_frame.pack(pady=10)

        tk.Button(
            mem_frame,
            text="M+",
            width=10,
            command=self.memory_add
        ).grid(row=0, column=0)

        tk.Button(
            mem_frame,
            text="M-",
            width=10,
            command=self.memory_subtract
        ).grid(row=0, column=1)

        tk.Button(
            mem_frame,
            text="MR",
            width=10,
            command=self.memory_recall
        ).grid(row=0, column=2)

        tk.Button(
            mem_frame,
            text="MC",
            width=10,
            command=self.memory_clear
        ).grid(row=0, column=3)

        tk.Button(
            mem_frame,
            text="Save History",
            width=15,
            command=self.save_history
        ).grid(row=0, column=4)


root = tk.Tk()
app = ScientificCalculator(root)
root.mainloop()