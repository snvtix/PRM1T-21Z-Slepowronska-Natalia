import os.path
def file_sizes(path):
    d = {}
    if os.path.isdir(path):
        l = os.listdir(path)
        for i in l:
            if os.path.isfile(f"{path}/{i}"):
                enl = os.path.splitext(f"{path}/{i}")
                print(enl)
                enll = enl[1]
                size = os.path.getsize(f"{path}/{i}")
                d.get(enl)
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
    a = str(input())
    print(file_sizes(a))
