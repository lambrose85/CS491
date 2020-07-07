"""Reading and writing from a file in python"""

f = open("test.txt", "x")
list= ['this is line 1\n', 'this is line 2\n', 'this is line 3\n']
f.writelines(list)
f.close()
f = open("test.txt")
print(f.readline())
print(f.readline())
f2= open("test.txt", "a")
f2.write("This is the fourth line\n")
f2.close()
while True:
    buff = f.readline()
    print(buff)
    if len(buff) ==0:
        break

