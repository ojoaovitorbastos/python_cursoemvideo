# Seu salario com 15% de aumento
salario_original = float(input('Qual seu salário atual? '))

aumento = salario_original * 0.15

novo_salario = aumento + salario_original

print('Se você recebe {}R$, e seu chefe te da um aumento de 15%, você passa a receber {}R$'.format(salario_original, novo_salario))
