from typing import List
from carrega_servidores import *


def myFunc(e):  # funça organiza por key 'ip'
    return e['nome']


def busca_binaria_recursiva(nome: str, servidores_dns: List[dict], lim_inf, lim_sup, ips=[]) -> List[str]:
    if not servidores_dns:
        return ips
    if not lim_sup:
        max_indices = (len(servidores_dns) - 1)
        lim_sup = max_indices
    mediana = int((lim_inf + lim_sup) / 2)
    resutado_busca3 = []
    encontrado = False

    if nome.upper() in (servidores_dns[mediana]['nome']).upper():
        resutado_busca3.append(servidores_dns[mediana]['ip'])
        print(servidores_dns[mediana])

    if (nome[0].upper() <= (servidores_dns[mediana]['nome'].upper())[0]):
        lim_inf = lim_inf
        lim_sup = mediana
    else:
        lim_inf = mediana
        lim_sup = lim_sup

    servidores_dns.pop(mediana)
    lim_sup = lim_sup - 1  # com a exclusão de um item da lista, o limite superior é alterado, decrescendo em 1.
    return busca_binaria_recursiva(nome, servidores_dns, lim_inf, lim_sup)


lista_falsa = servidores_dns.copy()
lista_falsa.sort(key=myFunc)
print("LISTA DE SERVIDORES (COPIA): " + str(lista_falsa))  # imprimir apenas para conferencia
print("TESTE IMPRESSÃO de IP: " + str(lista_falsa[0]['ip']))

nome_buscado = input("digite o nome do servidor buscado: ")
busca4 = busca_binaria_recursiva(nome_buscado, lista_falsa)
print("IP's encontrados para servidor informado: " + str(busca4))
print(len(busca4))
print("fim")