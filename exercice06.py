def trier_liste(liste):
    return sorted(liste)

def eliminer_doublons(liste):
    return list(set(liste))


def version_naive(liste1,liste2):
    fusion = liste1 + liste2
    fusion = eliminer_doublons(fusion)
    return trier_liste(fusion)


def fusion(liste1, liste2):
    resultat = liste1 + liste2
    resultat = list(set(resultat))
    min_l= min(resultat)
    max_l = max(resultat)
    taille = len(resultat)
    print("liste additionnée:", resultat)
    print("minimum de nouvelle liste:", min_l)
    print("maimum de nouvelle liste:", max_l)
    print("taille de nouvelle liste:", taille)

    liste_f = []
    for i in range(taille):
        min_r = min(resultat)
        liste_f.append(min_r)
        resultat.remove(min_r)
    return liste_f

def version_naive(liste1,liste2):
    fusion = liste1 + liste2
    fusion = eliminer_doublons(fusion)
    return trier_liste(fusion)

liste_non_triee = [3, 2, 1, 2, 4, 3, 5]
liste_triee = trier_liste(liste_non_triee)
print("liste triée:", liste_triee)
liste_sans_doublons = eliminer_doublons(liste_triee)
print("liste sans doublons:", liste_sans_doublons)

liste1 = [1, 3, 5, 1, 5, 7]
liste2 = [2, 4, 2, 6, 8, 8]
print(fusion(liste1, liste2))

tri_naif = version_naive(liste1, liste2)