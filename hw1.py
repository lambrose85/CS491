"""
Book problem programming assignment 
"""


def books(array):
    length = len(array)
    if(length ==0):
        print("No one has read this")
    if(length ==1):
        print(array[0]+" has read this")
    if(length == 2):
        print(array[0]+" and "+array[1]+" have read this")
    if(length ==3):
        print(array[0]+", "+array[1]+" and "+array[2]+" have read this")
    if(length ==4 ):
        print(array[0]+", "+array[1]+" and 2 others have read this")
    if(length >4):
        x = length-2
        print(array[0]+", "+array[1]+" and "+str(x)+" others have read this")


#initialize array/list then add names with while loop
booklist = list()
print('Add names to list, press q/Q to finish')
index =0
flag = True
while flag:
    s = input()
    if(s=='q'or s=='Q'):
        flag=False
    else:
        print("Added "+s+" to list")
        booklist.append(s)
        index += 1
    
books(booklist)


