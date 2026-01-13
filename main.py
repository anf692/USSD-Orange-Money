solde=5000
historiques=[]
historique_soldes = []

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
    print("4. Historique des transferts") 
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
    global solde
    print(f"\nVotre solde actuel est egale a : {solde} FCFA")

#fonction pour l'achat de credit
def Acheter_crédit():
    global solde
    
    while True:
        montant_saisie= input("Entrez le montant a acheter: ")
        
        if montant_saisie.replace(" ", "").isnumeric():
            
            montant= int(montant_saisie)
            if solde < montant:
                print("Solde insuffisant")
                return
        
            #verification et appel a la fonction confirmation pour voir s'il a 'confirmer' ou 'annuler'
            if confirmation(f"Voulez-vous  achater {montant} de credit? "):
                solde -= montant
                #ajout de l'action dans liste des historiques
                historiques.append(f"Vous avez acheter {montant} FCFA de credit")
                print(f"\nFelication!!! compte recharger. Votre nouveux solde est {solde} FCFA ")
            return
        
        else:
            print("Montant incorrect!!!")


#fonction pour les transferes
def Effectuer_transfert():
    global solde 

    print("\n--- Services ---")
    print("1. Transfert National")
    print("2. Transfert internationale")
    print("0. Retour")
    
    while True:
        choix = input("Choisissez une option : ").strip()
        
        if choix == '0':
            return # Sort de la fonction et revient au menu principal

        if choix in ('1', '2'):
            while True:
                numero_beneficiaire = input("Entrez le numero du beneficiaire : ").strip()
                montant_saisie = input("Entrez le montant a envoyer : ").strip()

                #Valider que les entrées sont bien des chiffres
                if not numero_beneficiaire.isnumeric() or not montant_saisie.isnumeric():
                    print("Erreur : Veuillez saisir uniquement des chiffres pour le numéro et le montant.")
                    continue


                montant = int(montant_saisie)

                #Validation de la longueur du numéro (ex: 9 chiffres pour le SN)
                if len(numero_beneficiaire) != 9: 
                    print("Erreur : Le numéro de bénéficiaire doit comporter 9 chiffres.")
                    continue

                #Validation du solde
                if solde < montant:
                    print(f"Solde insuffisant. Votre solde actuel est de {solde} FCFA.")
                    continue
                    
                else:
                    historique_soldes.append(solde)
                    
                    # --- PROCESSUS DE TRANSFERT ---
                    if choix == '1':
                        message = f"Voulez-vous effectuer un transfert national de {montant} FCFA au +221 {numero_beneficiaire} ?"
                    else: 
                        message = f"Voulez-vous effectuer un transfert international de {montant} FCFA a {numero_beneficiaire} ?"

                    # Appel de la fonction de confirmation
                    if confirmation(message):
                        solde -= montant
                        print(f"\nFélicitations !! Envoi effectué. Votre nouveau solde est {solde} FCFA")
                        #ajout de l'action dans liste des historiques
                        historiques.append(f"Vous avez envoier {montant} FCFA a {numero_beneficiaire}")
                        return # Transaction terminée, sortie de la fonction
                    else:
                        print("Transaction annulée.")
                        return

        else:
            print("Choix invalide !!!")

#fonction pour les historiques
def Historiques():
    print("\n--- Historique ---")

    if not historiques:
        print("Aucune opération effectuée.")
    else:
        for i, action in enumerate(historiques):
            print(f"{i}. {action}")


#fonction pour les achats de forfait internet
def Forfaits_internet():
    global solde 
    global historiques 

    forfait = {
        "1": (500, "100 Mo"),
        "2": (1000, "500 Mo"),
        "3": (2000, "1 Go")
    }

    print("\n--- Forfaits Internet ---")
    print("1. 100 Mo - 500 FCFA")
    print("2. 500 Mo - 1000 FCFA")
    print("3. 1 Go - 2000 FCFA")
    print("0. Retour")
    
    while True:
        choix = input("Entrez votre option: ")

        if choix == "0":
            return

        if choix in forfait:
            prix, nom = forfait[choix]

            if solde < prix:
                print(f"Solde insuffisant ({solde} FCFA restants).")
                continue 

            # Appel de la fonction de confirmation
            if confirmation(f"Voulez-vous acheter {nom} pour {prix} FCFA ?"):
                if Code_secret():
                    solde -= prix
                    historiques.append(f"Achat Internet : {nom} (-{prix} FCFA)")
                    print(f"\n Forfait {nom} activé avec succès !")
                    return 
                else:
                    print(" Échec : Code secret incorrect.")

            else:
                print("Annulation de l'achat.")
        else:
            print("Choix invalide !!!")

#fonction pour annuler le dernier transfere   
def Annuler_transfert():
    global solde
    
    #Vérifier si l'historique contient des données
    if not historique_soldes:
        print("Aucun transfert à annuler dans l'historique.")
        return

    # Demander confirmation
    if confirmation("Voulez-vous vraiment annuler le transfert ?"):
        
        #Vérifier le code secret
        if not Code_secret():
            # Récupérer et retirer le dernier solde de la pile
            solde_precedent = historique_soldes.pop() 
            solde = solde_precedent
            print(f"Annulation réussie. Solde restauré à : {solde} FCFA")
            historiques.append(f"Annulation de transfere : solde = {solde_precedent} FCFA")
        
        else:
            print("Erreur : Code secret incorrect. Annulation annulée.")

            

#Programme principal
Code_ussd()

while True:
    Affichage_menu()
    choix = input("Entrez votre choix : ").strip()
    
    if choix == "1":
        Consulter_solde()
    elif choix == "2":
        Acheter_crédit()
    elif choix == "3":
        Effectuer_transfert()
    elif choix == "4":
        Historiques()
    elif choix == "0":
        print("\nMerci d'avoir utilisé Orange Money 🇸🇳")
        break
    else:
        print("Choix invalide")