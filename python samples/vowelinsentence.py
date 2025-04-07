def countvowels(alpha):
    count = 0
    vowels = 'aeiou'
    for i in alpha:
        for j in vowels:
            if i == j:
                count+=1
    x = f'number of times vowels occured is {count}' 

    return x





word = 'find the vowels in the sentence'
print(countvowels(word))
