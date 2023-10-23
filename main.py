import user
import work
import time
import json
dentro = work.get_all_work()
jogadas = json.dumps(dentro)

for x in dentro:
    print(x[0])
    print(x[1])
    print(x[2])

print(jogadas)