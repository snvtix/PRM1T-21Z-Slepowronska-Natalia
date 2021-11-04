list = []

with open("data.txt", "r+", encoding="utf-8") as file:
    i = 1
    for i in file:
        a = i
        a = int(a)
        a = chr(a)
        list.append(a)

with open("wpisz.txt", "w") as xx:
    i = 1
    for i in list:
        xx.write(i)


