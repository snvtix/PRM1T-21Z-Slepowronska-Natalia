def anagram(a, b):
    a = a.lower()
    b = b.lower()
    c = list(a)
    d = list(b)
    c.sort()
    d.sort()
    if c == d:
        return True
    else:
        return False


x = input("podaj ciag znakow ")
y = input("podaj ciag znakow ")
anagramy = anagram(x, y)

if anagramy:
    print("Słowa:", x, "i", y, "to anagramy (True)")
else:
    print("Słowa:", x, "i", y, "to nie anagramy (False)")