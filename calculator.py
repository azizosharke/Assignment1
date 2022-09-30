from sys import exit


# function to check if a number exists else an error
# This function checks whether the values enter by the user are integers. If not,
# it prints out a value error and if true the code the def function will execute

def check_if_is_number(expression):
    try:
        int(expression)
        return True
    except ValueError:
        return False

    # it’s a for loop that iterates through the list provided. It also checks if the words the user types are in that
    # list. if the user uses something like / the division sign, it will print invalid expression.
    # The exit () is for closing the program in case of an error.
    # creating an empty list to hold the user values


def calculator():
    calc = input("Enter your Expression Here: ")
    # remove white spaces
    calc = calc.replace(' ', '')
    # check for invalid expression
    for expression in calc:
        if expression not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*']:
            print('Invalid Expression: ' + expression)
            exit()


    # creating an empty list to hold the user values
    # for loop to iterate through the list of the expression the user typed, then appending them to that expression
    new_list = []
    for expression in calc:
        new_list.append(expression)
    # creating a variable and giving it a value of 0- to be used basically to compare values in a list

    n = 0
    # creating a while loop to check if the appended list (new list) is in range. checks if the values provided in a
    # list are numbers and also checks if there exist the appended values in the list combines the new list with the
    # appended list clears the list checks if the list contains decimal points, if true it prints Bad formatting.,
    # else it creates a new variable for the second number in the list
    # checks if the second expression is a number and if true, it is combined with the number in the list before it.
    # clears the list to allow it to have space for other numbers(expressions)
    while n < len(new_list) - 1:

        if check_if_is_number(new_list[n]) and check_if_is_number(new_list[n + 1]):
            new_list[n] = new_list[n] + new_list[n + 1]
            del new_list[n + 1]
        elif check_if_is_number(new_list[n]) and new_list[n + 1] == ".":

            try:
                n = new_list[n + 2]
            except IndexError:
                print("Bad Formatting")
                exit()
            if check_if_is_number(new_list[n + 2]):
                new_list[n] += new_list[n + 1] + new_list[n + 2]
                del new_list[n + 2]
                del new_list[n + 1]

        else:
            n += 1
    return new_list


def operation(num1, operator, num2):
    if operator == "+":
        return str(int(num1) + int(num2))
    elif operator == "-":
        return str(int(num1) - int(num2))
    elif operator == "*":
        return str(int(num1) * int(num2))

computation = calculator()

# check if is 1 or not
while len(computation) != 1:
    # multiplication iteration
    # del its to clear the list to allow computation of new inputs from the user

    n = 0
    while n < len(computation) - 1:
        if computation[n] in ['*']:
            computation[n - 1] = operation(
                computation[n - 1], computation[n], computation[n + 1])
            del computation[n + 1]
            del computation[n]
        n += 1
    # addition and subtraction iterations
    n = 0
    while n < len(computation) - 1:
        if computation[n] in ["+", "-"]:
            computation[n - 1] = operation(
                computation[n - 1], computation[n], computation[n + 1])
            del computation[n + 1]
            del computation[n]
        n += 1

print('Result: ', int(computation[0]))
