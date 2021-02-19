import sys
"""
For this exercise, create a program that takes (at least) three command line arguments.  The first two will be integers; the third will be a float. 

"""
def exercise2(args):
    args=validate(args)
    print(
        args[0]+args[1], #SUM of 1st and 2nd
        args[0]*args[2], #Products of 1st and 3rd
        args[0]%args[1], #Modulo of 1st by 2nd
        args[2]//args[0] #Int Quot of 3rd by 1st
    ) 
    #Add 1 to all 3 arguments
    for i in range(0,2):
        args[i] = args[i] + 1
    print(
        args[0]>>3,     #Bitwise Right Shift 3 1st
        args[1]/2,      #2nd divided by 2
        args[0]|args[1] #Bitwise OR of 1st and 2nd
    ) 
    print(
        args[0]+len(args), #SUM of 1st and number of arguments (not counting script name)
    )

def validate(args):
    """Validates that the first 2 are integers and 3rd is a float"""
    try:
        if len(args) < 3:
            raise Exception("Not enough arguments given")
        args[0] = int(args[0])
        args[1] = int(args[1])
        args[2] = float(args[2])
        return(args)
    except Exception as e:
        print(e)
        print("\nPlease enter at least two integers and one float")
        exit()

if __name__ == "__main__":
    #Make sure there are enough arguments given to run
    if len(sys.argv) > 1:
        #Strip the script filename we don't need it
        exercise2(sys.argv[1:])
    else:
        #Pass it on through and let the vaildater do it's job
        validate(sys.argv)