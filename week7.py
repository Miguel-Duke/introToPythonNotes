# Welcome to week 7 of into to python!

def simpleFunction():
    print('This is an example function!')
    return

def parameterFunction(example_parameter):
    print('This is an example of a function with a parameter, the parameter is', example_parameter)
    return

def returnFunction(x):
    x = x + 1
    return x

simpleFunction()
parameterFunction('arguemnt') # The value passed to a function is called an 'argument'

x = 1
x = returnFunction(x)
print('Our return example added one to x to get', x)

# Some class examples below!

def myfunc(value):
    x = 2    # Variables definied inside a function are called local variables!
    print(a +  x)    # You can use global variables in your functions if you wish!
    return           # Be cautious using global variables inside functions as it inhibits program readability!

# main_1

a = 5    # Varibales not defined in a single function are called global variables!
myfunc(a)

def main_1():    # It is often considered a best practice to put your "main program" in a function of its own. 
    b = 8      # Remember that this will cause all of the otherwise global variables to become local variables!
    print('My favorite number is', b)

# New example! main_2

def dimes_nickels(change):
    dimes = change // 10
    change = change % 10
    nickels = change // 5
    return dimes, nickels

def main_2():
    amount = int(input('How much money?:'))
    Dimes, Nickels = dimes_nickels(amount)    # This is an example of unpacking! The function is going to return two values, so if we provide to variables it will assign them in order!
    print('There are', Dimes, 'dimes and', Nickels, 'nickels!')    # On a similar note, if you have multiple values and one variable it will assign those values as a tuple to the variable!

# New example! main_3

def largest(numbers):
    if len(numbers) == 0:
        return -1
    else:
        big = numbers[0]
        for i in range(1, len(numbers) - 1):
            if numbers[i] > big:
                big = numbers[i]
        return big

def main_3():
    list_1 = [4, 7, 12, 3, 2]
    print( 'The largest number in list 1 is', largest(list_1) )

# New example! main_4

def doubleit(num):    # This function is an example of how variables dont change as they are passed to functions in parameters. Int type!
    numDubs = num * 2
    print(numDubs)
    return

def changeIt(name):    # This function is an example of how variables dont change as they are passed to functions in parameters. String type!
    name = 'Malzahar'
    print('Our prophet is', name)
    return

def doubleThem(values):    # This function is an example of how variables can change as they are passed to functions in parameters!  List type!
    for i in range(len(values)):    # The key here is that lists are 'mutable' types. Passing a value into a function without a avaible assignment variable 
        values[i] = values[i] * 2   # only changes the value if the value type is mutable! Lists are mutable but strings, ints, and tuples are not!
    print(values)
    return

def main_4():
    val = 77
    print('val is,', val)
    doubleit(val)
    print('val is still', val)
    Name_1 = 'Talon'
    print('is', Name_1, 'our prophet?')
    changeIt(Name_1)
    print('Ahh yes,', Name_1)    # Name_1 will still be Talon here!

    list_2 = [1, 3, 6, 8]
    doubleThem(list_2.copy)    # When the '.copy' concept is used a mutable type like a list will not be changed by passing it to a function!
    print('List_2 is', list_2)
    doubleThem(list_2)
    print('List_2 is now', list_2)   # Lists are mutable vaiable types and therefore can be changed when passed to functions as parameters!




main_1()
main_2()
main_3()
main_4()












