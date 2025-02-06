from cryptographie_classique.Cesar.cesar import build_cesar_key
from cryptographie_classique.Hill.hill import gcd_euclid


def encode_vigenere(message, mot_code):
    """
    Cette fonction réalise le chiffrement de vigenere du message
    param message: message en chiffrer
    :type message: str
    param mot_code: clé de chiffrement
    :type mot_code: str
    return: cryptogramme
    :rtype: str
    """
    cryptogramme = ""
    # Générer ma liste d'alphabets
    alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1) ]
    # Générer position du mot_code (clé)
    position = [alphabets.index(i) for i in mot_code]
    index_code = 0
    # Boucle pour chiffrer
    for i in message:
        # Récupérer l'indice de la lettre i
        index_i = alphabets.index(i)
        # récupérer la position, j'ai utilisé le modulo pr ne pas dépasser les 26 lettres d'alphabets (éviter de déborder)
        j = position[index_code % len(position)]
        cryptogramme += alphabets[ (index_i + j)  % 26]
        index_code += 1

    return cryptogramme


def decode_vigenere(message, mot_code):
    """
     Cette fonction réalise le déchiffrement de vigenere du cryptogramme
    param message: cryptogramme à déchiffrer
    :type message: str
    param mot_code: clé de chiffrement
    :type mot_code: str
    return: message en clair
    :rtype: str
    """
    message_clair = ""
    # Générer ma liste d'alphabets
    alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    # Générer position du mot_code (clé)
    position_mot_code = [alphabets.index(i) for i in mot_code]
    index_pos = 0
    # Boucle pour déchiffrer
    for i in message:
        # Récupérer l'indice de la lettre i
        index_i = alphabets.index(i)
        # récupérer la position, j'ai utilisé le modulo pr ne pas dépasser les 26 lettres d'alphabets (éviter de déborder)
        j = position_mot_code[index_pos % len(position_mot_code)]
        message_clair += alphabets[(index_i - j) % 26]
        index_pos += 1

    return message_clair



def guess_password(cryptogramme, len_password):
    """
    Cette fonction détermine le mot de passe surt base du cryptogramme et de la longueur du mot de passe.
    Elle utilise la cryptanalyse du chiffre de césar pour déterminer chaque lettre du mot de passe.
    param cryptogramme: cryptogramme à cryptanalyser
    :type cryptogramme: str
    param len_password: longueur du mot de passe
    :type len_password: int
    return: le mot de passe deviné
    :rtype: str
    """
    # Générer les groupes de lettres, chaque groupe correspond à une lettre du mot de passe
    groupes = [cryptogramme[i::len_password] for i in range(len_password)]
    mot_de_passe = ""
    # Boucle pour déterminer chaque lettre du mot de passe
    for i in groupes:
        # Déterminer la clé de chiffrement de césar pour chaque groupe
        mot_de_passe += chr(build_cesar_key(i) + ord('a'))
    return mot_de_passe



def guess_key_lenght(histo):
    """
    Cette fonction détermine la longueur du mot de passe.
    La valeur correspond au mode de l'histogramme des pgcd des distances des répétitions.
    param histo: histogramme des pgcd
    :type histo: dict
    return: la longueur du mot de passe (le mode)
    :rtype: int
    """

    # Déterminer la valeur la plus fréquente
    valeur_frequente = max(histo.values())
    # Récupérer la clé correspondante
    for cle, valeur in histo.items():
        if valeur == valeur_frequente:
            return cle
    return 0


def build_histogram(pgcd):
    """
    Cette méthode construit l'histogramme des pgcd.
    param: les pgcd
    :type pgcd: list
    return: histogramme des pgcd
    :rtype: dict
    """

    # Initier un dictionnaire pour enregistrer les pgcd et leur fréquence
    histo = {}
    # Boucle pour construire l'histogramme
    for i in pgcd:
        # Si la clé existe déjà, j'incrémente la valeur
        if i in histo:
            histo[i] += 1
        else:
            # Sinon, j'ajoute la clé avec la valeur 1
            histo[i] = 1
    return histo


def get_pgcd(distances):
    """
    Cette fonction calcul le pgcd entre toutes les distances de répétitions
    param distances: distances de répétition
    :type distances: list
    return: les pgcd des distances 2 à 2
    :rtype: list
    """
    pgcd = []
    # Boucle pour calculer le pgcd entre toutes les distances
    for i in range(len(distances)):
        for j in range(i + 1, len(distances)):
            pgcd.append(gcd_euclid(distances[i], distances[j]))
    return pgcd



def get_distances(dictonary_len_3):
    """
    Cette fonction calcul les distances des réptitions sur base de la position des occurences.
    param dictonary_len_3: les répititions et leur position
    :type dictonary_len_3: dict
    return: les distances
    :rtype: list
    """
    distances = []
    # Boucle pour calculer les distances, j'ai utilisé 2 boucles pour comparer chaque élément avec les autres
    for key, value in dictonary_len_3.items():
        for i in range(len(value)):
            for j in range(i + 1, len(value)):
                distances.append(value[j] - value[i])
    return distances


def get_sequence_positions(cryptogramme):
    """
    Cette fonction identifie les séquences de 3 lettres qui se répetent et leur position.
    param cryptogramme: cryptogramme à cryptanalyser
    :type cryptogramme: str
    return: dictionnaire des séquences (clé=séquence de 3 lettres) et leurs positions (valeur=tableau de position)
    :rtype: dict
    """
    # Initier un dictionnaire pour enregistrer les séquences et leur position
    dictionnaire = {}
    # Boucle pour identifier les séquences de 3 lettres
    for i in range(len(cryptogramme) - 2):
        sequence = cryptogramme[i:i + 3] # récupérer la séquence de 3 lettres
        if sequence in dictionnaire:
            dictionnaire[sequence].append(i)
        else:
            dictionnaire[sequence] = [i]
    return dictionnaire


def cryptanalyse_vigenere(cryptogramme):
    """
    Cette fonction réalise une cryptanalyse d'un cryptogramme de vigenère.
    Elle détermine les séquences de répétition via get_sequence_positions
    Calcul les distances via get_distances
    Détermine les pgcd via get_pgcd et leur histogramme via build_histogram
    Devine la longueur du mot de passe via guess_key_lenght et le mot de passe lui-même via guess_password
    Le mot de passe est alors afficher et sa valeur finale demandée à l'utilisateur,
     afin de corriger les éventuelles erreurs de cryptanalyse.

    param cryptogramme: cryptogramme à cryptanalyser
    :type cryptogramme: str
    return: message en clair
    :rtype: str
    """
    # Récupérer les positions des séquences de 3 lettres
    sequence_positions = get_sequence_positions(cryptogramme)
    # Calculer les distances
    distances = get_distances(sequence_positions)
    # Calculer les pgcd
    pgcd = get_pgcd(distances)
    # Construire l'histogramme des pgcd
    histogram = build_histogram(pgcd)
    # Déterminer la longueur du mot de passe
    longueur_cle = guess_key_lenght(histogram)
    mot_de_passe_probable = guess_password(cryptogramme, longueur_cle)
    # Afficher le mot de passe probable
    print(f"Mot de passe potentiel: {mot_de_passe_probable}")
    mot_de_passe = input('Mot de passe ? ')
    return decode_vigenere(cryptogramme, mot_de_passe)


def main():
    """
    Fonction principale
    """
    with open("cryptogramme_vigenere.txt", "r", encoding='utf-8') as file:
        cryptogramme = file.read()
        print(cryptanalyse_vigenere(cryptogramme))




if __name__ == "__main__":
    main()