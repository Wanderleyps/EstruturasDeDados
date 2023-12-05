from ArvBin import ArvBin
from No import No

arvBin = ArvBin()

op = None

while (op != 0):
    print("\nMenu lista simples:")
    print("1. Inserir")
    print("2. Remover")
    print("3. Buscar")
    print("4. Quantidade")
    print("5. Altura")
    print("6. Pré-ordem")
    print("7. Em-ordem")
    print("8. Pós-ordem ")
    print("0. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        valor = int(input("Digite o valor a ser inserido: "))
        arvBin.insere(valor)
    elif escolha == "2":
        valor = int(input("Digite o valor a ser removido: "))
        print(arvBin.remove(valor))
    elif escolha == "3":
        valor = int(input("Digite o valor a ser buscado: "))
        print(arvBin.busca(valor))
    elif escolha == "4":
        print('Quantidade de nós: ', arvBin.totalNO())
    elif escolha == "5":
        print('Altura da árvore: ', arvBin.altura())
    elif escolha == "6":
        print('Pré-ordem: ')
        arvBin.preOrdem()
    elif escolha == "7":
        print('Em-ordem: ')
        arvBin.emOrdem()
    elif escolha == "8":
        print('Pós-ordem: ')
        arvBin.posOrdem()
    elif escolha == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
