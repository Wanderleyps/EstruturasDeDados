'''''
-------------------- ATIVIDADE 06 --------------------
'''''

import sys


def algoritmo_a(n, m):
    soma = 0
    for i in range(n):
        for j in range(m):
            soma = soma + 1
    return soma


def algoritmo_b(n, vetor):
    menor = sys.maxsize  # maior número inteiro
    for i in range(n):
        if vetor[i] < menor:
            menor = vetor[i]
    return menor


def algoritmo_c(matriz, n):
    for i in range(n):
        for j in range(n):
            matriz[i][j] = i * j
    return matriz


def algoritmo_d(n, vetor):
    menor = sys.maxsize  # maior número inteiro
    for i in range(n):
        if vetor[i] < menor:
            menor = vetor[i]
    if menor < 0:
        for i in range(n):
            menor = menor * (i + 1)
    return menor


def algoritmo_e(n, vetor):
    menor = sys.maxsize  # maior número inteiro
    for i in range(n):
        if vetor[i] < menor:
            menor = vetor[i]
    if menor < 0:
        for i in range(n):
            menor = menor * (i + 1)
    elif menor > 0:
        for i in range(n * n):
            print(menor)
    else:
        print(menor)

##############################################################


def busca(nome, pessoas):
    for pessoa in pessoas:
        if pessoa.getNome() == nome:
            return pessoa
    return None

# a)


def exibir(nome, pessoas):
    pessoa = busca(nome, pessoas)
    if pessoa is not None:
        pessoa.exibirDados()
    else:
        print("Pessoa não encontrada")

# b)


def exibir_alternativo(nome, pessoas):
    pessoa = busca(nome, pessoas)
    if pessoa is not None:
        pessoa.exibirDados()
    else:
        print("Pessoa não encontrada")

# c)


def atualizar(nome, idade, salario, pessoas):
    pessoa = busca(nome, pessoas)
    if pessoa is not None:
        pessoa.setIdade(idade)
        pessoa.setSalario(salario)
    else:
        print("Pessoa não encontrada")
