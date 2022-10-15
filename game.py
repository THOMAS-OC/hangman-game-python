"""Le but du jeu est simple : deviner toute les lettres qui doivent composer un mot, 
Le nombre de tentative est limité à 10 essais.
A chaque fois que le joueur devine une lettre, celle-ci est affichée. 
Dans le cas contraire, le nombre de tentative diminue.."""

import random as r

file = open("mots.txt", "r") #Lecture du fichier

mots = file.readlines() #Liste de mots

random_word = r.choice(mots) # Choix d'un mot
random_word = random_word.strip()

file.close()

tentative = 10 #Nombre de tentatives maintenant la boucle

correct_letters = [] #Ensemble des lettres trouvés et corrects.
incorrect_letters = [] #Ensemble des lettres incorrects.

dynamic_word = [] # Liste dynamique des lettres du mot

remaining_characters = [] # lettres restantes

while tentative > 0 :
    print("\n -------------------------------------- \n")
    if correct_letters:
        print(f"Il vous reste {len(remaining_characters)} caractères à trouver ! \n ")
    else :
        print(f"Le mot que vous devez deviner comporte {len(random_word)} caractères ! \n ")

    print(dynamic_word)
    input_user = input("Veuillez saisir une lettre en minuscule sur votre clavier : \n>>> ")

    # Gestion des doublons de saisie
    if input_user.lower() in correct_letters or input_user.lower() in incorrect_letters :
        print("Vous avez déjà utilisé cette lettre ! \n")

    # Gestion d'une lettre trouvée
    elif input_user.lower() in random_word and input_user.lower() not in correct_letters :

        correct_letters.append(input_user.lower())

        dynamic_word = [] # reset et re-constitution du mot dynamique
        remaining_characters = []
        for letter in random_word :
            if letter in correct_letters :
                dynamic_word.append(letter)
            else :
                remaining_characters.append("_")
                dynamic_word.append("_")

        # Gestion de la victoire si le mot dynamique correspond au mot selectionné
        if list(random_word) == dynamic_word :
            print("\nVictoire !! Vous avez sauvé le condamné !!!!")
            break

        else :
            print("\nBravo !")
    
    # Gestion d'une erreur
    else :
        incorrect_letters.append(input_user.lower())
        tentative-=1
        # Cas d'échec de la partie
        if tentative == 0 :
            print("Echec ! le pendu est mort..")
            break
        # Cas tentative décrémenté
        else :
            print(f"Raté ! Il vous reste {tentative} tentatives !\n")