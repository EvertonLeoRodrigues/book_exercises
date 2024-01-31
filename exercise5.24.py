#Modifique o programa anterior de forma a ler um número n.
#Imprima os n primeiros números primos

while(True):
    primeNumber = int(input("Digit one prime number or 0 for exit: "))
    if(primeNumber == 0):
        break
    cont = 3
    numberOfPrimeNumbers = 0
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