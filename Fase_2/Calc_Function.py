#The program was concepted to use functions to calculate simple operations

def soma(term1,term2):
    return(term1+term2)

def sub(term1,term2):
    return(term1-term2)

def mult(term1,term2):
    return(term1*term2)

def div(term1, term2):
    return(term1/term2)

operation=(input('Qual a operação a ser realizada? (+ - * /)'))

term1=float(input('digite o primeiro número'))
term2=float(input('Digite o segundo número'))

if operation=='+':
    result=soma(term1,term2)
else:
        if operation=='-':
                result=sub(term1,term2)
        else:
                if operation=='*':
                        result=mult(term1,term2)
                else:
                        result=div(term1,term2)

print('A operação escolhida foi {} e o resultado da operação foi {}'.format(operation,result))