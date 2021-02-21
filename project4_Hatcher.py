import collections
import string

def find_offset(word, list):
    converted_dict = {}
    #n is possible 0-25
    for n in range(0,26):
        i=0
        guessed = ''
        for c in sorted(list):
            if i+n > 25:
                i = 0-n
            converted_dict[c] = string.ascii_uppercase[n+i]
            i+=1
        for z in range(0, len(word), 5):
            guessed += converted_dict.get(word[z:z+5])
        print(n," - ",guessed)
    while True:
        try:
            offset = int(input("What is the offset? "))
            break
        except:
            print("Offset must be an integer")
            continue
    i=0
    solved_dict={}
    for c in sorted(a):
        if i+offset > 25:
            i = 0-offset
        solved_dict[c] = string.ascii_uppercase[offset+i]
        i+=1
    return(solved_dict)

f = open('word_search_encoded.txt')
text = f.read()
f.close()

split = text.split('\n\n')
search = split[0]
search_letters = search.split()
words = split[1].split('\n')

d={}
a=[]
for l in search_letters:
    d[l] = search_letters.count(l)
for k,v in d.items():
    a.append(k)

solved_dict = find_offset(words[1], a)

new_file = open('word_search_decoded.txt','w')
new_file.close()
word_search = ''
search_words = ''
with open('word_search_decoded.txt','a') as f:
    for s in search.split('\n'):
        guess=''
        for letter in s.split():
            guess += solved_dict.get(letter)
            guess+=' '
        guess = guess.strip()
        word_search+=guess.replace(' ', '')
        word_search+='\n'
        f.write(guess)
        f.write('\n')
    for w in words:
        f.write('\n')
        guess=''
        for i in range(0, len(w), 5):
            guess += solved_dict.get(w[i:i+5])
        search_words+=guess
        search_words+='\n'
        f.write(guess)
word_search=word_search.strip()
search_words=search_words.strip()
print()
print('******************************** SOLUTION ********************************')
matrix=[]
i=0
for r in word_search.split('\n'):
    #x={}
    #j=0
    row=[]
    for c in r:
        row.append(c)
        #x[str(j)+':'+str(i)] = c
        #j+=1
    matrix.append(row)
    i+=1
found=False
for w in search_words.split('\n'):
    total_letters=len(w)
    count=1
    direction=''
    row=0
    col=0
    found=False
    for i in range(0, len(matrix)):
        if w[0] in matrix[i]:
            for g in range(0,len(matrix[i])):
                if matrix[i][g] == w[0]:
                    row=i
                    col=g
                    while not found:
                        #Look right      [0,+b]
                        count=1
                        while total_letters > count:
                            for b in range(1,len(w)):
                                if len(matrix[row]) > col+b:
                                    if matrix[row][col+b] == w[b]:
                                        count+=1
                                        next
                                    else:
                                        count=total_letters+1
                                        break
                                else:
                                    count=total_letters+1
                                    break
                            if count == total_letters:
                                found=True
                                break
                            else:
                                continue
                        if found:
                            direction='RIGHT'
                            break
                        #Look right/down [+b,+b]
                        count=1
                        while total_letters > count:
                            for b in range(1,len(w)):
                                if len(matrix[row]) > col+b and len(matrix) > row+b:
                                    if matrix[row+b][col+b] == w[b]:
                                        count+=1
                                        next
                                    else:
                                        count=total_letters+1
                                        break
                                else:
                                    count=total_letters+1
                                    break
                            if count == total_letters:
                                found=True
                                break
                            else:
                                continue
                        if found:
                            direction='RIGHT/DOWN'
                            break
                        #Look down       [+b,0]
                        count=1
                        while total_letters > count:
                            for b in range(1,len(w)):
                                if len(matrix) > row+b:
                                    if matrix[row+b][col] == w[b]:
                                        count+=1
                                        next
                                    else:
                                        count=total_letters+1
                                        break
                                else:
                                    count=total_letters+1
                                    break
                            if count == total_letters:
                                found=True
                                break
                            else:
                                continue
                        if found:
                            direction='DOWN'
                            break
                        #Look left/down  [+b,-b]
                        count=1
                        while total_letters > count:
                            for b in range(1,len(w)):
                                if col-b >= 0 and len(matrix) > row+b:
                                    if matrix[row+b][col-b] == w[b]:
                                        count+=1
                                        next
                                    else:
                                        count=total_letters+1
                                        break
                                else:
                                    count=total_letters+1
                                    break
                            if count == total_letters:
                                found=True
                                break
                            else:
                                continue
                        if found:
                            direction='RIGHT/DOWN'
                            break
                        #Look left       [0,-b]
                        count=1
                        while total_letters > count:
                            for b in range(1,len(w)):
                                if col-b >= 0:
                                    if matrix[row][col-b] == w[b]:
                                        count+=1
                                        next
                                    else:
                                        count=total_letters+1
                                        break
                                else:
                                    count=total_letters+1
                                    break
                            if count == total_letters:
                                found=True
                                break
                            else:
                                continue
                        if found:
                            direction='LEFT'
                            break
                        #Look left/up    [-b,-b]
                        count=1
                        while total_letters > count:
                            for b in range(1,len(w)):
                                if col-b >= 0 and row-b >= 0:
                                    if matrix[row-b][col-b] == w[b]:
                                        count+=1
                                        next
                                    else:
                                        count=total_letters+1
                                        break
                                else:
                                    count=total_letters+1
                                    break
                            if count == total_letters:
                                found=True
                                break
                            else:
                                continue
                        if found:
                            direction='LEFT/UP'
                            break
                        #Look up         [-b,0]
                        count=1
                        while total_letters > count:
                            for b in range(1,len(w)):
                                if row-b >= 0:
                                    if matrix[row-b][col] == w[b]:
                                        count+=1
                                        next
                                    else:
                                        count=total_letters+1
                                        break
                                else:
                                    count=total_letters+1
                                    break
                            if count == total_letters:
                                found=True
                                break
                            else:
                                continue
                        if found:
                            direction='UP'
                            break
                        #Look right/up   [-b,+b]
                        break
        if found:
            print('{:<30s} found in row {:>2d} column {:>2d} going {}'.format(w, row, col, direction))
            break
    if not found:
        print("{:<30s} not found".format(w))