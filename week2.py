#this program sums together two numbers
#input will always save the value as a string unless told to do otherwise
#we use the int command to save the variable as an integer, if we do not
#python will add the values as a string, so say 5 + 5 would be 55 and not the
#int 10 like we would want.

num1 = input('enter number 1')
num1 = int(num1)
num2 = input('enter number 2')
num2 = int(num2)

answer = num1 + num2

print(answer)

#you can use the type command to display what manner of variable it being used.

num3 = ('Five')
num4 = (5)

print( type(num3))
print( type(num4))

#space
print('SPACE')
#space

#python has "dynamic typing". Variable types can change from strings, ect as
#the code progresses.

value_1 = 6.66
print( type (value_1) )

value_1 = ('Six.SixSix')
print( type (value_1) )

#space
print('SPACE')
#space

#using a // instead of just one / will keep division answers as integers and not
#decimals (or "float").
#the % gives us the remainder after the // division.

value = input('how much change do you have?')
value = int(value)

quarters = value // 25
print('there are', quarters ,'quarters')

value = value % 25

dimes = value // 10
print('there are', dimes, 'dimes')

value = value % 10

nickels = value // 5
print('there are', nickels, 'nickels')

value = value % 5

pennies = value // 1
print('there are', pennies, 'pennies')

#space
print('SPACE')
#space







