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