import sys
"""
For this exercise, you will be given at least three command line arguments.  The first two will be integers; the third will be a string.  Use what you have learned so far to create a program which accomplishes the following:

Prints the larger of the two integers.  If they are equal, do not print either one.
If the word "time" appears in the string, print the sum of the integers.
If both the integers are odd, or one of them is a multiple of 3, print the string.
If there are more than three command line arguments (excluding the filename), print the word "error".

"""

def exercise3(args):
    args = validate(args)
    #Prints the larger of the two integers.  If they are equal, do not print either one.
    if args[0] > args[1]:
        print(args[0])
    elif args[1] > args[0]:
        print(args[1])
    #If the word "time" appears in the string, print the sum of the integers.
    if 'time' in args[2]:
        print(args[0]+args[1])
    #If both the integers are odd, or one of them is a multiple of 3, print the string
    if (args[0]%2 and args[1]%2) or not (args[0]%3) or not (args[1]%3):
        print(args[2])
    #If there are more than three command line arguments (excluding the filename), print the word "error".
    if len(args) > 3:
        print('error')

def validate(args):
    """Validates that 1st and 2nd arguments are integers and 3rd is a string"""
    try:
        if len(args) < 3:
            raise Exception("Not enough arguments")
        args[0] = int(args[0])
        args[1] = int(args[1])
    except Exception as e:
        print(e)
        print('\nPlease provide at least 2 integers followed by 1 string')
        exit()
    return(args)

if __name__ == "__main__":
    #Make sure there are enough arguments given to run
    if len(sys.argv) > 1:
        #Strip the script filename we don't need it
        exercise3(sys.argv[1:])
    else:
        #Pass it on through and let the vaildater do it's job
        validate(sys.argv)