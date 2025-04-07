def check_prime(x):
    if x<2:
        return False
    for i in range(2,(x//2)+1):
        if x%i == 0:
            return False
       
    return True

li = [1,2,3,4,5,6,13,17,78,47,9]

for i in li:
    if check_prime(i):
        print(f"{i} is prime")
    else:
        print(f'{i} is not prime')