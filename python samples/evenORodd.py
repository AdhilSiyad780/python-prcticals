def oddeven(alpha):
    odd = []
    even = []
    for i in alpha:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)

    print(even)
    print(odd)
li = [1,2,3,4,5,6,7,8,9]

oddeven(li)