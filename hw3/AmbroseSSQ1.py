"""Using map and lambda to rewrite the sum of squares from previous homework"""

def mysum(x):
   result=list(map(lambda n:n**2, x))
   a = sum(result)
   return a

def getSum(x):
    val = sum(x)
    return val

Test = []
print("enter a number")
result = input()
sumval = int(result)
for i in range(1,sumval+1):
    Test.append(i) 

val = mysum(Test)
sqrSum = getSum(Test)**2

final = sqrSum-val
print("Difference is: "+str(final))

