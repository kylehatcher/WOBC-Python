import sys
x=0
t=0
for i in range(1,int(sys.argv[1])+1):
    if i%12 == 0:
        x+=1
        print(str(x) + ' dozen')
    elif i%3 == 0:
        print('triangle')
    elif i%4 == 0:
        print('square')
    t+=i
print(t)