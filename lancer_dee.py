import random
print("#Cliquer Sur 1 pour lancer le dée")
print("#Cliquer Sur 0 pour Quitter")
x=int(input("Veuillez choisir un Numero"))
while True:
    x = int(input("Veuillez Saisir Votre Choix"))
    if(x==1):
          print(random.randint(1,6))
    if(x==0):
         print("operation arreter")
         break