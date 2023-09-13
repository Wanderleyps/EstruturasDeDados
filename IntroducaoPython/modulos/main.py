# Importe algumas funções do módulo calculadora
# from calculadora import somar, subtrair, multiplicar

import calculadora as calc

resultado_soma = calc.somar(5, 3)
resultado_subtracao = calc.subtrair(10, 4)
resultado_multiplicacao = calc.multiplicar(6, 7)
resultado_divisao = calc.dividir(8, 2)

print("Soma:", resultado_soma)
print("Subtração:", resultado_subtracao)
print("Multiplicação:", resultado_multiplicacao)
print("Divisão:", resultado_divisao)
