class Fraction:
    fraction_type = "ordinal"

    def __init__(self):
        self.l = 1
        self.m = 1

    def listing(self):
        print(f"{self.l}/{self.m}")

    def __mul__(self, other):
        return (self.l*other)/self.m

if __name__ == "__main__":
    obiekt = Fraction()
    obiekt2 = Fraction()
    obiekt.l = 1
    obiekt.m = 2
    a = input()
    a = int(a)
    obiekt.listing()
    print(obiekt.__mul__(a))
    print(obiekt.fraction_type)
    print(obiekt2.fraction_type)
    Fraction.fraction_type = "not ordinal"
    print(obiekt.fraction_type)
    print(obiekt2.fraction_type)



