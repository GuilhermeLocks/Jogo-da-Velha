JOGADA_PARA_O_COMPUTADOR_GANHAR = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23
JOGADA_PARA_O_COMPUTADOR_NAO_PERDER = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23
JOGADA_DO_COMPUTADOR = VERIFICA_SE_O_COMPUTADOR_JOGOU = resultado = empate = 0
PRIMEIRA_OPCAO_DE_JOGADA = 1, 3, 7, 9
SEGUNDA_OPCAO_DE_JOGADA = 1, 3, 7, 9
jogadas_diponiveis = ['x', 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_1 = [1,1,1,1,1,1,2,2,2,3,3,3,3,4,4,4,5,5,5,5,6,7,7,8]
lista_2 = [2,3,4,5,7,9,3,5,8,5,6,7,9,5,6,7,6,7,8,9,9,8,9,9]
lista_3 = [3,2,7,9,4,5,1,8,5,7,9,5,6,6,5,1,4,3,2,1,3,9,8,7]
import random
def jogo(empate, resultado):
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
    if resultado == 'jogador_ganhou':
        print('jogo ganho')
        return resultado
    if resultado == 'computador_ganhou':
        print('jogo perdido')
        return resultado
    if resultado == 'empate':
        print('jogo empatado')
        return resultado
jogo(empate, resultado)
while resultado == 0:
    while True:
        jogada = input('Qual sua jogada? ')
        if jogada.isnumeric() == True:
            jogada = int(jogada)
            if jogada in jogadas_diponiveis:
                jogadas_diponiveis.remove(jogada)
                jogadas_diponiveis.insert(jogada, 'x')
                break
            else:
               print('Essa posição ja esta ocupada, tente novamente')
        else:
            print('Jogada invalida tente novamente')
    jogo(empate, resultado)
    print('erro1')
    for c in JOGADA_PARA_O_COMPUTADOR_GANHAR:
        if jogadas_diponiveis[lista_1[c]] == jogadas_diponiveis[lista_2[c]] == 'o' and jogadas_diponiveis[lista_3[c]] != 'o' and jogadas_diponiveis[lista_3[c]] != 'x' and VERIFICA_SE_O_COMPUTADOR_JOGOU == 0:
            print('Computador11 jogou: {}'.format(jogadas_diponiveis[lista_3[c]]))
            jogadas_diponiveis[lista_3[c]] = 'o'
            resultado = 'computador_ganhou'
            VERIFICA_SE_O_COMPUTADOR_JOGOU += 1
    print('erro2')
    for c in JOGADA_PARA_O_COMPUTADOR_NAO_PERDER:
        if jogadas_diponiveis[lista_1[c]] == jogadas_diponiveis[lista_2[c]] == 'x' and jogadas_diponiveis[lista_3[c]] != 'o' and jogadas_diponiveis[lista_3[c]] != 'x' and VERIFICA_SE_O_COMPUTADOR_JOGOU == 0:
            print('Computador12 jogou: {}'.format((jogadas_diponiveis[lista_3[c]])))
            jogadas_diponiveis[lista_3[c]] = 'o'
            VERIFICA_SE_O_COMPUTADOR_JOGOU += 1
    print('erro3')
    for c in PRIMEIRA_OPCAO_DE_JOGADA:
        if VERIFICA_SE_O_COMPUTADOR_JOGOU == 0 and jogadas_diponiveis[5] == 'x':
            if jogadas_diponiveis[c] == c:
                print('Computador13 jogou: {}'.format((jogadas_diponiveis[3])))
                jogadas_diponiveis[c] = 'o'
                VERIFICA_SE_O_COMPUTADOR_JOGOU += 1
    print('erro4')
    for c in SEGUNDA_OPCAO_DE_JOGADA:
        if VERIFICA_SE_O_COMPUTADOR_JOGOU == 0 and jogadas_diponiveis[5] != 'x' and jogadas_diponiveis[5] != 'o':
            print('Computador14 jogou: {}'.format((jogadas_diponiveis[5])))
            jogadas_diponiveis[5] = 'o'
            VERIFICA_SE_O_COMPUTADOR_JOGOU += 1
    print('erro5')
    if VERIFICA_SE_O_COMPUTADOR_JOGOU == 0:
        for c in range(0, 100):
            JOGADA_DO_COMPUTADOR = jogadas_diponiveis[random.randint(1, (len(jogadas_diponiveis)) - 1)]
            if JOGADA_DO_COMPUTADOR != 'o' and JOGADA_DO_COMPUTADOR != 'x':
                print('Computador15 jogou: {}'.format(int(jogadas_diponiveis[JOGADA_DO_COMPUTADOR])))
                jogadas_diponiveis[JOGADA_DO_COMPUTADOR] = 'o'
                break
    print('erro6')
    jogo(empate, resultado)
    VERIFICA_SE_O_COMPUTADOR_JOGOU = 0
jogo(empate, resultado)
