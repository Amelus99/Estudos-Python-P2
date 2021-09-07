from typing import List

vetorOrdenado: List[int] = [1, 2, 5, 7, 9, 11, 12, 18, 19, 21]
print(vetorOrdenado)


def busca_sequencial(chave_pesquisa: int, vetor: List[int]):
    for i in range(len(vetor)):
        if vetor[i] == chave_pesquisa:
            return i
        if vetor[i] > chave_pesquisa:
            return -1
    return -1


busca_sequencial(10, vetorOrdenado)


def busca_sequencial_recursiva(chave: int, vetor: List[int], i: int = 0):
    if i >= len(vetor) or vetor[i] > chave:
        return -1
    if vetor[i] == chave:
        return i
    return busca_sequencial_recursiva(chave, vetor, i + 1)


print(busca_sequencial_recursiva(0, vetorOrdenado))
print(busca_sequencial_recursiva(2, vetorOrdenado))
print(busca_sequencial_recursiva(5, vetorOrdenado))
print(busca_sequencial_recursiva(8, vetorOrdenado))


def busca_binaria(chave: int, vetor: List[int]) -> int:
    primeiro: int = 0
    ultimo: int = len(vetor) - 1

    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        if vetor[meio] == chave:
            ## Item encontrado
            return meio

        if chave < vetor[meio]:
            ultimo = meio - 1
        else:
            primeiro = meio + 1

    return -1  ## item não encontrado


vetor = [1, 2, 5, 7, 9, 11, 12, 18, 19, 21]
print(busca_binaria(2, vetor))
print(busca_binaria(7, vetor))
print(busca_binaria(19, vetor))
print(busca_binaria(21, vetor))
print(busca_binaria(0, vetor))
print(busca_binaria(6, vetor))
print(busca_binaria(25, vetor))


def busca_binaria_recursiva(vetor: List[int], chave: int, primeiro=0, ultimo=None) -> int:
    if not ultimo:
        ultimo = len(vetor) - 1

    meio = (primeiro + ultimo) // 2

    if vetor[meio] == chave:
        return meio

    if meio == 0 or primeiro == ultimo:
        return -1

    if chave < vetor[meio]:
        return busca_binaria_recursiva(vetor, chave, primeiro, meio)
    else:
        return busca_binaria_recursiva(vetor, chave, meio + 1, ultimo)


vetor = [2, 3, 5, 7, 9, 11, 12, 18, 19, 21]
print(busca_binaria_recursiva(vetor, 2))
print(busca_binaria_recursiva(vetor, 19))
print(busca_binaria_recursiva(vetor, 18))
print(busca_binaria_recursiva(vetor, 11))
print(busca_binaria_recursiva(vetor, 21))
print(busca_binaria_recursiva(vetor, 12))
print(busca_binaria_recursiva(vetor, 22))
print(busca_binaria_recursiva(vetor, 6))
print(busca_binaria_recursiva(vetor, 1))
