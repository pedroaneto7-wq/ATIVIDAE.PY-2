import os

os.system ('cls')

primeiro_numero = float (input('digite o numero'))
segundo_numero = float (input('digite o numero'))

soma = primeiro_numero + segundo_numero
media = (primeiro_numero + segundo_numero)/2
produto = primeiro_numero * segundo_numero


if primeiro_numero >= segundo_numero:
    maior= primeiro_numero
    menor= segundo_numero
else:
    maior = segundo_numero
    menor = primeiro_numero
    resultado = ('primeiro_numero maior que segundo_numero')

print(f'soma: , {soma}')
print(f'produto: ,{produto}')
print(f'mair numero: , {maior}')
print(f'menor numero; , {menor}')
print(f'media: , {media}')
