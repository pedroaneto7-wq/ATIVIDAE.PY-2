import os

os.system ('cls')



primeira_nota = float (input('digite sua nota'))
segunda_nota = float (input('digite sua nota'))
terceira_nota = float (input('digite sua nota'))

media = (primeira_nota + segunda_nota + terceira_nota) / 3
if media >= 7:
    print('aprovado')
else:
    print('reprovado')

print('sua media é: ', media)

print(' fim do programa')


