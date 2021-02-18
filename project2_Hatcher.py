# can be loaded in interactive with (from project2_Hatcher import *)
# then ran like password_checker("passwordHere")
# or ran from command line with (python project2_Hatcher.py passwordHere)

import sys
import string

def check_pw_length(password):
    if len(password) < 14:
        return(False)
    else:
        return(True)

def check_characters(password):
    upper=0
    lower=0
    num=0
    spec=0
    for char in password:
        if char in string.ascii_uppercase:
            upper+=1
        if char in string.ascii_lowercase:
            lower+=1
        if char in string.digits:
            num+=1
        if char in string.punctuation:
            spec+=1
    if upper < 1 or lower < 1 or num < 1 or spec < 1:
        return(False)
    else:
        return(True)

def check_consecutive(password):
    consec = 0
    last = ''
    for char in password:
        if consec <= 3:
            if char in string.ascii_uppercase and last == 'upper':
                consec+=1
            elif char in string.ascii_lowercase and last == 'lower':
                consec+=1
            elif char in string.digits and last == 'num':
                consec+=1
            elif char in string.punctuation and last == 'spec':
                consec+=1
            else:
                consec=1
                if char in string.ascii_uppercase:
                    last='upper'
                if char in string.ascii_lowercase:
                    last='lower'
                if char in string.digits:
                    last='num'
                if char in string.punctuation:
                    last='spec'
        else:
            return(False)
    return(True)


def check_whitespace(password):
    for char in password:
        if char in string.whitespace:
            return(False)
    return(True)

def password_checker(arg):
    if not arg:
        exit("Please enter a password")
    else:
        password = arg

    if not check_pw_length(password):
        print(False)
    elif not check_characters(password):
        print(False)
    elif not check_consecutive(password):
        print(False)
    elif not check_whitespace(password):
        print(False)
    else:
        print(True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit("Please enter a single password")
    else:
        password_checker(sys.argv[1])