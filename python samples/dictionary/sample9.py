def dunc(alpha):
    beta = {}
    for key,value in alpha.items():
        if value < 25:
            beta[key]=value
    return beta


dict1 = {'a': 10, 'b': 20, 'c': 30}
print(dunc(dict1))
