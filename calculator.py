from sys import exit
# function to check if a number exists else an error
def check_if_is_number(expression):
    try:
        int(expression)
        return True
    except ValueError:
        return False
def calculator():
    calc = input("Enter your Expression Here: ")
    # remove white spaces
    calc = calc.replace(' ', '')
    # check for invalid expression
    for expression in calc:
        if expression not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*']:
            print('Invalid Expression: ' + expression)
            exit()

def operation(num1, operator, num2):
    if operator == "+":
        return str(int(num1) + int(num2))
    elif operator == "-":
        return str(int(num1) - int(num2))
    elif operator == "*":
        return str(int(num1) * int(num2))


