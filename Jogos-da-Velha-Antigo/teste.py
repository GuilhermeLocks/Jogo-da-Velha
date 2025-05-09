import random   # DADOS E BIBLIOTECA PARA O JOGO
lista_1 = [1,1,1,1,1,1,2,2,2,3,3,3,3,4,4,4,5,5,5,5,6,7,7,8]
lista_2 = [2,3,4,5,7,9,3,5,8,5,6,7,9,5,6,7,6,7,8,9,9,8,9,9]
lista_3 = [3,2,7,9,4,5,1,8,5,7,9,5,6,6,5,1,4,3,2,1,3,9,8,7]
jogos_computador_2 = jogos_computador_1 = jogada_computador_1 = jogada_computador_2 = result = cont_1 = cont_2 = 0
jogadas_diponiveis = ['x', 1, 2, 3, 4, 5, 6, 7, 8, 9]
def velha(jogada_computador_2):   # REALIZA A JOGADA DO JOGADOR
    for c in range(0, 10):
        if jogada_computador_2 == c:
            jogadas_diponiveis[c] = 'x'
    print('''
------------------------------
         JOGO DA VELHA          
------------------------------

        {}  |  {}  |  {}
       ------------------
        {}  |  {}  |  {}
       ------------------
        {}  |  {}  |  {}

------------------------------
'''.format(jogadas_diponiveis[1], jogadas_diponiveis[2], jogadas_diponiveis[3], jogadas_diponiveis[4],
jogadas_diponiveis[5], jogadas_diponiveis[6] ,jogadas_diponiveis[7] ,jogadas_diponiveis[8], jogadas_diponiveis[9]))
velha(jogada_computador_2)
while result == 0:

    jogos_computador_1 = 0
    jogos_computador_2 = 0

    while True:  # JOGADA
        jogada = input('Qual sua jogada? ')
        if jogada.isnumeric() == True:
            jogada = int(jogada)
            if jogada in jogadas_diponiveis:
                jogadas_diponiveis.remove(jogada)
                jogadas_diponiveis.insert(jogada, 'x')
                break
            else:
                print('Essa posição ja esta oculpada, tente novamente')
        else:
            print('Jogada invalida tente novamente')

    velha(jogada_computador_2)
    for c in range(0, 10):
        if c != jogadas_diponiveis[c]:
            cont_2 += 1
        if cont_2 == 10:
            result = 'e'
    cont_2 = 0
    if result == 'x':
        print('jogo ganho')
        break
    if result == 'o':
        print('jogo perdido')
        break
    if result == 'e':
        print('jogo empatado')
        break

    if jogos_computador_1 == 0:
        for c in range(0, 24):  # JOGADA PARA O COMPUTADOR GANHAR
            if jogadas_diponiveis[lista_1[c]] == jogadas_diponiveis[lista_2[c]] == 'o' and jogadas_diponiveis[lista_3[c]] != 'o' and jogadas_diponiveis[lista_3[c]] != 'x':
                print('Computador11 jogou: {}'.format(jogadas_diponiveis[lista_3[c]]))
                jogadas_diponiveis[lista_3[c]] = 'o'
                result = 'o'
                jogos_computador_1 += 1
                break

    if jogos_computador_1 == 0:
        for c in range(0, 24):  # JOGADA PARA O COMPUTADOR NÃO PERDER
            if jogadas_diponiveis[lista_1[c]] == jogadas_diponiveis[lista_2[c]] == 'x' and jogadas_diponiveis[lista_3[c]] != 'o' and jogadas_diponiveis[lista_3[c]] != 'x':
                print('Computador12 jogou: {}'.format((jogadas_diponiveis[lista_3[c]])))
                jogada_computador_1 = jogadas_diponiveis[lista_3[c]]
                jogadas_diponiveis[lista_3[c]] = 'o'
                jogos_computador_1 += 1

    if jogos_computador_1 == 0:  # PRIMEIRA JOGADA COMPUTADOR
        if jogadas_diponiveis[5] == 'x':
            if jogadas_diponiveis[3] == 3:
                jogadas_diponiveis[3] = 'o'
                jogada_computador_1 = 3
                jogos_computador_1 += 1
                print('Computador13 jogou: {}'.format((jogada_computador_1)))
            elif jogadas_diponiveis[1] == 1:
                jogadas_diponiveis[1] = 'o'
                jogada_computador_1 = 1
                jogos_computador_1 += 1
                print('Computador13 jogou: {}'.format((jogada_computador_1)))
            elif jogadas_diponiveis[7] == 7:
                jogadas_diponiveis[7] = 'o'
                jogada_computador_1 = 7
                jogos_computador_1 += 1
                print('Computador13 jogou: {}'.format((jogada_computador_1)))
            elif jogadas_diponiveis[9] == 9:
                jogadas_diponiveis[9] = 'o'
                jogada_computador_1 = 9
                jogos_computador_1 += 1
                print('Computador13 jogou: {}'.format((jogada_computador_1)))
        elif jogadas_diponiveis[1] == 'x' or jogadas_diponiveis[3] == 'x' or jogadas_diponiveis[7] == 'x' or jogadas_diponiveis[9] == 'o':
            if jogadas_diponiveis[5] == 5:
                jogadas_diponiveis[5] = 'o'
                jogada_computador_1 = 5
                jogos_computador_1 += 1
                print('Computador13 jogou: {}'.format((jogada_computador_1)))
    if jogos_computador_1 == 0:  # JOGADA ALEATÓRIA COMPUTADOR
        while True:
            jogada_computador_1 = jogadas_diponiveis[random.randint(1, (len(jogadas_diponiveis)) - 1)]
            if jogada_computador_1 != 'o' and jogada_computador_1 != 'x':
                break
        for c in range(1, 10):
            if jogada_computador_1 == c:
                jogadas_diponiveis[c] = 'o'
                jogada_computador_1 = c
        print('Computador13 jogou: {}'.format(int(jogada_computador_1)))

    velha(jogada_computador_2)
    for c in range(0, 10):
        if c != jogadas_diponiveis[c]:
            cont_2 += 1
        if cont_2 == 10:
            result = 'e'
    cont_2 = 0
    if result == 'x':
        print('jogo ganho')
        break
    if result == 'o':
        print('jogo perdido')
        break
    if result == 'e':
        print('jogo empatado')
        break