# CLI calculator program
import sys

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

print("Select operation.")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(sys.argv[1])

num1 = int(sys.argv[2])
num2 = int(sys.argv[3])

if choice == 1:
    print(num1, "+", num2, "=", addition(num1, num2))

elif choice == 2:
    print(num1, "-", num2, "=", subtraction(num1, num2))

elif choice == 3:
    print(num1, "*", num2, "=", multiplication(num1, num2))

elif choice == 4:
    print(num1, "/", num2, "=", division(num1, num2))
else:
    print("Invalid input")