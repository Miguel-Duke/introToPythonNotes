# This is an example we did as a class week 7 of intro to python!
# The module for this is intList_classModule.py

import intList_classModule

def main():
    numList = []    # This empty list is the placeholder variable for the user actions.
    response = intList_classModule.menu()
    while response != 5:    # This while statement is keeps the program open and running so long as the user does not choose 5.

        if response == 1:
            intList_classModule.addList(numList)
        elif response == 2:
            intList_classModule.printList(numList)
        elif response == 3:
            item = int(input('What are you looking for?:'))
            if item in numList:
                print('Its there!')
            else:
                print('Its not there!')
        else:
            intList_classModule.removeList(numList)

        response = intList_classModule.menu() # This function call keeps the program running so long as the user does not choose option 5.

main() # This funciton call is what actually runs the program!