

import os.path

with open("tekst.txt", "w", encoding = "utf-8") as file:

   file.write("Raz dwa trzy\n")
   file.write("cztery")

print(os.path.isfile("tekst.txt"))


s = "      test         \n"
print(s.strip())

z = "test, test"
print(z.split())