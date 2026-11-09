#Questão1:Entrada de Dados e Operações Financeiras
#Crie um programa em Python que simule a compra de um produto.

nomeproduto = input("Digite o nome do produto: ")
precounitario = float(input("Digite o valor unitário: "))
quantidadevendida = int(input("Digite a quantidade ventida: "))
subtotal = (precounitario * quantidadevendida)
print(f"Valor do subtotal: {subtotal}" )

imposto = (subtotal + precounitario) * 0.8
print(f"Valor do imposto: {imposto}" )

valortotal = (subtotal + imposto)
print(f"Valor Total: {valortotal:.2f}")

