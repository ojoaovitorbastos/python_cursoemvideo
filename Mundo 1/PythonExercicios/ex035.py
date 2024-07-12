# Com o valor de três retas pode-se formar um triângulo?
r1 = int(input('Digite o valor da reta um: '))
r2 = int(input('Digite o valor da reta dois: '))
r3 = int(input('Digite o valor da reta três: '))

c1 = bool((r1 + r2) > r3)
c2 = bool((r2 + r3) > r1)
c3 = bool((r1 + r3) > r2)

if c1 and c2 and c3:
    print('Com essas três retas pode-se formar um triângulo!')
else:
    print('Com essas três retas não pode-se formar um triângulo.')
