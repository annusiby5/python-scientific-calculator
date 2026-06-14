import math

history = []

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return "Error: Division by zero!"
        return num1 / num2
    elif operation == '%':
        return num1 % num2
    elif operation == '^':
        return num1 ** num2
    else:
        return "Invalid operation!"

def show_history():
    if not history:
        print("\nNo calculations performed yet.\n")
    else:
        print("\n=== Calculation History ===")
        for item in history:
            print(item)
        print()

def square_root():
    try:
        num = float(input("Enter number: "))
        if num < 0:
            print("Cannot calculate square root of a negative number.")
        else:
            result = math.sqrt(num)
            record = f"√{num} = {result}"
            history.append(record)
            print("Result:", result)
    except ValueError:
        print("Invalid input!")

def calculator():
    while True:
        print("\n====== Advanced Calculator ======")
        print("1. Basic Calculation")
        print("2. Square Root")
        print("3. View History")
        print("4. Clear History")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            try:
                num1 = float(input("Enter first number: "))
                operation = input("Enter operation (+, -, *, /, %, ^): ")
                num2 = float(input("Enter second number: "))

                result = calculate(num1, num2, operation)

                expression = f"{num1} {operation} {num2} = {result}"
                history.append(expression)

                print("Result:", result)

            except ValueError:
                print("Please enter valid numbers!")

        elif choice == '2':
            square_root()

        elif choice == '3':
            show_history()

        elif choice == '4':
            history.clear()
            print("History cleared.")

        elif choice == '5':
            print("Thank you for using the calculator!")
            break

        else:
            print("Invalid choice. Please select 1-5.")

calculator()