from datetime import datetime

from src.ui import afficher_header, afficher_menu, demander_choix_menu, demander_client, demander_template
from src.storage import charger_liste, log_action
from src.exports import exporter_csv
from src.storage import sauvegarder_liste, supprimer_par_numero, supprimer_par_nom, ajouter_articles, afficher_liste, charger_template



def run_app():
    afficher_header()
    
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
            print("-" * 40)


        elif choix == "2":
            afficher_liste(shopping)

        elif choix == "3":
            shopping = supprimer_par_numero(shopping)
            sauvegarder_liste(shopping)
            log_action("DEL_NUM", f"{len(shopping)} total")
            print("-" * 40)


        elif choix == "4":
            shopping = supprimer_par_nom(shopping)
            sauvegarder_liste(shopping)
            log_action("DEL_NAME", f"{len(shopping)} total")
            print("-" * 40)
  

        
        elif choix == "5":
            nom = demander_template()
            if nom:
                items = charger_template(nom)
                if items:
                    shopping.clear()
                    shopping.extend(items)
                    sauvegarder_liste(shopping)
                    log_action("")
                
                print("-" * 40)

  

        elif choix == "5":
            nom = demander_template()  # ex: "arrivee" / "menage" / "depart"
            if nom:
                articles = charger_template(nom)  # lit templates/nom.txt
                if articles:
                    shopping.clear()
                    shopping.extend(articles)
                    sauvegarder_liste(shopping)
                    log_action("TEMPLATE", f"chargé: {nom} ({len(shopping)} articles)")
                    print(f"✅ Template '{nom}' chargé ({len(shopping)} articles).")
                else:
                    print("❌ Template introuvable ou vide.")


    


        elif choix == "6":
            print("EXPORT_CSV", f"{len(shopping)} item(s)")   
            print("-" * 40)



        elif choix == "0":
            log_action("QUIT", "fin du programme")
            print("\nMerci d'avoir utilisé Smart List Generator.")
            print("À bientôt 👋")
            print("-" * 40)

            break

            













































        '''elif choix == "5":
            nom = demander_template()
            items = charger_template(nom)
            if items is None:
                print("Template introuvable.")
            else:
                shopping = items[:]   # remplace la liste par le template
                sauvegarder_liste(shopping)  #écrit dans data/shopping.txt
                log_action("LOAD_TEMPLATE", f"{nom} | {len(shopping)} item(s)")
                print(f"✅ Template '{nom}' chargé avec succès ({len(shopping)} articles).")
                print("-" * 40)'''

    
