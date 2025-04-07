def anagram(alpha,beta):
    count = 0
    for char in alpha:
        for i in beta:
            if i==char:
                count+=1
  
    if count == len(beta):
        return True
    return False


print(anagram('list','tist'))