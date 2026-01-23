shopping = []

def afficher_menu():
    print("1 - Ajouter un article : ")
    print("2 - Supprimer un article : ")
    print("3 - Afficher les articles : ")
    print("4 - Trier les article par ordre alphabetique : ")
    print("5 - Quitter")

def main():
    while True:
        afficher_menu()

        choix = input("quel est ton choix ?: ").strip().lower()

        if choix == "1":
            article = input("ajouter un article : ").strip().lower()
            
            if article not in shopping:
                shopping.append(article)
                print(f"{article} : est ajouter . ")
            else:
                print(f"{article} : deja dans la liste .")

            print("articles dans la liste :", shopping)
            continue

        if choix == "5":
            input("vous ete sur le point de quitter : ")
            print("exit..!")
            break

if __name__ == "__main__":
    main()
