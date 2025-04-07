def largest(alpha):
    large = 0

    for i in alpha:
        if i>large:
            large=i
    return large


li = [1,2,3,4,5,45,6,7,8,9]
print(largest(li))