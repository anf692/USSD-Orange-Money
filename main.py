solde=5000
historiques=[]

#fonction pour la saisie du code ussd
def Code_ussd():
    while True:
        code= input("Pour acceder a orange money taper (#144#) : ")
        
        #verification si la saisie commence par # et se termine par # et egale a #144#
        if code == '#144#':
            break
        else:
            print("Code invalide!!!!")


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
                
                # --- Gestion du numéro sénégalais ---
                if numero_beneficiaire.startswith("+221"):
                    numero_beneficiaire = numero_beneficiaire.replace("+221", "")

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


