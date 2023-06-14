# Basic calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
    
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    else:
        return a / b
while True:
    print(" Select an operation:")
    print(" Addition +")
    print(" Subtraction -")
    print(" Multiplication *")
    print(" Division /")
