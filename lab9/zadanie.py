import os.path
import json

class Ksiazka_telefoniczna:

    def __init__(self):
        self. tytul = "<ksiazka telefoniczna>"
        self.slownik = {}

    def add_record(self, imie, numer):
         if numer.isdigit():
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

    def print_json(self, son):
        with open(son, "r+") as file:
            json.dump(self.slownik, file)

    def read_json(self, son):
        with open(son, "r+") as file:
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
