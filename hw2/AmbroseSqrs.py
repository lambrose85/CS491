def squareSums(num):
    sqr = 0
    for i in range(1,num+1):
        sqr+= i**2
    return sqr
    
def squareSum(num):
    sqr =0
    for i in range(1,num+1):
        sqr+=i
    sqr = sqr**2
    print(sqr)
    return sqr


print("enter a number")
value = input()
value = int(value)
num = squareSums(value)
print(num)
res= squareSum(value)
dif=res-num
print("difference between square of sum and sum of squars: "+str(dif))
