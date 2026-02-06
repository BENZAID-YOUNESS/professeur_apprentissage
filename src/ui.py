
from src.config import APP_NAME, APP_VERSION, APP_AUTHOR


def afficher_header():
    print("=" * 40)
    print(f"{APP_NAME} (v{APP_VERSION})")
    print(f"Auteur : {APP_AUTHOR}")
    print("=" * 40)


def afficher_menu():
    print("\n" + "=" * 40)
    print("\nSMART LIST GENERATOR — MENU")
    print("=" * 40)
    print("1 ➜ Ajouter des articles")
    print("2 ➜ Afficher la liste (numérotée)")
    print("3 ➜ Supprimer par numéro")
    print("4 ➜ Supprimer par nom")
    print("5 ➜ Charger un template")
    print("6 ➜ Exporter en CSV")
    print("0 ➜ Quitter")
    print("-" * 40)



def demander_choix_menu():
    while True:
        choix = input("Quel est ton choix ? ").strip()
        if choix in {"0", "1", "2", "3", "4", "5", "6"}:
            return choix
        print("Choix invalide. Recommence.")


def demander_client():
    while True:
        client = input("Nom du client : ").strip().lower()
        if client:
            return client
        print("Le nom de client ne peut pas être vide.")

import os

def demander_template():
    dossier = "templates"
    fichiers = sorted([f for f in os.listdir(dossier) if f.endswith(".txt")])

    if not fichiers:
        print("Aucun template trouvé.")
        return None

    print("\nTemplates disponibles :")
    for i, f in enumerate(fichiers, start=1):
        print(f"{i} ➜ {f.replace('.txt','')}")

    while True:
        choix = input("Choisis un template (numéro) : ").strip()
        if choix.isdigit():
            idx = int(choix) - 1
            if 0 <= idx < len(fichiers):
                return fichiers[idx].replace(".txt","")

        print("Choix invalide. Réessaie.")
