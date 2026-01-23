shopping = []
def affiche_menu():
    print("\n===== MENU SHOPPING =====")
    print("1 - Ajouter un article")
    print("7 - Quitter")

def main():
    
    while True:
        affiche_menu()
        choix = input("quel est ton choix ? ").strip().lower()
        if choix == "1":
            article = input("ajouter un article : ").strip().lower()
            if article not in shopping:
                shopping.append(article)
                print(f"{article} : à était ajouter .", shopping)
                continue
            else:
                print(f"{article} : existe de dans la liste", shopping)
        elif choix == "5":
            verification = input("vous quitter ").strip().lower()
            if verification == "exit":
                print("au revoir ")
                break
                continue
            else:
                print("invalide")
                
           

if __name__ == "__main__":
    main()



            
            





