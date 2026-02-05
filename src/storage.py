import os
from datetime import datetime

from src.config import CHEMIN_LISTE, CHEMIN_HISTORY, DATA_FOLDER


def assurer_dossiers():
    os.makedirs(DATA_FOLDER, exist_ok=True)


def log_action(action, details=""):
    assurer_dossiers()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ligne = f"{timestamp} | {action}"
    if details:
        ligne += f" | {details}"
    with open(CHEMIN_HISTORY, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")


def charger_liste():
    assurer_dossiers()
    try:
        with open(CHEMIN_LISTE, "r", encoding="utf-8") as f:
            return [ligne.strip() for ligne in f if ligne.strip()]
    except FileNotFoundError:
        return []


def sauvegarder_liste(shopping):
    assurer_dossiers()
    with open(CHEMIN_LISTE, "w", encoding="utf-8") as f:
        for article in shopping:
            f.write(article + "\n")


def afficher_liste(shopping):
    if not shopping:
        print("Liste vide.")
        return
    for i, item in enumerate(shopping, start=1):
        print(f"{i}. {item}")


def ajouter_articles(shopping):
    articles = input("Ajouter un ou plusieurs articles (ex: lait, pain) : ").strip().lower()
    nouveaux = [a.strip() for a in articles.split(",") if a.strip()]
    for a in nouveaux:
        if a not in shopping:
            shopping.append(a)
            print(f"{a} : ajouté.")
        else:
            print(f"{a} : déjà présent.")
    print("Liste :", shopping)
    return shopping


def supprimer_par_numero(shopping):
    if not shopping:
        print("Liste vide.")
        return shopping

    afficher_liste(shopping)
    choix = input("Numéro à supprimer : ").strip()
    if not choix.isdigit():
        print("Tu dois entrer un numéro.")
        return shopping

    idx = int(choix)
    if 1 <= idx <= len(shopping):
        supprime = shopping.pop(idx - 1)
        print(f"{supprime} : supprimé.")
    else:
        print("Numéro hors limite.")
    return shopping


def supprimer_par_nom(shopping):
    if not shopping:
        print("Liste vide.")
        return shopping

    nom = input("Nom exact à supprimer : ").strip().lower()
    if nom in shopping:
        shopping.remove(nom)
        print(f"{nom} : supprimé.")
    else:
        print(f"{nom} n'existe pas dans la liste.")
    return shopping


