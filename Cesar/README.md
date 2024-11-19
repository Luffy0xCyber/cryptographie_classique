# Chiffrement de Cesar

## Introduction 

Dans le cadre de mon cours de _Mathématiques et physiques appliquées_,
j'ai du codé le chiffrement de Cesar.

## C'est quoi ?

Mais d'abord c'est quoi le chiffrement de Cesar ? et en quoi ça consiste ?
Il s'agit d'un décalage dans l'alphabets latin.
Le procédé est simple, il suffit de réaliser un décalage de n rangs dans l'alphabets.
Par exemple, si on faisait un décalage de 1 rang, alors : A => B et B => C .
... 
Pour déchiffrer le message, il suffit de faire le procédé inverse.

## Comment je l'ai codé ?

J'ai codé ce chiffrement étape par étape. En effet, j'ai divisé le problème en plein de petits problème et j'ai codé chaque fonction.
Les tests unitaires étaient fournis et cela m'aidait à voir si j'avais juste ou pas. 
Cette segmentaion dans mon code me permet aussi d'utiliser uen focntion quand j'en avais besoin...
J'ai aussi utilisé le debugger, des print pour debug ainsi que la documentation python.




## Porblèmes que j'ai eu ?

L'un des premiers problèmes que j'ai eu c'est les lettres accentués.
En effet, dans mon première fonction j'avais cela :
```py
def cesar_shifting(letter, key):
    if letter.isalpha():
        if letter.isupper():
            position_initial = ord('A')
        else:
            position_initial = ord('a')
        return chr((((ord(letter) - position_initial) + key) %26) + position_initial)
    else:
        return letter
```
Le soucis avec le code ci-dessus est le ```isalpha()```. 
Cette méthode me posait problème car elle permettait que des lettres comme
'é','è'... soient prises en compte. Or, comme je l'ai mentionné au-dessus, le chiffrement de Cesar fait un décalage uniquement sur les alphabets.De plus, pour le dernier test unitaire au lieu d'avoir la bonne réponse
j'avais une fausse réponse : ```Exige beaucoup de toi-mhme et attends peu des autres. Ainsi beaucoup d'ennuis te seront gpargngs.```

On constate rapidement que chaque lettre où il est censé avoir un accent a été remplacé par une autre. En effet, comme la méthode ```isalpha()``` laissait passer
les lettres accentués alors il calcule sa position et lui donne une lettre ! 
Après des recherhces, j'ai compris qu'il fallait remplacer cela avec la méthode ```isascii()```. Cette fois-ci, cette méthode
prends juste les alphabets.

## Conclusion 

J'avais déjà compris le chiffrement de Cesar lors de mon corus théorique mais le fait de le coder et le faire moi même, m'a beaucoup aidé à visuliser le chiffrement et puis cela a été aussi un rappel pour moi.
Très fière d'avoir enfin codé mon première chiffrement. Hâte de faire le reste ! 