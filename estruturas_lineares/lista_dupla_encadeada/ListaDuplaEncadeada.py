from No import No


class ListaDuplaEncadeada:
    def __init__(self):
        self.__inicio = None
        self.__fim = None
        self.__qtd = 0

    def is_vazia(self):
        return self.__inicio is None

    def tamanho(self):
        return self.__qtd

    def inserir_inicio(self, valor):
        novo_no = No(valor)
        if (self.is_vazia()):
            self.__fim = novo_no
        else:
            self.__inicio.ant = novo_no
            novo_no.prox = self.__inicio
        self.__inicio = novo_no
        self.__qtd += 1

    def inserir_final(self, valor):
        if (self.is_vazia()):
            self.inserir_inicio(valor)
        else:
            novo_no = No(valor)
            novo_no.ant = self.__fim
            self.__fim = novo_no
        self.__qtd += 1

    def remover_inicio(self):
        if (self.is_vazia()):
            return None
        valor = self.__inicio.valor
        self.__inicio = self.__inicio.prox
        if (self.__inicio == None):
            self.__fim = None
        else:
            self.__inicio.ant = None
        self.__qtd -= 1
        return valor

    def remover_final(self):
        if (self.is_vazia()):
            return None
        valor = self.__fim.valor
        if (self.__inicio == self.__fim):
            self.__inicio = None
            self.__fim = None
        else:
            self.__fim.ant.prox = None
            self.__fim = self.__fim.ant
        self.__qtd -= 1
        return valor

    def imprimir(self):
        qtd = 0
        atual = self.__inicio
        while (atual != None):
            print(atual.valor, end=' <-> ')
            qtd = qtd + 1
            atual = atual.prox
        print("None")
