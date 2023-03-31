import random

def deviner():
    while True:
        saisi=int(input("Veuillez saisir un nombre Entre 0 et 20 : "))
        if((saisi>20)or(saisi<0)):
            print("Le nombre est hors de l'intervalle")

        if(saisi==random.randint(0,20)):

            print("Bravo Vous avez devinez le nombre")
        else:
            print(str(saisi)+"Ce n'est pas le nombre choisi , Essayer un autre fois")

deviner()

