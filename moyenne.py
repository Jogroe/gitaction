def calculer_moyenne(liste):
    if len(liste) == 0:
        return 0
    else:
        return sum(liste) / len(liste)