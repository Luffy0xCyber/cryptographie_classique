import random

def encode_hill(message, key):
    """
    Cette fonction chiffre un message selon la technique de Hill
    param message: message à chiffrer
    param key: matrice de chiffrement 2x2
    return: cryptogramme
    """

def inverse_modulo(number, p):
    """
    Cette fonction implémente l'algorithme d'euclide étendu

    :param number:   nombre à inverser
    :param p : c le modulo
    :return (pgcd, u, v) u*number+v*p = pgcd relation de bézout
    """


def gcd_euclid(number1, number2):
    """
    Cette fonction implémente l'algorithme d'euclide tel que décrit
    ![ici](https://upload.wikimedia.org/wikipedia/commons/3/3a/Algorithme_PGCD.svg)
    :param number1: premier entier dont il faut calculer le pgcd
    :param number2: second entier dont il faut calculer le pgcd
    :return: le pgcd des deux entiers donnés en argument
    """



def inverse(key):
    """
    Cette fonction calcul la clé de déchiffrement sur base de la clé.
    Pour ce faire, elle calcul la matrice inverse dans l'esapce modulo 26.
    param key: matrice de chiffrement de Hill
    return: matrice de déchiffrement de Hill
    """



def build_key_hill():
    """
    Cette fonction construit une matrice inversible modulo 26 qui peut servir de clé pour le chiffrement de Hill.
    return: matrice inversible dans l'espace modulo 26
    """



def decode_hill(cryptogramme, key):
    """
    Cette fonction déchiffre un message selon la technique de Hill.
    Elle calcul la clé de déchiffrement et puis l'utilisé pour déchiffrer le cryptogramme.
    param cryptogramme: cryptogramme à déchiffrer
    param key: clé de chiffrement
    return: message en clair
    """


def cryptanalyse_hill(cryptogramme, mot):
    """
    Cette fonction effectue une cryptanalyse par force brute d'un cryptogramme chiffrer selon Hill.
    Afin de choisir le message décrypté, elle utilise le mot probable.
    param cryptogramme: cryptogramme à cryptanalyser
    param mot: le mot que le message en clair contient
    return: message en clair.
    """
