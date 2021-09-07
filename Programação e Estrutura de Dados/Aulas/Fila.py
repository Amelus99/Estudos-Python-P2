class No:
    def __init__(self, carga=0, proximo=None):
        self.carga = carga
        self.proximo = proximo

    def __repr__(self):
        return '%s -> %s' % (self.carga, self.proximo)


class Fila:
    def __init__(self, cabeca=None, cauda=None):
        self.cabeca = cabeca
        self.cauda = cauda

    def is_empty(self):
        return self.cabeca is None and self.cauda is None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    def inserir(self, elemento):
        novo_no = No(elemento)

        if self.cabeca == None:
            self.cabeca = self.cauda = novo_no
        else:
            self.cauda.proximo = novo_no
            self.cauda = novo_no

    def remover(self):
        assert self.cabeca != None, "Impossível remover elemento de fila vazia."
        elemento_a_remover = self.cabeca
        self.cabeca = self.cabeca.proximo
        return elemento_a_remover


def main():
    fila = Fila()
    fila.inserir(50)
    fila.inserir(20)
    fila.inserir(30)
    fila.inserir(10)
    fila.remover()
    print(fila)


main()
