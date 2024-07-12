from random import randint
from time import sleep

print('\033[33m-=-' * 18)
print('\033[34mVou pensar em um número entre 0 e 5, tente adivinhar!')
print('\033[33m-=-' * 18)

num = randint(0, 5)
chute = int(input('\033[36mEm que número eu pensei? '))

print('\033[35mPROCESSANDO...\033[m') 
sleep(3)

if chute == num:
    print('\033[32mVocê acertou PARABÉNS!2\033[m')
else:
    print('\033[31mVocê ERROU! eu pensei no número' ,  num, 'e não no número', chute, '\033[m')
