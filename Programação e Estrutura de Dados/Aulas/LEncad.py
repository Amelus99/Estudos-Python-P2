class No:
    def __init__(self, carga: object = None, prox: 'No' = None):
        self.carga = carga
        self.prox = prox

    def __str__(self):
        return str(self.carga)


# ----------------------------------------------------------------------------------

class ListaEncadeada:
    def __init__(self):
        self.cabeca: 'No' = None
        self.cauda: 'No' = None

    def imprime_lista(self):
        if self.cabeca is None:
            print("Lista Vazia")
            return
        atual: 'No' = self.cabeca
        while atual is not None:
            print(str(atual.carga) + " ")
            atual = atual.prox

    def inserir_valor_no_inicio(self, valor: object):
        novo = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo
        else:
            novo.prox = self.cabeca
            self.cabeca = novo

    def inserir_valor_no_fim(self, valor: object):
        novo = No(valor)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo
        else:
            self.cauda.prox = novo
            self.cauda = novo

    def remove_do_inicio(self):
        if self.cabeca is None:
            print("Lista Vazia")
            return
        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cabeca = self.cabeca.prox

    def remove_do_fim(self):
        if self.cabeca is None:
            print("Lista Vazia")
            return
        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            atual: 'No' = self.cabeca
            while atual.prox is not self.cauda:
                atual = atual.prox
            self.cauda = atual
            atual.prox = None

    def faz_impar(self):
        atual: 'No' = lista.cabeca
        while atual is not None:
            valor = (atual.carga % 2)
            if valor == 1:
                lista1.inserir_valor_no_fim(atual.carga)
            atual = atual.prox

    def faz_par(self):
        atual: 'No' = lista.cabeca
        while atual is not None:
            valor = (atual.carga % 2)
            if valor == 0:
                lista2.inserir_valor_no_fim(atual.carga)
            atual = atual.prox


# ----------------------------------------------------------------------------------
'''
n1 = No()
n1.carga = 1

n2 = No("d")

n3 = No()
n3.carga = No("c")

n4 = No(2)

n1.prox = n2
n2.prox = n3
n3.prox = n4
n4.prox = None

lista = ListaEncadeada()
lista.cabeca = n1
lista.cauda = n4

print(lista.cabeca)
print(lista.cabeca.prox)
print(lista.cauda)
'''
# ----------------------------------------------------------------------------------
'''
lista = ListaEncadeada()
lista.inserir_valor_no_inicio("aaa")
lista.inserir_valor_no_inicio("bbb")
lista.inserir_valor_no_inicio("novo")

print(lista.cabeca)
print(lista.cabeca.prox)
print(lista.cabeca.prox.prox)

lista = ListaEncadeada()
lista.inserir_valor_no_fim("aaa")
lista.inserir_valor_no_fim("bbb")
lista.inserir_valor_no_fim("ccc")

print(lista.cabeca)
print(lista.cabeca.prox)
print(lista.cabeca.prox.prox)
'''
# ----------------------------------------------------------------------------------
'''
n1 = No("a")
n2 = No(2)
n3 = No("c")
n4 = No(4)

n1.prox = n2
n2.prox = n3
n3.prox = n4

lista = ListaEncadeada()
lista.cabeca = n1
lista.cauda = n4
lista.imprime_lista()
'''
# ----------------------------------------------------------------------------------
'''
n1 = No(1)
n2 = No(2)
n3 = No(3)
n4 = No(4)

n1.prox = n2
n2.prox = n3
n3.prox = n4

lista = ListaEncadeada()
lista.cabeca = n1
lista.cauda = n4
lista.imprime_lista()
lista.remove_do_inicio()
lista.remove_do_fim()
print()
lista.imprime_lista()
'''
# ----------------------------------------------------------------------------------
'''
lista = ListaEncadeada()
lista.inserir_valor_no_fim(1)
lista.inserir_valor_no_fim(2)
lista.inserir_valor_no_fim(6)
lista.inserir_valor_no_fim(7)
lista.inserir_valor_no_fim(8)

lista1 = ListaEncadeada()
lista1.faz_impar()
print("Lista Impar")
lista1.imprime_lista()

print()

lista2 = ListaEncadeada()
lista2.faz_par()
print("Lista Par")
lista2.imprime_lista()
'''
# ----------------------------------------------------------------------------------
'''
lista = ListaEncadeada()
lista.inserir_valor_no_fim(1)
lista.inserir_valor_no_fim(7)
print('Lista 1')
lista.imprime_lista()
print()

lista2 = ListaEncadeada()
lista2.inserir_valor_no_fim(3)
lista2.inserir_valor_no_fim(4)
lista2.inserir_valor_no_fim(8)
print('Lista 2')
lista2.imprime_lista()
print()

lista3 = ListaEncadeada()
atual: 'No' = lista.cabeca
while atual is not None:
    lista3.inserir_valor_no_fim(atual.carga)
    atual = atual.prox
atual: 'No' = lista2.cabeca
while atual is not None:
    lista3.inserir_valor_no_fim(atual.carga)
    atual = atual.prox
print('Lista 3')
lista3.imprime_lista()
'''
# ----------------------------------------------------------------------------------
#'''

#'''
# ----------------------------------------------------------------------------------
