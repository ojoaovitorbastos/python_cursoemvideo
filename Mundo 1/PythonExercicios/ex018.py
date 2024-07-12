# Calculando seno, cosseno e tangente de um ângulo
from math import sin, cos, tan, radians

angulo = float(input('Digite o valor de um Ângulo: '))

seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))

print('O ângulo {} tem o SENO de {:.2f}'.format(angulo, seno))
print('O ângulo {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O ângulo {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))
