import random
partitura = ['si', 'do', 're', 'mi', 'fá', 'sol', 'lá', 'si', 'do']

for c in range(1, 8):
    print(partitura[c] , c)

while True:
    aleatoria_antes_depois = random.randint(0, 1)

    aleatoria_valor = random.randint(1, 7)
    aleatoria_nota = partitura[aleatoria_valor]

    if aleatoria_antes_depois == 0:
        letra = input(f'Qual vem antes do {aleatoria_nota}? ')
        if letra == partitura[aleatoria_valor-1]:
            print('Resposta certa')
        else:
            print(f'Resposta errado, o certo seria {partitura[aleatoria_valor-1]}')


    if aleatoria_antes_depois == 1:
        letra = input(f'Qual vem depois do {aleatoria_nota}? ')
        if letra == partitura[aleatoria_valor+1]:
            print('Resposta certa')
        else:
            print(f'Resposta errado, o certo seria {partitura[aleatoria_valor+1]}')

