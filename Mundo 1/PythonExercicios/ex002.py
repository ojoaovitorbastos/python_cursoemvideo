# Mostra o nome do usuario com formatação
nome = input('Qual o seu nome? ')
print('Prazer em te conhecer,  {}{}{}!'.format('\033[4;36;40m', nome, '\033[m'))
