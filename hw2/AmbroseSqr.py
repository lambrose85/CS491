
print("Enter a number to have its individual digits squared then combined to a new number")
num = input()

if num.isdigit():
    print("is number")
else:
    print("not number")
    check = False
    while(check==False):
        print("Enter an integer ")
        num = input()
        if num.isdigit():
          check = True

val = int(num)
exp=val**2
temp = str(num)

length = len(temp)
result = ""
for i in range(length):
   exp=int(temp[i])**2
   result +=str(exp)

print(int(result))



