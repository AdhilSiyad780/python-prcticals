
def whitespace(alpha):
    item = ""
    for i in alpha:
        if i != ' ':
            item = item+i
    return item
    
word = 'remove the whitespace'
print(whitespace(word))