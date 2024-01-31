estoque = {
    'tomate':[1000, 2.30],
    'alface':[500, 0.45],
    'batata':[2001, 1.20],
    'feijão':[100, 1.50]
}


venda = []
while True:
    nome_produto = input('Digite o produto que deseja comprar ou \"sair\" para sair: ').lower()
    if nome_produto == 'sair':
        break
    quantidade_produto = int(input('Digite a quantidade que deseja comprar: '))
    encontrado = False
    for nome, dados in estoque.items():
        
        if nome_produto == nome and quantidade_produto <= dados[0]:
            venda.append([nome_produto, quantidade_produto])
            encontrado = True
            break
    if not encontrado:
        print('Não possuímos este produto em estoque:')
        
total = 0

print('Vendas:\n')

for operacao in venda:
    produto, quantidade = operacao
    preco = estoque[produto][1]
    custo = preco * quantidade
    print(f'{produto:12s}: {quantidade:3d}x{preco:6.2f} = R${custo:6.2f}')
    estoque[produto][0] -= quantidade
    total += custo
print(f'Custo total: R${total:21.2f}\n')
print('Estoque\n')
for chave, dados in estoque.items():
    print('Descrição: ', chave)
    print('Quantidade: ', dados[0])
    print(f'Preço: {dados[1]:6.2f}\n')        


