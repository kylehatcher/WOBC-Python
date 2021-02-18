import sys

def unique_check(text):
    cap=text.upper()
    for c in text:
        up=c.upper()
        if cap.count(up) == 1:
            print(c)
            break
    print("")

if len(sys.argv) > 1:
    unique_check(sys.argv[1])