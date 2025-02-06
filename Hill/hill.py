import random

def encode_hill(message, key):
    """
    Cette fonction chiffre un message selon la technique de Hill
    param message: message à chiffrer
    param key: matrice de chiffrement 2x2
    return: cryptogramme
    """
    # la liste position va stocker les positions de chaque lettre du message ex. a = 0
    position = []
    cryptogramme = ''
    # La liste d'alphabets va nous permettre de trouver les positions de chaque lettre
    liste_alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                       'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # La 1ère étape est de trouver les positions des lettres du message à chiffrer
    for lettre in message :
        lettre = lettre.lower()
        if lettre in liste_alphabets:
            position.append(liste_alphabets.index(lettre))
    # En hill, on fonctionne avec une matrice de 2*2 ; le message doit être
    # divisé en bloc de 2 lettres... Donc j'ai choisi d'ajouter une lettre.
    # Ici, c'est le z (j l'ai trouvé en faisant du test random sur plusieurs lettres)
    if len(position) %2 !=0 :
        position.append(liste_alphabets.index('z'))
    # La 2ème étape est de faire cette multiplication matricielle
    # dans cette boucle, on va avancer 2 par 2 puisqu'en hill ça fonctionne avec une paire de nombres
    for i in range(0, len(position), 2):
        res_ligne1 = ((key[0][0] * position[i]) + (key[0][1] * position[i+1])) %26
        res_ligne2 = ((key[1][0] * position[i]) + (key[1][1] * position[i+1])) %26
        cryptogramme += liste_alphabets[res_ligne1] + liste_alphabets[res_ligne2]
    return cryptogramme


def inverse_modulo(number, p):
    """
    Cette fonction implémente l'algorithme d'euclide étendu

    :param number:   nombre à inverser
    :param p : c le modulo
    :return (pgcd, u, v) u*number+v*p = pgcd relation de bézout
    """
    # a c le nombre à inverse, b représente le modulo
    a, b = number, p
    # u et v c pr la relation de Bézout. Les coefficients permettent de reconstruire le PGCD !
    u1, u2 = 1, 0
    v1, v2 = 0, 1
    while b!= 0 :
        quotient = a // b
        # Mise à jour des variables
        a, b = b, a % b

        # Mettre à jour les coefficients
        u1, u2 = u2, u1 - quotient * u2
        v1, v2 = v2, v1 - quotient * v2

    # dans le cas où il n'y a pas d'inverse
    if a != 1:
        return None
    # Sinon on retourne l'inverse modulo!
    return u1 % p


def gcd_euclid(number1, number2):
    """
    Cette fonction implémente l'algorithme d'euclide tel que décrit
    ![ici](https://upload.wikimedia.org/wikipedia/commons/3/3a/Algorithme_PGCD.svg)
    :param number1: premier entier dont il faut calculer le pgcd
    :param number2: second entier dont il faut calculer le pgcd
    :return: le pgcd des deux entiers donnés en argument
    """
    # la boucle signifie qu'on continue tant que number2 est différent de 0
    # car comme c'est montré dans le lien(cf.docstring ci-dessus), on continue de boucler
    # jusqu'à ce que le reste vaut 0!
    while number2 != 0:
        #number1 prend la valeur de b
        #number2 prend la valeur du reste qui est une opération modulaire à faire
        number1, number2 = number2, number1 % number2
    # on retourne le number1 car qd number2 vaut 0 alors le number1 contient le pgcd !
    return number1



def inverse(key):
    """
    Cette fonction calcul la clé de déchiffrement sur base de la clé.
    Pour ce faire, elle calcul la matrice inverse dans l'esapce modulo 26.
    param key: matrice de chiffrement de Hill
    return: matrice de déchiffrement de Hill
    """
    # matrice 2*2 ; On l'initie une matrice !
    matrice = [[0,0],[0,0]]
    # calculer du déterminant (formule cf. cours)
    determinant = (key[0][0] * key[1][1]) - (key[1][0] * key[0][1]) % 26
    # Formule pour trouver l'inverse :
    inverse_determinant = inverse_modulo(determinant, 26)
    # Calcul de la matrice inverse, j'ai utilisé la formule vue en cours
    matrice[0][0] = (inverse_determinant * key[1][1])%26
    matrice[0][1] = (inverse_determinant * (- key[0][1]))%26
    matrice[1][0] = (inverse_determinant * (- key[1][0]))%26
    matrice[1][1] = (inverse_determinant * key[0][0])%26
    return matrice



def build_key_hill():
    """
    Cette fonction construit une matrice inversible modulo 26 qui peut servir de clé pour le chiffrement de Hill.
    return: matrice inversible dans l'espace modulo 26
    """
    # Générer des matrices, mais à condition : Il faut respecter le critère d'inversibilité modulo 26 !
    # matrice 2*2
    # Génération de la matrice aléatoirement
    while True:
        a = random.randint(0, 25)
        b = random.randint(0, 25)
        c = random.randint(0, 25)
        d = random.randint(0, 25)
        matrice = [[a,b], [c,d]]
        # Calculer le determinant
        determinant = (matrice[0][0]*matrice[1][1]) - (matrice[1][0]*matrice[0][1]) % 26
        if gcd_euclid(determinant, 26) == 1:
            # ça retourne une matrice inversible !
            return matrice


def decode_hill(cryptogramme, key):
    """
    Cette fonction déchiffre un message selon la technique de Hill.
    Elle calcul la clé de déchiffrement et puis l'utilisé pour déchiffrer le cryptogramme.
    param cryptogramme: cryptogramme à déchiffrer
    param key: clé de chiffrement
    return: message en clair
    """
    inverse_matrice = inverse(key)
    return encode_hill(cryptogramme, inverse_matrice)


def cryptanalyse_hill(cryptogramme, mot):
    """
    Cette fonction effectue une cryptanalyse par force brute d'un cryptogramme chiffrer selon Hill.
    Afin de choisir le message décrypté, elle utilise le mot probable.
    param cryptogramme: cryptogramme à cryptanalyser
    param mot: le mot que le message en clair contient
    return: message en clair.
    """
    # On va tester toutes les combinaisons possibles de clé pour trouver le message clair
    for a in range(26):
        for b in range(26):
            for c in range(26):
                for d in range(26):
                    key = [[a,b], [c,d]]
                    det = (a*d - b*c)%26
                    if gcd_euclid(det,26) == 1:
                        message_clair = decode_hill(cryptogramme, key)
                        if mot in message_clair:
                             return message_clair
    return None

# De base, j'avais utilisé une boucle infinie pour trouver le message clair(cf. ci-dessous). Sauf que
# ça ne marchait pas toujours. J'ai demandé à Monsieur ludwig et il m'a dit que le mieux c'était de
# faire une boucle imbriquée pour tester toutes les combinaisons possibles de clé.
# while True:
#     matrice = build_key_hill()
#     message_clair = decode_hill(cryptogramme, matrice)
#     if mot in message_clair:
#         return message_clair


def main():
    """
    Fonction principale
    """
    with open("cryptogramme_hill.txt", "r",encoding='utf-8' ) as file:
        cryptogramme = file.read()
        print(cryptanalyse_hill(cryptogramme, "huitieme")) # On sait que le message contient le mot "huitieme", c'était dans la consigne.

if __name__ == "__main__":
    main()
