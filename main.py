tab=[
    [0,1,'a',1],
    [2,2,2,2],
    [3,3,3,3],
    [4,4,4,4]
]
import fonction as fct
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
        col=int(col)
        ligne = f.readline()
        lig = ligne.strip()  # nbr etat
        lig=int(lig)
        ligne = f.readline()
        EI = ligne.strip(" ") #etat initial
        ligne = f.readline()
        ET = ligne.strip(" ") #etat terminal
        ligne = f.readline()
        nbr_transition = ligne.strip()  # etat terminal
        print("a =",nbr_transition)
        ligne = f.readline()
        b = list(ligne.strip())  # etat terminal
        print("b =", b)
        #ligne = f.readline()
        print(type(EI))
        print("Etat(s) initial(aux) : ",EI[1:])#affiche le ou les EI
        print("Etat(s) terminal(aux) : ",ET[1:])#affiche le ou les ET
        print("col =",col,"lig =",lig)
        #matrice=fct.creer_matrice(lig+1,col+1)
        #print(matrice)
        matrice=[]
        while ligne:
            temp =list(ligne.strip())
            print(temp, ":")
            matrice=fct.ajoute_int(matrice,int(temp[0]),temp[1],int(temp[2]))
            print("teste", i)
            for c in range(lig + 1):
                print("\n")
                for j in range(col + 1):
                    print(matrice[c][j], end=' ')
            print("\n")
            ligne = f.readline()
        '''matrice=[]
        for i in range(lig):
            # créer une sous-liste vide pour chaque ligne
            ligne = []
            # boucle for pour chaque colonne
            for j in range(col):
                # ajouter un élément à la sous-liste en utilisant une méthode d'entrée
                variable = input("Entrez la valeur de la variable {}: ".format(j + 1))
                ligne.append(variable)
            # ajouter la sous-liste à la liste principale de la matrice
            matrice.append(ligne)'''

        # afficher la matrice résultante
        for c in range(lig+1):
            print("\n")
            for j in range(col+1):
                print(matrice[c][j], end=' ')
        print("\n")
Afficher("C3-9.txt")
