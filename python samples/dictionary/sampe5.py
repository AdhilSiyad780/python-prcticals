#Group by Length: Write a function that takes a list of words and returns a dictionary that groups the words by their length.
def lengthre(alpha):
    gama = {}
    for key in alpha:
        gama[key]=len(key)
    return gama
      


li = ['alikkutti','moideen','sajimon','sanggaran']
print(lengthre(li))

