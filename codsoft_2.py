# Python program for a simple calculator

# add numbers
def add(num1, num2):
    return num1 + num2

# subtract numbers
def subtract(num1, num2):
    return num1 - num2

# multiply numbers
def multiply(num1, num2):
    return num1 * num2

# divide numbers
def divide(num1, num2):
    if num2 == 0:
        return "Cannot divide by zero!"
    else:
        return num1 / num2

while True:
    
        print("Please select an operation :-\n"
              "1. Add\n"
              "2. Subtract\n"
              "3. Multiply\n"
              "4. Divide\n")
        
        select = int(input("Select operation from 1, 2, 3, 4: "))
        if select not in [1, 2, 3, 4]:
            print("Invalid input. Please enter 1, 2, 3, or 4.")
            continue

        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        if select == 1:
            print(f"{n1} + {n2} = {add(n1, n2)}")
        elif select == 2:
            print(f"{n1} - {n2} = {subtract(n1, n2)}")
        elif select == 3:
            print(f"{n1} * {n2} = {multiply(n1, n2)}")
        elif select == 4:
            print(f"{n1} / {n2} = {divide(n1, n2)}")

        calculate = input("Do you want to calculate again? (y/n): ")
        if calculate.lower() != "y":
            break

    
