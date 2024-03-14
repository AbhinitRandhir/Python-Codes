# n=int(input("Enter the value of n:"))
# d=int(input("Enter the value of d:"))
# c=int(input("Enter the value of c:"))
# try:
#     q=n/(d-c)
#     print("Quotient:",q)
# except ZeroDivisionError:
#     print("Division by Zero!")



def divide_numbers(a, b):
    try:
        result = a / b
        print("The result of division is:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")

# Example usage
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

divide_numbers(num1, num2)