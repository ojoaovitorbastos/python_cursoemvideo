# Mostrando informações sobre um nome com Funcionalidades

nome = str(input('Qual seu nome completo? '))

nomeSplit = nome.split()
nomeJoin = ''.join(nomeSplit)

print('Seu nome todo em maiúsculo é: {}'.format(nome.upper()))
print('Seu nome todo em minúsculo é: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nomeJoin)))
print('Seu primeiro nome tem {} letras'.format(len(nomeSplit[0])))
