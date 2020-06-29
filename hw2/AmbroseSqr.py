


    

def numCheck(num):
    if num.isdigit():
        print("calculating")
        return True
    else:
        print("NAN")
        return False

print("Enter a number to have its individual digits squared then combined to a new number")
num = input()

if num.isdigit():
    print("is number")
else:
    print("not number")
temp = str(num)


