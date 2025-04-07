def anagram(anag,alpha):
    count = 0
    for i in anag:
        for j in alpha:
            if i in j:
                count+=1
    if len(anag)==count:
        return True
    return False
    

anag='adhil'
alpha='dhila'
print(anagram(anag,alpha))