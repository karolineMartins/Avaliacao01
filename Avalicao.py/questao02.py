#Questão2: Regras de Desconto com Estrutura Condicional
#Para alavancar as vendas,a loja criou uma política de descontos progressivos
#baseada no valor total da compra. 


valor = float(input("Digite o valor total da compra: "))
desconto5 = (valor * 0.05)
desconto10 = (valor * 0.10)
desconto15 = (valor * 0.15)


if valor < 100.00:
    print("Sem Desconto")
elif valor <= 299.99:
    desconto5 = print("5 % de desconto.") 
elif valor <= 499.99:
    desconto10 = print("10% de desconto")
else:
    desconto15 = print("15% de desconto")

print(f"Valor original: {valor}")
