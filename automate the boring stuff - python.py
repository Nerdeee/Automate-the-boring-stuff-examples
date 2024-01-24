import random
import copy
import pprint
import re

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

# Chapter 6 - Manipualting Strings]

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
print(partitionString.ljust(80, '*'))
print(80-(len(partitionString)))
print('hello'.rjust(50))

# picnicTable example
def printPicnic(itemsDict, leftWidth, rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k, v in itemsDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwhich': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)

# strip, lstrip, rstrip
wString = "      remove whitespace         "
print(wString.lstrip())
print(wString.strip())

# ord, chr
print(chr(ord('A') + 1))

# English to Pig Latin
'''print('Enter the English message to translate into Pig Latin: ')
message = input()

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')

pigLatin = []
for word in message.split():
    prefixNonLetters = ''
    while len(word) > 0 and not word[0].isalpha:
        prefixNonLetters+=word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefixNonLetters)
        continue
'''

print('Hello'.upper().isupper())

# regular expressions - .search(), .group(), .groups()

phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumberRegex.search('My number is 415-555-4242.')
print('My phone number is: ' + mo.group())

phoneNumberRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo2 = phoneNumberRegex2.search('My number is 415-555-4242.')
print('My area code is : ' + mo2.group(1) + ' and my phone number is ' + mo2.group(2))
areaCode, phoneNumber = mo2.groups()

print('My area code is: ' + areaCode + ' my phone number is ' + phoneNumber)

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group() + ' was found')

batRegex = re.compile(r'Bat(man|mobile|copter)')
mo3 = batRegex.search('Batmobile lost a wheel')
print(mo3.group(1))

phoneNumberOptional = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo4 = phoneNumberOptional.search('My phone number is 123-456-7890')
print('Matched full phone number: ' + mo4.group())

mo5 = phoneNumberOptional.search('My phone number is 456-7890')
print('Matched everything but the area code: ' + mo5.group())

haRegex = re.compile(r'(Ha){3,5}')
mo6 = haRegex.search('HaHaHaHaHa')
print(mo6.group())

mo7 = haRegex.search('Ha')
print(mo7 == None)

# ? has a double meaning in regular expressions. Either a nongreedy match when using something like {3,5} or it could mean that the part of the preceeding part is optional

# findall()

findAllRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo8 = findAllRegex.findall('Home: 123-456-7890 Work: 998-765-4321')
print('findall method with no groups in reg expression', mo8)

findAllRegexGroups = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo9 = findAllRegexGroups.findall('Home: 123-456-7890 Work: 998-765-4321')
print('findall method with groups', mo9)

# character classes

xmasRegex = re.compile(r'\d+\s\w+')
mo10 = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo10)

# ^ negative character class (find a substring that matches the opposite of what is defined in the regular expression)
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo11 = vowelRegex.findall('Robocop eats baby food. BABY FOOD')
print(mo11)

consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo12 = consonantRegex.findall('Robocop eats baby food. BABY FOOD')
print(mo12)

# ^ can also be used at the beginnig of a regular expression to indicate tyhat the searched string must begin with this reg ex
# $ is the opposite of ^ in that it must match the end of the searched string
beginsWithHello = re.compile(r'^Hello')
mo13 = beginsWithHello.search('Hello there')
print(mo13)

beginsAndEndsWithNum = re.compile(r'^\d+$')
mo14 = beginsAndEndsWithNum.search('12345678')
print(mo14)

# the wildcard "." character
wildCardRegex = re.compile(r'.at')
mo15 = wildCardRegex.findall("the cat in the hat had a bat to make things flat")
print(mo15)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo16 = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo16.groups())
print(mo16)

newLineRegex = re.compile('.*', re.DOTALL)
mo17 = newLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo17.group())

# re.IGNORECASE - an argument you can pass into the compile method that will be case insensitive
caseInsensitiveRegex = re.compile('wham', re.IGNORECASE)
mo18 = caseInsensitiveRegex.search('The made a WHAM sound when it hit the sign')
print(mo18.group())

# sub()
subNamesRegex = re.compile(r'Agent \w+')
mo19 = subNamesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob')
print(mo19)

# use re.VERBOSE for long expressions that allow multine regexs and comments
