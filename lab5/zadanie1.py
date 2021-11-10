list = [] # nie nazywamy listy "list", ponieważ list() to wbudowana funkcja w pythonie, a nie nazywa się zbiorów danych/zmiennych i funkcji tak samo

with open("data.txt", "r+", encoding="utf-8") as file:
    i = 1 # niepotrzebne, można usunąć
    for i in file:
        a = i # niepotrzebna linijka, to tylko zmiana nazwy zmiennej, można było od razu napisać "for a in file" i byłoby to samo
        a = int(a)
        a = chr(a) 
        list.append(a) # ok, można też zapisać w jednej linijce: list.append(chr(int(a)))

with open("wpisz.txt", "w") as xx:
    i = 1 # niepotrzebne, można usunąć
    for i in list:
        xx.write(i)


