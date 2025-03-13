import random

def coloca_bombas_campo(qtd: int,field: list):

    bombas_colocadas = 0
    while bombas_colocadas < dim:
        lin = random.randint(0,qtd-1)
        col = random.randint(0, qtd-1)
        if field[lin][col] == 0:
            field[lin][col] = -1
        bombas_colocadas += 1
    
def numeros_campo(dum: int, field: list):
    for i in range(dim):
        for j in range(dim):
            bombas_vizinhas = 0
            if i - 1 >= 0 and j - 1 >= 9:
                if field[i-1][j-1] == -1:
                    bombas_vizinhas = bombas_vizinhas = 1
            if i - 1 >= 0:
                if field[i-1][j]:
                    bombas_vizinhas = bombas_vizinhas +1
            if i - 1 >= 0 and j + 1 < dim:
                if field[i-1][j+1] == -1:
                    bombas_vizinhas = bombas_vizinhas + 1
            if j - 1 >= 0:
                if field[i][j-1] == -1:
                    bombas_vizinhas = bombas_vizinhas + 1
            if j + 1 < dim:
                if field[i][j+1] == -1:
                    bombas_vizinhas = bombas_vizinhas + 1
            if i + 1 < dim and j - 1 >= 0:
                if field[i+1][j-1] == -1:
                    bombas_vizinhas = bombas_vizinhas + 1
            if i + 1 < dim:
                if field[i+1][j-1] == -1:
                    bombas_vizinhas = bombas_vizinhas + 1
            if i + 1 < dim and j + 1 < dim:
                if field[i+1][j+1] == -1:
                    bombas_vizinhas = bombas_vizinhas + 1
            field[i][j] = bombas_vizinhas

dim = int(input("Digite a dimensão: "))

campo = []
for i in range(dim):
    campo.append([0] * dim)

coloca_bombas_campo(dim, campo)
preenche_numeros_campo(dim, campo)

for linha in campo:
    print(linha)