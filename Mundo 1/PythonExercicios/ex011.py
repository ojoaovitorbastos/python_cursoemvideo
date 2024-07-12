# Calcula quantas latas de tinta precisa para pintar uma parede
print('{}'.format('Quantas latas de tinta preciso para pintar uma parede?'))
larg = float(input('Qual a largura da sua parede? '))
alt = float(input('Qual a altura da sua parede? '))

area = larg * alt
qTinta = area / 2

print('Sabendo que sua parede tem {}m de área, e que uma lata de tinta pinta 2m quadrados, você vai precisar de {} latas de tinta para pintar sua parede!'.format(area, qTinta))
 
