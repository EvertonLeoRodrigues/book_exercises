#Escreva um programa que leia um número e verifique se é ou não um número primo.
#Para fazer essa verificação, calcule o resto da divisão do numero por 2 e depois
#por todos os números impares até o número lido. Se o resto de uma dessas divisões for 
#igual a zero, o número não é primo. Observe que o 0 e 1 não são primos e que 2 é o único
#número primo que é par

while(True):
    primeNumber = int(input("Digit one prime number or 0 for exit: "))
    if(primeNumber == 0):
        break
    cont = 3
    prime = True

    while(cont < primeNumber):
        if(primeNumber % cont == 0 or primeNumber%2==0):
            prime = False
            break
        cont+=2

    if(prime):
        print("Is a prime number!")
    else:
        print("Isn't a prime number!")
