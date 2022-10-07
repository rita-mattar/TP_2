""""
Rita Mattar
402
TP2
"""
import random

def nombre()
    """
    cette fonction defini les nombres maximales et minimales
    """
    global minimum, maximum
    minimum = int(input("écrivez un nombre minimal:" ))
    maximum = int(input("écrivez un nombre maximal"))
    print(f"vos numéro était sauvgarder. Maintenant essay de deviner le nombre que j'ai choisi entre {minimum} et {maximum}")

def jeu_devinette ():

    """
    fonction du jeu
    ce dernier détermine le nombre d'essaies, aide le joueur a deviner le nombre et lui offre de rejouer
    """
    nombre()
    chiffre = random.randint (minimum,maximum)
    chances_counter = 1
    chances = int(input("deviner le nombre:"))
    while chances !=chiffre:
        if chances > chiffre:
            print("votre nombre est plus grand que le nombre choisi ")
            chances_counter =  chances_counter + 1
            chances = int(input("deviner un autre nombre "))

        else:
            print("votre nombre est plus petit que le nombre choisi")
            chances_counter = chances_counter + 1
            chances = int(input("deviner un autre nombre"))

    print (f"exellent, vous avez reussi a deviner le bon nombre qui etait {chances}")
    print(f"vous avez reussit a devibe le nombre dans {chances_counter}")
    rejouer = str(input("voulez vous faire un autre tour? (y/n"))
    if rejouer == "y":
        jeu_devinette()
    else:
        print("merci d'avoir joué, au revoir")

jeu_devinette()