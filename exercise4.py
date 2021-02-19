import sys
"""
This exercise is intended to test your knowledge of loops and previous material.  For this exercise,

Create a program that takes one command line argument.  It will be an integer.
For each number between 1 and the argument (inclusive), print the word "triangle" if the number is a multiple of three.
Print "square" if it is a multiple of four.
If it is a multiple of 12, do not print triangle or square.  Instead, print "x dozen" where x is the numeral representing how many dozen you're at("1 dozen" for 12, "2 dozen" for 24, etc.)
Lastly, print the sum of the numbers between 1 and the argument (inclusive).

"""

def exercise4(args):
    args = validate(args)
    number_of_dozen=0
    sum_of_numbers=0
    #Loop through each number from 1 to given
    for i in range(1,args[0]+1):
        #If multiple of 12 print 'x dozen'
        if i%12 == 0:
            number_of_dozen+=1
            print('{} dozen'.format(number_of_dozen))
        #If multiple of 3 preint 'triangle'
        elif i%3 == 0:
            print('triangle')
        #If multiple of 4 print 'square'
        elif i%4 == 0:
            print('square')
        #Add number to tally sum of all numbers
        sum_of_numbers+=i
    #Print sum of number from 1 to given
    print(sum_of_numbers)

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
        exercise4(sys.argv[1:])
    else:
        #Pass it on through and let the vaildater do it's job
        validate(sys.argv)