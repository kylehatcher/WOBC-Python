import sys
"""
For this exercise, create a function called factorial that takes one integer argument and calculates its factorial. A factorial is the product of a whole number and all the positive whole numbers beneath it.  For example, 4 factorial (usually written 4!) is 4x3x2x1 = 24.  The factorial function should print the factorial value:  4x3x2x1 = 24   It should not return a value.

"""

def exercise5(args):
    args = validate(args)
    factorial(args[0])

def factorial(given_number):
    #Start factorial total at 1 so we don't multiply by 0
    factorial=1
    #Will hold the full equation as a string (3x2x1)
    equation=''
    #Loop through each number counting down
    while given_number > 0:
        factorial=factorial*given_number
        if given_number != 1:
            equation = equation + str(given_number) + 'x'
        else:
            #This keeps from having an 'x' on the end (3x2x1x)
            equation = equation + str(given_number)
        given_number = given_number - 1
    print('{} = {}'.format(equation, factorial))

def validate(args):
    """Validates that the argument is an integer"""
    try:
        args[0] = int(args[0])
    except Exception as e:
        print(e)
        print('\nPlease provide at least 1 integer')
        exit()
    return(args)

if __name__ == "__main__":
    #Make sure there are enough arguments given to run
    if len(sys.argv) > 1:
        #Strip the script filename we don't need it
        exercise5(sys.argv[1:])
    else:
        #Pass it on through and let the vaildater do it's job
        validate(sys.argv)