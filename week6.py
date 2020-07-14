# Week 6 of intro to python!

# Functions = named group of statements which can be executed upon request!

# When you 'call' a function you are requesting a set of code to run from elsewhere.
# If the function you are calling is in another file you may need to use the 'import' keyword and reference the file.

# When you define a function you use 'def' followed by the function name, which is always followed by a set of parenthesis () and a :
# The contents of a function should be indented like a loop or if statement
# The final statement in your function should be 'return'

def printcolor():  # Function definition
    print("Blue")  # Function functionality xD
    return         # Function exit statement

# "Main Document"

print('Hello')

printcolor() # Here we are calling the function

printcolor() # You may call a function many times within the same program!

def printColour(aColor):  # Inside the definition of this function we have provided a variable. This variable must be provided with a peice of information, which is whatever is 
    print(aColor)         # provided in the ()
    return

# "Main Document"

print('Hello')

printColour("Blue")       # Here we have a call to our printColour function and we pass the information of "Blue" or "Black" which takes the place of the parameter "aColor" 
                          # in the function definition!
printColour("Black")


# This time we are asking the user to provide us with the information for the function parameter! 
def print_Color(favColor):
    print(favColor)
    return

user_color = input('What is your favorite color?:')

print_Color(user_color)

# Here we are iterating print statements
def countSticks(sticks, howMany):    # We pass the values of 'sticks' and 'howMany' when we assign the variables inside of the call function in the main document. 
    for i in range(howMany):         # countSticks(variable for the value or parameter 1, variable for the value of parameter 2)
        print(sticks)
    return

num_sticks = int(input('How many sticks are there?:'))
string_sticks = 'sticks'

print('Hello')

countSticks(string_sticks, num_sticks)

# Compute the average of two values
def average(num1, num2):
    sum = num1 + num2    # sum and result are 'local variables' and cannot be used outside the function definition!
    result = sum / 2
    return

answer = average(10, 20)      # When the funciton is complete the place 'average' sits will be replaced with the final value, therefore we have to do something with the value 
print('The average of 10 and 20 is', answer) # that is returned. A good thing to do here is to wrap the returned value inside a unique variable.