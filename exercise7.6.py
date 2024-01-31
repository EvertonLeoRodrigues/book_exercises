"""Write a program that reads three strings. Print the result of replacing, 7
in the first string, the characters from the second string with those from the third.
"""

def replacing_char(string1, string2, string3):
    return string1.replace(string2, string3)

print(replacing_char('Olá mundo', 'mundo', 'inferno'))