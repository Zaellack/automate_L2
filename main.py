tab=[
    [0,1,'a',1],
    [2,2,2,2],
    [3,3,3,3],
    [4,4,4,4]
]
print(len(tab))
for c in range(len(tab)):
    print("\n")
    for j in range(len(tab)):
        print(tab[c][j],end=' ')
print("\n")
i=0
def Afficher(fichier):
    EI=[]
    ET=[]
    with open(fichier, "r") as f:
        ligne = f.readline()
        col = ligne.strip()  # nbr alphabet
        ligne = f.readline()
        lig = ligne.strip()  # nbr etat
        ligne = f.readline()
        EI = ligne.strip(" ") #etat initial
        ligne = f.readline()
        ET = ligne.strip(" ") #etat terminal
        ligne = f.readline()
        print(type(EI))
        print("Etat(s) initial(aux) : ",EI[1:])#affiche le ou les EI
        print("Etat(s) terminal(aux) : ",ET[1:])#affiche le ou les ET
        print("col =",col,"lig =",lig)
        while ligne:
            ligne = ligne.strip()  # enlever le caractère de nouvelle ligne
            print(ligne, ":")
            ligne = f.readline()
Afficher("C3-9.txt")
