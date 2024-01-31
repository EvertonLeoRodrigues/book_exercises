""" Write a program that reads two strings and returns a tird with the common characters
from the first and second strings!
"""
first_string = input('Enter your first string: ').lower()
second_string = input('Enter yout second string: ').lower()


def common_char(first_string, second_string):
    common_characters = list(set([char for char in first_string if char in second_string]))
    return ''.join(common_characters)


    

print(common_char(first_string, second_string))

