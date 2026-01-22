shopping = []

def afficher_menu():
    print("1 - Ajouter")
    print("2 - Supprimer")
    print("3 - Afficher")
    print("4 - Trier")
    print("5 - Quitter")

while True:
    afficher_menu()

    choix = input("quel est ton choix ?: ").strip().lower()

    if choix == "1":
        articles = input("ajouter un article : ").strip().lower()
        listes_articles = [a.strip() for a in articles.split(",") if a.strip()]

        for article in listes_articles:
            if article not in shopping:
                shopping.append(article)
                print(f"{article} : est ajouter . ")
            else:
                print(f"{article} : deja dans la liste .")

            print("articles dans la liste :", shopping)
