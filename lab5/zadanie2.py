i = 1 # niepotrzebne, można usunąć
s = {}

while True:
    print("podaj imie")
    imie = input()
    if not imie:
        break
    else:
        print("podaj haslo")
        haslo = input()
        s[imie] = haslo
print(s)

with open("zad2.txt", "w") as aaa:
    for i in s:
        aaa.write(i)
        aaa.write(",")
        aaa.write(s[i])
        aaa.write("\n") #ok, można też zapisać w jednej linijce: aaa.write(f'{i},{s[i]}\n')
