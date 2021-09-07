class No:
    def __init__(self, carga: object = None,
                 ant: 'No' = None,
                 prox: 'No' = None):
        self.carga = carga
        self.prox = prox
        self.ant = ant

    def __str__(self):
        return str(self.carga)


class ListaCircular:

    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def imprime_lista(self):
        if self.cabeca is None:
            print("Lista vazia")
            return

        atual: 'No' = self.cabeca
        print(atual)

        while atual is not self.cauda:
            print(atual.prox)
            atual = atual.prox

    def inserir_no_inicio(self, valor: object):
        novo: 'No' = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo
        else:
            novo.prox = self.cabeca
            self.cabeca = novo
            novo.prox.ant = novo
            self.cabeca.ant = self.cauda
            self.cauda.prox = self.cabeca

    def inserir_no_fim(self, valor):
        novo: 'No' = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo
        else:
            novo.ant = self.cauda
            novo.ant.prox = novo
            self.cauda = novo
            self.cauda.prox = self.cabeca
            self.cabeca.ant = self.cauda

    def remover_do_inicio(self):
        if self.cabeca is None:
            print("Lista vazia")
            return

        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cabeca = self.cabeca.prox
            self.cabeca.ant = self.cauda
            self.cauda.prox = self.cabeca

    def remover_do_fim(self):
        if self.cabeca is None:
            print("Lista vazia")
            return

        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cauda = self.cauda.ant
            self.cauda.prox = self.cabeca
            self.cabeca.ant = self.cauda

    def numero(self):
        if self.cabeca is None:
            print("Lista vazia")
            return
        else:
            atual: 'No' = self.cabeca
            valor = 0
            while True:
                valor = valor + 1
                self.cabeca = self.cabeca.prox
                if atual == self.cabeca:
                    break
            print(valor)
            return


LCircular: 'ListaCircular' = ListaCircular()

LCircular.inserir_no_fim('H')
LCircular.inserir_no_fim(2)
LCircular.inserir_no_fim('O')


print('Lista')
LCircular.imprime_lista()

print()

print('Tamanho da Lista')
LCircular.numero()
