number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
cont = 0
rest = number1

while (rest >= number2):
    rest -= number2
    cont+=1
    

print(cont, rest)