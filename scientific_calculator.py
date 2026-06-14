import math
from datetime import datetime


class ScientificCalculator:
    def __init__(self):
        self.memory = 0
        self.history = []

    # Basic Operations
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

    def power(self, a, b):
        return a ** b

    def modulus(self, a, b):
        return a % b

    # Scientific Operations
    def square_root(self, x):
        return math.sqrt(x)

    def factorial(self, x):
        return math.factorial(int(x))

    def sine(self, x):
        return math.sin(math.radians(x))

    def cosine(self, x):
        return math.cos(math.radians(x))

    def tangent(self, x):
        return math.tan(math.radians(x))

    def logarithm(self, x):
        return math.log10(x)

    # Expression Evaluation
    def evaluate_expression(self, expression):
        try:
            return eval(expression)
        except:
            return "Invalid Expression"

    # Memory Functions
    def memory_add(self, value):
        self.memory += value

    def memory_subtract(self, value):
        self.memory -= value

    def memory_recall(self):
        return self.memory

    def memory_clear(self):
        self.memory = 0

    # History
    def add_history(self, record):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(f"[{timestamp}] {record}")

    def show_history(self):
        if not self.history:
            print("\nNo history found.")
        else:
            print("\n===== HISTORY =====")
            for item in self.history:
                print(item)

    def save_history(self):
        with open("history.txt", "w") as file:
            for item in self.history:
                file.write(item + "\n")
        print("History saved to history.txt")

    # Unit Conversions
    def kg_to_lb(self, kg):
        return kg * 2.20462

    def lb_to_kg(self, lb):
        return lb / 2.20462

    def km_to_mile(self, km):
        return km * 0.621371

    def mile_to_km(self, mile):
        return mile / 0.621371

    def celsius_to_fahrenheit(self, c):
        return (c * 9 / 5) + 32

    def fahrenheit_to_celsius(self, f):
        return (f - 32) * 5 / 9


calculator = ScientificCalculator()


while True:

    print("\n========== ADVANCED SCIENTIFIC CALCULATOR ==========")
    print("1. Basic Operations")
    print("2. Scientific Operations")
    print("3. Evaluate Expression")
    print("4. Memory Functions")
    print("5. Unit Converter")
    print("6. View History")
    print("7. Save History")
    print("8. Exit")

    choice = input("Enter choice: ")

    try:

        # BASIC OPERATIONS
        if choice == "1":

            a = float(input("Enter first number: "))
            op = input("Operation (+ - * / % ^): ")
            b = float(input("Enter second number: "))

            if op == "+":
                result = calculator.add(a, b)
            elif op == "-":
                result = calculator.subtract(a, b)
            elif op == "*":
                result = calculator.multiply(a, b)
            elif op == "/":
                result = calculator.divide(a, b)
            elif op == "%":
                result = calculator.modulus(a, b)
            elif op == "^":
                result = calculator.power(a, b)
            else:
                result = "Invalid Operation"

            print("Result:", result)
            calculator.add_history(f"{a} {op} {b} = {result}")

        # SCIENTIFIC OPERATIONS
        elif choice == "2":

            print("\n1. sqrt")
            print("2. factorial")
            print("3. sin")
            print("4. cos")
            print("5. tan")
            print("6. log10")

            sci = input("Select: ")
            num = float(input("Enter number: "))

            if sci == "1":
                result = calculator.square_root(num)
                operation = "sqrt"

            elif sci == "2":
                result = calculator.factorial(num)
                operation = "factorial"

            elif sci == "3":
                result = calculator.sine(num)
                operation = "sin"

            elif sci == "4":
                result = calculator.cosine(num)
                operation = "cos"

            elif sci == "5":
                result = calculator.tangent(num)
                operation = "tan"

            elif sci == "6":
                result = calculator.logarithm(num)
                operation = "log"

            else:
                result = "Invalid Option"
                operation = ""

            print("Result:", result)
            calculator.add_history(f"{operation}({num}) = {result}")

        # EXPRESSION EVALUATION
        elif choice == "3":

            expression = input(
                "Enter expression (Example: 5+6*3-2): "
            )

            result = calculator.evaluate_expression(expression)

            print("Result:", result)
            calculator.add_history(
                f"Expression: {expression} = {result}"
            )

        # MEMORY FUNCTIONS
        elif choice == "4":

            print("\n1. M+")
            print("2. M-")
            print("3. MR")
            print("4. MC")

            mem = input("Select: ")

            if mem == "1":
                value = float(input("Enter value: "))
                calculator.memory_add(value)

            elif mem == "2":
                value = float(input("Enter value: "))
                calculator.memory_subtract(value)

            elif mem == "3":
                print("Memory =", calculator.memory_recall())

            elif mem == "4":
                calculator.memory_clear()
                print("Memory Cleared")

        # UNIT CONVERTER
        elif choice == "5":

            print("\n1. KG -> LB")
            print("2. LB -> KG")
            print("3. KM -> MILE")
            print("4. MILE -> KM")
            print("5. C -> F")
            print("6. F -> C")

            conv = input("Select: ")
            value = float(input("Enter value: "))

            if conv == "1":
                result = calculator.kg_to_lb(value)

            elif conv == "2":
                result = calculator.lb_to_kg(value)

            elif conv == "3":
                result = calculator.km_to_mile(value)

            elif conv == "4":
                result = calculator.mile_to_km(value)

            elif conv == "5":
                result = calculator.celsius_to_fahrenheit(value)

            elif conv == "6":
                result = calculator.fahrenheit_to_celsius(value)

            else:
                result = "Invalid Conversion"

            print("Result:", result)

        # HISTORY
        elif choice == "6":
            calculator.show_history()

        # SAVE HISTORY
        elif choice == "7":
            calculator.save_history()

        # EXIT
        elif choice == "8":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

    except Exception as e:
        print("Error:", e)