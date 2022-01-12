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
        suma = suma + yprim[j]*yprim[j] # "TypeError: list indices must be integers or slices, not float", poza tym to mialo byc w kodzie testujacym
        # j to kolejne wartosci z listy yprim, nie indeksy, jeśli chcemy mieć dostęp do indeksów, nalezy wykorzystać enumerate():
        '''
        for idx, val in enumerate(yprim):
            uma = suma + yprim[idx]*yprim[idx]
        '''
        # ale wystarczy zrobić:
        '''
        for j in yprim:
            suma = suma + j*j
        '''
    print(suma)
    wynik = math.sqrt(suma) # to mialo byc w kodzie testujacym
    print(wynik)

    # funkcja nic nie zwraca (nie ma return), a powinna zwracac listę yprim

if __name__=="__main__":

    x = [1,2,3,4]
    y = [0.5,1,2,3.5] 

    print(rn(x,y))

# poprawne rozwiązanie:
'''
import math

def rn(x,y):

    yprim = []

    assert len(x) == len(y)

    for i in range(0, len(x)-1):
        yprim.append((y[i+1]-y[i])/(x[i+1]-x[i]))
    
    return yprim


if __name__=="__main__":

    x = [1,2,3,4]
    y = [0.5,1,2,3.5] 

    try:
        yprim = rn(x,y)

        suma = 0
        for j in yprim:
            suma = suma + j*j 

        wynik = math.sqrt(suma)
        print(wynik)
        
    except AssertionError:
        print('maja rozna dlugosc')
'''
