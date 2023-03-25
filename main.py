num = float(input("Digite um número: "))

if num >= 0:
    print("O número é positivo!")
else:
    print("O número é negativo!")

qtd_maca = int(input("Digite a quantidade de maçãs compradas: "))

if qtd_maca < 12:
    preco_unit = 1.3
else:
    preco_unit = 1

custo_total = qtd_maca * preco_unit
print("O custo total da compra é de R$ %.2f" %custo_total)

