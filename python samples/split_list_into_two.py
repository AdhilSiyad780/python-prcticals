def split(alpha,scm):
    part1 = alpha[:index]
    part2 = alpha[index:]

    return part1,part2

li = [1,2,3,4,5,6,7,8,9,10]
index=5
first,last=split(li,index)

print(first)
print(last)
