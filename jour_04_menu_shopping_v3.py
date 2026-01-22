def afficher_menu():
    print("\n====== MENU SHOPPING ======")
    print("1 - Ajouter un article")
    print("2 - Supprimer un article (par nom)")
    print("3 - Afficher la liste")
    print("4 - Trier la liste")
    print("5 - Supprimer par numéro (pop)")
    print("6 - Afficher le nombre d’articles")
    print("7 - Quitter")


def demander_choix():
    choix = input("Ton choix (1-7) : ").strip()
    if not choix.isdigit():
        return 0
    return int(choix)


def main():
    shopping = []

    while True:
        afficher_menu()
        choix = demander_choix()

        if choix == 1:
            article = input("ajouter un article : ").strip()
            if article == "":
                print("pas d'article ...!")
            else:
                shopping.append(article)
                print(f"{article}: ajouter") 

        elif choix == 2:
            if len(shopping) == 0:
                print("❌ La liste est vide.")
                continue

            else:
                article = input("Nom de l'article à supprimer : ").strip().lower()

                if article == "":
                    print("❌ Tu n'as rien écrit.")
                elif article in shopping:
                    shopping.remove(article)
                    print(f"✅ Article supprimé : {article}")
                else:
                    print("❌ Article introuvable.")







        elif choix == 3:
            if len (shopping) == 0:
                print("la liste est vide ..! ")
            else:
                print("liste shopping : ")
                for  article in shopping:
                    print(f"- {article}")


        elif choix == 4:
            shopping.sort()
            print("liste: trier")

        elif choix == 5:
            if len(shopping) == 0:
                print("❌ La liste est vide.")
                continue
            else:
                print("📋 Liste numérotée :")
                for i, article in enumerate(shopping, start=1):
                    print(f"{i} - {article}")

                numero = input("Numéro à supprimer : ").strip()

            if not numero.isdigit():
                print("❌ Tu dois entrer un numéro.")
            else:
                numero = int(numero)

                if numero < 1 or numero > len(shopping):
                    print("❌ Numéro invalide.")
                else:
                    supprime = shopping.pop(numero - 1)
                    print(f"✅ Supprimé : {supprime}")


      

   
        
        elif choix == 6:
            print(f"📦 Nombre d’articles : {len(shopping)}")

        elif choix == 7:
            print("✅ Fin du programme.")
            break
        else:
                print("❌ Choix invalide. Entre un nombre de 1 à 7.")


main()





#cette code est un niveau superieur on 
#va le laisser on commentaire
#if choix == 1:
# saisie = input("Ajouter un article (ex: jupe ou jupe, chemise) : ").strip().lower()

    #if saisie == "":
        #print("❌ Rien à ajouter.")
    #else:
        #morceaux = saisie.split(",")

        #for m in morceaux:
            #article = m.strip()

            #if article == "":
                #continue

            #if article in shopping:
                #print(f"⚠️ Déjà dans la liste : {article}")
            #else:
                #shopping.append(article)
                #print(f"✅ Ajouté : {article}")'''


