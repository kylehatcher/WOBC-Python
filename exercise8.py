import sys
import math

def common_letter(text):
    text=text.upper()
    u=[]
    d={}
    for c in text:
        if c not in u:
            u.append(c)
    for c in u:
        d[c] = text.count(c)
    count=0
    char=''
    for key, value in d.items():
        if value > count and key!=' ':
            count=value
            char=key
    print(str(char) + ' is the most common letter. It occurs ' + str(count) + ' times.')

def percent_the(text):
    text=text.upper()
    count=0
    total=0
    for word in text.split():
        total+=1
        if word == 'THE':
            count+=1
    percent = math.floor((count/total)*100)
    print("The word 'The' is " + str(percent) + "% of the words.")

def first_ten(text):
    firstTen = ''
    split=text.split()
    for i in range(0,10):
        firstTen = firstTen+split[i]+' '
    f = open('challenge8_output.txt', 'w')
    f.write(firstTen)
    f.close()
    print(firstTen)

with open(sys.argv[1]) as f:
    text=f.read()
    common_letter(text)
    percent_the(text)
    first_ten(text)