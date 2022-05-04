a = input("Podaj zmienna a: ")
b = input("Podaj zmienna b: ")

a = int(a)
b = int(b)

c = b % a
c = int(c)
if c == 0:
    c = a


def nww(a, b, c):
    return a*b/c

e = max(a, b)
f = nww(a, b, c)

for i in range(e, 101):
    if i == f:
        print("Najmniejsza wspolna wielokrotnosc: ", i)
        break
else:
    print("Najmniejsza wspolna wielokrotnosc nie miesci sie w zakresie")







