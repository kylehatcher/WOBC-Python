import sys
"""
Write a function named counts that counts all of the occurring characters in a string (UTF-8).  If you have a string like "aba", the result should be {"a":2, "b":1}  If the string is empthy, return {}.  

"""

def exercise7(args):
    args=validate(args)
    charcter_count_dictionary={}
    for i in range(0, len(args)):
        charcter_count_dictionary.update(count_character(args[i]))
    print(charcter_count_dictionary)

def count_character(string):
    """Counts the number of times a character appears in the arguments"""
    charcter_count_dictionary={}
    for char in string:
        charcter_count_dictionary[char] = string.count(char)
    return(charcter_count_dictionary)

def validate(args):
    """Validates that there is an argument"""
    if "exercise7.py" in args[0]:
        print({})
        exit()
    return(args)

if __name__ == "__main__":
    #Make sure there are enough arguments given to run
    if len(sys.argv) > 1:
        #Strip the script filename we don't need it
        exercise7(sys.argv[1:])
    else:
        #Pass it on through and let the vaildater do it's job
        validate(sys.argv)