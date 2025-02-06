import unittest
from cryptographie_classique.Hill.hill import *


class TestHill(unittest.TestCase):

    def test_encode_hill(self):
        test_message = "jesuisfoudevousdemandercela"
        test_key = [[1, 2], [3, 5]]
        expected_results = "rvgyskhhaxuncmyrcuanldvjapyv"
        assert encode_hill(test_message, test_key) == expected_results, "Fécalome, ne perds pas ton temps à chercher la définition, travail plutôt ton calcul matriciel dans un espace modulo ;-)"

    def test_inverse(self):
        test_key = [[1, 2], [3, 5]]
        expected_results = [[21, 2],[3, 25]]
        assert inverse(test_key) == expected_results, "Fécalome, ne perds pas ton temps à chercher la définition, travail plutôt ton calcul matriciel dans un espace modulo ;-)"


    def test_build_key_hill(self):
        key = build_key_hill()
        det = key[0][0]*key[1][1]-key[1][0]*key[0][1]
        assert det != 0, "Fécalome, ne perds pas ton temps à chercher la définition, travail plutôt ton calcul matriciel dans un espace modulo ;-)"
        assert gcd_euclid(det, 26) == 1, "Fécalome, ne perds pas ton temps à chercher la définition, travail plutôt ton calcul matriciel dans un espace modulo ;-)"

    def test_decode_hill(self):
        test_cryptogramme = "rvgyskhhaxuncmyrcuanldvjapyv"
        test_key = [[1, 2], [3, 5]]
        expected_results = "jesuisfoudevousdemandercelaz"
        assert decode_hill(test_cryptogramme, test_key) == expected_results, "Fécalome, ne perds pas ton temps à chercher la définition, travail plutôt ton calcul matriciel dans un espace modulo ;-)"

    def test_decode_hill2(self):
        test_cryptogramme = "rvgyskhhaxuncmyrcuanldvjapyv"
        test_key = [[1, 2], [3, 5]]
        key = inverse(test_key)
        expected_results = "jesuisfoudevousdemandercelaz"
        assert encode_hill(test_cryptogramme, key) == expected_results, "Fécalome, ne perds pas ton temps à chercher la définition, travail plutôt ton calcul matriciel dans un espace modulo ;-)"

    def test_cryptanalyse_hill(self):
        test_cryptogramme = "rvgyskhhaxuncmyrcuanldvjapyv"
        expected_results = "jesuisfoudevousdemandercelaz"
        assert cryptanalyse_hill(test_cryptogramme, "vous") == expected_results, "Fécalome, ne perds pas ton temps à chercher la définition, travail plutôt ton calcul matriciel dans un espace modulo ;-)"

if __name__ == "__main__":
    unittest.main()