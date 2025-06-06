from collections import defaultdict
import csv


def main():
    #add code here
    # Chemin vers le fichier CSV
    fichier_csv = "data/OrderItems.csv"
    # Dictionnaire pour stocker les quantités vendues par article
    ventes_par_article = defaultdict(int)
    # Lecture du fichier CSV
    with open(fichier_csv, mode='r') as fichier:
        lecteur_csv = csv.DictReader(fichier)
        for ligne in lecteur_csv:
            article = ligne['ProductID']
            quantite = int(ligne['Quantity'])
            ventes_par_article[article] += quantite
    # Affichage des résultats
    print("Quantités vendues par article :")
    for article, quantite in ventes_par_article.items():
        print(f"{article}: {quantite}")
    return

if __name__ == "__main__":
    main()