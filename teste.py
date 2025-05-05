lista_1 = [1,1,1,1,1,1,2,2,2,3,3,3,3,4,4,4,5,5,5,5,6,7,7,8]
lista_2 = [2,3,4,5,7,9,3,5,8,5,6,7,9,5,6,7,6,7,8,9,9,8,9,9]
lista_3 = [3,2,7,9,4,5,1,8,5,7,9,5,6,6,5,1,4,3,2,1,3,9,8,7]
jogadas_diponiveis = ['x', 1, 2, 3, 4, 5, 6, 7, 8, 9]
for c in range(0, 24):
    print(c)
    if jogadas_diponiveis[lista_1[c]] == jogadas_diponiveis[lista_2[c]] == 'o' and jogadas_diponiveis[lista_3[c]] != 'o' and jogadas_diponiveis[lista_3[c]] != 'x':
        jogadas_diponiveis[lista_3[c]] = 'o'
        result = 'o'
        break
    elif jogadas_diponiveis[lista_1[c]] == jogadas_diponiveis[lista_2[c]] and jogadas_diponiveis[lista_3[c]] != 'o' and jogadas_diponiveis[lista_3[c]] != 'x':
        jogadas_diponiveis[lista_3[c]] = 'o'
print('''
12 3
13 2
14 7 
15 9 
17 4 
19 5 
23 1
25 8
28 5
35 7
36 9
37 5
39 6
45 6
46 5
47 1
56 4
57 3
58 2
59 1
69 3
78 9
79 8
89 7
''')



