import os.path
import json


class Ksiazka_telefoniczna:
    def __init__(self):
        self.tytul = "<ksiazka telefoniczna>"
        self.slownik = {}

    def add_record(self, imie, numer):
        if numer.isdigit(): #'int' object has no attribute 'isdigit', powinno być: str(numer)
            if imie in self.slownik.values():
                print("osoba jest w ksiazce telefonicznej")
            else:
                self.slownik[imie] = numer
        else:
            print("to nie numer")

    def print_all(self):
        print(self.tytul)
        for i in self.slownik:
            print("dane", i, ":", "numer", self.slownik[i])

    def print_json(self, son): #write_json, tak miała nazywać się ta funkcja
        #self.son = son --> tego brakuje
        with open(son, "r+") as file: #jeżeli plik nie istnieje otrzymujemy błąd 'No such file or directory' co oznacza, że ta funkcja nie tworzy nowego pliku, tylko szuka go w obecnym katalogu, a powinna tworzyć plik i zapisywać do niego wynik, powinno być open(son, "w")
            json.dump(self.slownik, file)

    def read_json(self, son):
        with open(son, "r+") as file: #FileNotFoundError: No such file or directory; zła kolejność: funkcja powinna najpierw sprawdzać, czy plik istnieje, a potem próbować go otworzyć lub wyświetlać komunika
            if os.path.isfile(son):
                slownik = json.load(file)
                for j in slownik:
                    self.add_record(j, slownik[j])
            else:
                print("plik nie istnieje")


if __name__ == "__main__":
    obiekt = Ksiazka_telefoniczna()

    i = 0
    a = input("podaj liczbe osob: ")
    a = int(a)
    while i < a:
        imie = input("podaj imie: ")
        numer = input("podaj numer: ")
        obiekt.add_record(imie, numer)
        i = i + 1

    obiekt.print_all()
    son = input("podaj nazwe pliku: ")
    obiekt.print_json(son)
    soon = input("podaj nazwe pliku: ")
    obiekt.read_json(soon)
    obiekt.print_all()

#funkja write_json() mogłaby wyglądać tak:
'''
def write_json(self, son):
    self.son = son
    with open(self.son, "w") as file:
        json.dump(self.slownik, file)
'''
#a jej wywołanie:
'''
obiekt.write_json('zadanie.json') 
'''
#funkcja read_json() mogłaby wyglądać tak:
'''
def read_json(self, son):
    if os.path.isfile(son):
        with open(son, "r+") as file:
            slownik = json.load(file)
            for j in slownik:
                self.add_record(j, slownik[j])
    else:
        print("plik nie istnieje")
'''
#wywołanie funkcja read_json():
'''
obiekt.read_json('nowy.json') # plik 'nowy.json' to plik swotrzony ręcznie przechowujący nowy słównik, który zostaje dodany do istniejącego słownika
'''
#brak podpunktu f); metody '__add__(self, other); mogłaby np. wyglądać tak:
'''
 def __add__(self, other):
        new = Ksiazka_telefoniczna()
        for record in self.slownik:
            new.add_record(record, self.slownik[record])
        for record in other.slownik:
            new.add_record(record, other.slownik[record])
        return new
'''
#testowanie 'if __name__ == "__main__":' jest ok, ale wygodniej byłoby gdyby nie było input() tylko podanie argumentów przy wywołaniu funkcji:
'''
if __name__ == "__main__:
    obiekt = Ksiazka_telefoniczna()

    obiekt.add_record("Ania", 1111)
    obiekt.add_record("Ola", 2222)
    obiekt.add_record("Ania", 3333) # test czy dodaje rekord, jeśli dane imię jest już w słowniku
    obiekt.add_record("Ela", '4444cc') # test czy liczba.isdigit() działa
    obiekt.print_all()

    obiekt.write_json('ksiazka1.json') # ksiazka1.json -> plik, do którego zostaje zapisany słównik
    obiekt.read_json('nowy.json') # plik 'nowy.json' to plik swotrzony ręcznie przechowujący nowy słównik, który zostaje dodany do istniejącego słownika (test)
    obiekt.print_all()
'''
