# Reads the file
# Parses each line
# Counts how many times each log level (ERROR, INFO, WARNING) appears
# Outputs the result as a dictionary

# log_counts = {}

# with open('log.txt', 'r') as myfile:
#     for line in myfile:
#         level = line.split(':')[0]
#         log_counts[level] = log_counts.get(level, 0) + 1
        
# print(log_counts)

# Count word frequence in a sentence
# import re

# sentence = "Hello, world! Hello world. HELLO... World?"
# frequency = {}
# myText = re.sub(r'[^\w\s]', '', sentence).lower()
# print(myText)

# Opens log.txt
# Reads lines
# Cleans punctuation and case
# Counts word frequency

# import re

# wordFrequency = {}

# with open('log.txt', 'r') as myFile:
#     for line in myFile:
#         cleanLine = re.sub(r'[^\w\s]', '', line).lower()
#         # print(cleanLine)
#         words = cleanLine.split()
#         for word in words:
#             wordFrequency[word] = wordFrequency.get(word, 0) + 1
#     print(wordFrequency)
    
# Return the sum of two numbers if they are even, else return their difference
# num1, num2 = input("num1: "), input("num2: ")
# if (int(num1) % 2 == 0) and (int(num2) % 2 == 0):
#     print(num1)
#     print(f"Their sum is: {int(num1)+int(num2)}")
# else:
#     print(f"Their difference is: {abs(int(num1)-int(num2))}")

# Print numbers 1 to 100. For multiples of 3 print Fizz, for 5 print Buzz, for both print FizzBuzz.
# for i in range(1,101):
#     print(i)
#     if (i % 3 == 0) and (i % 5 == 0):
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
        
# sentence = 'this is my string'
# sentence = sentence.split()
# print(' '.join(sentence[::-1]))

# Write a function to reverse a string without using slicing.
# def reverseString(someString):
#     result = ''
#     for char in someString:
#         result = char + result
#     return result

# myString = 'helloWorld'
# print(reverseString(myString))

# Find the Maximum of Three Numbers
# def findMax(x, y, z):
#     result= max(x,y,z)
#     # result = max(max1,z)
#     return result

# print(findMax(22,145,1))
# import string
# # Check if a string is the same forward and backward.
# myString = 'sjtjs'
# myOtherString = 'notthesame'

# def checkString(someString):
#     return someString == someString[::-1]

# # def checkString(someString):
# #     opposite = ''
# #     for char in someString:
# #         opposite = char + opposite
# #     return someString == opposite
    
# print(checkString('bassel'))

# Count how many times an element appears in a list.
# import re
# items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# def func1(someString):
#     clean = re.sub(r'[^\w\s]', '', someString).split()
#     print(clean)
#     frequency = {}
#     for item in clean:
#         frequency[item] = frequency.get(item, 0) + 1
#     most = max(frequency, key=frequency.get)

# items = 'apple, banana, apple, orange, banana, apple'
# print(func1(items))

# frequency = {}
# for item in items:
#     frequency[item] = frequency.get(item, 0) + 1
# print(frequency)

# Given a tuple, count how many times an item occurs and find its first index.
# t = (1, 2, 3, 2, 4, 2)
# emptyList = []
# for i, element in enumerate(t):
#     if element not in emptyList:
#         emptyList.append(element)
#         print(f'Item: {element} of index {i} was found {t.count(element)} times in the tuple')

# Find the Longest Word in a Sentence
# sentence = 'i want to find the longest word here'
# sent = sentence.split()
# maxLen, output = 0, ''
# # print(len('longest'))
# for i in sent:
#     if len(i) > maxLen:
#         maxLen = len(i)
#         output = i
# print(output)

# Remove Duplicates from List
# myList = ['apple', 'orange', 'apple', 'banana', 'apple', 'apple', 'banana', 'orange', 'berries']
# copyList = []
# for fruit in myList:
#     if fruit in copyList:
#         continue
#     else:
#         copyList.append(fruit)
        
# print(f'Final list is: {copyList}')

# Given a list of strings, return a dictionary with word counts.
# words = ['apple', 'banana', 'apple', 'orange', 'banana']
# myDict = {}
# for word in words:
#     myDict[word] = myDict.get(word, 0) + 1
    
# print(myDict)

# Given a text file called log.txt:
    # Reads the file
    # Parses each line
    # Counts how many times each log level (ERROR, INFO, WARNING) appears
    # Outputs the result as a dictionary
    
with open('log.txt', 'r') as myFile:
    emptyDict = {}
    for line in myFile:
        word = line.split(':')[0]
        emptyDict[word] = emptyDict.get(word, 0) + 1
    print(emptyDict)