import math
def rn(x,y):
    yprim = []
    suma = 0

    if len(x) == len(y):
        for i in range(0, len(x)-1):
             yprim.append((y[i+1]-y[i])/(x[i+1]-x[i]))
    else:
        assert "maja rozna dlugosc"

    for j in yprim:
        suma = suma + yprim[j]*yprim[j]

    print(suma)
    wynik = math.sqrt(suma)
    print(wynik)

if __name__=="__main__":

    x = [1,2,3,4]
    y = [0.5,1,2,3.5]

    print(rn(x,y))
