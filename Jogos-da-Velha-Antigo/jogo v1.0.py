jogadas_diponiveis = [1, 2, 3, 4, 5, 6, 7, 8, 9]
import random
linha_11 = '1'
linha_12 = '2'
linha_13 = '3'
linha_21 = '4'
linha_22 = '5'
linha_23 = '6'
linha_31 = '7'
linha_32 = '8'
linha_33 = '9'
result = ''
jogada_computador = 0
jogo = 0

while True:

    #jogo


    print('-'*30)
    print('         JOGO DA VELHA          ')
    print('-'*30)
    print('''
            {}  |  {}  |  {}
          -----------------
            {}  |  {}  |  {}
          -----------------
            {}  |  {}  |  {}
    '''.format(linha_11, linha_12, linha_13, linha_21, linha_22, linha_23, linha_31, linha_32, linha_33))
    print('-'*30)
    #recebe jogada
    while True:
        jogada = input('Qual sua jogada? ')
        if jogada.isnumeric() == True:
            jogada = int(jogada)
            if jogada in jogadas_diponiveis:
                jogada = int(jogada)
                break
            else:
                print('Essa posição ja esta oculpada, tente novamente')
        else:
            print('Jogada invalida tente novamente')


    # realiza a jogada


    for c in range(1, 10):
        if jogada == c:
            if c in jogadas_diponiveis:
                if c == 1:
                    linha_11 = 'x'
                    jogadas_diponiveis.remove(1)
                if c == 2:
                    linha_12 = 'x'
                    jogadas_diponiveis.remove(2)
                if c == 3:
                    linha_13 = 'x'
                    jogadas_diponiveis.remove(3)
                if c == 4:
                    linha_21 = 'x'
                    jogadas_diponiveis.remove(4)
                if c == 5:
                    linha_22 = 'x'
                    jogadas_diponiveis.remove(5)
                if c == 6:
                    linha_23 = 'x'
                    jogadas_diponiveis.remove(6)
                if c == 7:
                    linha_31 = 'x'
                    jogadas_diponiveis.remove(7)
                if c == 8:
                    linha_32 = 'x'
                    jogadas_diponiveis.remove(8)
                if c == 9:
                    linha_33 = 'x'
                    jogadas_diponiveis.remove(9)

    # verifica se alguem ganhou

    if linha_11 == linha_12 == linha_13:
        if linha_11 == 'x':
            result = 'x'
            break
        elif linha_11 == 'o':
            result = 'o'
            break
    elif linha_21 == linha_22 == linha_23:
        if linha_21 == 'x':
            result = 'x'
            break
        elif linha_21 == '0':
            result = 'o'
            break
    elif linha_31 == linha_32 == linha_33:
        if linha_31 == 'x':
            result = 'x'
            break
        elif linha_31 == 'o':
            result = 'o'
            break
    elif linha_11 == linha_21 == linha_31:
        if linha_11 == 'x':
            result = 'x'
            break
        elif linha_11 == 'o':
            result = 'o'
            break
    elif linha_12 == linha_22 == linha_32:
        if linha_12 == 'x':
            result = 'x'
            break
        elif linha_12 == 'o':
            result = 'o'
            break
    elif linha_13 == linha_23 == linha_33:
        if linha_13 == 'x':
            result = 'x'
            break
        elif linha_13 == 'o':
            result = 'o'
            break
    elif linha_11 == linha_22 == linha_33:
        if linha_11 == 'x':
            result = 'x'
            break
        if linha_11 == 'o':
            result = 'o'
            break
    elif linha_13 == linha_22 == linha_31:
        if linha_13 == 'x':
            result = 'x'
            break
        elif linha_13 == 'o':
            result = 'o'
            break

###### jogada para o computador ganhar >

    if jogo == 0:
        if linha_11 == 'o' and linha_13 == 'o':
            if linha_12 == '2':
                linha_12 = 'o'
                jogadas_diponiveis.remove(2)
                result = 'o'
                break
        elif linha_11 == 'o' and linha_12 == 'o':
            if linha_13 == '3':
                linha_13 = 'o'
                jogadas_diponiveis.remove(3)
                result = 'o'
                break
        elif linha_12 == 'o' and linha_13 == 'o':
            if linha_11 == '1':
                linha_11 = 'o'
                jogadas_diponiveis.remove(1)
                result = 'o'
                break
        elif linha_21 == 'o' and linha_23 == 'o':
            if linha_22 == '2':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                result = 'o'
                break
        elif linha_21 == 'o' and linha_22 == 'o':
            if linha_23 == '6':
                linha_23 = 'o'
                jogadas_diponiveis.remove(6)
                result = 'o'
                break
        elif linha_22 == 'o' and linha_23 == 'o':
            if linha_21 == '4':
                linha_21 = 'o'
                jogadas_diponiveis.remove(4)
                result = 'o'
                break
        elif linha_31 == 'o' and linha_33 == 'o':
            if linha_32 == '8':
                linha_32 = 'o'
                jogadas_diponiveis.remove(8)
                result = 'o'
                break
        elif linha_31 == 'o' and linha_32 == 'o':
            if linha_33 == '9':
                linha_33 = 'o'
                jogadas_diponiveis.remove(9)
                result = 'o'
                break
        elif linha_32 == 'o' and linha_33 == 'o':
            if linha_31 == '7':
                linha_31 = 'o'
                jogadas_diponiveis.remove(7)
                result = 'o'
                break
        elif linha_11 == 'o' and linha_31 == 'o':
            if linha_21 == '4':
                linha_21 = 'o'
                jogadas_diponiveis.remove(4)
                result = 'o'
                break
        elif linha_11 == 'o' and linha_21 == 'o':
            if linha_31 == '7':
                linha_31 = 'o'
                jogadas_diponiveis.remove(7)
                result = 'o'
                break
        elif linha_21 == 'o' and linha_31 == 'o':
            if linha_11 == '1':
                linha_11 = 'o'
                jogadas_diponiveis.remove(1)
                result = 'o'
                break
        elif linha_12 == 'o' and linha_32 == 'o':
            if linha_22 == '5':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                result = 'o'
                break
        elif linha_12 == 'o' and linha_22 == 'o':
            if linha_32 == '8':
                linha_32 = 'o'
                jogadas_diponiveis.remove(8)
                result = 'o'
                break
        elif linha_22 == 'o' and linha_32 == 'o':
            if linha_12 == '2':
                linha_12 = 'o'
                jogadas_diponiveis.remove(2)
                result = 'o'
                break
        elif linha_13 == 'o' and linha_33 == 'o':
            if linha_23 == '6':
                linha_23 = 'o'
                jogadas_diponiveis.remove(6)
                result = 'o'
                break
        elif linha_13 == 'o' and linha_23 == 'o':
            if linha_33 == '9':
                linha_33 = 'o'
                jogadas_diponiveis.remove(9)
                result = 'o'
                break
        elif linha_23 == 'o' and linha_33 == 'o':
            if linha_13 == '3':
                linha_13 = 'o'
                jogadas_diponiveis.remove(3)
                result = 'o'
                break
        elif linha_11 == 'o' and linha_33 == 'o':
            if linha_22 == '5':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                result = 'o'
                break
        elif linha_11 == 'o' and linha_22 == 'o':
            if linha_33 == '9':
                linha_33 = 'o'
                jogadas_diponiveis.remove(9)
                result = 'o'
                break
        elif linha_22 == 'o' and linha_33 == 'o':
            if linha_11 == '1':
                linha_11 = 'o'
                jogadas_diponiveis.remove(1)
                result = 'o'
                break
        elif linha_13 == 'o' and linha_31 == 'o':
            if linha_22 == '5':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                result = 'o'
                break
        elif linha_13 == 'o' and linha_22 == 'o':
            if linha_31 == '7':
                linha_31 = 'o'
                jogadas_diponiveis.remove(7)
                result = 'o'
                break
        elif linha_22 == 'o' and linha_31 == 'o':
            if linha_13 == '3':
                linha_13 = 'o'
                jogadas_diponiveis.remove(3)
                result = 'o'
                break

###### jogada para o computador não perder

    if jogo == 0:
        if linha_11 == 'x' and linha_13 == 'x':
            if linha_12 == '2':
                linha_12 = 'o'
                print('erro')
                jogadas_diponiveis.remove(2)
                jogo += 1
        elif linha_11 == 'x' and linha_12 == 'x':
            if linha_13 == '3':
                linha_13 = 'o'
                jogadas_diponiveis.remove(3)
                jogo += 1
        elif linha_12 == 'x' and linha_13 == 'x':
            if linha_11 == '1':
                linha_11 = 'o'
                jogadas_diponiveis.remove(1)
                jogo += 1
        elif linha_21 == 'x' and linha_23 == 'x':
            if linha_22 == '2':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                jogo += 1
        elif linha_21 == 'x' and linha_22 == 'x':
            if linha_23 == '6':
                linha_23 = 'o'
                jogadas_diponiveis.remove(6)
                jogo += 1
        elif linha_22 == 'x' and linha_23 == 'x':
            if linha_21 == '4':
                linha_21 = 'o'
                jogadas_diponiveis.remove(4)
                jogo += 1
        elif linha_31 == 'x' and linha_33 == 'x':
            if linha_32 == '8':
                linha_32 = 'o'
                jogadas_diponiveis.remove(8)
                jogo += 1
        elif linha_31 == 'x' and linha_32 == 'x':
            if linha_33 == '9':
                linha_33 = 'o'
                jogadas_diponiveis.remove(9)
                jogo += 1
        elif linha_32 == 'x' and linha_33 == 'x':
            if linha_31 == '7':
                linha_31 = 'o'
                jogadas_diponiveis.remove(7)
                jogo += 1
        elif linha_11 == 'x' and linha_31 == 'x':
            if linha_21 == '4':
                linha_21 = 'o'
                jogadas_diponiveis.remove(4)
                jogo += 1
        elif linha_11 == 'x' and linha_21 == 'x':
            if linha_31 == '7':
                linha_31 = 'o'
                jogadas_diponiveis.remove(7)
                jogo += 1
        elif linha_21 == 'x' and linha_31 == 'x':
            if linha_11 == '1':
                linha_11 = 'o'
                jogadas_diponiveis.remove(1)
                jogo += 1
        elif linha_12 == 'x' and linha_32 == 'x':
            if linha_22 == '5':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                jogo += 1
        elif linha_12 == 'x' and linha_22 == 'x':
            if linha_32 == '8':
                linha_32 = 'o'
                jogadas_diponiveis.remove(8)
                jogo += 1
        elif linha_22 == 'x' and linha_32 == 'x':
            if linha_12 == '2':
                linha_12 = 'o'
                jogadas_diponiveis.remove(2)
                jogo += 1
        elif linha_13 == 'x' and linha_33 == 'x':
            if linha_23 == '6':
                linha_23 = 'o'
                jogadas_diponiveis.remove(6)
                jogo += 1
        elif linha_13 == 'x' and linha_23 == 'x':
            if linha_33 == '9':
                linha_33 = 'o'
                jogadas_diponiveis.remove(9)
                jogo += 1
        elif linha_23 == 'x' and linha_33 == 'x':
            if linha_13 == '3':
                linha_13 = 'o'
                jogadas_diponiveis.remove(3)
                jogo += 1
        elif linha_11 == 'x' and linha_33 == 'x':
            if linha_22 == '5':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                jogo += 1
        elif linha_11 == 'x' and linha_22 == 'x':
            if linha_33 == '9':
                linha_33 = 'o'
                jogadas_diponiveis.remove(9)
                jogo += 1
        elif linha_22 == 'x' and linha_33 == 'x':
            if linha_11 == '1':
                linha_11 = 'o'
                jogadas_diponiveis.remove(1)
                jogo += 1
        elif linha_13 == 'x' and linha_31 == 'x':
            if linha_22 == '5':
                linha_22 = 'o'
                jogadas_diponiveis.remove(5)
                jogo += 1
        elif linha_13 == 'x' and linha_22 == 'x':
            if linha_31 == '7':
                linha_31 = 'o'
                jogadas_diponiveis.remove(7)
                jogo += 1
        elif linha_22 == 'x' and linha_31 == 'x':
            if linha_13 == '3':
                linha_13 = 'o'
                jogadas_diponiveis.remove(3)
                jogo += 1

##### jogada computador
    
    if jogo == 0:
        if jogada_computador == 0:
            if linha_22 == 'x':
                if linha_13 == '3':
                    linha_13 = 'o'
                    jogadas_diponiveis.remove(3)
                elif linha_11 == '1':
                    linha_11 = 'o'
                    jogadas_diponiveis.remove(1)
                elif linha_31 == '7':
                    linha_31 = 'o'
                    jogadas_diponiveis.remove(7)
                elif linha_33 == '9':
                    linha_33 = 'o'
                    jogadas_diponiveis.remove(9)
            elif linha_11 == 'x' or linha_13 == 'x' or linha_31 == 'x' or linha_33 == 'o':
                    if linha_22 == '5':
                        linha_22 = 'o'
                        jogadas_diponiveis.remove(5)
        jogada_computador = 1
        if jogada_computador == 1:
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
#####
    # verifica se alguem ganhou
    if linha_11 == linha_12 == linha_13:
        if linha_11 == 'x':
            result = 'x'
            break
        elif linha_11 == 'o':
            result = 'o'
            break
    elif linha_21 == linha_22 == linha_23:
        if linha_21 == 'x':
            result = 'x'
            break
        elif linha_21 == '0':
            result = 'o'
            break
    elif linha_31 == linha_32 == linha_33:
        if linha_31 == 'x':
            result = 'x'
            break
        elif linha_31 == 'o':
            result = 'o'
            break
    elif linha_11 == linha_21 == linha_31:
        if linha_11 == 'x':
            result = 'x'
            break
        elif linha_11 == 'o':
            result = 'o'
            break
    elif linha_12 == linha_22 == linha_32:
        if linha_12 == 'x':
            result = 'x'
            break
        elif linha_12 == 'o':
            result = 'o'
            break
    elif linha_13 == linha_23 == linha_33:
        if linha_13 == 'x':
            result = 'x'
            break
        elif linha_13 == 'o':
            result = 'o'
            break
    elif linha_11 == linha_22 == linha_33:
        if linha_11 == 'x':
            result = 'x'
            break
        if linha_11 == 'o':
            result = 'o'
            break
    elif linha_13 == linha_22 == linha_31:
        if linha_13 == 'x':
            result = 'x'
            break
        elif linha_13 == 'o':
            result = 'o'
            break
print('-'*30)
if result == 'x':
    print('jogo ganho')
elif result == 'o':
    print('jogo perdido')
print('-'*30)
print('         JOGO DA VELHA          ')
print('-'*30)
print('''
        {}  |  {}  |  {}
      -----------------
        {}  |  {}  |  {}
      -----------------
        {}  |  {}  |  {}
'''.format(linha_11, linha_12, linha_13, linha_21, linha_22, linha_23, linha_31, linha_32, linha_33))
print('-'*30)
