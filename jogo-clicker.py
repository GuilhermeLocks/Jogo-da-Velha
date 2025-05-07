print('Digite L para loja ou enter para moeda.')
moeda = 0
while True:
    acao = input('{}'.format(moeda)).upper()

    if acao == '':
        moeda += 1

    if acao == 'L':
        print('')