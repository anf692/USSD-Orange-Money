solde=5000

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