
from src.config import APP_NAME, APP_VERSION, APP_AUTHOR


def afficher_header():
    print("=" * 40)
    print(f"{APP_NAME} (v{APP_VERSION})")
    print(f"Auteur : {APP_AUTHOR}")
    print("=" * 40)


def afficher_menu():
    print("\n===== MENU SHOPPING =====")
    print("1 - Ajouter des articles")
    print("2 - Afficher la liste numérotée")
    print("3 - Supprimer par numéro (pop)")
    print("4 - Supprimer par nom (remove)")
    print("5 - Quitter")
    print("6 - Exporter CSV (client + date)")


def demander_choix_menu():
    while True:
        choix = input("Quel est ton choix ? ").strip()
        if choix in {"1", "2", "3", "4", "5", "6"}:
            return choix
        print("Choix invalide. Recommence.")


def demander_client():
    while True:
        client = input("Nom du client : ").strip().lower()
        if client:
            return client
        print("Le nom de client ne peut pas être vide.")
