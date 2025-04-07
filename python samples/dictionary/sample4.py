# Write a function that takes two dictionaries and returns a list of keys that are present in both dictionaries.

def present(alpha,beta):
    gama = {}

    for key1,values in alpha.items():
        
        if key1 in beta.keys():
            gama[key1]=values
        else:
            continue
    return gama


dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 20, 'c': 15, 'a': 10}

print(present(dict1,dict2))

