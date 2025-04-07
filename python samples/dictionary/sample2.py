
#Write a function that takes a dictionary and a value and returns the key(s)
#associated with that value. If multiple keys have the same value, return them in a list.


def swapped(alpha):
    x = []
    for values in alpha.values():
        if values not in x:
            x.append(values)
    return x
d = {'a': 10, 'b': 20, 'c': 10, 'd': 30, 'e': 20}

print(swapped(d))
