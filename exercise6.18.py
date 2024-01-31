#Escreva um programa que gere um dicionario, em que cada chave seja um caracter, e seu
#valor seja o numero desse caracter encontrado em uma frase lida.

import string


letras = string.ascii_letters

frase = input('Digite uma frase: ')

numeros_caracteres_encontrados = {letra: frase.count(letra) for letra in letras}

for chave in list(numeros_caracteres_encontrados.keys()):
    if numeros_caracteres_encontrados[chave] == 0:
        numeros_caracteres_encontrados.pop(chave)

print(numeros_caracteres_encontrados)
