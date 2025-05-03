from tabuleiro import jogadas_diponiveis
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