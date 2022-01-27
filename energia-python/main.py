import csv
from collections import defaultdict

counter = {}

with open('pronunciamentos.csv', encoding='utf-8', mode='r') as file:
    reader = csv.DictReader(file)
    iterdict = iter(reader)
    next(iterdict)
    for row in reader:
        if "geração" in row[None][4]:
            deputado = row[None][1]
            if deputado not in counter:
                counter[deputado] = 0
            counter[deputado] += 1
        if "energia" in row[None][4]:
            deputado = row[None][1]
            if deputado not in counter:
                counter[deputado] = 0
            counter[deputado] += 1
        if "solar" in row[None][4]:
            deputado = row[None][1]
            if deputado not in counter:
                counter[deputado] = 0
            counter[deputado] += 1
        if "fotovoltaica" in row[None][4]:
            deputado = row[None][1]
            if deputado not in counter:
                counter[deputado] = 0
            counter[deputado] += 1

print(counter)
print(len(counter))


a_file = open("resultado-levantamento.csv", "w")
writer = csv.writer(a_file)
for key, value in counter.items():
    writer.writerow([key, value])

a_file.close()




