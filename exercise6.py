import sys

def which_fibonacci(num):
    found = False
    count=2
    nth=0
    n1=0
    n2=1
    if num == 0:
        print('Index: 1')
    elif num == 1:
        print('Index: 2')
    elif num > 1:
        while nth < num:
            count += 1
            nth = n1 + n2
            n1 = n2
            n2 = nth
        if nth == num:
            print('Index: ' + str(count))
        else:
            print('Index: 0')
    next_fibonacci(nth, n1, n2, num)

def next_fibonacci(nth, n1, n2, num):
    while nth <= num:
        nth = n1 + n2
        n1 = n2
        n2 = nth
    print('Next: ' + str(nth))

for i in range(1,len(sys.argv)):
    which_fibonacci(int(sys.argv[i]))