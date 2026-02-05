from datetime import datetime

from src.ui import afficher_header, afficher_menu, demander_choix_menu, demander_client
from src.storage import charger_liste, log_action
from src.exports import exporter_csv
from src.storage import sauvegarder_liste, supprimer_par_numero, supprimer_par_nom, ajouter_articles, afficher_liste


def run_app():
    afficher_header()
    print("=== Smart List Generator (Phase 6) ===")
    print("Démarré :", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    client = demander_client()
    log_action("CLIENT", client)
    log_action("START", "lancement du programme")

    shopping = charger_liste()
    log_action("LOAD", f"{len(shopping)} article(s) chargé(s)")

    while True:
        afficher_menu()
        choix = demander_choix_menu()

        if choix == "1":
            shopping = ajouter_articles(shopping)
            sauvegarder_liste(shopping)
            log_action("ADD", f"{len(shopping)} total")

        elif choix == "2":
            afficher_liste(shopping)

        elif choix == "3":
            shopping = supprimer_par_numero(shopping)
            sauvegarder_liste(shopping)
            log_action("DEL_NUM", f"{len(shopping)} total")

        elif choix == "4":
            shopping = supprimer_par_nom(shopping)
            sauvegarder_liste(shopping)
            log_action("DEL_NAME", f"{len(shopping)} total")

        elif choix == "5":
            log_action("QUIT", "fin du programme")
            print("Au revoir 👋")
            break

        elif choix == "6":
            exporter_csv(client, shopping)
            log_action("EXPORT_CSV", f"{len(shopping)} item(s)")
