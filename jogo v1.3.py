import random
jogos = jogo_1 = 0
jogada_computador = 0
jogadas_diponiveis = ['x', 1, 2, 3, 4, 5, 6, 7, 8, 9]
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
########################################## O JOGO #################################################
def jogo(jogada):
    tabulerio = ('''
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
########################################## JOGADA #################################################
while True:
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
########################################## REALIZA A JOGADA DO JOGADOR #################################################
        if jogada == 1:
            jogadas_diponiveis[1] = 'x'
        if jogada == 2:
            jogadas_diponiveis[2] = 'x'
        if jogada == 3:
            jogadas_diponiveis[3] = 'x'
        if jogada == 4:
            jogadas_diponiveis[4] = 'x'
        if jogada == 5:
            jogadas_diponiveis[5] = 'x'
        if jogada == 6:
            jogadas_diponiveis[6] = 'x'
        if jogada == 7:
            jogadas_diponiveis[7] = 'x'
        if jogada == 8:
            jogadas_diponiveis[8] = 'x'
        if jogada == 9:
            jogadas_diponiveis[9] = 'x'
############################################ jogada para o computador ganhar ###########################################
    if jogadas_diponiveis[1] == jogadas_diponiveis[3] == 'o' and jogadas_diponiveis[2] == 2:
        jogadas_diponiveis[2] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[1] == jogadas_diponiveis[2] == 'o' and jogadas_diponiveis[3] == 3:
        jogadas_diponiveis[3] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[1] == jogadas_diponiveis[7] == 'o' and jogadas_diponiveis[4] == 4:
        jogadas_diponiveis[4] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[1] == jogadas_diponiveis[4] == 'o' and jogadas_diponiveis[7] == 7:
        jogadas_diponiveis[7] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[1] == jogadas_diponiveis[9] == 'o' and jogadas_diponiveis[5] == 5:
        jogadas_diponiveis[5] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[1] == jogadas_diponiveis[5] == 'o' and jogadas_diponiveis[9] == 9:
        jogadas_diponiveis[9] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[2] == jogadas_diponiveis[3] == 'o' and jogadas_diponiveis[1] == 1:
        jogadas_diponiveis[1] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[2] == jogadas_diponiveis[8] == 'o' and jogadas_diponiveis[5] == 5:
        jogadas_diponiveis[5] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[2] == jogadas_diponiveis[5] == 'o' and jogadas_diponiveis[8] == 8:
        jogadas_diponiveis[8] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[3] == jogadas_diponiveis[9] == 'o' and jogadas_diponiveis[6] == 6:
        jogadas_diponiveis[6] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[3] == jogadas_diponiveis[6] == 'o' and jogadas_diponiveis[9] == 9:
        jogadas_diponiveis[9] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[3] == jogadas_diponiveis[7] == 'o' and jogadas_diponiveis[5] == 5:
        jogadas_diponiveis[5] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[3] == jogadas_diponiveis[5] == 'o' and jogadas_diponiveis[7]== 7:
        jogadas_diponiveis[7] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[4] == jogadas_diponiveis[6] == 'o' and jogadas_diponiveis[5] == 2:
        jogadas_diponiveis[5] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[4] == jogadas_diponiveis[5] == 'o' and jogadas_diponiveis[6] == 6:
        jogadas_diponiveis[6] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[4] == jogadas_diponiveis[7] == 'o' and jogadas_diponiveis[1] == 1:
        jogadas_diponiveis[1] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[5] == jogadas_diponiveis[6] == 'o' and jogadas_diponiveis[4] == 4:
        jogadas_diponiveis[4] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[5] == jogadas_diponiveis[8] == 'o' and jogadas_diponiveis[2] == 2:
        jogadas_diponiveis[2] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[5] == jogadas_diponiveis[9] == 'o' and jogadas_diponiveis[1] == 1:
        jogadas_diponiveis[1] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[5] == jogadas_diponiveis[7] == 'o' and jogadas_diponiveis[3] == 3:
        jogadas_diponiveis[7] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[6] == jogadas_diponiveis[9] == 'o' and jogadas_diponiveis[3] == 3:
        jogadas_diponiveis[3] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[7] == jogadas_diponiveis[9] == 'o' and jogadas_diponiveis[8] == 8:
        jogadas_diponiveis[8] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[7] == jogadas_diponiveis[8] == 'o' and jogadas_diponiveis[9] == 9:
        jogadas_diponiveis[9] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[8] == jogadas_diponiveis[9] == 'o' and jogadas_diponiveis[7] == 7:
        jogadas_diponiveis[7] = 'o'
        result = 'o'
        break
############################################ jogada para o computador NÃO PERDER ###########################################
    if jogadas_diponiveis[1] == jogadas_diponiveis[3] and jogadas_diponiveis[2] == 2:
        jogadas_diponiveis[2] = 'o'
    elif jogadas_diponiveis[1] == jogadas_diponiveis[2] and jogadas_diponiveis[3] == 3:
        jogadas_diponiveis[3] = 'o'
    elif jogadas_diponiveis[2] == jogadas_diponiveis[3] and jogadas_diponiveis[1] == 1:
        jogadas_diponiveis[1] = 'o'
    elif jogadas_diponiveis[4] == jogadas_diponiveis[6] and jogadas_diponiveis[5] == 2:
        jogadas_diponiveis[5] = 'o'
    elif jogadas_diponiveis[4] == jogadas_diponiveis[5] and jogadas_diponiveis[6] == 6:
        jogadas_diponiveis[6] = 'o'
    elif jogadas_diponiveis[5] == jogadas_diponiveis[6] and jogadas_diponiveis[4] == 4:
        jogadas_diponiveis[4] = 'o'
    elif jogadas_diponiveis[7] == jogadas_diponiveis[9] and jogadas_diponiveis[8] == 8:
        jogadas_diponiveis[8] = 'o'
    elif jogadas_diponiveis[7] == jogadas_diponiveis[8] and jogadas_diponiveis[9] == 9:
        jogadas_diponiveis[9] = 'o'
    elif jogadas_diponiveis[8] == jogadas_diponiveis[9] and jogadas_diponiveis[7] == 7:
        jogadas_diponiveis[7] = 'o'
    elif jogadas_diponiveis[1] == jogadas_diponiveis[7] and jogadas_diponiveis[4] == 4:
        jogadas_diponiveis[4] = 'o'
    elif jogadas_diponiveis[1] == jogadas_diponiveis[4] and jogadas_diponiveis[7] == 7:
        jogadas_diponiveis[7] = 'o'
    elif jogadas_diponiveis[4] == jogadas_diponiveis[7] and jogadas_diponiveis[1] == 1:
        jogadas_diponiveis[1] = 'o'
    elif jogadas_diponiveis[2] == jogadas_diponiveis[8] and jogadas_diponiveis[5] == 5:
        jogadas_diponiveis[5] = 'o'
    elif jogadas_diponiveis[2] == jogadas_diponiveis[5] and jogadas_diponiveis[8] == 8:
        jogadas_diponiveis[8] = 'o'
    elif jogadas_diponiveis[5] == jogadas_diponiveis[8] and jogadas_diponiveis[2] == 2:
        jogadas_diponiveis[2] = 'o'
    elif jogadas_diponiveis[3] == jogadas_diponiveis[9] and jogadas_diponiveis[6] == 6:
        jogadas_diponiveis[6] = 'o'
    elif jogadas_diponiveis[3] == jogadas_diponiveis[6] and jogadas_diponiveis[9] == 9:
        jogadas_diponiveis[9] = 'o'
    elif jogadas_diponiveis[6] == jogadas_diponiveis[9] and jogadas_diponiveis[3] == 3:
        jogadas_diponiveis[3] = 'o'
    elif jogadas_diponiveis[1] == jogadas_diponiveis[9] and jogadas_diponiveis[5] == 5:
        jogadas_diponiveis[5] = 'o'
    elif jogadas_diponiveis[1] == jogadas_diponiveis[5] and jogadas_diponiveis[9] == 9:
        jogadas_diponiveis[9] = 'o'
    elif jogadas_diponiveis[5] == jogadas_diponiveis[9] and jogadas_diponiveis[1] == 1:
        jogadas_diponiveis[1] = 'o'
    elif jogadas_diponiveis[3] == jogadas_diponiveis[7] and jogadas_diponiveis[5] == 5:
        jogadas_diponiveis[5] = 'o'
    elif jogadas_diponiveis[3] == jogadas_diponiveis[5] and jogadas_diponiveis[7] == 7:
        jogadas_diponiveis[7] = 'o'
    elif jogadas_diponiveis[5] == jogadas_diponiveis[7] and jogadas_diponiveis[3] == 3:
        jogadas_diponiveis[7] = 'o'
######################################### PRIMEIRA JOGADA COMPUTADOR ######################################
    if jogos == 0:
        if jogada_computador == 0:
            if jogadas_diponiveis[5] == 'x':
                if jogadas_diponiveis[3] == 3:
                    jogadas_diponiveis[3] = 'o'
                    jogo_1 = 3
                    jogada_computador += 1
                elif jogadas_diponiveis[1] == 1:
                    jogadas_diponiveis[1] = 'o'
                    jogo_1 = 1
                    jogada_computador += 1
                elif jogadas_diponiveis[7] == 7:
                    jogadas_diponiveis[7] = 'o'
                    jogo_1 = 7
                    jogada_computador += 1
                elif jogadas_diponiveis[9] == 9:
                    jogadas_diponiveis[9] = 'o'
                    jogo_1 = 9
                    jogada_computador += 1
            elif jogadas_diponiveis[1] == 'x' or jogadas_diponiveis[3] == 'x' or jogadas_diponiveis[7] == 'x' or jogadas_diponiveis[9] == 'o':
                if jogadas_diponiveis[5] == 5:
                    jogadas_diponiveis[5] = 'o'
                    jogo_1 = 5
                    jogada_computador += 1
        else:
######################################### JOGADA ALEATÓRIA COMPUTADOR ######################################
            while True:
                jogada_computador = jogadas_diponiveis[random.randint(1, (len(jogadas_diponiveis)) - 1)]
                if jogada_computador != 'o' and jogada_computador != 'x':
                    break
            if jogada_computador == 1:
                jogadas_diponiveis[1] = 'o'
                jogo_1 = 1
            elif jogada_computador == 2:
                jogadas_diponiveis[2] = 'o'
                jogo_1 = 2
            elif jogada_computador == 3:
                jogadas_diponiveis[3] = 'o'
                jogo_1 = 3
            elif jogada_computador == 4:
                jogadas_diponiveis[4] = 'o'
                jogo_1 = 4
            elif jogada_computador == 5:
                jogadas_diponiveis[5] = 'o'
                jogo_1 = 5
            elif jogada_computador == 6:
                jogadas_diponiveis[6] = 'o'
                jogo_1 = 6
            elif jogada_computador == 7:
                jogadas_diponiveis[7] = 'o'
                jogo_1 = 7
            elif jogada_computador == 8:
                jogadas_diponiveis[8] = 'o'
                jogo_1 = 8
            elif jogada_computador == 9:
                jogadas_diponiveis[9] = 'o'
                jogo_1 = 9
    print('Computador jogou: {}'.format(int(jogo_1)))
    print(jogo(jogada), 'erro')
################################################ FIM DO JOGO #####################################################
print(jogo(jogada))
if result == 'x':
    print('jogo ganho')
elif result == 'o':
    print('jogo perdido')