import os


date = input ("mettez la date du jour comme ceci : JJ/MM/AAAA ")
conso_max = input("Quelle est votre consommation max par mois ? ")
conso_restant = input("A combien est votre consommation aujourd'hui ? ")


"""try:
    FileNotFoundError:
    with open('conso.txt', 'r') as file:
        first_line = file.readline(0)
        if not first_line:
                with open('conso.txt', 'w') as file:
                        file.write(f"{conso_max}\n")

except:
    with open('conso.txt', 'a') as file:
# Le fichier est vide, écrire à la ligne suivante ici
        file.write(f"{conso_max}\n")"""

def creer_fichier_conso_max(nom_fichier, conso_max):
    # Vérifie si le fichier existe
    if not os.path.isfile('conso.txt'):
        # Si le fichier n'existe pas, le crée
        with open('conso.txt', 'w') as file:
            file.write(f"{conso_max}\n")
            print(f"Le fichier {nom_fichier} a été créé avec la consommation maximale {conso_max} Go.")
    else:
        # Si le fichier existe, vérifie s'il est vide
        with open(nom_fichier, 'a+') as file:
            file.seek(0) # Aller au début du fichier
            if file.read(1) == '': # Si le fichier est vide
                file.write(f"{conso_max}\n")
                print(f"Le fichier {nom_fichier} était vide, la consommation maximale {conso_max} Go a été écrite.")
            else:
                breakpoint


# Exemple d'utilisation
creer_fichier_conso_max('conso.txt', 200)


#Récup la dernière ligne du fichier texte
def recuperer_derniere_ligne(nom_fichier):
    with open('conso.txt', 'r') as fichier:
        for ligne in fichier:
            derniere_ligne = ligne.strip()
    return derniere_ligne

conso_restant_float = float(conso_restant)

derniere_ligne_str = recuperer_derniere_ligne('conso.txt')
derniere_ligne_float = float(derniere_ligne_str)

conso_today = (derniere_ligne_float - conso_restant_float)
conso_today_int = float(conso_today)


print(f"Nous somme le {date}")
print(f"Votre consommation maximum est de : {conso_max} Go.")
print(f"Votre consommation hier était de : {derniere_ligne_float} Go.")
print(f"Aujourd'hui elle est de : {conso_restant} Go.")
print(f"vous avez utilisé {conso_today_int} Go.")


# Ouvrir le fichier en mode écriture
with open('conso.txt', 'a') as file:
    file.write(f"Consommation du {date} est de :\n")
    file.write(f"Consommation max : {conso_max} Go.\n")
    file.write(f"La consommation restante hier etait de : {derniere_ligne_float} Go.\n")
    file.write(f"Vous avez utiliser : {conso_today_int} Go aujourd'hui.\n")
    file.write(f"La consommation restante en Go est de :\n")
    file.write(f"{conso_restant}\n")
    

    
