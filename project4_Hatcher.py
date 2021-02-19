import collections
import string

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


b_i_d = {}
#n is possible 0-25
for n in range(0,26):
    i=0
    guessed = ''
    for c in sorted(a):
        if i+n > 25:
            i = 0-n
        b_i_d[c] = string.ascii_lowercase[n+i]
        i+=1
    for z in range(0, len(words[1]), 5):
        guessed += b_i_d.get(words[1][z:z+5])
    print(n," - ",guessed)

offset = int(input("What is the offset? "))

i=0
for c in sorted(a):
    if i+offset > 25:
        i = 0-offset
    b_i_d[c] = string.ascii_lowercase[offset+i]
    i+=1
new_file = open('word_search_decoded.txt','w')
new_file.close()
with open('word_search_decoded.txt','a') as f:
    for s in search.split('\n'):
        guess=''
        for letter in s.split():
            guess += b_i_d.get(letter)
            guess+=' '
        guess = guess.strip()
        f.write(guess)
        f.write('\n')
    for w in words:
        f.write('\n')
        guess=''
        for i in range(0, len(w), 5):
            guess += b_i_d.get(w[i:i+5])
        f.write(guess)