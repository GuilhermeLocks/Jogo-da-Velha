########################################### DADOS E BIBLIOTECA PARA O JOGO #############################
import random
lista_1 = [1,1,1,1,1,1,2,2,2,3,3,3,3,4,4,4,5,5,5,5,6,7,7,8]
lista_2 = [2,3,4,5,7,9,3,5,8,5,6,7,9,5,6,7,6,7,8,9,9,8,9,9]
lista_3 = [3,2,7,9,4,5,1,8,5,7,9,5,6,6,5,1,4,3,2,1,3,9,8,7]
jogadas_diponiveis = ['x', 1, 2, 3, 4, 5, 6, 7, 8, 9]
jogos = jogada_computador = jogada = result = 0
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
    jogos = 0
    while True:
        jogada = random.randint(1,9)
        if jogada in jogadas_diponiveis:
            print('Jogador jogou {}'.format(jogada))
            jogadas_diponiveis[jogada] = 'x'
            break
####################################### JOGADA PARA O COMPUTADOR GANHAR ###################################
    for c in range(0, 24):
        if jogos == 0:
            if jogadas_diponiveis[lista_1[c]] == jogadas_diponiveis[lista_2[c]] == 'o' and jogadas_diponiveis[lista_3[c]] != 'o' and jogadas_diponiveis[lista_3[c]] != 'x' and jogos == 0:
                jogada_computador = jogadas_diponiveis[lista_3[c]]
                jogadas_diponiveis[lista_3[c]] = 'o'
                print('Computador jogou {}'.format(jogada_computador))
                print('erro1')
                jogos += 1
                result = 'o'
                break
    ####################################### JOGADA PARA O COMPUTADOR NÃO PERDER ###################################
            elif jogadas_diponiveis[lista_1[c]] == jogadas_diponiveis[lista_2[c]] == 'x' and jogadas_diponiveis[lista_3[c]] != 'o' and jogadas_diponiveis[lista_3[c]] != 'x' and jogos == 0:
                jogada_computador = jogadas_diponiveis[lista_3[c]]
                jogadas_diponiveis[lista_3[c]] = 'o'
                print('Computador jogou {}'.format(jogada_computador))
                print('erro2')
                jogos += 1
######################################### PRIMEIRA JOGADA COMPUTADOR ######################################
    if jogos == 0:
        if jogadas_diponiveis[5] == 'x':
            if jogadas_diponiveis[3] == 3:
                jogadas_diponiveis[3] = 'o'
                jogada_computador = 3
                print('Computador jogou {}'.format(jogada_computador))
                print('erro3')
            elif jogadas_diponiveis[1] == 1:
                jogadas_diponiveis[1] = 'o'
                jogada_computador = 1
                print('Computador jogou {}'.format(jogada_computador))
                print('erro4')
            elif jogadas_diponiveis[7] == 7:
                jogadas_diponiveis[7] = 'o'
                jogada_computador = 7
                print('Computador jogou {}'.format(jogada_computador))
                print('erro5')
            elif jogadas_diponiveis[9] == 9:
                jogadas_diponiveis[9] = 'o'
                jogada_computador = 9
                print('Computador jogou {}'.format(jogada_computador))
                print('erro6')
        elif jogadas_diponiveis[1] == 'x' or jogadas_diponiveis[3] == 'x' or jogadas_diponiveis[7] == 'x' or jogadas_diponiveis[9] == 'o':
            if jogadas_diponiveis[5] == 5:
                jogada_computador = 5
                jogadas_diponiveis[5] = 'o'
                print('Computador jogou {}'.format(jogada_computador))
                print('erro7')
        else:
            while True:
                jogada_computador = random.randint(1, 9)
                if jogada_computador in jogadas_diponiveis:
                    jogadas_diponiveis[jogada_computador] = 'o'
                    print('Computador jogou {}'.format(jogada_computador))
                    print('erro8')
                    break
    velha(jogada)
    if 1 in jogadas_diponiveis:
        jogos = 0
    elif 2 in jogadas_diponiveis:
        jogos = 0
    elif 3 in jogadas_diponiveis:
        jogos = 0
    elif 4 in jogadas_diponiveis:
        jogos = 0
    elif 5 in jogadas_diponiveis:
        jogos = 0
    elif 6 in jogadas_diponiveis:
        jogos = 0
    elif 7 in jogadas_diponiveis:
        jogos = 0
    elif 8 in jogadas_diponiveis:
        jogos = 0
    elif 9 in jogadas_diponiveis:
        jogos = 0
    else:
        break
if result == 'x':
    print('jogo ganho')
elif result == 'o':
    print('jogo perdido')
else:
    print('jogo empatado')