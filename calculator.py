from sys import exit
# function to check if a number exists else an error
def check_if_is_number(expression):
    try:
        int(expression)
        return True
    except ValueError:
        return False
def operation(num1, operator, num2):
    if operator == "+":
        return str(int(num1) + int(num2))
    elif operator == "-":
        return str(int(num1) - int(num2))
    elif operator == "*":
        return str(int(num1) * int(num2))


