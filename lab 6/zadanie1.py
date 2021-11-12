with open("splot.txt", "r+", encoding = "utf-8") as file:
    a = file.read()
    b = a.lower()
    c = "konwolucja"
    s = "splot"

    for i in b:
        d = b.count("splot ")
        e = b.count("splot.")
        f = b.count("splot:")

    k = d + e + f
    print("slowo splot wystepuje w tekscie: ", k, " razy")
    h = b.replace(s,c,k)

with open("zadanie1.txt", "r+", encoding = "utf-8") as file:
    file.write(h)


# wszystko dobrze





