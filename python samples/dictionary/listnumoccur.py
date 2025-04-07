def count(alpha):
    dic = {}
    for ocur in alpha:
        if ocur in dic:
            dic[ocur]+=1
        else:
            dic[ocur]=1
    return dic



li = [1,2,3,4,5,6,7,8,94,5,6,7,8,92,3,4,5,6,78,8]
print(count(li))