import sys
"""
For this exercise, create two functions:

which_fibonacci receives a non-negative integer, which may or may not be a Fibonacci number. If it is, then it returns its position in the sequence. For example, 2 is the 4th Fibonacci number. If 1 is given as the argument, the function should return 2. If the argument is not a Fibonacci number, the function returns 0.
next_fibonacci received a non-negative integer and returns the next largest Fibonacci number. If the argument is itself a Fibonacci number, it should return the next Fibonacci number, not the argument itself. If 1 is received, next_fibonacci should return 2.

"""

def exercise6(args):
    args = validate(args)
    for i in range(0,len(args)):
        which_fibonacci(args[i])

def which_fibonacci(given_number):
    """receives a non-negative integer, which may or may not be a Fibonacci number. If it is, then it returns its position in the sequence. For example, 2 is the 4th Fibonacci number. If 1 is given as the argument, the function should return 2. If the argument is not a Fibonacci number, the function returns 0."""
    #Since 0 is always index 1 and 1 is always index 2 we will start at 2
    index=2
    #Nth value in Fibonacci sequence
    nth=0
    #2 values ago in Fibonacci sequence
    n1=0
    #Last value in Fibonacci sequence
    n2=1
    #0 is always first
    if given_number == 0:
        print('Index: 1')
    #1 is always second
    elif given_number == 1:
        print('Index: 2')
    #Now we can get started
    elif given_number > 1:
        #Make sure we don't go over our given number
        while nth < given_number:
            #Add one at beginning since we already checked for the first 2
            index += 1
            nth = n1 + n2
            n1 = n2
            n2 = nth
        #If they equal then we found it
        if nth == given_number:
            print('Index: {}'.format(index))
        else:
            #This means our Nth value is larger than our given number and it wasn't found
            print('Index: 0')
    #Makes things quicker since we have already stepped through and now just need the next value
    next_fibonacci(nth, n1, n2, given_number)

def next_fibonacci(nth, n1, n2, given_number):
    """received a non-negative integer and returns the next largest Fibonacci number. If the argument is itself a Fibonacci number, it should return the next Fibonacci number, not the argument itself. If 1 is received, next_fibonacci should return 2."""
    while nth <= given_number:
        nth = n1 + n2
        n1 = n2
        n2 = nth
    print('Next: ' + str(nth))

def validate(args):
    """Validates that the arguments are positive integers"""
    try:
        for i in range(0, len(args)):
            args[i] = int(args[i])
            if args[i] < 0:
                raise Exception('Must be positive integer')
    except Exception as e:
        print(e)
        print('\nPlease provide at least 1 positive integer')
        exit()
    return(args)

if __name__ == "__main__":
    #Make sure there are enough arguments given to run
    if len(sys.argv) > 1:
        #Strip the script filename we don't need it
        exercise6(sys.argv[1:])
    else:
        #Pass it on through and let the vaildater do it's job
        validate(sys.argv)