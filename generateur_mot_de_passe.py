import random
import string
print("Cliquer Sur 1 Pour Generer votre Mot De Passe")
print("Cliquer Sur 2 Pour Quitter ")
#mot de passe longueur  de longueur 8
while True:
    x=int(input("Saisissze Votre Choix"))
    if(x==1):
            st=string.ascii_letters
            var=""
            for i in range(3) :
                var+=random.choice(st)+str(random.choice(string.digits))+str(random.choice(string.punctuation))
    print(var)

    if(x==2):
        print("Quitter Le generateur")
        break


