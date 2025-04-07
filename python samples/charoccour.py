

word = 'lkksdflkadjfyiufsjdvzkxcaisduoj'
dic = {}
for letter in word:
    if letter != ' ':
        if letter in dic:
            dic[letter]+=1
        else:
            dic[letter]=1

print(dic)
   
        
          