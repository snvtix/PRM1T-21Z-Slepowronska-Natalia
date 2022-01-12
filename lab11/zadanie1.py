import os.path # import os, bo z tej biblioteki są wykorzystywane rózne funkcje, nie tylko path

def file_sizes(path):
    d = {}
    if os.path.isdir(path):
        l = os.listdir(path)
        for i in l:
            if os.path.isfile(f"{path}/{i}"):
                enl = os.path.splitext(f"{path}/{i}") # tu powinno być: enl = os.path.splitext(i)
                print(enl) # niepotrzebne
                enll = enl[1] # moze byc, ale tez niepotrzebne
                size = os.path.getsize(f"{path}/{i}")
                d.get(enl) # niepotrzebne
                if enl in d.keys():
                    d[enll] = v
                    v = v + size
                    d[enll] = v
                else:
                    d[enll] = size
        return d
    else:
        assert os.path.isdir(path), "nie jest to katalog"

if __name__=='__main__':
    a = str(input()) # tutaj nie miał być input() tylko podanie jako argumentu do funkcji ściezki do katalogu: 'books/poe'
    print(file_sizes(a))

# brak try except w kodzie testującym
# uzyskano zły wynik:
'''
('books/poe/beczka-amontillada', '.txt')
('books/poe/czarny-kot', '.mobi')
('books/poe/studnia-i-wahadlo', '.pdf')
('books/poe/zaglada-domu-usherow', '.txt')
'''
# mozliwe poprawne rozwiazanie:
'''
import os

def file_sizes(file_path):
    d = {}
    if os.path.isdir(file_path):
        l = os.listdir(file_path)
        for i in l:
            if os.path.isfile(f"{file_path}/{i}"):
                enl = os.path.splitext(i)
                size = os.path.getsize(f"{file_path}/{i}")
                if enl[1] in d:
                    d[enl[1]] += size
                else:
                    d[enl[1]] = size
        return d
    else:
        assert os.path.isdir(file_path)


if __name__ == "__main__":
    try:
        print(file_sizes('books/poe')) # test działania programu
        print(file_sizes('book')) # test obsługi wyjątku
    except AssertionError:
        print('nie jest to katalog')
'''
