import random
import copy
import pprint

names = ['sasha', 'ben', 'wes', 'owen']

c1, c2, c3, c4 = names

print('enter a name of a pet')
name = input()

if name not in names:
    print('There is no animal with that name here')
else:
    print('The animal ' + name + ' exists')

# Enumerating a list
items = ['pens', 'pencils', 'erasers']

for index, item in enumerate(items):
    print('Index: ' + str(index) + ' Item: ' + item)

# Using random.choice and random.shufflehi
rChoice = random.choice(items)
print(rChoice)

random.shuffle(items)
print(items)

test = 6
test *= 2
print(test)

# append and insert methods

items.append('notebook')
print(items)
items.insert(0, 'laptop')
print(items)

# remove method
items.remove('pencils')
print(items)

testRemList = ['cat', 'cat', 'cat', 'dog', 'cat', 'dog', 'turtle', 'elephant']
testRemList.remove('cat')
testRemList.remove('cat')
print(testRemList)

# sort method
userNames = ['Bob', 'andrew', 'zac', 'Tim', 'Chris']
userNames.sort(key=str.lower)
print(userNames)

# \
print('The man in the ' + \
      'yellow hat')

# ranges in strings

rangeInStringName = "Louis"
print(rangeInStringName[1:3])

newRangeInStringName = rangeInStringName[0:3] + "uygwgyqgyf" + rangeInStringName[2:4]
print(newRangeInStringName)

# tuple and list casting 
print(tuple([1,2,3]))
print(list((1,2,3)))

# references 
reg_list = [1,2,3]
ref_list = reg_list
ref_list[1] = 10
print(reg_list)
print(ref_list)

# copy
spam_copy = ['A', 'B', 'C', 'D']
print(id(spam_copy))
spam_cheese = copy.copy(spam_copy)
print(id(spam_cheese))

spam_cheese[1] = '42'
print('spam_copy = ', spam_copy)
print('spam_cheese = ', spam_cheese)

# dictionary
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
yourCat = {'disposition': 'loud', 'color': 'gray', 'size': 'fat'}
print(myCat['size'])
print(myCat == yourCat)

birthdays = {'Alice': 'Mar 4', 'Bob': 'April 7'}

while True:
    print('Enter your name')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print('your bithday is ', birthdays[name])
    else:
        print('Your birthday was not found in our database. Enter your birthday below:')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated')

# dictionary methods
print()
for items in birthdays.values():
    print(items)

print()

for items in birthdays.items():
    print(items)

print('Alice' in birthdays.keys())

# get() method
picnicItems = {'Apple': 1, 'Ham': 3}
print('I am bringing ' + str(picnicItems.get('Cheese', 2)) + ' cheese.')

picnicItems.setdefault('Cheese', 2)
print(picnicItems)

charCountMessage = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in charCountMessage:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# pprint.pprint(count)
print(pprint.pformat(count))

# tic tac toe
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
           'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
           'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(myBoard):
    print(myBoard['top-L'], '|' ,myBoard['top-M'], '|' ,myBoard['top-R'])
    print('- + - + -')
    print(myBoard['mid-L'], '|' ,myBoard['mid-M'], '|' ,myBoard['mid-L'])
    print('- + - + -')
    print(myBoard['low-L'], '|' ,myBoard['low-M'], '|' ,myBoard['low-R'])

turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print(turn + ' turn to move')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)

# Chapter 6 - Manipualting Strings

# isX()
stringIsAlNum = "Hello"
print(stringIsAlNum.isalnum())
stringIsSpace = " "
print(stringIsSpace.isspace())
print(stringIsAlNum.isspace())

# startsWith, endsWith
helloString = "Hello there"
print(helloString.startswith('He'))

# split, join
print(', '.join(['Barrack', 'Obama']))
longPhrase = 'This is a long phrase with lots of words with an s'
print(longPhrase.split('s'))

# partition
partitionString = "This is a string that needs to be partitioned"
firstPart, midPart, lastPart = partitionString.partition('n')
print(firstPart)
print(midPart)
print(lastPart)

# rjust, ljust, center
print(partitionString.rjust(10))
print(partitionString.ljust(5, '*'))
print(partitionString.center(3, '-'))
print('hello'.rjust(50))

# picnicTable example
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwhich': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
