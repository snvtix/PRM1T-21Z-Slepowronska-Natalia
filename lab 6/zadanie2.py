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


# wynik jest dobry, ale zadanie nie dokońca dobrze rozwiązane
# progtam sam miał wyszukiwać wielkie litery, a nie mieć je na sztywno podane
# możnaby było to zrealizować np. w następujący sposób:

'''
my_list = []

with open("splot.txt", "r+", encoding = "utf-8") as file:
    a = file.read()
    ld = 0
    for i in a:
        if i.isupper():
            ld = ld + 1
            my_list.append(i)

num_all = len(my_list)
dict_of_counts = {item:my_list.count(item) for item in my_list}

for key, val in dict_of_counts.items():
    dict_of_counts[key] = val/num_all

print(dict_of_counts)
'''
