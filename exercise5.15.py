#Escreva um programa oara controlar uma pequena máquina registradora.
#Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
#Utilize a tabela de códigos a seguir para obter o preço de cada produto.
#Código 1: 0.50 - Código 2: 1.00 - Código 3: 4.00 - Código 5: 7.00 - Código 9: 8.00
#Seu programa deve exibir o total das compras depois que o usuário digitar 0.
#Qualquer outro código deve gerar a mensagem de erro "Código inválido"



valueForPay = 0
while True:
    code = int(input("Digit your code: \n1 \n2 \n3 \n5 \n9: "))
    if(code == 1):
        quantityOfPurchases = int(input("Digit de quantity of purchases: "))
        valueForPay +=  (quantityOfPurchases*0.50)
    elif(code == 2):
        quantityOfPurchases = int(input("Digit de quantity of purchases: "))
        valueForPay += (quantityOfPurchases*1)
    elif(code == 3):
        quantityOfPurchases = int(input("Digit de quantity of purchases: "))
        valueForPay += (quantityOfPurchases*4)
    elif(code == 5):
        quantityOfPurchases = int(input("Digit de quantity of purchases: "))
        valueForPay += (quantityOfPurchases*7)
    elif(code == 9):
        quantityOfPurchases = int(input("Digit de quantity of purchases: "))
        valueForPay += (quantityOfPurchases*8)
    elif(code == 0):
        print(f"the value for payment is R${valueForPay:.2f}!")
        break
    else:
        print("!!!!!The entered code is invalid!!!!!")