import json
import math

def ot(a, b, c):
    ot = a + b + c
    return ot

def ok(a):
    ok = 2 * a * math.pi
    return ok

def opr(a, b):
    opr = a * 2 + b * 2
    return opr

def pt(a, b ,c):
    pt = (1 / 4) * math.sqrt((a + b + c) * (a + b - c) * (a - b + c) * (b + c - a))
    return pt

def pk(k):
    pk = k * k * math.pi
    return pk

def ppr(a, b):
    ppr = a * b
    return ppr

with open("zadanie1.json", "r+") as file:
    s = json.load(file)
    print(s)

    bp1 = s["1bok_prostokąta"]
    bp2 = s["2bok_prostokąta"]
    k = s["promień_koła"]
    bt1 = s["1bok_trójkąta"]
    bt2 = s["2bok_trójkąta"]
    bt3 = s["3bok_trójkąta"]

    while True:
        a = input("podaj polecenie (o - obwod, p - pole) ")
        if a == "o":
            b = input("podaj figure (t - trojkat, k - kolo, pr - prostokat) ")
            if b == "t":
                print("boki trojkata wynosza: ", bt1, ",", bt2, ",", bt3)
                ot = ot(bt1, bt2, bt3)
                print("obwod trojkata wynosi: ", ot)
            elif b == "k":
                print("promien kola wynosi: ", k)
                ok = ok(k)
                print("obwod kola wynosi: ", ok)
            elif b == "pr":
                print("boki prostokata wynosza: ", bp1, ",", bp2)
                opr = opr(bp1, bp2)
                print("obwod prostokata wynosi: ", opr)
        elif a == "p":
            b = input("podaj figure (t - trojkat, k - kolo, pr - prostokat) ")
            if b == "t":
                print("boki trojkata wynosza: ", bt1, ",", bt2, ",", bt3)
                pt = pt(bt1, bt2, bt3)
                print("pole trojkata wynosi: ", pt)
            if b == "k":
                print("promien kola wynosi: ", k)
                pk = pk(k)
                print("pole kola wynosi: ", pk)
            elif b == "pr":
                print("boki prostokata wynosza: ", bp1, ",", bp2)
                ppr = ppr(bp1, bp2)
                print("pole prostokata wynosi: ", ppr)
        elif a == "koniec":
            break