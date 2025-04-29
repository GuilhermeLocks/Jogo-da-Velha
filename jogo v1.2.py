jogadas_diponiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
jogada_computador = jogo = 0
linha_11 = '1'
linha_12 = '2'
linha_13 = '3'
linha_21 = '4'
linha_22 = '5'
linha_23 = '6'
linha_31 = '7'
linha_32 = '8'
linha_33 = '9'
import random
result = ''
while True:
    print('-' * 30)
    print('         JOGO DA VELHA          ')
    print('-' * 30)
    print('''
            {}  |  {}  |  {}
          -----------------
            {}  |  {}  |  {}
          -----------------
            {}  |  {}  |  {}
    '''.format(linha_11, linha_12, linha_13, linha_21, linha_22, linha_23, linha_31, linha_32, linha_33))
    print('-' * 30)
########## recebe jogada
    while True:
        jogada = input('Qual sua jogada? ')
        if jogada.isnumeric() == True:
            jogada = int(jogada)
            if jogada in jogadas_diponiveis:
                jogadas_diponiveis.remove(jogada)
                break
            else:
                print('Essa posição ja esta oculpada, tente novamente')
        else:
            print('Jogada invalida tente novamente')
########## realiza a jogada
    if jogada == 1:
        linha_11 = 'x'
    if jogada == 2:
        linha_12 = 'x'
    if jogada == 3:
        linha_13 = 'x'
    if jogada == 4:
        linha_21 = 'x'
    if jogada == 5:
        linha_22 = 'x'
    if jogada == 6:
        linha_23 = 'x'
    if jogada == 7:
        linha_31 = 'x'
    if jogada == 8:
        linha_32 = 'x'
    if jogada == 9:
        linha_33 = 'x'
########## verifica se alguem ganhou
    if linha_11 == linha_12 == linha_13 == 'x':
        result = 'x'
        break
    elif linha_11 == linha_12 == linha_13 == 'o':
        result = 'o'
        break
    elif linha_21 == linha_22 == linha_23 == 'x':
        result = 'x'
        break
    elif linha_21 == linha_22 == linha_23 == '0':
        result = 'o'
        break
    elif linha_31 == linha_32 == linha_33 == 'x':
        result = 'x'
        break
    elif linha_31 == linha_32 == linha_33 == 'o':
        result = 'o'
        break
    elif linha_11 == linha_21 == linha_31 == 'x':
        result = 'x'
        break
    elif linha_11 == linha_21 == linha_31 == 'o':
        result = 'o'
        break
    elif linha_12 == linha_22 == linha_32 == 'x':
        result = 'x'
        break
    elif linha_12 == linha_22 == linha_32 == 'o':
        result = 'o'
        break
    elif linha_13 == linha_23 == linha_33 == 'x':
        result = 'x'
        break
    elif linha_13 == linha_23 == linha_33 == 'o':
        result = 'o'
        break
    elif linha_11 == linha_22 == linha_33 == 'x':
        result = 'x'
        break
    elif linha_11 == linha_22 == linha_33 == 'o':
        result = 'o'
        break
    elif linha_13 == linha_22 == linha_31 == 'x':
        result = 'x'
        break
    elif linha_13 == linha_22 == linha_31 == 'o':
        result = 'o'
        break
########### jogada para o computador ganhar
    if linha_11 == linha_13 == 'o' and linha_12 == '2':
        linha_12 = 'o'
        result = 'o'
        break
    elif linha_11 == linha_12 == 'o' and linha_13 == '3':
        linha_13 = 'o'
        result = 'o'
        break
    elif linha_12 == linha_13 == 'o' and linha_11 == '1':
        linha_11 = 'o'
        result = 'o'
        break
    elif linha_21 == linha_23 == 'o' and linha_22 == '2':
        linha_22 = 'o'
        result = 'o'
        break
    elif linha_21 == linha_22 == 'o' and linha_23 == '6':
        linha_23 = 'o'
        result = 'o'
        break
    elif linha_22 == linha_23 == 'o' and linha_21 == '4':
        linha_21 = 'o'
        result = 'o'
        break
    elif linha_31 == linha_33 == 'o' and linha_32 == '8':
        linha_32 = 'o'
        result = 'o'
        break
    elif linha_31 == linha_32 == 'o' and linha_33 == '9':
        linha_33 = 'o'
        result = 'o'
        break
    elif linha_32 == linha_33 == 'o' and linha_31 == '7':
        linha_31 = 'o'
        result = 'o'
        break
    elif linha_11 == linha_31 == 'o' and linha_21 == '4':
        linha_21 = 'o'
        result = 'o'
        break
    elif linha_11 == linha_21 == 'o' and linha_31 == '7':
        linha_31 = 'o'
        result = 'o'
        break
    elif linha_21 == linha_31 == 'o' and linha_11 == '1':
        linha_11 = 'o'
        result = 'o'
        break
    elif linha_12 == linha_32 == 'o' and linha_22 == '5':
        linha_22 = 'o'
        result = 'o'
        break
    elif linha_12 == linha_22 == 'o' and linha_32 == '8':
        linha_32 = 'o'
        result = 'o'
        break
    elif linha_22 == linha_32 == 'o' and linha_12 == '2':
        linha_12 = 'o'
        result = 'o'
        break
    elif linha_13 == linha_33 == 'o' and linha_23 == '6':
        linha_23 = 'o'
        result = 'o'
        break
    elif linha_13 == linha_23 == 'o' and linha_33 == '9':
        linha_33 = 'o'
        result = 'o'
        break
    elif linha_23 == linha_33 == 'o' and linha_13 == '3':
        linha_13 = 'o'
        result = 'o'
        break
    elif linha_11 == linha_33 == 'o' and linha_22 == '5':
        linha_22 = 'o'
        result = 'o'
        break
    elif linha_11 == linha_22 == 'o' and linha_33 == '9':
        linha_33 = 'o'
        result = 'o'
        break
    elif linha_22 == linha_33 == 'o' and linha_11 == '1':
        linha_11 = 'o'
        result = 'o'
        break
    elif linha_13 == linha_31 == 'o' and linha_22 == '5':
        linha_22 = 'o'
        result = 'o'
        break
    elif linha_13 == linha_22 == 'o' and linha_31 == '7':
        linha_31 = 'o'
        result = 'o'
        break
    elif linha_22 == linha_31 == 'o' and linha_13 == '3':
        linha_13 = 'o'
        result = 'o'
        break
########## jogada para o computador não perder
    if jogo == 0:
        jogo = 1
        if linha_11 == linha_13 == 'x' and linha_12 == '2':
            linha_12 = 'o'
            jogadas_diponiveis.remove(2)
        elif linha_11 == linha_12 == 'x' and linha_13 == '3':
            linha_13 = 'o'
            jogadas_diponiveis.remove(3)
        elif linha_12 == linha_13 == 'x' and linha_11 == '1':
            linha_11 = 'o'
            jogadas_diponiveis.remove(1)
        elif linha_21 == linha_23 == 'x' and linha_22 == '2':
            linha_22 = 'o'
            jogadas_diponiveis.remove(5)
        elif linha_21 == linha_22 == 'x' and linha_23 == '6':
            linha_23 = 'o'
            jogadas_diponiveis.remove(6)
        elif linha_22 == linha_23 == 'x' and linha_21 == '4':
            linha_21 = 'o'
            jogadas_diponiveis.remove(4)
        elif linha_31 == linha_33 == 'x' and linha_32 == '8':
            linha_32 = 'o'
            jogadas_diponiveis.remove(8)
        elif linha_31 == linha_32 == 'x' and linha_33 == '9':
            linha_33 = 'o'
            jogadas_diponiveis.remove(9)
        elif linha_32 == linha_33 == 'x' and linha_31 == '7':
            linha_31 = 'o'
            jogadas_diponiveis.remove(7)
        elif linha_11 == linha_31 == 'x' and linha_21 == '4':
            linha_21 = 'o'
            jogadas_diponiveis.remove(4)
        elif linha_11 == linha_21 == 'x' and linha_31 == '7':
            linha_31 = 'o'
            jogadas_diponiveis.remove(7)
        elif linha_21 == linha_31 == 'x' and linha_11 == '1':
            linha_11 = 'o'
            jogadas_diponiveis.remove(1)
        elif linha_12 == linha_32 == 'x' and linha_22 == '5':
            linha_22 = 'o'
            jogadas_diponiveis.remove(5)
        elif linha_12 == linha_22 == 'x' and linha_32 == '8':
            linha_32 = 'o'
            jogadas_diponiveis.remove(8)
        elif linha_22 == linha_32 == 'x' and linha_12 == '2':
            linha_12 = 'o'
            jogadas_diponiveis.remove(2)
        elif linha_13 == linha_33 == 'x' and linha_23 == '6':
            linha_23 = 'o'
            jogadas_diponiveis.remove(6)
        elif linha_13 == linha_23 == 'x' and linha_33 == '9':
            linha_33 = 'o'
            jogadas_diponiveis.remove(9)
        elif linha_23 == linha_33 == 'x' and linha_13 == '3':
            linha_13 = 'o'
            jogadas_diponiveis.remove(3)
        elif linha_11 == linha_33 == 'x' and linha_22 == '5':
            linha_22 = 'o'
            jogadas_diponiveis.remove(5)
        elif linha_11 == linha_22 == 'x' and linha_33 == '9':
            linha_33 = 'o'
            jogadas_diponiveis.remove(9)
        elif linha_22 == linha_33 == 'x' and linha_11 == '1':
            linha_11 = 'o'
            jogadas_diponiveis.remove(1)
        elif linha_13 == linha_31 == 'x' and linha_22 == '5':
            linha_22 = 'o'
            jogadas_diponiveis.remove(5)
        elif linha_13 == linha_22 == 'x' and linha_31 == '7':
            linha_31 = 'o'
            jogadas_diponiveis.remove(7)
        elif linha_22 == linha_31 == 'x' and linha_13 == '3':
            linha_13 = 'o'
            jogadas_diponiveis.remove(3)
        else:
            jogo -= 1
########### jogada computador
    if jogo == 0:
        if jogada_computador == 0:
            if linha_22 == 'x':
                if linha_13 == '3':
                    linha_13 = 'o'
                    jogadas_diponiveis.remove(3)
                    jogada_computador += 1
                elif linha_11 == '1':
                    linha_11 = 'o'
                    jogadas_diponiveis.remove(1)
                    jogada_computador += 1
                elif linha_31 == '7':
                    linha_31 = 'o'
                    jogadas_diponiveis.remove(7)
                    jogada_computador += 1
                elif linha_33 == '9':
                    linha_33 = 'o'
                    jogadas_diponiveis.remove(9)
                    jogada_computador += 1
            elif linha_11 == 'x' or linha_13 == 'x' or linha_31 == 'x' or linha_33 == 'o':
                if linha_22 == '5':
                    linha_22 = 'o'
                    jogadas_diponiveis.remove(5)
                    jogada_computador += 1
        if jogada_computador == 0:
            jogada_computador = jogadas_diponiveis[random.randint(0, (len(jogadas_diponiveis)) - 1)]
            jogadas_diponiveis.remove(jogada_computador)
            if jogada_computador == 1:
                linha_11 = 'o'
            elif jogada_computador == 2:
                linha_12 = 'o'
            elif jogada_computador == 3:
                linha_13 = 'o'
            elif jogada_computador == 4:
                linha_21 = 'o'
            elif jogada_computador == 5:
                linha_22 = 'o'
            elif jogada_computador == 6:
                linha_23 = 'o'
            elif jogada_computador == 7:
                linha_31 = 'o'
            elif jogada_computador == 8:
                linha_32 = 'o'
            elif jogada_computador == 9:
                linha_33 = 'o'
########### verifica se alguém ganhou
        if linha_11 == linha_12 == linha_13 == 'x':
            result = 'x'
            break
        elif linha_11 == linha_12 == linha_13 == 'o':
            result = 'o'
            break
        elif linha_21 == linha_22 == linha_23 == 'x':
            result = 'x'
            break
        elif linha_21 == linha_22 == linha_23 == '0':
            result = 'o'
            break
        elif linha_31 == linha_32 == linha_33 == 'x':
            result = 'x'
            break
        elif linha_31 == linha_32 == linha_33 == 'o':
            result = 'o'
            break
        elif linha_11 == linha_21 == linha_31 == 'x':
            result = 'x'
            break
        elif linha_11 == linha_21 == linha_31 == 'o':
            result = 'o'
            break
        elif linha_12 == linha_22 == linha_32 == 'x':
            result = 'x'
            break
        elif linha_12 == linha_22 == linha_32 == 'o':
            result = 'o'
            break
        elif linha_13 == linha_23 == linha_33 == 'x':
            result = 'x'
            break
        elif linha_13 == linha_23 == linha_33 == 'o':
            result = 'o'
            break
        elif linha_11 == linha_22 == linha_33 == 'x':
            result = 'x'
            break
        elif linha_11 == linha_22 == linha_33 == 'o':
            result = 'o'
            break
        elif linha_13 == linha_22 == linha_31 == 'x':
            result = 'x'
            break
        elif linha_13 == linha_22 == linha_31 == 'o':
            result = 'o'
            break
print('-' * 30)
if result == 'x':
    print('jogo ganho')
elif result == 'o':
    print('jogo perdido')
print('-' * 30)
print('         JOGO DA VELHA          ')
print('-' * 30)
print('''
        {}  |  {}  |  {}
      -----------------
        {}  |  {}  |  {}
      -----------------
        {}  |  {}  |  {}
'''.format(linha_11, linha_12, linha_13, linha_21, linha_22, linha_23, linha_31, linha_32, linha_33))
print('-' * 30)