def anagram(a, b):
    a = a.lower()
    b = b.lower()
    c = list(a)
    d = list(b)
    c.sort()
    d.sort()
    # Można prościej:
    return c == d


x = input("podaj ciag znakow ")
y = input("podaj ciag znakow ")
anagramy = anagram(x, y)

if anagramy:
    print("Słowa:", x, "i", y, "to anagramy (True)")
else:
    print("Słowa:", x, "i", y, "to nie anagramy (False)")