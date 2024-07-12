# Escolhe qual aluno irá começar a apresentação
from random import choice

aluno1 = str(input('Digite um aluno: '))
aluno2 = str(input('Digite um aluno: '))
aluno3 = str(input('Digite um aluno: '))
aluno4 = str(input('Digite um aluno: '))

aluno = choice([aluno1, aluno2, aluno3, aluno4])

print('O aluno escolhido foi {}!'.format(aluno))
