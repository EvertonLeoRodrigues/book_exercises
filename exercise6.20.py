#Escreva um programa que compare duas listas. Considere a primeira lista a versão
#inicial e a segunda como a versão após alterações. Utilizando operações com conjuntos,
#seu programa deverá imprimir a lista de modificações entre essas duas versões listando:
#°Os elementos que não mudaram
#°Os novos elementos
#°Os elementos que foram removidos

lista = [round(x**(1/2), 2) for x in range(100)]

# valore_a_ser_modificados = [item for item in lista if item % 2 == 1]

lista_modificada = [i*-1 if i%2==1 else i for i in lista]

print(lista)
print('----------------------------------------------------')
print(lista_modificada)
print('----------------------------------------------------')
unchange = set(lista)&set(lista_modificada)
elementos_removidos = set(lista) - set(lista_modificada)
novos_elementos = set(lista_modificada) - set(lista)

print(f'Elementos que não mudaram: {unchange}\nNovos elementos: {novos_elementos}\nElementos removidos: {elementos_removidos}!')
