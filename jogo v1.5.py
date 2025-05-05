########################################### DADOS E BIBLIOTECA PARA O JOGO #############################
import random
lista_1 = [1,1,1,1,1,1,2,2,2,3,3,3,3,4,4,4,5,5,5,5,6,7,7,8]
lista_2 = [2,3,4,5,7,9,3,5,8,5,6,7,9,5,6,7,6,7,8,9,9,8,9,9]
lista_3 = [3,2,7,9,4,5,1,8,5,7,9,5,6,6,5,1,4,3,2,1,3,9,8,7]
jogadas_diponiveis = ['x', 1, 2, 3, 4, 5, 6, 7, 8, 9]
jogos = jogo_1 = jogada_computador = jogada = result = 0
########################################## REALIZA A JOGADA DO JOGADOR ############################
def velha(jogada):# REALIZA A JOGADA DO JOGADOR
    for c in range(0, 10):
        if jogada == c:
            jogadas_diponiveis[c] = 'x'
########################################## O JOGO #################################################
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
velha(jogada)
########################################## JOGADA #################################################
while result == 0:
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
####################################### JOGADA PARA O COMPUTADOR GANHAR ###################################
    for c in range(0, 24):
        if jogadas_diponiveis[lista_1[c]] == jogadas_diponiveis[lista_2[c]] == 'o' and jogadas_diponiveis[lista_3[c]] != 'o' and jogadas_diponiveis[lista_3[c]] != 'x' and jogos == 0:
            jogadas_diponiveis[lista_3[c]] = 'o'
            result = 'o'
            jogos += 1
            break
####################################### JOGADA PARA O COMPUTADOR NÃO PERDER ###################################
        elif jogadas_diponiveis[lista_1[c]] == jogadas_diponiveis[lista_2[c]] and jogadas_diponiveis[lista_3[c]] != 'o' and jogadas_diponiveis[lista_3[c]] != 'x' and jogos == 0:
            jogo_1 = jogadas_diponiveis[lista_3[c]]
            jogadas_diponiveis[lista_3[c]] = 'o'
            jogos += 1
            print('Computador jogou: {}'.format(jogo_1))
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
                for c in range(1, 10):
                    if jogada_computador == c:
                        jogadas_diponiveis[c] = 'o'
                        jogo_1 = c
        jogos = 0
        print('Computador jogou: {}'.format(int(jogo_1)))
    velha(jogada)
velha(jogada)
if result == 'x':
    print('jogo ganho')
elif result == 'o':
    print('jogo perdido')