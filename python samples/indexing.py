arr1=[1,2,3,4,6,8,9,3,5,5,5,3,3,3]
arr2=[]
count=0
for i in arr1:
    for j in arr1:
        if i==j:
            count+=1
            if count>1 and i not in arr2:
                arr1.append(i)
        
    
print(arr2)