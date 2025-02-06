# À la découverte des chiffrements historiques

## Introduction
Salut ! Je suis Anas E., étudiant en cybersécurité. Passionné par mon cours de mathématiques, j'ai voulu découvrir les fondements de la cryptographie en implémentant trois méthodes historiques de chiffrement (César, Hill et Vigenère). À travers ce projet, je partage le code 
et les explications de ces algorithmes de manière simple. 

## Le chiffrement de César : la simplicité à l'état pur

Imaginez que vous voulez envoyer un message secret à un ami. Le chiffrement de César, c'est un peu comme avoir un code secret où vous décalez chaque lettre d'un certain nombre de positions dans l'alphabet. Par exemple, avec un décalage de 3, 'A' devient 'D', 'B' devient 'E', et ainsi de suite.

Pour les matheux curieux, voici comment ça fonctionne :
- Pour chiffrer : on prend la position de la lettre, on ajoute la clé, et on fait le modulo 26
- Pour déchiffrer : on fait l'inverse !


## Le chiffrement de Hill : quand les maths s'en mêlent

Créé par Lester S. Hill en 1929, ce chiffrement est plus sophistiqué. Au lieu de traiter les lettres une par une, il les prend par groupes et utilise des matrices pour les mélanger. C'est un peu comme si vous mélangiez les ingrédients d'une recette selon une formule mathématique précise !

L'aspect cool ? Une même lettre peut donner différents résultats selon sa position dans le texte. C'est déjà plus difficile à décrypter que le chiffrement de César !

## Le chiffrement de Vigenère : l'art du camouflage

Le Vigenère, c'est comme un César sur-vitaminé. Au lieu d'utiliser toujours le même décalage, on utilise un mot-clé qui détermine des décalages différents pour chaque lettre. Par exemple, si votre mot-clé est "CHAT", chaque lettre sera décalée différemment selon qu'elle correspond au 'C', au 'H', au 'A' ou au 'T'.

C'est beaucoup plus malin que le César car une même lettre dans votre message peut être chiffrée de plusieurs façons différentes. Cependant, il existe une technique appelée "attaque de Kasiski" qui peut percer ce code en cherchant des motifs qui se répètent.

## En pratique

J'ai créé trois programmes Python pour tester tout ça :
- ```cesar.py``` pour le chiffrement de César
- ```hill.py``` pour le chiffrement de Hill
- ```vigenere.py``` pour le chiffrement de Vigenère

Chaque programme est accompagné de ses tests (```cesar_test.py, hill_test.py, vigenere_test.py```) pour s'assurer que tout fonctionne correctement.

## Pour conclure

Ces méthodes de chiffrement, bien qu'obsolètes aujourd'hui, sont fascinantes car elles nous montrent l'évolution des techniques de cryptographie. C'est un excellent moyen de comprendre les bases avant de plonger dans les méthodes modernes plus complexes. Et qui sait ? Peut-être que ça vous donnera envie d'explorer davantage ce domaine passionnant !