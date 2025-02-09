import os
from art import logo

def clear_screen():
    print("\n"*20)
def calculate(n1, n2, operator):
    if operator == "+": return n1 + n2
    if operator == "-": return n1 - n2
    if operator == "*": return n1 * n2
    if operator == "/": return n1 / n2 if n2 != 0 else "Error! Division by zero."
    return "Invalid operator"

while True:
    print(logo)
    first_number = float(input("Enter first number: "))

    while True:
        operator = input("Enter an operator (+, -, *, /): ")
        second_number = float(input("Enter second number: "))

        result = calculate(first_number, second_number, operator)
        print(f"Result: {first_number} {operator} {second_number} = {result}")

        if input("Type 'y' to continue, 'n' to restart: ").lower() == "n":
            clear_screen()
            break
        first_number = result
        clear_screen()
        print(logo)
        print(f"Current number: {first_number}")
