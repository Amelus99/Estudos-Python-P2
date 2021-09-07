import csv


def carrega_servidores_dns():
    servidores_dns = []
    with open('dns-br.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        next(csv_reader, None)  # pula os cabeçalhos
        for row in csv_reader:
            servidor_dns = dict()
            servidor_dns['ip'] = row[0]
            servidor_dns['nome'] = row[1]
            servidores_dns.append(servidor_dns)
    return servidores_dns

servidores_dns = carrega_servidores_dns()

# print(carrega_servidores_dns())
