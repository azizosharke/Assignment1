from sys import exit


# Function to check if a given character is a number.
# returns true/false.

def is_number(token):
    return str(token).replace('.', '').isdigit()


