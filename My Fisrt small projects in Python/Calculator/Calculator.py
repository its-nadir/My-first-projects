import art

def calculator():
    def add(n1, n2): return n1 + n2
    def subtract(n1, n2): return n1 - n2
    def multiply(n1, n2): return n1 * n2
    def divide(n1, n2): return n1 / n2 if n2 != 0 else "Error! Division by zero."

    operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

    def clear_screen():
       print("\n"*20)

    while True:
        print(art.logo)
        num1 = float(input("What is the first number?: "))

        while True:
            print("Available operations:", " ".join(operations.keys()))
            operation_symbol = input("Pick an operation: ")
            num2 = float(input("What is the next number?: "))

            if operation_symbol in operations:
                result = operations[operation_symbol](num1, num2)
                print(f"{num1} {operation_symbol} {num2} = {result}")
            else:
                print("Invalid operation. Try again.")
                continue

            choice = input(f"Type 'y' to continue with {result}, or 'n' to start a new calculation: ").lower()

            if choice == "y":
                num1 = result
            else:
                clear_screen()
                break

calculator()
