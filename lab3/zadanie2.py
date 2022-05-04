lista = []
i = 0
i = int(i)
a = input("how many words? ")
a = int(a)

while i < a:
    str = input("enter the string ")
    str.lower()
    if str == str[::-1]:
        print("string is a palindrome")
        lista = lista + [str]
    else:
        print("string is not a palindrome")
        break
    i = i + 1

sorted(lista)
print(list(set(lista)))

#odsylam zadanie 2 z labow 3 :)