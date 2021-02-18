import sys

def counts(string):
    d={}
    for c in string:
        d[c] = string.count(c)
    return(d)

d={}
if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):
        d.update(counts(sys.argv[i]))
print(d)