shopping = ["pantalon", "chemise", "veste", "chaussures"]

while True:
    print("\n====== MENU SHOPPING ======")
    print("1 - Ajouter un article")
    print("2 - Supprimer un article (par nom)")
    print("3 - Afficher la liste")
    print("4 - Trier la liste")
    print("5 - Supprimer par numéro (pop)")
    print("6 - Afficher le nombre d’articles")
    print("7 - Quitter")

    choix = input("Ton choix (1-7) : ").strip()

    if not choix.isnumeric():
        print("❌ Choix invalide : entre un numéro.")
        continue

    choix = int(choix)

    if choix < 1 or choix > 7:
        print("❌ Choix invalide : entre un numéro entre 1 et 7.")
        continue

    if choix == 1:
        article = input("Article à ajouter : ").strip()
        if article == "":
            print("❌ Article vide.")
        else:
            shopping.append(article)
            print(f"✅ Ajouté : {article}")

    elif choix == 2:
        article = input("Article à supprimer (nom exact) : ").strip()
        if article in shopping:
            shopping.remove(article)
            print(f"✅ Supprimé : {article}")
        else:
            print("❌ Cet article n'existe pas dans la liste.")

    elif choix == 3:
        if len(shopping) == 0:
            print("📭 Liste vide.")
        else:
            print("\n📌 Liste shopping :")
            for article in shopping:
                print(f"- {article}")

    elif choix == 4:
        shopping.sort()
        print("✅ Liste triée.")

    elif choix == 5:
        if len(shopping) == 0:
            print("📭 Liste vide.")
            continue

        print("\n📌 Liste numérotée :")
        for i, article in enumerate(shopping, start=1):
            print(f"{i} - {article}")

        numero = input("Numéro à supprimer : ").strip()

        if not numero.isnumeric():
            print("❌ Tu dois entrer un numéro.")
            continue

        numero = int(numero)

        if numero < 1 or numero > len(shopping):
            print("❌ Numéro invalide.")
            continue

        supprime = shopping.pop(numero - 1)
        print(f"✅ Supprimé : {supprime}")

    elif choix == 6:
        print(f"📦 Nombre d’articles : {len(shopping)}")

    elif choix == 7:
        print("✅ Fin du programme.")
        break


