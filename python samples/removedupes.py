def remove_dupe(old_list):
    new_list=[]
    for x in old_list:
        if x not in new_list:
            new_list.append(x)
    return new_list
    
li = [1,2,3,4,5,6,4,5,6,7]
print(remove_dupe(li))
