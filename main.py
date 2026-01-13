import os
import json

historique_soldes = []

FICHIER_HISTORIQUE = "historique.json"
SOLDE_INITIALE = "solde.json"

#fontion pour initialiser le solde
def initialiser_solde():
    if not os.path.exists(SOLDE_INITIALE):
        with open(SOLDE_INITIALE, "w") as f:
            json.dump({"solde": 5000}, f, indent=4)
       
#fontion pour initialiser la fichier pour les historiques
def initialiser_historique():
    if not os.path.exists(FICHIER_HISTORIQUE):
        with open(FICHIER_HISTORIQUE, "w") as f:
            json.dump({"historiques": []}, f, indent=4)

#fontion pour charger la liste      
def charger_historique():
    initialiser_historique()
    with open(FICHIER_HISTORIQUE, "r") as f:
        return json.load(f)["historiques"]
   
#fontion pour ajouter un historique
def ajouter_historique(message):
    historique = charger_historique()
    historique.append(message)

    with open(FICHIER_HISTORIQUE, "w") as f:
        json.dump({"historiques": historique}, f, indent=4)

#fonction pour la saisie du code ussd
def Code_ussd():
    while True:
        code= input("Pour acceder a orange money taper (#144#) : ")
        
        #verification si la saisie commence par # et se termine par # et egale a #144#
        if code == '#144#':
            break
        else:
            print("Code invalide!!!!")

#fonction pour le code secret
def Code_secret():
    tentatives = 3
    while tentatives > 0:
        pin = input(f"Entrez votre code secret ({tentatives} essais restants): ")
        if pin == '1234':
            return True 
        else:
            tentatives -= 1
            print("Code invalide!!!!")
    return False

#fonction pour afficher le menu principal
def Affichage_menu():
    print("\n=========Menu Principal==========\n")
    print("1. Consulter le solde")
    print("2. Acheter du crédit")
    print("3. Effectuer un transfert") 
    print("4. Achat de fortait internet") 
    print("5. Annuler un transfere") 
    print("6. Historique des transactions") 
    print("0. Quitter ?")
    

#fonction pour gerer les confirmations et retour au precedent
def confirmation(message):
    print("\n" + message)
    print("1. Confirmer")
    print("2. Annuler")

    while True:
        choix = input("Votre choix : ")
        
        if choix == "1":
            return  True
        elif choix == "2":
            return False
        else:
            print("Incorrect")

#fonction pour afficher le solde
def Consulter_solde():
    with open(SOLDE_INITIALE, "r") as f:
        data=  json.load(f)
        print(f"\nVotre solde actuel est egale a : {data['solde']} FCFA")

#fonction pour l'achat de credit
def Acheter_crédit():
    while True:
        montant_saisie = input("Entrez le montant à acheter (ou 'q' pour quitter) : ").strip()
        
        if montant_saisie.lower() == 'q':
            break

        #verification pour entrer
        if montant_saisie.isnumeric():
            montant = int(montant_saisie)
            
            try:
                #on lis et le fichier
                with open(SOLDE_INITIALE, "r") as f:
                    donnees = json.load(f)
                    
            except (FileNotFoundError, json.JSONDecodeError, KeyError):
                print("Erreur : Impossible de lire le solde.")
                return

            #verifie si le solte est inferieur au montant
            if donnees['solde'] < montant:
                print(f"Solde insuffisant (Solde actuel : {donnees['solde']} FCFA)")
                return

            #on appel la fonction confirmation()
            if confirmation(f"Voulez-vous acheter {montant} FCFA de crédit ?"):
                donnees['solde'] -= montant
                
                # Mise à jour du solde
                with open(SOLDE_INITIALE, "w") as f:
                    json.dump(donnees, f, indent=4)
                
                # Mise à jour de l'historique
                ajouter_historique(f"Achat de {montant} FCFA de crédit")
                
                print(f"\nFélicitations !!! Crédit acheté.")
                print(f"Votre nouveau solde est : {donnees['solde']} FCFA")
                return
            else:
                print("Transaction annulée.")
                return
        else:
            print("Erreur : Veuillez saisir un montant valide (chiffres uniquement).")

#fonction pour les transferes
def Effectuer_transfert():

    print("\n--- Services ---")
    print("1. Transfert National")
    print("2. Transfert internationale")
    print("0. Retour")
    
    while True:
        choix = input("Choisissez une option : ").strip()
        
        if choix == '0':
            return 

        #verifie s'il a choisi 1 ou 2
        if choix in ('1', '2'):
            while True:
                numero_beneficiaire = input("Entrez le numero du beneficiaire : ").strip()
                montant_saisie = input("Entrez le montant a envoyer : ").strip()

                #Valider que les entrées sont bien des chiffres
                if not numero_beneficiaire.isnumeric() or not montant_saisie.isnumeric():
                    print("Erreur : Veuillez saisir uniquement des chiffres pour le numéro et le montant.")
                    continue

                #on fait la convertion du montant
                montant = int(montant_saisie)

                #Validation de la longueur du numéro (ex: 9 chiffres pour le SN)
                if len(numero_beneficiaire) != 9: 
                    print("Erreur : Le numéro de bénéficiaire doit comporter 9 chiffres.")
                    continue
                    
                try:
                    #on lis et le fichier
                    with open(SOLDE_INITIALE, "r") as f:
                        donnees = json.load(f)
                        
                except (FileNotFoundError, json.JSONDecodeError, KeyError):
                    print("Erreur : Impossible de lire le solde.")
                    return

                #Validation du solde
                if donnees['solde'] < montant:
                    print(f"Solde insuffisant. Votre solde actuel est de {donnees['solde']} FCFA.")
                    continue
                    
                else:
                    
                    historique_soldes.append(donnees['solde'])
                    
                    # --- PROCESSUS DE TRANSFERT ---
                    if choix == '1':
                        message = f"Voulez-vous effectuer un transfert national de {montant} FCFA au +221 {numero_beneficiaire} ?"
                    else: 
                        message = f"Voulez-vous effectuer un transfert international de {montant} FCFA a {numero_beneficiaire} ?"

                    # Appel de la fonction de confirmation
                    if confirmation(message):
                        donnees['solde'] -= montant
                        
                        # Mise à jour du solde
                        with open(SOLDE_INITIALE, "w") as f:
                            json.dump(donnees, f, indent=4)
                            
                        print(f"\nFélicitations !! Envoi effectué. Votre nouveau solde est {donnees['solde']} FCFA")
                        #ajout de l'action dans liste des historiques
                        ajouter_historique(f"Vous avez envoyé {montant} FCFA à {numero_beneficiaire}")
                        return 
                    else:
                        print("Transaction annulée.")
                        return

        else:
            print("Choix invalide !!!")

#fonction pour les achats de forfait internet
def Forfaits_internet():

    print("\n--- Forfaits Internet ---")
    print("1. 100 Mo - 500 FCFA")
    print("2. 500 Mo - 1000 FCFA")
    print("3. 1 Go - 2000 FCFA")
    print("0. Retour")
    
    while True:
    
        choix=input("Entrez votre option: ")

        # on creer une dictionnaire de forfait disponible
        forfait={
            "1":(500, "100 Mo"),
            "2":(1000, "500 Mo"),
            "3":(2000, "1 Go")
        }
        
        #si le choix == 0 on retour au menu
        if choix == "0":
            return

        #on verifie si le choix est dans le dictionnaire
        if choix in forfait:
            prix, nom = forfait[choix]
            
            try:
                #on lis et le fichier
                with open(SOLDE_INITIALE, "r") as f:
                    donnees = json.load(f)
                    
            except (FileNotFoundError, json.JSONDecodeError, KeyError):
                print("Erreur : Iempossible de lire le solde.")
                return
    
            #verification du solde s'il est suffisant
            if donnees['solde'] < prix:
                print("Solde insuffisant")
                return

            # Appel de la fonction de confirmation
            if confirmation(f"Voulez-vous Acheter {nom} pour {prix} FCFA ?"):
                #on verifie si le pwd est correct et on decremente
                if Code_secret():
                    donnees['solde'] -= prix
                    
                    # Mise à jour du solde
                    with open(SOLDE_INITIALE, "w") as f:
                        json.dump(donnees, f, indent=4)
                
                    #ajout de l'action dans la liste des historiques
                    ajouter_historique(f"Achat Internet : {nom} (-{prix} FCFA)")
                    print(f"\n Forfait {nom} activé avec succès !")
                    return
                else:
                    print(" Échec : Code secret incorrect.")
                    
            else:
                print("Annulation de l'achat.")
                
        else:
            print("Choix invalide!!!")

#fonction pour annuler le dernier transfere   
def Annuler_transfert():
    
    with open(SOLDE_INITIALE, "r") as f:
        donnees = json.load(f)

    # Vérifier si l'historique contient des données
    if not historique_soldes:
        print("Aucun transfert à annuler dans l'historique.")
        return

    # Demander confirmation
    if confirmation("Voulez-vous vraiment annuler le transfert ?"):
        
        if Code_secret():
            # Récupérer et retirer le dernier solde de la pile
            solde_precedent = historique_soldes.pop()
            donnees['solde'] = solde_precedent
            
            # Mise à jour du solde
            with open(SOLDE_INITIALE, "w") as f:
                json.dump(donnees, f, indent=4)
            
            print(f"Annulation réussie. Solde restauré à : {donnees['solde']} FCFA")
            ajouter_historique(f"Annulation de transfert : solde restauré à {solde_precedent} FCFA")
        else:
            print("Erreur : Code secret incorrect. Annulation avortée.")
    else:
        print("Action annulée par l'utilisateur.")

#fonction pour les historiques
def Historiques():
    print("\n--- Historique des transactions ---")

    historique = charger_historique()

    if not historique:
        print("Aucune opération effectuée.")
    else:
        for i, action in enumerate(historique, start=1):
            print(f"{i}. {action}")


#Programme principal
Code_ussd()

while True:
    initialiser_solde()
    initialiser_historique()
    
    Affichage_menu()
    choix = input("Entrez votre choix : ").strip()
    
    if choix == "1":
        Consulter_solde()
    elif choix == "2":
        Acheter_crédit()
    elif choix == "3":
        Effectuer_transfert()
    elif choix == "4":
        Forfaits_internet()
    elif choix == "5":
        Annuler_transfert()
    elif choix == "6":
        Historiques()
    elif choix == "0":
        print("\nMerci d'avoir utilisé Orange Money 🇸🇳")
        break
    else:
        print("Choix invalide")