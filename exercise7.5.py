"""Write a program that reads two strings and generates a third one, from which 
the characters of the second string have been removed from the first!
"""

def removed_char(string1, string2):
    for char in string2:
        string1 = string1.replace(char, '')

    return string1



string3 = removed_char('AAATTGGAAA', 'TG')
print(string3)