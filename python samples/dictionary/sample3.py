def re_value(alpha,val): 
    for key,values in alpha.items():
        if values==val:
            return key



dict1 = {'a': 10, 'b': 20, 'c': 30}
value =  10

print(re_value(dict1,value))
#  Write a function that takes a dictionary and a value and
# returns the key(s) associated with that value. If multiple keys have the same value, return them in a list.