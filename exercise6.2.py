# #Write a program that reads a two lists and generates a third with the elements of
# #the first two

list1 = []
list2 = []

while(True):
    digitList1 = input("Digite qualquer valor para adicionar à lista 1 ou 0 para sair: ")
    if(digitList1 == "0"):
        break
    try:
        floatValue = float(digitList1)
        if floatValue.is_integer():
            list1.append(int(floatValue))
        else:
            list1.append(floatValue)
    except ValueError:
        list1.append(digitList1)

while(True):
    digitList2 = input("Digite qualquer valor para adicionar à lista 2 ou 0 para sair: ")
    if(digitList2 == "0"):
        break
    try:
        floatValue = float(digitList2)
        if floatValue.is_integer():
            list2.append(int(floatValue))
        else:
            list2.append(floatValue)
    except ValueError:
        list2.append(digitList2)

print(list1)
print(list2)
print(list1+list2)
