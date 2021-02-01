import mat

print('Coloque um valor de ângulo para ter seno, cosseno e tangente')
angulo=float(input('Digite o valor do ângulo'))
cosseno= mat.cos(angulo)
seno=mat.sin(angulo)
tangente=mat.tan(angulo)
print('O angulo digitado foi {}, o seno deste ângulo é {}, o cosseno é {} e a tangente é {}'.format(cosseno, seno, tangente))
