#Escreva um programa que compare duas listas. Utilizando operações com conjuntos, imprima:
#°Os valores comuns às duas listas
#°Os valores que só existem na primeira
#°Os valores que existem apenas na segunda
#°Uma lista com os elementos não repeditos das duas listas
#°A primeira lista sem os elementos repetidos da segunda

lista_1 = []
lista_2 = []

while True:
    num1 = input('Digite números inteiros para a PRIMEIRA lista ou \"Enter\" para sair: ')
    if num1 == '':
        break
    try:
        int_num = int(num1)
        lista_1.append(int_num)
    except:
        print('Digite apenas valores inteiros!')

while True:
    num2 = input('Digite números inteiros para a SEGUNDA lista ou \"Enter\" para sair: ')
    if num2 == '':
        break
    try:
        int_num = int(num2)
        lista_2.append(int_num)
    except:
        print('Digite apenas valores inteiros!')

set_1 = set(lista_1)
set_2 = set(lista_2)

valores_iguais = set_1 & set_2
valores_apenas_da_primeira = set_1 - set_2
valores_apenas_da_segunda = set_2 - set_1
valores_nao_repetidos_nos_conjuntos = set_1|set_2
set_3 = set_1+set_2


print(f'\n{valores_iguais}\n{valores_apenas_da_primeira}\n{valores_apenas_da_segunda}\n{valores_nao_repetidos_nos_conjuntos}\n{set_3}')
