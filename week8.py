# Week 8 of intro to python notes!

# Strings!

# Strings are immutable, therefore they cannot be changed in the same way lists can.

# Methods are functions which are used with a specific type of object.


# Techniques to "manipulate" strings:

# ~ Sclicing: is indicated by two brackets and a colon [:], [start index : stop index + 1]. If you dont give a stop index parameter it automatically goes to the end of the string, [3:] = index 3 to last index + 1.

# You can use the method "find" by specifying what string it will work with.     stringName.find("example")
# Find will tell you not only if something is in a string but also what index position it is at. Find specifically tells you where the FIRST occurance of (what you are searching for) is.
# If find cannot find it the returned value is -1.

# Good class "find" example:              The goal is to capitalize the first w!
#    word = input('Enter a scentence')
#    pos = word.find("w")
#    if pos == -1:
#        print("There is no w")
#    else:
#        word = word[0:pos]+"W"+[pos+1:]

# You can also give find a second parameter which is what index to start searching at.    example = stringName.find(item, index to start searching from)

# Class find example 2:                   The goal here is to count the "w"'s
#    word = input("Enter a sentence")
#    count = 0
#    pos = word.find("w")
#    while pos != -1:
#        count += 1
#        pos = word.find("w", pos+1)

# Another method to be used is the .count method which takes one argument.    stringName.count("item")
# This counts the number of occurances of a particular item in a string.

# The .replace method replaces and item with another provided argument taking two arguments.
# stringName.replace(item to be replaced, item to replace it)

# Another method is the strip method.    stringName.strip()
# What strip does is remove all leading blanks as well as all trailing blacks:  _ _ _ words and stuff _ _ _      will then be      words and stuff

# stringName.capitalize() will capitalize the first character!

# stringName.split() will take a string and return a list. The list will contain smaller strings that are formed by breaking off where each space in a string is.
# example: word = "Hello there how are you".    word.split()  =  word['Hello', 'there', 'how', 'are', 'you']
# The split method can also create lists based on other characters as well, not just spaces.
# example: date = input('Enter a date')
# date = "3-9-2020"
# newDate = date.split('-')  =  newDate['3', '9', '2020']
# When using the split method, if no argument is given the defaults to a space, otherwise it uses the character provided in the argument.

# The join method takes a character as an argument and then places it in between list elemnets to form a string.
# "/".join(listName)
# example: date = ["3", "9", "2020"]
# newDate = "/".join(date)
# newDate - "3/9/2020"


# Class example 3
# Here we are going to ask the user to input a date in this format:    Month (day as a number), (year as a number)    ex: March 9, 2020
# Afterwards we are going to adjust the input to appear like this 03-09-2020
# So just to be clear    input = March 9, 2020   ---->    03-09-2020

def convertMonth(mon):
    mon = mon.lower()
    mon = mon.capitalize()
    if mon == 'January':
        return '01'
    elif mon == 'Febuary':
        return '02'
    elif mon == 'March':
        return '03'
    elif mon == 'April':
        return '04'
    elif mon == 'May':
        return '05'
    elif mon == 'June':
        return '06'
    elif mon == 'July':
        return '07'
    elif mon == 'August':
        return '08'
    elif mon == 'September':
        return '09'
    elif mon == 'October':
        return '10'
    elif mon == 'November':
        return '11'
    elif mon == 'December':
        return '12'
    else:
        return 'Error'

userDate = input("Please enter a date formatted: Month (1-31), (year numerically): ")
userDate = userDate.strip()    # Removes leading and trailing blanks!
while userDate.find('  ') != -1:    # This while statement looks for large sections of blanks inside the statement and continues to replace them with single blanks until the 
    userDate = userDate.replace("  ", " ")                                                                                                     # string is formatted properly!
while userDate.find(' ,') != -1:    # This while statement makes sure that the space to comma ratio is appropriate for the program.
    userDate = userDate.replace(" ,",',')
blankPos = userDate.find(" ")
month = userDate[0:blankPos]
commaPos = userDate.find(",")
day = userDate[blankPos + 1: commaPos]
year = userDate[commaPos + 2: ]

monthNum = convertMonth(month)    # function to convert month to a numerical representation

if len(day) == 1:
    day = '0' + day

print(monthNum + '-' + day + '-' + year)



    