# Preço de uma passagem de ônibus
viagem = float(input('Quantos Km tem sua viagem? '))

if viagem <= 200:
    print('Para uma viagem de {}Km, o preço da passagem é R${}'.format(viagem, viagem * 0.50))
else:
    print('Para uma viagem de {}Km, o preço da passagem é R${}'.format(viagem, viagem * 0.45))
