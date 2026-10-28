import psutil as p
import time
from datetime import datetime
import csv

with open('dados.csv', 'w', encoding="utf-8-sig", newline="") as arquivo:
    escritor_csv = csv.writer(arquivo, delimiter=";")

    escritor_csv.writerow(["Integrante", "CPU", "RAM", "Disco", "Data_Hora"])

    for i in range(100):

        cpu_percentual = p.cpu_percent(interval=1)
        memoria_percentual = p.virtual_memory().percent
        disco = p.disk_usage('/').percent
        data_hora = datetime.now()

        print('--- Uso da CPU ---')
        print(cpu_percentual, '%')

        print('--- Uso da Memória RAM ---')
        print(memoria_percentual, '%')

        print('--- Uso do Disco ---')
        print(disco, '%')

        print('--- Hora da Captura ---')
        print(data_hora)

        escritor_csv.writerow([
            "Giulia",
            cpu_percentual,
            memoria_percentual,
            disco,
            data_hora
        ])

        arquivo.flush()

        time.sleep(2)

    print("Captura finalizada! Foram coletados 100 dados.")
