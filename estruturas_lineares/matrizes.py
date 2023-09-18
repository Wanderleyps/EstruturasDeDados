def le_matriz(n):
    mat = []  # Inicializa uma matriz vazia

    for i in range(n):  # Loop para ler cada linha da matriz
        linha = []  # Inicializa uma lista vazia para representar uma linha

        for j in range(n):  # Loop para ler cada coluna da linha
            valor = float(input(f"Valor da posição ({i+1},{j+1}): "))
            linha.append(valor)  # Adiciona o valor à linha

        mat.append(linha)  # Adiciona a linha à matriz

    return mat


def print_matriz(mat):
    # Código que faz a impressão linha por linha da matriz
    for i in mat:
        for j in i:
            print(j, end=", ")  # imprime números na mesma linha separados por ,
        print()  # após impressão de uma linha, pula uma linha


def soma_matriz(mat1, mat2):
    # calcula a soma de mat1 com mat2
    n = len(mat1)  # definida como o tamanho
    mat3 = [[0 for j in range(n)] for i in range(n)]  # inicializa a matriz
    for i in range(n):
        for j in range(n):
            mat3[i][j] = mat1[i][j] + mat2[i][j]
    return mat3


# Lemos as duas matrizes:
n = int(input("Dimensão das matrizes: "))

print("Lendo Mat1")
mat1 = le_matriz(n)
print("Matriz 1")
print_matriz(mat1)

print("Lendo Mat2")
mat2 = le_matriz(n)
print("Matriz 2")
print_matriz(mat2)

matriz_soma = soma_matriz(mat1, mat2)
print("Imprimindo Mat3 linha por linha")
print_matriz(matriz_soma)
