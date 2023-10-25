import user
import work
import time
import json
dentro = work.get_all_work()
jogadas = json.dumps(dentro)
lista = []

print(jogadas)

for x in dentro:
    nario = {
        "work_id": x[0],
        "work_name": x[1]
    }
    lista.append(nario)


print(lista)

