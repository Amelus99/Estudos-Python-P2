municipios = open('MunicipiosPB.csv', 'r', encoding='utf-8')

aux = []
for linha in municipios.read().split(','):
    aux.append(linha)
print(aux)

municipios.close()