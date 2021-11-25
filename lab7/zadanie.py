import os.path

with open("rozprawa.txt", "r+") as file:

    r = file.read()
    s = {}

    z = r.lower()
    w = r.split()

    for i in w:
        if len(i) > 2:
            if i.isalpha():
                if i == i[::-1]:
                    str = (" " + i + " ")
                    s[i] = z.count(str)
    set(s)

    while True:
        a = input("podaj nazwe pliku (z rozszerzeniem): ")
        if os.path.isfile(a):
            break
        else:
            print("nie znaleziono takiego pliku")

    while True:
        b = input("podaj polecenie: ")
        if b == "koniec":
            break
        elif b == "palindromy":
            print("PALINDROM: WARTOSC")
            print(s)
        elif len(b) == 1:
                print("liczba wystapienia znaku ", b, ": ", r.count(b))
        elif len(b) > 1:
            b = b.lower()
            str = (" " + b + " ")
            print("liczba wystapienia znakow", b, ": ", z.count(str))





