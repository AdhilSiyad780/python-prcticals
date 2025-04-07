import math
def binomial_coefficient(n,k):
    sum1=1
    sum2=1
    sum3=1
  
    for i in range(1,n+1):
        sum1*=i
    for j in range(1,k+1):
        sum2*=j
        
    local = n-k
    for i in range(1,local+1):
        sum3*=i
    result = sum1/(sum2*sum3)
    new = math.ceil(result)
    return new
       
result = binomial_coefficient(32,4)
print('the number of ways to be dealt exactly 4 action is {result}')
