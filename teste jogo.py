linha_11 = '1'
linha_12 = '2'
linha_13 = '3'
linha_21 = '4'
linha_22 = '5'
linha_23 = '6'
linha_31 = '7'
linha_32 = '8'
linha_33 = '9'
('-' * 30)
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

cabeca = ('''        JOGO DA VELHA
------------------------------    
    
        {}  |  {}  |  {}
      -----------------
        {}  |  {}  |  {}
      -----------------
        {}  |  {}  |  {}
        
------------------------------
'''.format(linha_11, linha_12, linha_13, linha_21, linha_22, linha_23, linha_31, linha_32, linha_33))
print(cabeca)