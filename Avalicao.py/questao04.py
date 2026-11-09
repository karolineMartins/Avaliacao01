#Questão 4: Processamento de Vendas Diárias


# Questão 4: Processamento de Vendas Diárias

# Perguntar a quantidade de vendas
quantidade = int(input("Quantas vendas foram realizadas no dia? "))

# Inicializar as variáveis
total = 0
maior_venda = 0

# Repetição para registrar as vendas
for i in range(quantidade):
    valor = float(input(f"Digite o valor da {i + 1}ª venda: R$ "))

    # Somar os valores das vendas
    total = total + valor

    # Identificar a maior venda
    if valor > maior_venda:
        maior_venda = valor

# Calcular e exibir os resultados
if quantidade > 0:
    media = total / quantidade

    print("\n===== FECHAMENTO DO CAIXA =====")
    print(f"Total bruto arrecadado: R$ {total:.2f}")
    print(f"Média por venda: R$ {media:.2f}")
    print(f"Maior venda realizada: R$ {maior_venda:.2f}")

else:
    print("Nenhuma venda foi registrada.")
