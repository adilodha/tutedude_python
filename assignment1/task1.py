# write a Python program that does the following:
# 1. takes two numbers as input from the user
# 2. Performs the following operations on the two numbers:
#    a. Addition
#    b. Subtraction
#    c. Multiplication
#    d. Division
# 3. Displays the results of each operation on the screen.

def main():
    # Taking two numbers as input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Performing operations
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else "undefined (division by zero)"

    # Displaying results
    print(f"Addition: {addition}")
    print(f"Subtraction: {subtraction}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")

if __name__ == "__main__":
    main()