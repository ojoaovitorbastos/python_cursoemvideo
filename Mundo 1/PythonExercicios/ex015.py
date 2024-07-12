# Calcula o preço pagar de um aluguel de carro
dias = int(input('Quantos dias de aluguel? '))
kms = float(input('Quantos Km rodados? '))

valorTotal = (dias * 60) + (kms * 0.15)

print('O total a pagar é de R${}'.format(valorTotal))
