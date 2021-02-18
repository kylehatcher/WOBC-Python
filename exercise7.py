import sys

def counts(string):
    u=[]
    d={}
    for c in string:
        if c not in u:
            u.append(c)
    for c in u:
        d[c] = string.count(c)
    print(d)

if len(sys.argv) > 1:
    counts(sys.argv[1])
else:
    print('{}')