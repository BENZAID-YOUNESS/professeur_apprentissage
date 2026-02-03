import os
import csv
from datetime import datetime


FICHIER_LISTE = "shopping.txt"
HISTORY_FICHIER = "history.txt"
CLIENT = ""

# =========================
# DONNÉES
# =========================
shopping = []


# =========================
# AFFICHAGE
# =========================
def afficher_menu():
    print("\n===== MENU SHOPPING =====")
    print("1 - Ajouter des articles")
    print("2 - Afficher la liste numérotée")
    print("3 - Supprimer par numéro (pop)")
    print("4 - Supprimer par nom (remove)")
    print("5 - Quitter")
    print("6 - Exporter CSV (client + date)")


def afficher_liste_numerotee():
    if not shopping:
        print("La liste est vide.")
        return
    largeur = len(str(len(shopping)))

    for index, article in enumerate(shopping, 1):
        print(f"{index:>{largeur}} - {article}")


# =========================
# OUTILS
# =========================

def nettoyer_nom_fichier(texte: str) -> str:
    """Garde un nom simple pour fichier: lettres/chiffres/_- فقط"""
    texte = texte.strip().lower()
    ok = []
    for ch in texte:
        if ch.isalnum() or ch in ("_", "-"):
            ok.append(ch)
        elif ch in (" ", ".", ","):
            ok.append("_")
    propre = "".join(ok).strip("_")
    return propre if propre else "inconnu"


def exporter_csv():
    """Exporte la liste en CSV dans /exports avec client + timestamp."""
    
    if not CLIENT.strip():
        print("Nom du client vide. Export annulé.")
        log_action("EXPORT_CSV", "client_vide")
        return
    if not shopping:
        print("La liste est vide. Rien à exporter.")
        log_action("Export_CSV", "liste_vide")
        return
    # dossier exports
    client_safe = nettoyer_nom_fichier(CLIENT)
    dossier = os.path.join("exports", client_safe)
    os.makedirs(dossier, exist_ok=True)

    ts = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nom_fichier = f"{client_safe}_{ts}.csv"
    chemin = os.path.join(dossier, nom_fichier)

    nb_items = len(shopping)

    try:
        with open(chemin, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(["client", "timestamp", "numero", "article"])
            for i, article in enumerate(shopping, 1):
                writer.writerow([CLIENT, ts, i, article])

        print(f"✅ Export CSV créé : {chemin}")
        log_action("EXPORT_CSV", f"file={chemin} | items={nb_items}")

        conf = input("Vider la liste après export ? (o/n) : ").strip().lower()

        if conf == "o":
            shopping.clear()
            sauvegarder_liste()
            log_action("CLEAR_LIST", "apres_export")
            print("✅ Liste vidée.")
        else:
            print("ℹ️ Liste conservée.")

        #log_action("EXPORT_CSV", f"file={chemin} | items={nb_items}")

    except Exception as e:
        print("❌ Erreur export CSV :", e)
        log_action("ERROR", f"export_csv: {type(e).__name__}")



        

    


def log_action(action, details=""):
    """Écrit une ligne dans history.txt avec date/heure + action + détails."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ligne = f"{timestamp} | {action}"
    if details:
        ligne += f" | {details}"

    with open(HISTORY_FICHIER, "a", encoding="utf-8") as f:
        f.write(ligne + "\n")



def charger_liste():
    """Charge la liste depuis shopping.txt si le fichier existe."""
    global shopping
    try:
        with open(FICHIER_LISTE, "r", encoding="utf-8") as f:
            shopping = [ligne.strip() for ligne in f if ligne.strip()]
    except FileNotFoundError:
        shopping = []  # normal au premier lancement


def sauvegarder_liste():
    """Sauvegarde la liste dans shopping.txt (une ligne = un article)."""
    with open(FICHIER_LISTE, "w", encoding="utf-8") as f:
        for article in shopping:
            f.write(article + "\n")

def demander_choix_menu():
    """Retourne un choix valide parmi '1'..'5' (string)."""
    while True:
        choix = input("Quel est ton choix ? ").strip()
        if choix in {"1", "2", "3", "4", "5", "6"}:
            return choix
        print("Choix invalide. Entre un nombre de 1 à 5.")


def decouper_saisie_articles(saisie):
    """Transforme 'a, b, c' -> ['a','b','c'] sans doublons dans la saisie."""
    items = [x.strip().lower() for x in saisie.split(",") if x.strip()]
    # enlève les doublons tout en gardant l'ordre
    return list(dict.fromkeys(items))


# =========================
# ACTIONS
# =========================
def ajouter_articles():
    saisie = input("Ajouter un ou plusieurs articles (ex: lait, pain) : ").strip().lower()
    nouveaux = decouper_saisie_articles(saisie)

    if not nouveaux:
        print("Tu n'as rien saisi.")
        return

    for mot in nouveaux:
        if mot not in shopping:
            shopping.append(mot)
            log_action("ADD", mot)
        else:
            print(f"'{mot}' existe déjà dans la liste.")

    print("Liste :", shopping)


def supprimer_par_numero():
    if not shopping:
        print("La liste est vide, rien à supprimer.")
        return

    afficher_liste_numerotee()

    while True:
        saisie = input("Supprimer par numéro : ").strip()

        try:
            numero = int(saisie)  # ex: 1, 2, 3...
        except ValueError:
            log_action("ERROR", "supression numero invalide")
            print("Merci d'entrer un nombre (ex: 1, 2, 3).")
            continue

        index = numero - 1  # conversion vers index Python (0..)
        if 0 <= index < len(shopping):
            supprime = shopping.pop(index)   
            log_action("DEL_NUM", f"numero={numero} | article={supprime}")
            print(f"'{supprime}' a été supprimé. Liste : {shopping}")
            return
        else:
            log_action("ERROR", f"numero hors liste: {numero}")
            print("Numéro hors liste . Réessaie . ")

def supprimer_par_nom():
    if not shopping:
        print("La liste est vide, rien à supprimer.")
        return

    nom = input("Supprimer par nom : ").strip().lower()

    if nom in shopping:
        shopping.remove(nom)
        log_action("DEL_NAME", nom)
        print(f"'{nom}' a été supprimé. Liste : {shopping}")
    else:
        print(f"'{nom}' n'existe pas dans la liste. Liste : {shopping}")


# =========================
# PROGRAMME
# =========================
def main():
    print("=== Smart List Generator (Phase 1) ===")
    print("Démarré :", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    global CLIENT
    while True:
        CLIENT = input("Nom du client : ").strip().lower()
        if CLIENT:
            break
        print("le nom de client ne peut pas étre vide.")
    

    log_action("CLIENT", CLIENT)
    log_action("START", "lancement du programme")
    charger_liste()
    log_action("LOAD", f"{len(shopping)} article(s) chargé(s)")

    while True:
        afficher_menu()
        choix = demander_choix_menu()

        if choix == "1":
            ajouter_articles()
            sauvegarder_liste()
        elif choix == "2":
            afficher_liste_numerotee()
        elif choix == "3":
            supprimer_par_numero()
            sauvegarder_liste()
        elif choix == "4":
            supprimer_par_nom()
            sauvegarder_liste()
        elif choix == "5":
            sauvegarder_liste()
            log_action("QUIT", "sortie utilisateur")
            print("Au revoir 👋")
        elif choix == "6":
            exporter_csv()
            break


if __name__ == "__main__":
    main()
