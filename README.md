# Projet : Cryptographie Classique



## Introduction 

Projet regroupant des scripts Python d'exemples de chiffrements classiques (César, Vigenère, Hill). Chaque module fonctionne indépendamment 
et illustre les bases de la cryptographie par substitution ou par transformation matricielle.

## Structure 

```mermaid
graph TD

    A[cryptographie-classique] --> B[cesar]
    A --> C[vigenere]
    A --> D[hill]
    A --> E[README.md]

    B --> B1[cesar.py]
    B --> B2[cesar_test.py]
    B --> B3[cryptogramme_cesar.txt]

    C --> C1[vigenere.py]
    C --> C2[vigenere_test.py]
    C --> C3[cryptogramme_vigenere.txt]

    D --> D1[hill.py]
    D --> D2[hill_test.py]
```

## Fonctionnalités principales

- César : Décalage simple sur chaque lettre du message 
- Vigenère : Décalage selon une clé répétée, substitution polyalphabétique 
- Hill : Chiffrement par blocs via multiplication matricielle mod 26

<br>

Auteur : Anas EL Faijah <br>
Contacte moi : Via https://www.linkedin.com/in/anaselfaijah/  or elfaijahanas@gmail.com <br>