from ListaEncadeada import ListaEncadeada
from No import No

# Criando uma instância da ListaEncadeada
lista = ListaEncadeada()

# Verificando se a lista está vazia (deve retornar True)
print("Lista vazia:", lista.is_vazia())

# Inserindo elementos no início da lista
lista.inserir_inicio(10)
lista.inserir_inicio(20)
lista.inserir_inicio(30)

# Verificando o tamanho da lista (deve retornar 3)
print("Tamanho da lista:", lista.tamanho())

# Inserindo elementos no final da lista
lista.inserir_final(40)
lista.inserir_final(50)

# Imprimindo a lista
print("Lista após inserções iniciais:")
lista.imprimir()

# Removendo elementos do início da lista (deve remover 30, 20, 10)
lista.remover_inicio()
lista.remover_inicio()
lista.remover_inicio()

# Imprimindo a lista após remoções
print("\nLista após remoção do início:")
lista.imprimir()

# Removendo elementos do final da lista (deve remover 50, 40)
lista.remover_final()
lista.remover_final()

# Imprimindo a lista após remoção do final
print("\nLista após remoção do final:")
lista.imprimir()

# Inserindo elementos para teste de remoção por valor
lista.inserir_inicio(60)
lista.inserir_inicio(70)
lista.inserir_inicio(60)

# Imprimindo a lista antes da remoção por valor
print("\nLista antes da remoção por valor:")
lista.imprimir()

# Removendo elementos com valor 60 (deve remover ambos)
lista.remover_valor(60)

# Imprimindo a lista após remoção por valor
print("\nLista após remoção por valor:")
lista.imprimir()

# Verificando se a lista está vazia após todas as operações (deve retornar False)
print("\nLista vazia:", lista.is_vazia())
