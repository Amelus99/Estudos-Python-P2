class No:
    def __init__(self, carga=0, anterior=None):
        self.carga = carga
        self.anterior = anterior

    def __repr__(self):
        return '%s -> %s' % (self.carga, self.anterior)


class Pilha:
    def __init__(self):
        self.topo = None
        self.contador = 0

    def is_empty(self):
        return self.topo is None

    def push(self, elemento):
        no = No(elemento)
        no.anterior = self.topo
        self.topo = no
        self.contador += 1

    def pop(self):
        assert self.topo != None, "Impossível remover elemento de pilha vazia."
        elemento_a_remover = self.topo
        self.topo = self.topo.anterior
        self.contador -= 1
        return elemento_a_remover

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def __len__(self):
       atual = self.topo
       c = 0
       while atual is not None:
         c += 1
         atual = atual.anterior
       return c

    def __len__(self):
        return self.contador


def main():
    pilha = Pilha()
    pilha.push(50)
    pilha.push(20)
    pilha.push(30)
    pilha.push(10)
    print(pilha.pop())
    print(pilha)
    print(len(pilha))


main()
