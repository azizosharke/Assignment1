from sys import exit

precedence = {')' : 0, '(' : 0, '+' : 1, '-' : 1, '*' : 2, '/' : 2, '^' : 3 }

# function to check if a given character is a number.
# returns true/false.

def check_if_is_number(expression):
    return str(expression).replace('.', '').isdigit()


# function to check if a given character is an operator.
# returns true/false.

def is_operator(expression):
    return expression in ['+', '-', '*', '/', '^', '(', ')']




def calculator(expression):

    exp_list = convert_exp_to_list(expression)
    
    # check for invalid tokens
    for token in exp_list:
        if (not check_if_is_number(token)) and (not is_operator(token)):
            print('Invalid token: ' + token)
            exit()
    
    return solve_rpn(convert_rpn(expression)) # Convert the expression to RPN, then solve it.


# Function that converts a string containing a standard mathematical expression
# into a list containing an expression written in Reverse Polish Notation.
# Uses the shunting yard algorithm. https://en.wikipedia.org/wiki/Shunting-yard_algorithm

def convert_rpn(expression):
    exp_list = convert_exp_to_list(expression)
    output = []
    stack = []
    for token in exp_list:
        if check_if_is_number(token):
            output.append(token)
        else:
            if token == '(':
                stack.insert(0, token)
            elif token == ')' and stack:
                while stack[0] != '(' and stack:
                    output.append(stack[0])
                    del stack[0]
                if (not stack) or stack[0] != '(':
                    print("Invalid formatting of parentheses in expression.")
                    return -1
                del stack[0]
            else:
                if stack:
                    while (stack and
                          (token != '^' and precedence.get(token) <= precedence.get(stack[0])) or
                          (token == '^' and precedence.get(token) < precedence.get(stack[0]))):
                        output.append(stack[0])
                        del stack[0]
                stack.insert(0, token)
    while stack:
        output.append(stack[0])
        del stack[0]
    return output
    

# Function to solve RPN. Takes a list and outputs a floating point number.
# Uncomment line 83 to get the calculator to print its progress,
# and how it got to the result it found.

def solve_rpn(input_list):
    stack = []
    for token in input_list:                # For each character in the RPN string...
        if not is_operator(token):
            stack.append(token)             # If it's a number, put it on the stack.
        else:                               # If it's an operator "+-*/^"...
            y = stack.pop()                 # Take the last two numbers from the stack
            x = stack.pop()                 # and apply the operation to them,
            stack.append(operation(x, token, y)) # then put the result on the stack.
            #print (x, token, y, " = ", operation(x, token, y))
    return stack.pop()                      # The result is the last number on the stack.


# Function to convert a string expression (i.e. "2.3 + 1*4") into
# a list containing each section of the expression (i.e. [2.3,'+',1,'*',4])

def convert_exp_to_list(input_string):
    output_list = []
    n = 0
    while n != len(input_string):
        if check_if_is_number(input_string[n]):
            temp = input_string[n]
            while True:
                if n+1 >= len(input_string):
                    if (check_if_is_number(temp)):
                        temp = float(temp)
                    output_list.append(temp)
                    break
                elif check_if_is_number(input_string[n+1]) or input_string[n+1] == '.':
                    temp += input_string[n+1]
                    n += 1
                    continue
                if (check_if_is_number(temp)):
                    temp = float(temp)
                output_list.append(temp)
                break
        elif input_string[n] != ' ':
            output_list.append(input_string[n])
        n += 1
    return output_list


def operation(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        return num1 / num2
    elif operator == "^":
        return num1 ** num2
        

print('Result:', calculator(input("Enter your Expression Here: ")))