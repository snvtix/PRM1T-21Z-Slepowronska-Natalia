import os.path
import json

class SuperMarket:

    def __init__(self):
        self.nazwa = "Delikatesy"
        self.slownik = {}

    def add_data(self, sciezka):
        if os.path.isfile(sciezka):
            with open(sciezka, "r+") as file:
                data = json.load(file)
                for i in data.keys():
                    self.slownik[i] = data[i]
                return self.slownik
        else:
            print("plik nie znajduje sie w katalogu")

    def sale(self, produkt, przecena):
        if produkt in self.slownik.keys():
            if 0 < przecena < 1:
                self.slownik[produkt] = self.slownik[produkt] - (self.slownik[produkt]*przecena)
                return self.slownik
            else:
                print("przecena nie istnieje")
        else:
            print("produkt nie znajduje sie w sklepie")

class ConvenienceStore(SuperMarket):

    def percent_sale(self, produkt, przecena):
        super(ConvenienceStore, self).sale(produkt, przecena)
        print(self.slownik)
        print(f"cena produktu {produkt} zmienila sie o {przecena*100}% i wynosi teraz {self.slownik[produkt]} groszy")



if __name__ == "__main__":
    obiekt = SuperMarket()
    obiekt2 = ConvenienceStore()
    a = "zadanie2.json"
    print(obiekt.add_data(a))
    b = "pomidor"
    c = 0.5
    print(obiekt.sale(b, c))
    obiekt2.add_data(a)
    obiekt2.percent_sale(b, c)
    if isinstance(obiekt2, SuperMarket):
        print("ConvenienceStore jest obiektem klasy SuperMarket")
    else:
        print("ConvenienceStore nie jest obiektem klasy SuperMarket")