# Calcula a média de um aluno
nome = input('Nome do aluno: ')
nota1 = int(input('Quanto ele tirou na primeira prova? '))
nota2 = int(input('Quanto ele tirou na segunda prova? '))
soma = nota1 + nota2
media = soma / 2

print('A média do aluno {} foi {}'.format(nome, media))
