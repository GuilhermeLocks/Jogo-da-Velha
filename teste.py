jogadas_diponiveis = ['x', 1, 2, 3, 4, 5, 6, 7, 8, 9]
jogada = 0
def velha(jogada):
    for c in range(1, 10):
        if jogada == c:
            jogadas_diponiveis[c] = 'x'
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
jogada = int(input('digite sua jogada: '))




