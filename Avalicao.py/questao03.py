#Questão 3: Menu Interativo do Caixa com match/case


valor = 500.00

print("1 - À vista em dinheiro / Pix (10% de desconto)")
print("2 - Cartão de Débito (5% de desconto)")
print("3 - Cartão de Crédito (Preço normal em 1x)")
print("4 - Cartão de Crédito Parcelado (10% de juros)")

opcao = int(input("Escolha a forma de pagamento: "))

match opcao:
    case 1:
        valor_final = valor - (valor * 0.10)
        print("Pagamento à vista em dinheiro / Pix")
        print(f"Valor final: R$ {valor_final:.2f}")

    case 2:
        valor_final = valor - (valor * 0.05)
        print("Pagamento no cartão de débito")
        print(f"Valor final: R$ {valor_final:.2f}")

    case 3:
        valor_final = valor
        print("Pagamento no cartão de crédito em 1x")
        print(f"Valor final: R$ {valor_final:.2f}")

    case 4:
        valor_final = valor + (valor * 0.10)
        print("Pagamento no cartão de crédito parcelado")
        print(f"Valor final: R$ {valor_final:.2f}")

    case _:
        print("Opção de pagamento inválida!")


