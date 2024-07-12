# Número real convertido para sua parte inteira
import math

numReal = float(input('Digite um número real (ex: 6.14): '))

numInt = math.floor(numReal)

print('O número {} tem a parte inteira {}'.format(numReal, numInt))
