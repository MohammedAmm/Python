#  name of assign ment
import unittest
from assign1 import vowelsRemove
from assign1 import multiRemoveList
from assign2 import locator
from assign3 import multiplication
from assign4 import calcArea
from assign5 import dictionary
class TestAssignment(unittest.TestCase):
    def test_vowelsRemove(self):
        self.assertEqual(vowelsRemove("Mobile"),"Mbl")
    def test_multiRemoveList(self):
        self.assertEqual(multiRemoveList(['ahmooooed','mohamed']),['hmd','mhmd'])
    def test_locator(self):
        self.assertEqual(locator("This is javaScript","i"),[2, 5, 15])
    def test_multiplication(self):
        self.assertEqual(multiplication(3),[[1], [2, 4], [3, 6, 9]])
    def test_calcArea(self):
        self.assertEqual(calcArea("r",3),9)
    def test_dictionary(self):
        self.assertEqual(dictionary(["ahmed","fatma","Ibrahim","ammar","Islam"]),{'a': ['ahmed', 'ammar'], 'f': ['fatma'], 'I': ['Ibrahim', 'Islam']})
if __name__ == '__main__':
    unittest.main()