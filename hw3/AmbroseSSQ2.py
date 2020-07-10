""" finding the difference of sum square with reduce"""
import functools

def sumSqr(x):
     
    result= list(map(lambda n:n**2, x))
    a= functools.reduce(lambda y,z: y+z, x)
    b = functools.reduce(lambda j,k:j+k, result)
    a = a**2
    dif = a-b
    print(a)


    return dif


print("Enter a number")
val = int(input())
nums = []
for x in range(1, val+1):
    nums.append(x)
result = sumSqr(nums)
print("The difference is: "+str(result))
