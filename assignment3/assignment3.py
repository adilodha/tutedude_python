#1. calculate factorial using a function


def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n < 2:
        return 1
    else:
        return n * factorial(n - 1)



"""
Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.
"""

def task2():
    import math

    number = float(input("Enter a number: "))
    sqrt_value = math.sqrt(number)
    log_value = math.log(number)
    sine_value = math.sin(number)

    print(f"Square root of {number} = {sqrt_value}")
    print(f"Natural logarithm of {number} = {log_value}")
    print(f"Sine of {number} (in radians) = {sine_value}")


if __name__ == "__main__":
    # Test the factorial function
    number = int(input("Enter a non-negative integer to calculate its factorial: "))
    print(f"factorial of {number} = {factorial(number)}")

    task2()