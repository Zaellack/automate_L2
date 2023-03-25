# Définir une matrice de 3 x 4
matrice = [
    [1, 0, 0],
    [2, 0, 0],
    [3, 0, 0]
]

def ajoute_int(matrice, entier, a_ou_b, h):
    for i in range(len(matrice)):
        if entier in [ligne[0] for ligne in matrice]:
            ligne = [elem for elem in matrice[i] if elem != '']
            if a_ou_b == 'a':
                ligne[1] = h
            elif a_ou_b == 'b':
                ligne[2] = h
            elif a_ou_b == 'c':
                ligne[3] = h
            matrice[i] = ligne
            break
    else:
        matrice.append([entier] + [0] * (len(matrice[0]) - 1))
        if a_ou_b == 'a':
            matrice[-1][1] = h
        elif a_ou_b == 'b':
            matrice[-1][2] = h
        elif a_ou_b == 'c':
            matrice[-1][3] = h
        for i in range(len(matrice)):
            if matrice[i][0] == entier:
                matrice[i] = [entier] + [elem for elem in matrice[i][1:] if elem != '']
                break
    return matrice
matrice=[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
# Ajouter l'entier 2 dans la colonne 'a'
print(ajoute_int(matrice, 1, 'a',3))


# Ajouter l'entier 5 dans la colonne 'b'
print(ajoute_int(matrice, 5, 'b',6))

def creer_matrice(n, s):
    matrice = []
    for i in range(n):
        ligne = [0] * s
        matrice.append(ligne)
    return matrice