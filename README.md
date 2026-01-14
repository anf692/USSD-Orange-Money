# Simulation Orange Money (Python)

Ce projet est une **simulation du service Orange Money** réalisée en **Python**, utilisant un menu USSD interactif en ligne de commande.  
Il permet de gérer un solde, effectuer des transactions et conserver un **historique persistant** grâce aux fichiers JSON.

---

## Objectifs pédagogiques

Ce projet a pour but de :
- Comprendre la **persistance des données** avec des fichiers JSON
- Manipuler les **fichiers en lecture et écriture** en Python
- Structurer un programme avec des **fonctions**
- Simuler le fonctionnement d’un **service USSD réel**
- Gérer les **erreurs et validations utilisateur**

---

## Fonctionnalités

- Accès par code USSD `#144#`
- Authentification par code secret
- Consultation du solde
- Achat de crédit
- Transfert d’argent (national / international)
- Achat de forfaits Internet
- Annulation du dernier transfert
- Historique des transactions
- Données persistantes (solde et historique)

---

## Fichiers utilisés

| Fichier | Description |
|------|------------|
| `main.py` | Script principal |
| `solde.json` | Contient le solde actuel |
| `historique.json` | Contient l’historique des transactions |

Les fichiers `solde.json` et `historique.json` sont **créés automatiquement** s’ils n’existent pas.

---

# NB: 
dans le github regarde les tag avec les differentes version du projet

---

## Structure des fichiers JSON

### solde.json et historique.json
```json
{
    "solde": 5000
}


{
    "historiques": [
        "Achat de 1000 FCFA de crédit",
        "Transfert de 2000 FCFA vers 771234567"
    ]
}

