# DADOS E BIBLIOTECA PARA O JOGO

jogos_computador_1 = jogada_computador_1 = resultado = empate = 0
lista_1 = [1,1,1,1,1,1,2,2,2,3,3,3,3,4,4,4,5,5,5,5,6,7,7,8]
lista_2 = [2,3,4,5,7,9,3,5,8,5,6,7,9,5,6,7,6,7,8,9,9,8,9,9]
lista_3 = [3,2,7,9,4,5,1,8,5,7,9,5,6,6,5,1,4,3,2,1,3,9,8,7]
jogadas_diponiveis = ['x', 1, 2, 3, 4, 5, 6, 7, 8, 9]
import random

# jogo

def velha(empate, resultado):
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

    #verifica empate

    for c in range(0, 10):
        if c != jogadas_diponiveis[c]:
            empate += 1
        if empate == 10:
            resultado = 'e'

    #verifica o resultado

    if resultado == 'x':
        print('jogo ganho')
    if resultado == 'o':
        print('jogo perdido')
    if resultado == 'e':
        print('jogo empatado')

while resultado == 0:

    #JOGO
    velha(empate, resultado)

    # JOGADA
    while True:
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

    # JOGO
    velha(empate, resultado)

    #verifica se tem alguma jogada para ganhar
    if jogos_computador_1 == 0:
        for c in range(0, 24):
            if jogadas_diponiveis[lista_1[c]] == jogadas_diponiveis[lista_2[c]] == 'o' and jogadas_diponiveis[lista_3[c]] != 'o' and jogadas_diponiveis[lista_3[c]] != 'x':
                print('Computador11 jogou: {}'.format(jogadas_diponiveis[lista_3[c]]))
                jogadas_diponiveis[lista_3[c]] = 'o'
                resultado = 'o'
                jogos_computador_1 += 1
                break

    #verifica se tem alguma jogada para impedir a vitoria do oponente
    for c in range(0, 24):
        if jogadas_diponiveis[lista_1[c]] == jogadas_diponiveis[lista_2[c]] == 'x' and jogadas_diponiveis[lista_3[c]] != 'o' and jogadas_diponiveis[lista_3[c]] != 'x' and jogos_computador_1 == 0:
            print('Computador12 jogou: {}'.format((jogadas_diponiveis[lista_3[c]])))
            jogada_computador_1 = jogadas_diponiveis[lista_3[c]]
            jogadas_diponiveis[lista_3[c]] = 'o'
            jogos_computador_1 += 1

    #realiza a primeira jogada
    if jogos_computador_1 == 0:
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

    #realiza uma jogada aleatória
    if jogos_computador_1 == 0:
        while True:
            jogada_computador_1 = jogadas_diponiveis[random.randint(1, (len(jogadas_diponiveis)) - 1)]
            if jogada_computador_1 != 'o' and jogada_computador_1 != 'x':
                break
        for c in range(1, 10):
            if jogada_computador_1 == c:
                jogadas_diponiveis[c] = 'o'
                jogada_computador_1 = c
        print('Computador13 jogou: {}'.format(int(jogada_computador_1)))

    #zera a jogada do computador
    jogos_computador_1 = 0