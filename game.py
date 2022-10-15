"""Le but du jeu est simple : deviner toute les lettres qui doivent composer un mot, 
éventuellement avec un nombre limité de tentatives et des thèmes fixés à l’avance. 
A chaque fois que le joueur devine une lettre, celle-ci est affichée. 
Dans le cas contraire, le dessin d’un pendu se met à apparaître…"""
import random as r

file = open("mots.txt", "r")

mots = file.readlines()

print(r.choice(mots))