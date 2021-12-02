import json

with open("zadanie1.json", "r+") as file:
    s = json.load(file)
    print(s)

    bp1 = s["1bok_prostokąta"]
    bp2 = s["2bok_prostokąta"]
    k = s["promień_koła"]
    bt1 = s["1bok_trójkąta"]
    bt2 = s["2bok_trójkąta"]
    bt3 = s["3bok_trójkąta"]