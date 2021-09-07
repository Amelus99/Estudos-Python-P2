class No:
    def __init__(self, carga: object = None,
                 ant: 'No' = None,
                 prox: 'No' = None):
        self.carga = carga
        self.prox = prox
        self.ant = ant

    def __repr__(self):
        return '%s -> %s' % (self.carga, self.prox)


class EstruturaLinear:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

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

        elemento_a_remover = self.cabeca

        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cabeca = self.cabeca.prox
            self.cabeca.ant = None  # O anterior da nova cabeça agora passa a apontar para None

        return elemento_a_remover

    def remover_do_final(self):
        if self.cabeca is None:
            print("Lista vazia")
            return

        elemento_a_remover = self.cauda

        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            # Note que agora não é mais necessário percorrer a lista até o final, basta começar navegando pela cauda
            self.cauda = self.cauda.ant  # Faz a cauda apontar agora para o penúltimo elemento da lista
            self.cauda.prox = None  # o próximo da nova cauda agora passa a pontar para None

        return elemento_a_remover


class Fila(EstruturaLinear):
    def inserir(self, elemento):
        self.inserir_no_final(elemento)

    def remover(self):
        return self.remover_do_inicio()


fila = Fila()
fila.inserir(50)
fila.inserir(20)
fila.inserir(30)
fila.inserir(10)
fila.remover()
print(fila)


class Pilha(EstruturaLinear):
    def push(self, elemento):
        self.inserir_no_inicio(elemento)

    def pop(self):
        return self.remover_do_inicio()


pilha = Pilha()
pilha.push(50)
pilha.push(20)
pilha.push(30)
pilha.push(10)
pilha.pop()
print(pilha)
