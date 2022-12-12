import csv
import random
# script de la première attaque sur le système sans hachage
# Avec TCHAI v2, cette attaque ne pase pas la vérification du hash

def modify_tr():
    rows = []
    with open("data/transactions.csv", 'r+', newline='') as trfile:
        trreader = csv.reader(trfile,delimiter=',')
        trwriter = csv.writer(trfile, delimiter=',')
        for row in trreader:
            # modifie toutes les transactions de A vers B
            if row[0]=="A" and row[1]=='B':
                row[3]= 2000
            rows.append(row)
        # on retourne au début du fichier et on écrit les données modifié
        trfile.seek(0)
        trwriter.writerows(rows)

# seconde attaque, qui supprime une ligne pour entrainer une double dépense par exemple
def delete_tr():
    rows = []
    with open("data/transactions.csv", 'r', newline='') as trfile:
        trreader = csv.reader(trfile, delimiter=',')
        for row in trreader:
            print(row)
            rows.append(row)

    #on supprime une ligne aléatoire, en ignorant l'en-tete
    rows.pop(random.randint(1,len(rows)-1))
    with open("data/transactions.csv", 'w', newline='') as trfile:
        trwriter = csv.writer(trfile, delimiter=',')
        trwriter.writerows(rows)

# modify_tr() cette attaque est detectée par le hachage en place
delete_tr()