import csv  
import matplotlib.pyplot as plt  


chemin_fichier_59 = "/home/Etudiants/RT/BUT-RT-1/yl211305/Téléchargements/SAE105 projet/MN_59_previous-2020-2023.csv" 
chemin_fichier_05 = "/home/Etudiants/RT/BUT-RT-1/yl211305/Téléchargements/SAE105 projet/MN_05_previous-2020-2023.csv" 
chemin_fichier_75 = "/home/Etudiants/RT/BUT-RT-1/yl211305/Téléchargements/SAE105 projet/MN_75_previous-2020-2023.csv"
chemin_fichier_13 = "/home/Etudiants/RT/BUT-RT-1/yl211305/Téléchargements/SAE105 projet/MN_13_previous-2020-2023.csv"
chemin_fichier_44 = "/home/Etudiants/RT/BUT-RT-1/yl211305/Téléchargements/SAE105 projet/MN_44_previous-2020-2023.csv"
chemin_fichier_971 = "/home/Etudiants/RT/BUT-RT-1/yl211305/Téléchargements/SAE105 projet/MN_971_previous-2020-2023.csv"

#fonction ré-utilisé du deuxième tp avec juste une liste en plus pour rajouter les données filtrés
def charger_donnees(chemin_fichier):
    donnees = []  # Liste pour stocker les données filtrées
    with open(chemin_fichier, mode='r') as fichier_csv:  
        lecteur = csv.reader(fichier_csv, delimiter=";")  
        entete = next(lecteur)  #on igonre la première ligne (en-tête)
        for ligne in lecteur:  
            try:
                altitude = float(ligne[4])  #on récupère la valeur d'altitude (colonne 5)
                precipitation = float(ligne[6])  #on récupère la valeur de précipitation (colonne 7)
                donnees.append((altitude, precipitation))  
            except (ValueError, IndexError):  
                continue  #on ignore la ligne en cas d'erreur
    return donnees  

donnees_59 = charger_donnees(chemin_fichier_59)  
donnees_05 = charger_donnees(chemin_fichier_05)  
donnees_75 = charger_donnees(chemin_fichier_75)  
donnees_13 = charger_donnees(chemin_fichier_13)
donnees_44 = charger_donnees(chemin_fichier_44)
donnees_971 = charger_donnees(chemin_fichier_971)
donnees_combinees = donnees_59 + donnees_05 + donnees_75 + donnees_13 + donnees_44 + donnees_971  

# On groupera les données par tranches d'altitude avec un dictionnaire qui stockera les précipation par tranche d'altitude
tranches_altitude = {}
for altitude, precipitation in donnees_combinees: 
    tranche = int(altitude // 100) * 100  # On regroupe les altitudes par tranche de 100 m, ici la division euclidienne nous sert à diviser un nombre comme 330 qui deviendra 3 et ensuite le re-multiplier par 100 pour avoir 300 et avoir des tranches régulière pour une meilleur compréhension pour la suite
    if tranche not in tranches_altitude:  # Si la tranche n'existe pas encore
        tranches_altitude[tranche] = []  # On crée une nouvelle liste pour cette tranche
    tranches_altitude[tranche].append(precipitation)  #  et là on ajoute la précipitation à la tranche qui n'existait pas à la base

# On calcule la pluviométrie moyenne par tranche d'altitude
pluviometrie_moyenne = {tranche: sum(valeurs) / len(valeurs) for tranche, valeurs in tranches_altitude.items() if valeurs}  

# on trie les tranches par altitude manuellement
tranches_tries = sorted(pluviometrie_moyenne.items())  # on trie les tranches par altitude de manière croissante grâce à sorted()
# la fonction sorted() trie les éléments du dictionnaire pluviometrie_moyenne par les clés ici les tranches d'altitude.

# on extrait les données pour le graphique
altitudes = [item[0] for item in tranches_tries]  # la liste des tranches d'altitude
pluviometries = [item[1] for item in tranches_tries]  # la liste des précipitations moyennes

plt.plot(altitudes, pluviometries, marker='o')
plt.xlabel("Altitude (m)")  
plt.ylabel("Pluviométrie moyenne (mm)")  
plt.title("Pluviométrie moyenne par tranche d'altitude")  
plt.show()  # Affiche le graphique