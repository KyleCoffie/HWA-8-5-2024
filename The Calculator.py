#Task 1: Create functions for each arithmetic operation.

import math
num1 = float(input("Enter your first number to add"))
num2 = float(input("Enter your second number to add"))
print(num1 + num2)

num1 = float(input("Enter your first number to subtract"))
num2 = float(input("Enter your second number to subtract"))
print(num1 - num2)

num1 = float(input("Enter your first number to multiply"))
num2 = float(input("Enter your second number to multiply"))
print(num1 * num2)

num1 = float(input("Enter your first number to divide"))
num2 = float(input("Enter your second number to divide"))
print(num1 / num2)
#Task 2: Use inputs to ask the user what operation they want to perform, and what numbers they want to use.

import math

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


choice = input("Enter choice (1/2/3/4): ")
num1 = float(input("Enter a number"))
num2 = float(input("Enter a second number"))
if choice in ('1', '2', '3', '4'):
    if choice == '1':
        print(f"{num1} + {num2} = {(num1)+ (num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {(num1) - (num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {(num1) * (num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {(num1) / (num2)}")
else:
    print("Invalid input. Please choose a valid operation.")


#Task 3: Ensure your code can handle division by zero and other potential errors. So if you divide by 0, there is error handling set up to prevent an error from showing in the console.

