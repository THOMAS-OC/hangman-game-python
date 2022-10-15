"""Le but du jeu est simple : deviner toute les lettres qui doivent composer un mot, 
éventuellement avec un nombre limité de tentatives et des thèmes fixés à l’avance. 
A chaque fois que le joueur devine une lettre, celle-ci est affichée. 
Dans le cas contraire, le dessin d’un pendu se met à apparaître…"""
import random as r

file = open("mots.txt", "r") #Lecture du fichier

mots = file.readlines() #Liste de mots

random_word = r.choice(mots) #Choix d'un mot
random_word = random_word.strip()

file.close()

tentative = 10

print(random_word, "\n")

correct_letters = []
incorrect_letters = []

dynamic_word = [] #Liste dynamique des lettres du mot

while tentative > 0 :
    
    if correct_letters:
        print(f"Il vous reste {len(random_word) - len(dynamic_word)} caractères à trouver ! \n ")
    else :
        print(f"Le mot que vous devez deviner comporte {len(random_word)} caractères ! \n ")

    print(dynamic_word)
    input_user = input("Veuillez saisir une lettre en minuscule sur votre clavier : \n>>> ")


    if input_user.lower() in correct_letters or input_user.lower() in incorrect_letters :
        print("Vous avez déjà utilisé cette lettre ! \n")

    elif input_user.lower() in random_word and input_user.lower() not in correct_letters :

        correct_letters.append(input_user.lower())
        dynamic_word = []

        for letter in random_word :
            if letter in correct_letters :
                dynamic_word.append(letter)
            else :
                dynamic_word.append("_")

        if list(random_word) == dynamic_word :
            print("\nVictoire !! Vous avez sauvé le condamné !!!!")
            break

        else :
            print("\n Bravo !")
        
    else :
        incorrect_letters.append(input_user.lower())
        tentative-=1
        if tentative == 0 :
            print("Echec ! le pendu est mort..")

        else :
            print(f"Raté ! Il vous reste {tentative} tentatives !\n")