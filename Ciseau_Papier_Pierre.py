import random
def jeu():
    while True:
        options=["papier","caiseau","pierre"]
        choix=random.choice(options)

        saisi=input("Veuillez realiser votre choix: papier ou caiseau ou pierre : ")

        if(saisi==choix):
            print("Egaux")
        if(saisi=="papier" and choix=="caiseau"):
            print("vous avez perdu ->"+saisi+" VS "+choix)
        if(saisi=="papier" and choix=="pierre"):
            print("vous avez gagnée ->"+saisi+" VS "+choix)
        if(saisi=="pierre" and choix=="caiseau"):
            print("vous avez gagne->"+saisi+" VS "+choix)
        if(saisi=="pierre" and choix=="papier"):
            print("vous avez perdu ->"+saisi+" VS "+choix)
        if(saisi=="caiseau" and choix=="papier"):
            print("vous avez gagnée ->"+saisi+" VS "+choix)
        if(saisi=="caiseau" and choix=="pierre"):
            print("vous avez perdu ->"+saisi+" VS "+choix)




jeu()