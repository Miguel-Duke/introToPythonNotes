# Week 4 of class! The topic is making decisions in python!
# Indentation is how python recognizes common blocks. Standard indent is 4 spaces.
# Troubleshooting tip: if an error highlights the very start of a line, look
# to the line above it!

# If then statements!
# != means 'not equal to'
# == means 'is equal to'
# > 'greater than something', < 'less than something'
# >= 'greater than or equal to something', <= 'less than or equal to something'

number1 = int( input('Enter a number') )

if number1 != 0 :  
    answer = 100 / number1
    print('result is:', answer) 
else:
    print('Division by zero is not possible')

age1 = int(input('enter your age'))
if age1 >= 18 :
    print('vote tomorrow')
else:
    print('to young to vote')

grade = int(input('enter the student\'s grade'))
print('the student\'s grade is:', grade)

# When you have two operands that need to be true or false use a boolean operater 'and'
# You can also use the operator ' or ' if either condition can be met!

if grade >= 90:
    print('A')
if grade >= 80 and grade <90:
    print('B')
if grade >= 70 and grade <80:
    print ('C')
if grade < 70:
    print ('F')

# Instead of several 'if' statements you can use an 'elif' statement
# These statements skip the remaining 'if' statements in the event that one of
# the conditions are met. This method can skip redundant lines of code and save
# processing time.

if grade >= 90:
    print('Top 10 percent')
elif grade >= 50:
    print('Upper half')
elif grade <=  49:
    print('lower half')

# SPACING 

team = ['Mike', 'James', 'Ashley']

name1 = input('enter a name')

# the 'in' operator can be used to reference sequences
# to do the opposite you may use the 'not in' operator

if name1 in team:
    print(name1 , 'is on the team')
else:
    print(name1 , 'is not on the team')

team2 = team

team3 = ['Mike', 'James', 'Ashley']

if name1 in team2:
    print('That name is also in team 2')

# In the above example team and team2 both point to the same location in memory
# However despite being the "same" list of strings team3 points to a different
# location in memory.
# We can check on this by using the ' is ' operator.

if team is team2:
    print('team and team2 are the same object')
else:
    print('team and team2 are no the same object')

if team is team3:
    print('team and team3 are the same object')
else:
    print('team and team3 are not the same object')

# Due to how they share memory space team and team2 will be affected together by an
# adjustment to team.

print(team)
print(team2)

team.append('Trevor')
print(team)
print(team2)

# The above happens because while team and team2 are independent variable team2
# is set to point to the same memory space as team. Remember, variables dont
# hold the values themselves they simply point to the memory space where the values
# are held!

# An in class example:

number1 = int(input('enter a whole number'))
number2 = int(input('enter another value'))

print('pick one of these operations\n',
      '1 - for addition\n',
      '2 - for subtraction\n',
      '3 - for multiplication\n',
      '4 - for division')

choice = int(input())

if 1<= choice <=4: # this condensed statement says if the number is between 1 and 4
    if choice == 1: 
        print(number1 + number2)
    elif choice == 2: 
        print(number1 - number2)
    elif choice == 3:
        print(number1 * number2)
    else: # we can use else here because we know if they are in this menu this is the final option!
        if number2 == 0: 
            print('division by 0 is not possible') # we need a if else inside our fourth option in case they try to divide by 0
        else:
            print(number1 / number2)
else:
    print('invalid choice')


