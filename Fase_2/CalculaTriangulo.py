#The purpose of this script is calculate the triangle area

def tricalc(h,b):
    return(b*h/2)


qtd=int(input('Quantos triângulos você quer calcular?'))

while (qtd>0):
    qtd=qtd-1
    h=float(input('Digite a altura do triângulo'))
    b=float(input('Digite a base do triângulo'))
    resultado=tricalc(h,b)
    print('A área do triângulo é {}'.format(resultado))

print('Fim da execução do programa')
