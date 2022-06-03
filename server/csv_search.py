import csv
import os

#  função que retorna o resultado da busca do usuário no CSV
def search(key):
    headers = None
    values = None
    filtered = []
    if key == None:
        return None
    with open(
        os.path.join(os.getcwd(), "server/relatorio.csv"), "r", encoding="ISO-8859-1"
    ) as csv:
        for index, row in enumerate(csv):
            if index == 0:
                headers = row.rstrip("\n").split(",")
            if key.upper() in str(row).upper():
                values = row.rstrip("\n").split(",")
                filtered.append(dict(zip(headers, values)))

    return filtered
