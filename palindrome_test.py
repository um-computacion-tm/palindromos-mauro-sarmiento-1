import unittest
from palindrome import Palindrome

class TestPalindrome(unittest.TestCase):
    def testPalindromeNeuquenI(self):
        pal = Palindrome()
        result = pal.palindrome_true_or_false('neuquen')
        self.assertEqual(result, True)
    def testPalindromeNeuquenII(self):
        pal = Palindrome()
        result = pal.palindrome_true_or_false('Neuquén')
        self.assertEqual(result, True)
    def testPalindrome_I(self):
        pal = Palindrome()
        result = pal.palindrome_true_or_false('Atar a la rata')
        self.assertEqual(result, True)
    def testPalindrome_II(self):
        pal = Palindrome()
        result = pal.palindrome_true_or_false('Acaso hubo búhos acá')
        self.assertEqual(result, True)
    def testPalindrome_III(self):
        pal = Palindrome()
        result = pal.palindrome_true_or_false('Somos o no somos')
        self.assertEqual(result, True)
    def testPalindrome_IV(self):
        pal = Palindrome()
        result = pal.palindrome_true_or_false('Son robos o sobornos')
        self.assertEqual(result, True)
    def testPalindrome_V(self):
        pal = Palindrome()
        result = pal.palindrome_true_or_false('A mamá, Roma le aviva el amor a papá, y a papá, Roma le aviva el amor a mamá')
        self.assertEqual(result, True)
    def testPalindrome_VI(self):
        pal = Palindrome()
        result = pal.palindrome_true_or_false('A ti no, bonita')
        self.assertEqual(result, True)
    def testPalindrome_VII(self):
        pal = Palindrome()
        result = pal.palindrome_true_or_false('Adán y raza; azar y nada')
        self.assertEqual(result, True)
    def testPalindrome_VIII(self):
        pal = Palindrome()
        result = pal.palindrome_true_or_false('Todos los caminos llevan a Roma')
        self.assertEqual(result, False)
    def testPalindrome_IX(self):
        pal = Palindrome()
        result = pal.palindrome_true_or_false(
            'Adivina ya te opina, ya ni miles origina, ya ni cetro me domina, ya ni monarcas, a repaso ni mulato carreta, acaso nicotina, ya ni cita vecino, anima cocina, pedazo gallina, cedazo terso nos retoza de canilla goza, de pánico camina, ónice vaticina, ya ni tocino saca, a terracota luminosa pera, sacra nómina y ánimo de mortecina, ya ni giros elimina, ya ni poeta, ya ni vida'
                                            )
        self.assertEqual(result, True)
    def testPalindrome_X(self):
        pal = Palindrome()
        result = pal.palindrome_true_or_false('Dorime ame no dore, ameno dorime')
        self.assertEqual(result, False)
    def testPalindrome_XI(self):
        pal = Palindrome()
        result = pal.palindrome_true_or_false('Chippin in')
        self.assertEqual(result, False)
    def testPalindrome_XII(self):
        pal = Palindrome()
        result = pal.palindrome_true_or_false('Keanu Reeves')
        self.assertEqual(result, False)
    def testPalindrome_XIII(self):
        pal = Palindrome()
        result = pal.palindrome_true_or_false('As a child, you would wait and watch from far away')
        self.assertEqual(result, False)
    


if __name__ == '__main__':
    unittest.main()