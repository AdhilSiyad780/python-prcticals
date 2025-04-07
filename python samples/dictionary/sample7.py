def count(alpha):
    beta = {}
    for char in alpha:
        if char in beta:
            beta[char]+=1
        else:
            beta[char]=1
    return beta

gama = 'malayalam'
print(count(gama))
#Write a function that takes a string and returns a dictionary with the frequency of each character.