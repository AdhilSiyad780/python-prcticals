
# Write a function that merges two dictionaries. If a key exists in both, sum their values.


def merge(alpha,beta):
    main = beta.copy()
    new = {}
    for key,value in alpha.items():
        if key  in main:
            main[key]+=value
        else:
            main[key]=value
    return main




dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'b': 5, 'c': 15, 'd': 25}
print(merge(dict1,dict2))