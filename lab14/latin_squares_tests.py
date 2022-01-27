import unittest
import latin_squares as l

class LatinSquareTests(unittest.TestCase):
    def test_is_latin(self):
        kl=[[1,2,3,4],
            [2,3,4,1],
            [3,4,1,2],
            [4,1,2,3]]
        knl=[[3,2,1,4],
            [1,2,4,3],
            [2,4,3,1],
            [4,3,2,2]]
        self.assertEqual(l.is_latin(kl), True)
        self.assertEqual(l.is_latin(knl), False)

    def test_latin_square(self):
        k=l.latin_square(5)
        if len(k)==5:
            return True
        elif len(k[0])==5:
            return True
        else:
            return False
        self.assertEqual(l.is_latin(k), True)

