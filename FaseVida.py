# Programa criado para atender a uma atividade das aulas de Fran.

print('Este programa diz, à partir da sua idadade, em qual fase da vida a pessoa se encontra')

idade=int(input('Digite sua idade'))

if idade<=1:
    fase='Recém nascido'
else:
    if idade<=12:
        fase='Criança'
    else:
        if idade<=18:
            fase='Adolescente'
        else:
            if idade<=60:
                fase='Adulto'
            else:
                if idade>60:
                    fase='Idoso'

print('A idade consultada foi {} e a fase da vida referente a esta idade é {}'.format(idade,fase))