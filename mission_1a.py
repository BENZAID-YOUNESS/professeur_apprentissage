shopping = []

while True:

    print("- menu : ")
    print("1- ajouter : ")
    print("2- suprimer un article par non :")
    print("7- quitter .")

    choix = input("ton choix : ")
    if choix == "":
        print("tu n'as rien ecrit..! ")
        continue
    
    if choix == "1":
        article = input("ajouter un article : ").strip().lower()
        if article == "":
            print ("tu n'as rien ecrit..! ")
        else:
            shopping.append(article)
            print(f"{article} : etait ajouter .")

    elif choix == "2":
        if len(shopping) == 0:
            print("laliste est vide..!")
            continue

        article = input("entrer nom à suprimer : ").strip().lower()
        if article == "":
            print("tu as rien ecrit... ")
            continue

        if article in shopping:
            shopping.remove(article)
            print(f"{article} : est suprimer .")
        else:
            print(f"{article} : introuvable")
            


   
  
    
     
   
        
    
        



