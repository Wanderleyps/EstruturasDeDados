from ListaDuplaEncadeada import ListaDuplaEncadeada
from No import No

# Criando uma instância da ListaEncadeada
lista = ListaDuplaEncadeada()

op = None

while (op != 0):
    print("\nMenu:")
    print("1. Inserir Inicio")
    print("2. Inserir Final")
    print("3. Remover Inicio")
    print("4. Remover Final")
    print("5. Remover Por Valor")
    print("6. Ver Lista")
    print("0. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        valor = input("Digite o valor: ")
        lista.inserir_inicio(valor)
    elif escolha == "2":
        valor = input("Digite o valor: ")
        lista.inserir_final(valor)
    elif escolha == "3":
        print('Valor removido: ', lista.remover_inicio())
    elif escolha == "4":
        print('Valor removido: ', lista.remover_final())
    elif escolha == "5":
        valor = input("Digite o valor: ")
        print('Valor removido: ', lista.remover_valor(valor))
    elif escolha == "6":
        print('Tamanho: ', lista.tamanho())
        lista.imprimir()
    elif escolha == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
