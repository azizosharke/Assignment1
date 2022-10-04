from sys import exit




# Function to check if a given character is an operator.
# returns true/false.
def is_operator(token):
    return token in ['+', '-', '*', '/', '^', '(', ')']
