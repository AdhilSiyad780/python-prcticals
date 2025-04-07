sentence = 'i am the logest in this string'
long = ''
word = sentence.split()

for x in word:
    if len(x)>len(long):
        long=x
print(long)