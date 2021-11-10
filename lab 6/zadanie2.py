with open("splot.txt", "r+", encoding = "utf-8") as file:
    a = file.read()
    ld = 0
    for i in a:
        if i.isupper():
            ld = ld + 1

    b = a.count("S")
    c = a.count("W")
    d = a.count("M")
    e = a.count("G")

    slownik = {
        "S": b/ld,
        "W": c/ld,
        "M": d/ld,
        "G": e/ld,
    }

print(slownik)
z = str(slownik)

with open("zadanie2.txt", "r+", encoding = "utf-8") as file:
    file.write(z)