'''''
-------------------- ATIVIDADE 06 --------------------
'''''
# Q01


def algoritmo_a(n):
    soma = 0
    for i in range(n):
        soma = soma + i
    return soma

# Q02


def algoritmo_b(n):
    soma1 = 0
    soma2 = 0
    for i in range(n):
        soma1 = soma1 + 1
        soma2 = soma2 + i
    return soma1, soma2


def algoritmo_c(n, vetor):
    soma = 0
    for i in range(n):
        if vetor[i] % 2 == 0:
            soma = soma + vetor[i]
    return soma


def algoritmo_d(n):
    soma1 = 0
    for i in range(n):
        soma1 = soma1 + 1
    for j in range(n):
        soma1 = soma1 + j
    return soma1


def algoritmo_e(n):
    soma = 0
    for i in range(n):
        for j in range(n):
            soma = soma + 1
    return soma

