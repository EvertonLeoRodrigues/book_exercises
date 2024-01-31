"""Write a program that reads a two strings and returns a tird with just the characters
in one of those strings!
"""

def incommon_char(first_string, second_string):
    first_set = set(first_string.split())
    second_set = set(second_string.split())
    
    tird_string = list(first_set-second_set)
    return ' '.join(tird_string)

first_sentence = input('Enter your first sentence: ').lower()
second_sentence = input('Enter your second sentence: ').lower()

print(incommon_char(first_sentence, second_sentence))
