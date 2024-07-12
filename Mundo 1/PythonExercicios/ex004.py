# Mostra varias informações sobre oque foi digitado 

# Pega oque foi digitado 
valor = input('Digite algo: ')

# Mostra as informações sobre oque foi digitado
print('O tipo primitivo desse valor é ', type(valor))
print('Só tem espaços? ', valor.isspace())
print('É um número? ', valor.isnumeric())
print('É alfabético? ', valor.isalpha())
print('É alfanumérico? ', valor.isalnum())
print('Está todo em maiúsculo? ', valor.isupper())
print('Está todo em minúsculo? ', valor.islower())
print('Está capitalizada? ', valor.istitle())
