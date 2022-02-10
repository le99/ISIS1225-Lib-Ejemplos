import csv


archivo = './Data/ejemplo.csv'
reader = csv.DictReader(open(archivo, encoding='utf-8'), delimiter=",")
for e in reader:
    print(e)    # e es un diccionario con una linea del archivo


print()


reader = csv.reader(open(archivo, encoding='utf-8'), delimiter=",")
for e in reader:
    print(e)    # e es un tupla



# Doc:
# https://docs.python.org/3/library/csv.html
#https://docs.python.org/3/library/csv.html