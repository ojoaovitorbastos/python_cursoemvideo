# Calculando se um carro está dentro do limite de velocidade e mostrando o valor da multa
velocidade = float(input('Qual a velocidade do carro? '))

multa = float((velocidade - 60) * 7)

if velocidade > 60:
    print('O carro está acima do limite de velocidade!')
    print('MULTADO em R${}'.format(multa))
else:
    print('O carro está dentro do limite de velocidade.')
