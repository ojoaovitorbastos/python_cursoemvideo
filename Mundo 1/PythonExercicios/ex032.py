# Calculando se um ano é bissexto
ano = int(input('Digite um ano: '))

resultado = ano % 4

if resultado == 0:
    print('O ano é bissexto!')
else:
    print('O ano não é bissexto.')
