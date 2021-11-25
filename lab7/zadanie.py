import os.path

with open("rozprawa.txt", "r+") as file: #skoro nazwa pliku podana przez użytkownika została zdefiniowana jako 'a' to tutaj zamiast "rozprawa.txt" powinno być 'a'
    #program powinien działać dla każdego pliku jeśli istnieje w katalogu, nie tylko dla rozprawa.txt (co opisano ww komentarzu)
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
        elif len(b) > 1: #w tej pęli są zliczane również inne znaki niż litery, a w poleceniu było napisane: 'ciągi znaków zawierające wyłącznie litery', a np dla polecenia '**' otrzymujemy wynik 0, co oznacza, że wystąpienie tego ciągu zostało zliczone i liczba tych wystąpień w tekście równa jest 0
            b = b.lower()
            str = (" " + b + " ") #tutaj wyszukuje ciąg znaków jedynie jeśli jest oddzielnym słowem, a chodziło o wyszukanie danych ciągów znaków nawet jeśli są częścią dłuższego słowa
            print("liczba wystapienia znakow", b, ": ", z.count(str))





