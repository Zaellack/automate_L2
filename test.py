def ajoute_int(matrice, entier, a_ou_b, h):
    if not matrice:
        if a_ou_b == 'a':
            matrice.append([entier, h, 0, 0])
        elif a_ou_b == 'b':
            matrice.append([entier, 0, h, 0])
        elif a_ou_b == 'c':
            matrice.append([entier, 0, 0, h])
    else:
        for i in range(len(matrice)):
            if entier == matrice[i][0]:
                if a_ou_b == 'a':
                    matrice[i][1] = h
                elif a_ou_b == 'b':
                    matrice[i][2] = h
                elif a_ou_b == 'c':
                    matrice[i][3] = h
                break
        else:
            matrice.append([entier] + ['/'] * (len(matrice[0]) - 1))
            for i in range(len(matrice)):
                if matrice[i][0] == entier:
                    if a_ou_b == 'a':
                        matrice[i][1] = h
                    elif a_ou_b == 'b':
                        matrice[i][2] = h
                    elif a_ou_b == 'c':
                        matrice[i][3] = h
                    break

    return matrice


matrice=[]

# Ajouter l'entier 2 dans la colonne 'a'
print(ajoute_int(matrice, 1, 'a',3))


# Ajouter l'entier 5 dans la colonne 'b'
print(ajoute_int(matrice, 5, 'b',6))
print(ajoute_int(matrice, 5, 'c',6))
print(ajoute_int(matrice, 5, 'a',6))
