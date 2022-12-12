import csv
# script de la première attaque sur le système sans hachage
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

modify_tr()







