def remove_odd(dic):
    return {key:value for key,value in dic.items() if value%2==0}



my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(remove_odd(my_dict))
