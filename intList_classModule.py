# This is the module page for the intList class project done for week 7 of intro to python!
# Main file is intList_classExample.py

def menu():
    print('1) Add a number to the list')
    print('2) Print the entire list')
    print('3) Search the list for an item')
    print('4) Remove a number from the list')
    print('5) EXIT')
    
    choice = int(input('Enter your choice 1 - 5. :'))
    while choice < 1 or choice > 5:
        choice = int(input('Please choose an option between 1 and 5:'))
    return choice

def addList(item):
    itemAdd = int(input('What number would you like to add to the list?:'))
    item.append(itemAdd)
    return

def printList(lst):
    for i in lst:
        print(i)
    return

def removeList(lst):
    itemRemove = int(input('What number do you want to remove?:'))
    if itemRemove in lst:
        lst.remove(itemRemove)
    else:
        print('This number is not on the list')
    return




