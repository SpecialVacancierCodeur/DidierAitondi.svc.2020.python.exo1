#coding: utf-8
from math import sqrt

#je crée maintenant une fonction pour résoudre l'équation de second dégré. Ceci évitant les mauvaise valeurs ...
def resolution (a, b, c):
    try: #pour éviter les mauvaise valeur
        a, b, c = float(a), float(b), float(c)
    except:
        print("Erreur. Veuillez réésayer , ...!")
        return
    #je fais maintenant une dijonction de cas pour les valeurs de a b et c
    if (a == 0 and b == 0 and c == 0):
        print("0=0 est vrai dans R")
    elif (a == 0 and b == 0 and c != 0):
        print("Erreur! impossible d'avoir {} =0 !".format(c))
    elif (a == 0 and b != 0):
        x = c / b
        print(" x= {} est la seule solution !".format(x))
    else:
        D = b ** 2 - 4 * a * c
        find_answers(a, b, c, D)

#je crée une fonction pour trouver mes solutions pour l'équation de second dégré

def find_answers(a, b, c, D): #Mon D signifi mon discriminant
    if D < 0:
        print("Aucune solution pour cette équation dans R")
    elif D == 0:
        x = -b / (2 * a)
        print("Cette équation admet une seule solution x= {}".format(x))
    else:
        x1 = (-b - sqrt(D)) / (2 * a)
        x2 = (-b + sqrt(D)) / (2 * a)
        print("L'équation admin deux solutions dans R : x1= {} et x2= {}".format(x1, x2))

print("Salut. Je vais vous aider à résoudre une équation de second dégré ")
go_way=0
while go_way==0 :
    print("Entrez les valeurs pour  a,b et c")
    a = input("Entrer la valeur de a svp : ")
    b = input("Entrer la valeur de b svp : ")
    c = input("Entrer la valeur de c svp : ")
    resolution(a, b, c)
    go_way_val=input("Voulez vous résoudre une autre équation ? (O/N) \n Entrer 'N' pour arrêter le programme \n \n \t")
    if go_way_val=='N':
        go_way=2
