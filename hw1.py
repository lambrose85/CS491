"""
Book problem programming assignment 
"""


def books(arr):
    """
    get names to add to book list from user
    """
    print('Add names to list, press q/Q to finish')
    flag = True
    while flag:
        s = input("name\n")
        if(s=='q'or s=='Q'):
            flag=False
        else:
            print("Added "+s+" to list")


test= "hello"

books(test)
