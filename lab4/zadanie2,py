lista = []
print("podaj n")
n = input()
n = int(n)

import random
for i in range (n - 1):
    lista.append(random.randrange(100))
print(lista)

for i in range(n - 1):
    for j in range(n - 2):
        if lista[j] > lista[j + 1]:
            m = lista[j]
            lista[j] = lista[j +1]
            lista[j + 1] = m

print(lista)

#zadanie3

m = 1
for i in range(n - 1):
    if lista[i] % 2 == 0:
        print("liczba", lista[i], "jest parzysta")
    else:
        print("liczba", lista[i], "jest nieparzysta")
    m += 1

print("ilosc liczb sprawdzonych", m)