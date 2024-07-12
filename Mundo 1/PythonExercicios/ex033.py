# Maior e menor número em uma lista de três números
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))

lista = [n1, n2, n3]
maior = max(lista)
menor = min(lista)

print('O maior número é: {}'.format(maior))
print('O menor número é: {}'.format(menor))
