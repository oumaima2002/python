def acronyme():
    text=str(input("Veuillez Saisir une à acronyser:"))
    mots = text.split()
    var = ''
    for mot in mots:
           var+=str(mot[0].upper())
    print("Lacronyme est :"+var)



acronyme()

