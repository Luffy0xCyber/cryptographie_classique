import unittest
from vigenere import *


class TestVigenere(unittest.TestCase):

    def test_encode_vigenere(self):
        """Test case pour la méthode très naïve.'"""
        test_message = "jenemecalmepassurladifficultee"
        test_key = "ilovemath"
        expected_results = "rpbzqqctsupdvweuksiowajucnsbps"
        assert encode_vigenere(test_message,
                               test_key) == expected_results, "Bachi-bouzouk, si tu sais y faire avec César, c'est pas plus compliqué ici ;-)"

    def test_decode_vigenere(self):
        """Test case pour la méthode très naïve.'"""
        test_cryptogramme = "rpbzqqctsupdvweuksiowajucnsbps"
        test_key = "ilovemath"
        expected_results = "jenemecalmepassurladifficultee"

        assert decode_vigenere(test_cryptogramme,
                               test_key) == expected_results, "Bachi-bouzouk, si tu sais y faire avec César, c'est pas plus compliqué ici ;-)"


if __name__ == "__main__":
    unittest.main()
