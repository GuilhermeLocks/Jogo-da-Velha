import random
jogos = 0
jogada_computador = 0
result = ''
jogadas_diponiveis = ['x', 1, 2, 3, 4, 5, 6, 7, 8, 9]
########################################## O JOGO #################################################

print('''------------------------------
         JOGO DA VELHA          
------------------------------

        {}  |  {}  |  {}
       ------------------
        {}  |  {}  |  {}
       ------------------
        {}  |  {}  |  {}

------------------------------
'''.format(jogadas_diponiveis[1], jogadas_diponiveis[2], jogadas_diponiveis[3], jogadas_diponiveis[4],
           jogadas_diponiveis[5], jogadas_diponiveis[6], jogadas_diponiveis[7], jogadas_diponiveis[8],
           jogadas_diponiveis[9]))
def jogo(jogada):
########################################## REALIZA A JOGADA JO JOGADOR #################################################
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
########################################## O JOGO #################################################
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
'''.format(jogadas_diponiveis[1], jogadas_diponiveis[2], jogadas_diponiveis[3], jogadas_diponiveis[4], jogadas_diponiveis[5], jogadas_diponiveis[6] ,jogadas_diponiveis[7] ,jogadas_diponiveis[8], jogadas_diponiveis[9]))
########### verifica se alguém ganhou
    if jogadas_diponiveis[1] == jogadas_diponiveis[2] == jogadas_diponiveis[3] == 'x':
        result = 'x'
        return result
    elif linha_11 == linha_12 == linha_13 == 'o':
        result = 'o'
    elif linha_21 == linha_22 == linha_23 == 'x':
        result = 'x'
    elif linha_21 == linha_22 == linha_23 == '0':
        result = 'o'
    elif linha_31 == linha_32 == linha_33 == 'x':
        result = 'x'
    elif linha_31 == linha_32 == linha_33 == 'o':
        result = 'o'
    elif linha_11 == linha_21 == linha_31 == 'x':
        result = 'x'
    elif linha_11 == linha_21 == linha_31 == 'o':
        result = 'o'
    elif linha_12 == linha_22 == linha_32 == 'x':
        result = 'x'
    elif linha_12 == linha_22 == linha_32 == 'o':
        result = 'o'
    elif linha_13 == linha_23 == linha_33 == 'x':
        result = 'x'
    elif linha_13 == linha_23 == linha_33 == 'o':
        result = 'o'
    elif linha_11 == linha_22 == linha_33 == 'x':
        result = 'x'
    elif linha_11 == linha_22 == linha_33 == 'o':
        result = 'o'
    elif linha_13 == linha_22 == linha_31 == 'x':
        result = 'x'
    elif linha_13 == linha_22 == linha_31 == 'o':
        result = 'o'
    return tabulerio
while result == '':
##########################################JOGADA#################################################
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
    print(jogo(jogada), '1')
##########################################JOGADA_COMPUTADOR#######################################

    if jogos == 0:
        if jogada_computador == 0:
            if jogadas_diponiveis[5] == 'x':
                if jogadas_diponiveis[3] == '3':
                    jogadas_diponiveis[3] = 'o'
                    jogada_computador += 1
                elif jogadas_diponiveis[1] == '1':
                    jogadas_diponiveis[1] = 'o'
                    jogada_computador += 1
                elif jogadas_diponiveis[7] == '7':
                    jogadas_diponiveis[7] = 'o'
                    jogada_computador += 1
                elif jogadas_diponiveis[9] == '9':
                    jogadas_diponiveis[9] = 'o'
                    jogada_computador += 1
            elif jogadas_diponiveis[1] == 'x' or jogadas_diponiveis[3] == 'x' or jogadas_diponiveis[7] == 'x' or jogadas_diponiveis[9] == 'o':
                if jogadas_diponiveis[5] == '5':
                    jogadas_diponiveis[5] = 'o'
                    jogada_computador += 1
        if jogada_computador == 0:
            jogada_computador = jogadas_diponiveis[random.randint(0, (len(jogadas_diponiveis)) - 1)]
            if jogada_computador == 1:
                jogadas_diponiveis[1] = 'o'
            elif jogada_computador == 2:
                jogadas_diponiveis[2] = 'o'
            elif jogada_computador == 3:
                jogadas_diponiveis[3] = 'o'
            elif jogada_computador == 4:
                jogadas_diponiveis[4] = 'o'
            elif jogada_computador == 5:
                jogadas_diponiveis[5] = 'o'
            elif jogada_computador == 6:
                jogadas_diponiveis[6] = 'o'
            elif jogada_computador == 7:
                jogadas_diponiveis[7] = 'o'
            elif jogada_computador == 8:
                jogadas_diponiveis[8] = 'o'
            elif jogada_computador == 9:
                jogadas_diponiveis[9] = 'o'
    print(jogo(jogada), '2')