#Escreva um programa que exiba uma lista de opções(menu): adição, subtração, divisão, multiplicação
# e sai. Imprima a tabuada da operação escolhida. Repita até que a opção sair seja escolhida

while(True):
    option = int(input("Select one of the options: \n1. Addition\n2. Subtraction\n3. Division\n4. Multiplication\n5. Exit\n:"))

    if(option == 1):
        number = int(input("Select a number between 1 and 10: "))
        cont = 1
        while(cont<=10):
            print(number + cont)
            cont+=1
    elif(option == 2):
        number = int(input("Select a number between 1 and 10: "))
        cont = 10
        while(cont>=1):
            print(cont - number)
            cont-=1
    elif(option == 3):
        number = int(input("Select a number between 1 and 10: "))
        cont = 1
        while(cont<=10):
            print(number/cont)
            cont+=1
    elif(option == 4):
        number = int(input("Select a number between 1 and 10: "))
        cont = 1
        while(cont<=10):
            print(number * cont)
            cont+=1
    elif(option == 5):
        break
    else:
        print("Invalid option!")