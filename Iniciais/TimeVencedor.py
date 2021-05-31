# Este programa foi feito para atender a um exercício de Fran da lista de aprendizado

print('Este programa recebe o nome e o placar de dois times e diz o qual ganhou a partida')

time1=input('Qual o nome do time?')
time1qtd=int(input('Quantos gols foram feitos por este time na partida?'))
time2=input('Qual o nome do outro time?')
time2qtd=int(input('Quantos gols foram feitos por este?'))

if time1qtd>time2qtd:
   vencedor=time1
else:
    if time2qtd>time1qtd:
        vencedor=time2
    else:
        if time1qtd==time2qtd:
           vencedor='Empate'

print('O {} e o {} jogaram, o resultado foi {} X {}, respectivamente e o vencedor foi o {}'.format(time1,time2,time1qtd,time2qtd,vencedor))