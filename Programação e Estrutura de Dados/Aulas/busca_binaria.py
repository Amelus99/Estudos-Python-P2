from typing import List

from carrega_servidores import *


def busca_binaria_iterativa(ip: str, servidores_dns: List[dict]) -> str:
    primeiro = 0
    ultimo = len(servidores_dns) - 1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        if servidores_dns[meio]['ip'] == ip:
            return servidores_dns[meio]['nome']
        if ip < servidores_dns[meio]['ip']:
            ultimo = meio - 1
        else:
            primeiro = meio + 1
    return ''


def busca_binaria_recursiva(ip: str, servidores_dns: List[dict], primeiro: int = 0, ultimo: int = None) -> str:
    if not ultimo:
        ultimo = len(servidores_dns) - 1
    meio = (primeiro + ultimo) // 2
    if servidores_dns[meio]['ip'] == ip:
        return servidores_dns[meio]['nome']
    if ip < servidores_dns[meio]['ip']:
        return busca_binaria_recursiva(ip, servidores_dns, primeiro, meio)
    else:
        return busca_binaria_recursiva(ip, servidores_dns, meio + 1, ultimo)



if __name__ == '__main__':
    servidores_dns = carrega_servidores_dns()
    servidores_dns.sort(key=lambda d: d['nome'])
    #print(servidores_dns)
    print('Busca Binária Iterativa:')
    print(busca_binaria_iterativa('CLARO S.A.', servidores_dns.copy()))
    print('Busca Binária Recursiva:')
    print(busca_binaria_recursiva('CLARO S.A.', servidores_dns.copy()))
