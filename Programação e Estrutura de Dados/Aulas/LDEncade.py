class No:
    def __init__(self, carga: object = None, ant: 'No' = None, prox: 'No' = None):
        self.carga = carga
        self.prox = prox
        self.ant = ant

    def __str__(self):
        return str(self.carga)


class ListaDuplamenteEncadeada:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def imprimir_lista(self):
        if self.cabeca is None:
            print("Lista vazia")
            return

        atual: 'No' = self.cabeca
        while atual is not None:
            print(atual)
            atual = atual.prox

    def imprimir_lista_invertida(self):
        if self.cabeca is None:
            print("Lista vazia")
            return

        atual: 'No' = self.cauda
        while atual is not None:
            print(atual.carga)
            atual = atual.ant

    def inserir_no_inicio(self, valor: object):
        novo: 'No' = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo
        else:
            novo.prox = self.cabeca
            self.cabeca = novo
            novo.prox.ant = novo

    def inserir_no_final(self, valor):
        novo: 'No' = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo
        else:
            novo.ant = self.cauda  # O anterior do nó novo será a cauda atual
            novo.ant.prox = novo  # O próximo do elemento anterior será o novo elemento a ser inserido
            self.cauda = novo  # a cauda passa a ser o elemento novo a ser inserido

    def remover_do_inicio(self):
        if self.cabeca is None:
            print("Lista vazia")
            return

        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cabeca = self.cabeca.prox
            self.cabeca.ant = None  # O anterior da nova cabeça agora passa a apontar para None

    def remover_do_final(self):
        if self.cabeca is None:
            print("Lista vazia")
            return

        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            # Note que agora não é mais necessário percorrer a lista até o final, basta começar navegando pela cauda
            self.cauda = self.cauda.ant  # Faz a cauda apontar agora para o penúltimo elemento da lista
            self.cauda.prox = None  # o próximo da nova cauda agora passa a pontar para None

    def remover_de_posicao(self, pos):
        if pos == 0:
            self.remover_do_inicio()
            return
        atual: 'No' = self.cabeca
        contador: int = 0
        while atual is not None:
            if pos == contador:
                atual.ant.prox = atual.prox
                if atual.prox is not None:
                    atual.prox.ant = atual.ant
                else:
                    self.cauda = atual.ant
            atual = atual.prox
            contador += 1

    def removedor_de_repetidos(self, elemento):
        if self.cabeca is None:
            print("Lista vazia")
            return

        atual: 'No' = self.cabeca
        contador: int = 0
        if elemento == atual:
            contador =+1
        if contador == 2:
            while atual is not None:
                if elemento == contador:
                    atual.ant.prox = atual.prox
                    if atual.prox is not None:
                        atual.prox.ant = atual.ant
                    else:
                        self.cauda = atual.ant
                atual = atual.prox
                contador += 1

    #self.cabeca = self.cabeca.prox
    def __iter__(self):
        atual: 'No' = self.cabeca
        while atual is not None:
            yield atual
            atual = atual.prox

    def __setitem__(self, indice, valor):
        atual: 'No' = self.cabeca
        for i in range(indice):
            atual = atual.prox
        atual.carga = valor

    def __getitem__(self, indice):
        atual: 'No' = self.cabeca
        for i in range(indice):
            atual = atual.prox
        return atual.carga


lista: 'ListaDuplamenteEncadeada' = ListaDuplamenteEncadeada()
lista.inserir_no_inicio(50)
lista.inserir_no_inicio(30)
lista.inserir_no_inicio(20)
lista.inserir_no_inicio(10)
print(lista[0])
lista[0] = 100
print(lista[0])
print(lista[1])
print(lista[2])
for l in lista:
    print(l)
    sublista = [x.carga for x in lista if x.carga < 100]
    print(sublista)
