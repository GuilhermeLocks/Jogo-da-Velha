import random
import os

JOGADA_PARA_O_COMPUTADOR_NAO_PERDER = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
JOGADA_PARA_O_COMPUTADOR_GANHAR = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
JOGADA_DO_COMPUTADOR = VERIFICA_SE_O_COMPUTADOR_JOGOU = RESULTADO = EMPATE = 0
lista_1 = [1,1,1,1,1,1,2,2,2,3,3,3,3,4,4,4,5,5,5,5,6,7,7,8]
lista_2 = [2,3,4,5,7,9,3,5,8,5,6,7,9,5,6,7,6,7,8,9,9,8,9,9]
lista_3 = [3,2,7,9,4,5,1,8,5,7,9,5,6,6,5,1,4,3,2,1,3,9,8,7]
jogadas_diponiveis = ['x', 1, 2, 3, 4, 5, 6, 7, 8, 9]
JOGADAS_DISPONIVEIS = ['x', 1, 2, 3, 4, 5, 6, 7, 8, 9]
PRIMEIRA_OPCAO_DE_JOGADA = [1, 3, 7, 9]
SEGUNDA_OPCAO_DE_JOGADA = [1, 3, 7, 9]
RESULTADO = EMPATE = 0

def jogo(EMPATE=0, RESULTADO=0):
    os.system('cls')
    print('''------------------------------\n        JOGO DA VELHA          \n------------------------------\n\n        {}  |  {}  |  {}
      ------------------\n        {}  |  {}  |  {}\n      ------------------\n        {}  |  {}  |  {}\n\n------------------------------
'''.format(JOGADAS_DISPONIVEIS[1], JOGADAS_DISPONIVEIS[2], JOGADAS_DISPONIVEIS[3], JOGADAS_DISPONIVEIS[4],
JOGADAS_DISPONIVEIS[5], JOGADAS_DISPONIVEIS[6] ,JOGADAS_DISPONIVEIS[7] ,JOGADAS_DISPONIVEIS[8], JOGADAS_DISPONIVEIS[9]))

while True:

    VERIFICA_SE_O_COMPUTADOR_JOGOU = 0

    jogo()

    while True:
        jogada = input('Qual sua jogada? ')
        if jogada.isnumeric() == True:
            jogada = int(jogada)
            if jogada in JOGADAS_DISPONIVEIS:
                JOGADAS_DISPONIVEIS.remove(jogada)
                JOGADAS_DISPONIVEIS.insert(jogada, 'x')
                break
            else:
                print('Essa posição ja esta ocupada, tente novamente')
        else:
            print('Jogada invalida tente novamente')

    for c in range(0, 24):

        if JOGADAS_DISPONIVEIS[lista_1[c]] == 'x' and JOGADAS_DISPONIVEIS[lista_2[c]] == 'x' and JOGADAS_DISPONIVEIS[
            lista_3[c]] == 'x':
            JOGADAS_DISPONIVEIS[lista_1[c]] = '\033[0;32mx\033[m'
            JOGADAS_DISPONIVEIS[lista_2[c]] = '\033[0;32mx\033[m'
            JOGADAS_DISPONIVEIS[lista_3[c]] = '\033[0;32mx\033[m'
            RESULTADO = 'jogador_ganhou'

        if JOGADAS_DISPONIVEIS[lista_1[c]] == 'o' and JOGADAS_DISPONIVEIS[lista_2[c]] == 'o' and JOGADAS_DISPONIVEIS[
            lista_3[c]] == 'o':
            JOGADAS_DISPONIVEIS[lista_1[c]] = '\033[0;32mo\033[m'
            JOGADAS_DISPONIVEIS[lista_2[c]] = '\033[0;32mo\033[m'
            JOGADAS_DISPONIVEIS[lista_3[c]] = '\033[0;32mo\033[m'
            RESULTADO = 'computador_ganhou'

    for c in JOGADAS_DISPONIVEIS:

        try:
            int(c)
        except:
            EMPATE += 1

    if EMPATE == 10:
        RESULTADO = 'EMPATE'
    else:
        EMPATE = 0

    if RESULTADO == 'jogador_ganhou':
        print('jogo ganho')
        break
    if RESULTADO == 'computador_ganhou':
        print('jogo perdido')
        break
    if RESULTADO == 'EMPATE':
        print('jogo empatado')
        break



    for c in JOGADA_PARA_O_COMPUTADOR_GANHAR:
        if JOGADAS_DISPONIVEIS[lista_1[c]] == JOGADAS_DISPONIVEIS[lista_2[c]] == 'o' and JOGADAS_DISPONIVEIS[lista_3[c]] != 'o' and JOGADAS_DISPONIVEIS[lista_3[c]] != 'x' and VERIFICA_SE_O_COMPUTADOR_JOGOU == 0:
            print('Computador11 jogou: {}'.format(JOGADAS_DISPONIVEIS[lista_3[c]]))
            JOGADAS_DISPONIVEIS[lista_3[c]] = 'o'
            RESULTADO = 'computador_ganhou'
            VERIFICA_SE_O_COMPUTADOR_JOGOU += 1

    for c in JOGADA_PARA_O_COMPUTADOR_NAO_PERDER:
        if JOGADAS_DISPONIVEIS[lista_1[c]] == JOGADAS_DISPONIVEIS[lista_2[c]] == 'x' and JOGADAS_DISPONIVEIS[lista_3[c]] != 'o' and JOGADAS_DISPONIVEIS[lista_3[c]] != 'x' and VERIFICA_SE_O_COMPUTADOR_JOGOU == 0:
            print('Computador12 jogou: {}'.format((JOGADAS_DISPONIVEIS[lista_3[c]])))
            JOGADAS_DISPONIVEIS[lista_3[c]] = 'o'
            VERIFICA_SE_O_COMPUTADOR_JOGOU += 1

    for c in PRIMEIRA_OPCAO_DE_JOGADA:
        if VERIFICA_SE_O_COMPUTADOR_JOGOU == 0 and JOGADAS_DISPONIVEIS[5] == 'x':
            if JOGADAS_DISPONIVEIS[c] == c:
                print('Computador13 jogou: {}'.format((JOGADAS_DISPONIVEIS[3])))
                print('erro6')
                JOGADAS_DISPONIVEIS[c] = 'o'
                VERIFICA_SE_O_COMPUTADOR_JOGOU += 1

    for c in SEGUNDA_OPCAO_DE_JOGADA:
        if VERIFICA_SE_O_COMPUTADOR_JOGOU == 0 and JOGADAS_DISPONIVEIS[5] != 'x' and JOGADAS_DISPONIVEIS[5] != 'o':
            print('Computador14 jogou: {}'.format((JOGADAS_DISPONIVEIS[5])))
            JOGADAS_DISPONIVEIS[5] = 'o'
            VERIFICA_SE_O_COMPUTADOR_JOGOU += 1

    if VERIFICA_SE_O_COMPUTADOR_JOGOU == 0:
        while True:
            JOGADA_DO_COMPUTADOR = JOGADAS_DISPONIVEIS[random.randint(1, (len(JOGADAS_DISPONIVEIS)) - 1)]
            if RESULTADO == 'EMPATE':
                break
            if JOGADA_DO_COMPUTADOR != 'x' and JOGADA_DO_COMPUTADOR != 'o':
                print('Computador13 jogou: {}'.format(int(JOGADAS_DISPONIVEIS[JOGADA_DO_COMPUTADOR])))
                JOGADAS_DISPONIVEIS[JOGADA_DO_COMPUTADOR] = 'o'
                break

jogo()
