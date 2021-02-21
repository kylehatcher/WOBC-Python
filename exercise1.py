import sys
"""
This script takes two strings as arguments that are at least 4 characters in length.

"""
def exercise1(args):
    """Prints different outputs based on the given strings"""
    #Validate given arguments first
    validate(args)
    #Prints both strings separated by a space
    print(args[0],args[1])
    #Prints 1st char of string 1, 3rd char of string 2, last char of string 2, and length of string 1
    print(args[0][0],args[1][2],args[1][-1],len(args[0]), sep='')
    #Prints two blank lines
    print('\n')
    #Prints number of arguments plus one for the script filename
    print(len(args)+1)
    #Prints 2nd through 4th chars of string 1
    print(args[0][1:4])
    #Prints single quote (') in a sentance
    print("use of 'quotation' marks")
    #Requests user input and prints the 2nd char
    #Requires user to input at least 2 characters
    while True:
        try:
            print(input("please enter: ")[1])
            break
        except:
            continue

def validate(args):
    """Validates that there are at least 2 strings that are 4 characters long"""
    if not (len(args) >= 2 and len(args[0]) >= 4 and len(args[1]) >= 4):
        print("Please enter two strings containing at least 4 characters")
        exit()

if __name__ == "__main__":
    #Strip the script filename we don't need it
    exercise1(sys.argv[1:])