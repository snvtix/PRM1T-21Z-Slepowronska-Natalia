import numpy

def is_latin(s):
    for i in s:
        for j in range(0, len(i) - 1):
            if i[j] == i[j + 1]:
                return False
    m=numpy.array(s)
    t=m.transpose()
    for i in t:
        for j in range(0, len(i) - 1):
            if i[j] == i[j + 1]:
                return False
    return True

def latin_square(n):
    pass


