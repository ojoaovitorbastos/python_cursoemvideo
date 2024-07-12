# Sorteando a ordem de apresentão de uma turma
from random import shuffle

aluno1 = str(input('Digite um aluno: '))
aluno2 = str(input('Digite um aluno: '))
aluno3 = str(input('Digite um aluno: '))
aluno4 = str(input('Digite um aluno: '))

lista = [aluno1, aluno2, aluno3, aluno4]

# Embaralhe(lista) 
shuffle(lista)

print('O ordem de apresentação será: {}'.format(lista))
