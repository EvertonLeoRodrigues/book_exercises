"""Write a program that reads two strings. Check if the second string occurs within the first
one and print its position
"""

first_first = input('Write your first sentence: ')
second_sentence = input('Write your first sentence: ')

if second_sentence.lower() in first_first.lower():
    print(first_first.find(second_sentence))
else:
    print('The second sentence not in first!')