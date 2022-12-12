# TCHAI-Benjamin-PERRETTE-Timour-AMOURETTE


---------- Description ----------

Systèmes d'informations avancés, Projet TP.

Lien du sujet de TP à réaliser: https://kirgizov.link/teaching/esirem/advanced-information-systems/TP-PROJET.pdf 
Titre du projet: Tchaî - Chaîne de transactions
Travail réalisé sur 6 séances de 2 heures en binôme

Auteurs : Timour Amourette & Benjamin Perrette

Le projet est réalisé avec le langage de programmation Python, sous l'IDE PyCharm,  

Ce langage nous paraissait être le plus adéquat pour la réalisation de la chaîne de transactions. 

Nous utilisons le Framework web Flask qui permet facilement la création et le traitement des transactions. 

Afin d'enregistré les données des transactions et des utilisateurs nous avons créé des fichiers ".csv" qui sont simple à traité. 

---------- Test de l'application ----------


---------- Installation ----------

Le programme compile sous tout les IDE python. 
Il suffit ensuite de lancer un navigateur web avec l'adresse suivante : http://127.0.0.1:5000

---------- Utilisation ----------

L'interface contient 4 champs texte, 3 boutons et 1 tableau d'information. 
-Les 3 premiers champs servent à reseigner les informations nécessaire à la création d'une nouvelle transaction.
	Le champ "Sender" est pour celui qui envoie l'argent, le champ "Recipient" pour celui qui le reçoit et le champ "Amount" pour le montant de la transaction.
	Il suffit ensuite de cliquer sur le bouton "Add Transaction" qui ouvre une autre page indiquant que vous avez crée une transaction.
	Confirmez la création en cliquant sur "Confirmer".
-Le champ "Select User" permet de choisir un utilisateur afin de consulter l'historique de ces transaction.
	En cliquant sur "Transaction history" une autre page s'ouvrira montrant le solde de l'utilisateur et un tableau répertoriant ces transactions. 
-Le bouton "Vérification des données" ouvre une nouvelle page qui montre si les données sont valide ou non.
	Sur cette page sont afficher tout les utlisateurs et toute les transactions avec un message indiquant si les h sont bon.
-Le tableau répertorie toute les transactions avec le numéro de la transaction, l'envoyeur, le receveur, le montant ainsi que le h.
	Le h ne devrait pas être afficher dans le cas d'une application "sérieuse" de transaction, nous avons ici décider de l'afficher afin de pouvoir vérifier plus simplement pour l'exercice. 