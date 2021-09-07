from typing import List

from carrega_servidores import *
servidores_dns = carrega_servidores_dns()
'''
def busca_linear_iterativa(nome: str, servidores: List[dict]) -> str:
    for servidor in servidores:
        while nome == servidor['nome']:
            return servidor['ip']
        if nome < servidor['nome']:
            sdns = []
            for nome in servidores_dns:
                if nome['nome'] == nome:
                    sdns.append(servidor['ip'])


    return 'Servidor não foi encontrado!'
'''
def busca_linear(nome: str, servidores_dns: List[dict]) -> List[str]:
  resultado_busca = []
  for servidor in servidores_dns:
    if nome.upper() in servidor["nome"].upper(): #compara parte do nome, tornado o caso insensitive ao transformas ambas strings para UPPER
      resultado_busca.append(servidor["ip"])
      print(servidor)
  return resultado_busca #retorna lista com os ip correspondentes a nome digitado

#print("LISTA DE SERVIDORES: "+ str(servidores_dns))
nome_buscado = input("digite o nome do servidor buscado: ")
busca = busca_linear(nome_buscado,servidores_dns)
print("IP's encontrados para servidor informado: "+str(busca))
print("fim")

'''
def busca_linear_recursiva(ip: str, servidores: List[dict]) -> str:
    if len(servidores) == 0 or ip < servidores[0]['nome']:
        return ''
    if ip == servidores[0]['nome']:
        return servidores[0]['ip']
    servidores.pop(0)
    return busca_linear_recursiva(ip, servidores)


if __name__ == '__main__':
    servidores_dns = carrega_servidores_dns()
    servidores_dns.sort(key=lambda d: d['nome'])  # altero a chave pra definir por onde ordenar por key=lambda
    #print(servidores_dns)
    print('Busca Linear Iterativa:')
    print(busca_linear_iterativa('CLARO S.A.', servidores_dns.copy()))
    print('Busca Linear Recursiva:')
    print(busca_linear_recursiva('CLARO S.A.', servidores_dns.copy()))
'''