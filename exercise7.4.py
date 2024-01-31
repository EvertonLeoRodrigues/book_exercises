"""Write a program that reads a single string and prints how many times each character 
appears in that string!
"""

def many_times_char(string1):
    quanti_times_appears = {char : string1.count(char) for char in string1}
    return quanti_times_appears

print(many_times_char('O rato roeu a roupa do rei de roma!'))