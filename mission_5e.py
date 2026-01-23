shopping = []


def afficher_menu():
    print("\n===== MENU SHOPPING =====")
    print("1 - Ajouter un article")
    print("7 - Quitter")


def demander_choix():
    choix = input("Ton choix (1/7) : ").strip()

    if choix == "":
        print("❌ Tu n'as rien écrit.")
        return None

    return choix


def ajouter_article():
    article = input("Ajouter un article : ").strip().lower()

    if article == "":
        print("❌ Tu n'as rien écrit.")
        return

    if article in shopping:
        print(f"⚠️ '{article}' est déjà dans la liste.")
        return

    shopping.append(article)
    print(f"✅ Ajouté : {article}")

    print("📌 Liste actuelle :")
    for item in shopping:
        print(f"- {item}")


def main():
    while True:
        afficher_menu()
        choix = demander_choix()

        if choix is None:
            continue

        if choix == "1":
            ajouter_article()

        elif choix == "7":
            print("✅ Fin du programme.")
            break

        else:
            print("❌ Choix invalide. Entre 1 ou 7.")


if __name__ == "__main__":
    main()


