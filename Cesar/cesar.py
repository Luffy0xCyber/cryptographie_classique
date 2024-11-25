def cesar_shifting(letter, key):
    """
    Cette fonction effectue un décalage dans l'alphabet d'une lettre
    param letter: la lettre à décaler
    param key: la valeur de décalage
    return: la lettre décalée
    """
    # Si la lettre est majuscule
    if 'A' <= letter <= 'Z':
        return chr((ord(letter) - ord('A') + key) % 26 + ord('A'))
    # Si la lettre est minuscule
    elif 'a' <= letter <= 'z':
        return chr((ord(letter) - ord('a') + key) % 26 + ord('a'))
    # Si c pas une lettre
    else:
        return letter


def cesar(message, key):
    """
    Cette fonction effectue un décalage dans l'alphabet de toutes les lettres du message
    Elle utilise la fonction cesar_shifting.
    param message: message dont les lettres doivent être décalées
    param key: la valeur du décalage
    return: message (de)chiffré par le décalage
    """
    resultat = ""
    for lettre in message:
        resultat += cesar_shifting(lettre,key)
    return resultat

def build_cesar_key(cryptogramme):
    """
    Cette fonction calcul la valeur du décalage sur base du cryptogramme.
    Elle identifie la lettre la plus fréquente du cryptogramme et l'associe à la lettre 'e'.
    La différence entre les deux lettres permet d'obtenir la clé de chiffrement
    param cryptogramme: le cryptogramme à décrypter
    return: la valeur du décalage
    """
    # Initier un dict pour enregistre cheque lettre et sa fréquence
    lettre_et_frequence = {}
    for lettre in cryptogramme.lower():
        # S'assurer que la lettre est bien alphanumérique et pas des caractères cm '-'
        if  'a' <= lettre <= 'z':
            if lettre in lettre_et_frequence:
                lettre_et_frequence[lettre] +=1
            else:
                lettre_et_frequence[lettre] = 1
    # Avoir la lettre la plus fréquente
    lettre_plus_frequente = max(lettre_et_frequence, key=lettre_et_frequence.get)
    # Calculer la différence entre la lettre la plus fréquente et la lettre e !
    decalage = (ord(lettre_plus_frequente) - ord('e') )% 26
    return decalage




def crypto_cesar(cryptogramme):
    """
    Cette fonction réalise une cryptanalyse d'un message chiffré par la méthode de César.
    Elle utilise la fonction build_cesar_key pour déterminer la clé de chiffrement.
    Le décryptage est effectué à l'aide de la méthode cesar
    param cryptogramme: cryptogramme à cryptanalyser
    return: message en clair
    """
    # D'abord il faut trouver la clé de chiffrement
    cle = build_cesar_key(cryptogramme)
    # décrypter :
    message_clair = cesar(cryptogramme, -cle)
    return message_clair



def main():
    with open("cryptogramme_cesar.txt", "r",encoding='utf-8' ) as file:
        cryptogramme = file.read()
        print(crypto_cesar(cryptogramme))

if __name__ == "__main__":
    main()