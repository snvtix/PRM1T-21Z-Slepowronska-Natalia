slownik1 = {
    "Igor:": 24,
    "Rafał": 21,
    "Karol": 25,
    "Adam": 35,
    "Marek": 18,
    "Piotr": 42,
}
print(slownik1)

slownik1['Tomek'] = 57
print(slownik1)

slownik2 = {
    "Anna": 56,
    "Katarzyna": 28,
    "Dorota": 17,
    "Marta": 16,
}

slownik1.update(slownik2)
print(slownik1)

print("dlugosc slownika: ", len(slownik1))
print(slownik1.items())
print(slownik1.keys())
print(slownik1.values())

slownik1['Piotr'] = 48
slownik1['Dorota'] += 2
del slownik1["Marta"]
print(slownik1)

for i in slownik1:
    # Wyrażenie "20 < slownik1[i] < 50" zwraca wartość True lub False, więc można jeszcze prościej:
    slownik1[i] = 20 < slownik1[i] < 50

print(slownik1.items())


