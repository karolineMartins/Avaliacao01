#Questão2: Regras de Desconto com Estrutura Condicional
#Para alavancar as vendas,a loja criou uma política de descontos progressivos
#baseada no valor total da compra. 


valor = float(input("Digite o valor total da compra: "))


if valor < 100.00:
    desconto = 0
elif valor <= 299.99:
        desconto = 5 
elif valor <= 499.99:
        desconto = 10
else:
        desconto = 15


economia = valor * (desconto / 100)

valorfinal = valor - economia

print(f"Valor original: {valor}")

print(f"Valor do Desconto: {economia}")

print(f"Valor final: {valorfinal}")

