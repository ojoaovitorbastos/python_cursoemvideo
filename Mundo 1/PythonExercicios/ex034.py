# Calculando um aumento de sálario com uma condição
salario_atual = float(input('Qual seu sálario atual? '))

if salario_atual >= 1250:
    aumento = (salario_atual * 10) / 100
    novo_salario = salario_atual + aumento
    print('Seu novo sálario com um aumento de 10% é R${}'.format(novo_salario))
else:
    aumento = (salario_atual * 15) / 100
    novo_salario = salario_atual + aumento
    print('Seu novo sálario com um aumento de 15% é R${}'.format(novo_salario))
