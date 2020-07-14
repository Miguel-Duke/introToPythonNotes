#Week 3 !
# A sequence is a variable that stores a collection of data.
# There are 3 types of sequences: a string, a list, and a tuple.

# ' string '
word_1 = input('enter a string')
word_2 = 'this is also a string'

# All sequences are indexable, so we can access any individual character in a
# sequence by using brackets ' variable[#] '

print('The item at word_2s index 4 is', word_2[4])

print( word_2[0] )

# len function can be used with all sequences, all sequences are printable
# To find out how many characters are in a string use ' len(variable) '

size_word_2 = len(word_2)

print('The number of characters in word_2 is', size_word_2)

#To print out the last character of a string:

print('the last character in word_2 is', word_2[len(word_2) -1])

# you can also concatenate two sequences of the same type

concatenated_one = word_1 + word_2

print('The concatenated string is:', concatenated_one )

# to add a space between the concatenated strings add a blank string

concatenated_two = word_1 + ' ' + word_2
print ('We added a space here', concatenated_two )

# to remove a space between the end of the string and the next variable
# remove the comma and add a +

print ('Concatenated without the space' + concatenated_one)

# strings are immutable sequences, once they are made you cannot change any
# individual character in it alone

# a list is a sequence of any type of character

list_one = [ 3, 6, 1, 11 ] #list of ints
list_two = [ 'mike', 'miguel', 'toasty' ] #list of strings
list_three = [ 44.5, 66.7 ] #list of floats
list_four = [ 'money', 55.6, 4 ] #variety pack xD
list_five = [] #empty list

# printing lists will provide all of the characters on the right side of the =
# this includes brackets

print(list_two)

# printing lists without those extra characters can be done through indexing

print(list_two[0], list_two[1], list_two[2])

print('The size of list_two is:', len(list_two))

# concatenating lists

list_six = list_two + list_four

print('The new list contains:', list_six)

# list_seven = list_two + ' ' + list_four #this should add a space 

# print('The other new list contains:', list_seven) #commented out until solved

# unlike strings you are allowed to use indexing on the left side of a statement
# of a list to change the contents of the list. Therefore lists are a
# mutable type of sequence.

list_one[2] = 9
list_one[3] = 12

print('list_one is now:', list_one)

# you can add to a list by using the append command, ex

myList_one = [7]
myList_one.append(8)

print(myList_one)

# you can also prompt the user to add to a list

number_one = int(input('Enter an integer'))

myList_one.append(number_one)

print(myList_one)

# removing things from lists

list_one.pop(1)
print(list_one)

list_two.remove('toasty')
print(list_two)

# a ' tuple ' is similar to a list but instead of using [] use ()

tuple_1 = ('mike', 'miguel')
tuple_2 = (8, 16)
tuple_3 = ('toasty', 8, 66.6)

# tuples are just like lists but they are immutable! tuples do not support
# assignment, so if you are creating a collection of stuff that will not change
# use a tuple!

# functions that work with all sequences

lastList = [8, 16, 24]
x = len(lastList)
print(x)

y = min(lastList) # 'min' gives us the lowest value, or closest letter to A
print(y)

z = max(lastList) # 'max' gives us the highest value, or closest letter to Z
print(z)

a = sum(lastList) # 'sum' gives us the sum of the list
print(a)



