# Mostra onde aparece a primeira e a ultima letra A, e quantas vezes aparece
frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra A aparece {} vezes na frase.'.format(frase.upper().count('A')))
print('A primeira letra A aparece na posição {}.'.format(frase.find('A')+1))
print('A ultima letra A aparece na posição {}.'.format(frase.rfind('A')+1))
