import sys

def factorial(num):
    f=1
    e=''
    while num > 0:
        f=f*num
        if num != 1:
            e = e + str(num) + 'x'
        else:
            e = e + str(num)
        num = num - 1
    print(e + ' = ' + str(f))

factorial(int(sys.argv[1]))