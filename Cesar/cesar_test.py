import unittest
from Chiffrement.Cesar.cesar import *


class TestCesar(unittest.TestCase):

    def test_cesar_shifting(self):
        """Test case pour la méthode très naïve.'"""
        test_letter = ['a','b','c','x','y','z','A','B','C','X','Y','Z']
        test_key = [1, 2, 3, 4, 5, -1, 1, 2, 3, 4, 5, -1]
        expected_results = ['b','d','f', 'b', 'd', 'y', 'B','D','F', 'B', 'D', 'Y']
        for i, prime in enumerate(test_letter):
            assert cesar_shifting(test_letter[i], test_key[i]) == expected_results[i]

    def test_cesar(self):
        """Test case pour la méthode très naïve.'"""
        test_message = "Deutschland Uber Allen"
        test_key = 7
        expected_results = "Klbazjoshuk Bily Hsslu"
        assert cesar(test_message, test_key) == expected_results
    def test_build_cesar_key(self):
        """Test case pour la méthode très naïve.'"""
        test_crypto = cesar("Exige beaucoup de toi-même et attends peu des autres. Ainsi beaucoup d'ennuis te seront épargnés.", 7)
        expected_results = 7
        assert build_cesar_key(test_crypto) == expected_results
    # TODO : Problème avec accents
    def test_crypto_cesar(self):
        """Test case pour la méthode très naïve.'"""
        expected_results = "Exige beaucoup de toi-même et attends peu des autres. Ainsi beaucoup d'ennuis te seront épargnés."
        test_crypto = cesar("Exige beaucoup de toi-même et attends peu des autres. Ainsi beaucoup d'ennuis te seront épargnés.", 7)
        assert crypto_cesar(test_crypto) == expected_results


if __name__ == "__main__":
    unittest.main()
