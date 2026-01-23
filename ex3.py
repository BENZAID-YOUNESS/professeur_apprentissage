shopping = []

def affiche_menu():

    print("\n====== MENU SHOPPING ======")
    print("1 - Ajouter un article")
    print("2 - Supprimer un article (par nom)")
    print("3 - Afficher la liste")
    print("4 - Trier la liste")
    print("5 - Supprimer par numéro (pop)")
    print("6 - Afficher le nombre d’articles")
    print("7 - Quitter")

def main():
    while True:
        affiche_menu()   
        choix = input("quel est ton choix ? ") 
        
        choix == "1"
        article = input("ajouter un article : ")
        if article not in shopping:
            shopping.append(article)
            print(f"{article} : à était ajouter .", shopping)
            continue
        else:
            print(f"{article} : éxiste déja dans la liste .", shopping)
        break
if __name__ == "__main":
    main()