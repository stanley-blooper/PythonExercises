#Calculator

def calculator():
#enter kind of operation
    operation = input("Choose operation (+,-,*,/:): ")
    num1=float(input("Enter first number: "))
    num2=float(input("Enter second number: "))

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2

    else:
        return "Invalid operation"
    
    return f"The result is {result}"

print(calculator())