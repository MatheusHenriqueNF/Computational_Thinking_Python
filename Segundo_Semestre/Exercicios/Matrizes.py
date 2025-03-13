# matriz = [
#     ['Edu', 'Ana', 'Beto', 'Celi', 'Davi', 'João'],
#     [37, 42, 57, 67, 101, 237],
#     [47.8, 55.0, 61.3, -3.5, -6.0, 18.1]
# ]

# print(matriz[2])

sudoku = []

for i in range(9):
    sudoku.append([''] * 9)

sudoku [0][2]=1
sudoku [1][2]=2
sudoku [1][4]=3
sudoku [1][8]=4
sudoku [2][3]=5
sudoku [2][6]=6
sudoku [2][8]=7
sudoku [3][0]=5
sudoku [3][3]=1
sudoku [3][4]=0
sudoku [4][1]=7
sudoku [4][7]=2
sudoku [5][4]=7
sudoku [5][5]=8
sudoku [5][8]=9
sudoku [6][0]=8
sudoku [6][2]=7
sudoku [6][5]=8
sudoku [7][0]=4
sudoku [7][4]=4
sudoku [7][6]=3
sudoku [8][6]=5

for linha in sudoku:
    print(linha)