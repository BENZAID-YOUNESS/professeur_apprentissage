shopping = []
def afficche_menu():
    print("\n===== MENU SHOPPING =====")
    print("1 - Ajouter un article")
    print("7 - Quitter")

def main():
    afficche_menu
    while True:
        choix = input("quel est ton choix : ").strip().lower()  
        if choix  == "1":
            article = input("ajouter un article : ").strip().lower()
            if article not in shopping:
                shopping.append(article)
                print(f"{article} : à etait ajoute ." , shopping )
                continue
            else:
                print(f"{article} : existe déja dans la liste..! " , shopping )
                continue
                
        elif choix == "5":
            choix = input("tape exit pour quitter .").strip().lower()
            if  choix == "exit":
                print("au revoir . ")    
            else:
                print("non valide")
                continue
        break             
if __name__ == "__main__":
    main()           
 