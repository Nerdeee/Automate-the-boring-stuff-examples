import random

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