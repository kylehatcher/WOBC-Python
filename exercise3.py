import sys

if sys.argv[1] > sys.argv[2]:
    print(sys.argv[1])
elif sys.argv[2] > sys.argv[1]:
    print(sys.argv[2])

if 'time' in sys.argv[3]:
    print(int(sys.argv[1]) + int(sys.argv[2]))

if ((int(sys.argv[1])%2 == 1) and (int(sys.argv[2])%2 == 1)) or (int(sys.argv[1])%3==0) or (int(sys.argv[2])%3==0):
    print(sys.argv[3])

if len(sys.argv) > 4:
    print('error')