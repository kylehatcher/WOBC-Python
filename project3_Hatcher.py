# can be loaded in interactive with (from project3_Hatcher import *)
# then ran like password_generator() or password_generator(24)
# or ran from command line with (python project3_Hatcher.py passwordHere)

import sys
import string
from random import randint

def get_lower():
    random = randint(0, len(string.ascii_lowercase)-1)
    return(string.ascii_lowercase[random])

def get_upper():
    random = randint(0, len(string.ascii_uppercase)-1)
    return(string.ascii_uppercase[random])

def get_number():
    random = randint(0, len(string.digits)-1)
    return(string.digits[random])

def get_special():
    random = randint(0, len(string.punctuation)-1)
    return(string.punctuation[random])

def password_generator(length=14):
    password=''
    i=0
    last=0
    previous=0
    third=0
    types=[]
    while i < length:
        random = randint(1,4)
        #make sure password doesn't have more than 3 of the same types in a row
        if random==third and random==previous and random==last:
            continue
        types.append(random)
        third=previous
        previous=last
        last=random
        if random == 1:
            password = password + str(get_lower())
            i+=1
        if random == 2:
            password = password + str(get_upper())
            i+=1
        if random == 3:
            password = password + str(get_number())
            i+=1
        if random == 4:
            password = password + str(get_special())
            i+=1
    #make sure password has at least one of each type
    if 1 in types and 2 in types and 2 in types and 4 in types:
        print(password)
    else:
        password_generator(length)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            password_generator(int(sys.argv[1]))
        except:
            print("Script only accepts integers as argument or no argument")
    else:
        password_generator()