# TCHAI-Benjamin-PERRETTE-Timour-AMOURETTE

Auteurs : Timour Amourette & Benjamin Perrette


# Description 

Systèmes d'informations avancés, Projet TP.

Lien du sujet de TP à réaliser: https://kirgizov.link/teaching/esirem/advanced-information-systems/TP-PROJET.pdf 
Titre du projet: Tchaî - Chaîne de transactions
Travail réalisé sur 6 séances de 2 heures en binôme


Le projet a été réalisé entièrement avec le langage de programmation Python, sous l'IDE PyCharm,
Ce langage nous a semblé être le plus adéquat pour la réalisation de cette chaîne de transactions.

Nous utilisons le Framework web Flask qui permet d'effectuer facilement la création et le traitement des transactions, par le biais de méthodes HTML POST et GET.
Afin d'enregistrer et stocker les données des transactions et utilisateurs, nous avons créé des fichiers ".csv"
Ce choix de format à été motivé par une volonté de simplicité et de facilité de manipulation des données.
L'utilisation de fichiers csv permet d'illustrer le fonctionnement de l'application avec un échantillon de données,
ne nécessite aucune installation, ni d'herbérgement de serveur SQL ou autre.

# Test de l'application 

Des scripts d'attaque on été réalisés pour éprouver l'intégrité de l'application en simulant l'action d'un utilisateur malicieux. Ces scripts modifient directement les données stockées de différentes facons, en modifiant, ajoutant ou supprimant des lignes.
- La méthode modify_tr() prend arbitrairement une ligne de transaction et change son montant à 2000
- La méthode delete_tr() supprime une ligne aléatoire dans la liste des transactions
- La méthode add_tr() rajoute une transaction, dont le destinataire est le compte "Attaquant", à la fin du fichier de transactions

Pour les utiliser, il suffit d'éxecuter les différentes méthodes situées dans les fichiers attack.py, et de cliquer sur le bouton "vérification des données" de l'interface web. L'application alertera,(ou non,selon la version de Tchaî utilisée) des différentes modifications illicites qu'elle aura pu détecté.

# Installation 

Le programme peut s'éxecuter à partir de n'importe quel IDE ou terminal python. 
Il suffit ensuite de lancer un navigateur web avec l'adresse suivante : http://127.0.0.1:5000 pour accéder à l'interface web.

# Utilisation 

L'interface contient 4 champs texte, 3 boutons et 1 tableau d'information. 

- Les 3 premiers champs servent à renseigner les informations nécessaires à la création d'une transaction.
	Le champ "Sender" est pour celui qui envoie l'argent, le champ "Recipient" pour celui qui le reçoit, et le champ "Amount" pour le montant de la transaction.
	Il suffit ensuite de cliquer sur le bouton "Add Transaction" qui ouvre une autre page indiquant la réussite de la transaction.
	Confirmez la création en cliquant sur "Confirmer".
	
	
- Le champ "Select User" permet de choisir un utilisateur afin de consulter l'historique de ses transactions.
	En cliquant sur "Transaction history" une autre page s'ouvrira, montrant le solde actuel de l'utilisateur et un tableau répertoriant ses transactions. 
	
	
- Le bouton "Vérification des données" ouvre une nouvelle page qui indique si chacune des données est validée ou non par notre algorithme de chiffrement.
	Sur cette page sont affichés tous les utilisateurs et toutes les transactions avec un message indiquant si leur valeur de hachage est bonne.
	
	
- Le tableau visible sur la page principale répertorie toutes les transactions avec le numéro de la transaction, le nom de l'expéditeur, celui du destinataire, le montant émis ainsi que le hachage.


La valeur de hachage ne devrait bien entendu pas être visible dans le cas d'une application destinée au public, nous avons ici decidé de l'afficher dans le but de mieux illustrer le fonctionnement de l'application. 
