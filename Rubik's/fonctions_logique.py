## fonctions implémentant la logique du projet : ##
## génération du cube, mélange, application des mouvements, vérifications de victoire, etc. ## 

from constantes import *
from fonctions_debug import *

import random
import copy


# génère et retourne un rubik's cube résolu
# voir constantes.py pour la réprésentation
def generer_rubik_termine():
	
	rubik = []
	for z in range(TAILLE):
		rubik.append([])
	for y in range(TAILLE):
		for z in range(TAILLE):
			rubik[y].append([])
	for x in range(TAILLE):
		for y in range(TAILLE):
			for z in range(TAILLE):
				rubik[x][y].append("---")
	
	for x in range(TAILLE):
		for y in range(TAILLE):
			rubik[x][y][0] = "Y"+rubik[x][y][0][1:]
			for z in range(1,TAILLE-1):
				rubik[x][y][z] = "N"+rubik[x][y][0][1:]
			rubik[x][y][TAILLE-1] = "W"+rubik[x][y][0][1:]
	for x in range(TAILLE):
		for z in range(TAILLE):
			rubik[x][0][z] = rubik[x][0][z][:1]+"G"+rubik[x][0][z][2:]
			for y in range(1,TAILLE-1):
				rubik[x][y][z] = rubik[x][0][z][:1]+"N"+rubik[x][0][z][2:]
			rubik[x][TAILLE-1][z] = rubik[x][0][z][:1]+"B"+rubik[x][0][z][2:]
	for y in range(TAILLE):
		for z in range(TAILLE):
			rubik[0][y][z] = rubik[0][y][z][:2]+"O"
			for x in range(1,TAILLE-1):
				rubik[x][y][z] = rubik[0][y][z][:2]+"N"
			rubik[TAILLE-1][y][z] = rubik[0][y][z][:2]+"R"
			
	# TODO
	return rubik


# genere un rubik aleatoire
# nb_mouvs : nombre de mouvements aléatoires à appliquer
# retourne un tuple (rubik, scramble) (rubik : le cube généré, scramble : liste de tuples des mouvements effectués)
def generer_rubik(nb_mouvs):
			
	# TODO	
	return

# genere un rubik mélangé grâce au scramble en paramètre
# scramble : une cdc des mouvements à effectuer (par exemple "B2 F2 F' L2 B")
def generer_rubik_scramble(scramble):
	
	# TODO			
	return
	
# applique au rubik en paramètre nb_mouvs mouvements aléatoires
# retourne le scramble (liste de tuples des mouvements effectués)
def melanger(rubik,nb_mouvs):
	
	# TODO
	return
		
	
# retourne la couleur du cubelet correspondante à la face demandée
# exemple : ("YGO", "U") renvoie "Y"
def c(cubelet,f):
	
	# TODO
	return

# les fonctions suivantes permettent d'extraire une face du rubik en paramètre
# la face retournée, une matrice à deux dimensions, est ordonnée comme si le rubik avait été déplié
# f : lettre de la face à extraire, f = caractère (U,L,F,R,B,D)
# note : ces fonctions ne modifient PAS l'orientation (couleur) des cubelets
def extraire(rubik, f):
	
	if f=="U":
		return [[rubik[x][y][TAILLE-1] for y in range(TAILLE)] for x in range(TAILLE)]
		
	if f=="L":	
		return [[rubik[0][y][z] for z in range(TAILLE)] for y in range(TAILLE)]
		
	if f=="F":
		return [[rubik[x][0][z] for x in range(TAILLE)] for z in range(TAILLE)]
		
	if f=="R":
		return [[rubik[TAILLE-1][y][z] for z in range(TAILLE)] for y in range(TAILLE)]
		
	if f=="B":
		return [[rubik[x][TAILLE-1][z] for z in range(TAILLE)] for x in range(TAILLE)]
		
	if f=="D":
		return [[rubik[x][y][0] for y in range(TAILLE)] for x in range(TAILLE)]

	
# applique une rotation à la face passée en paramètre
# cette fonction ne modifie PAS l'orientation (couleur) des cubelets
# face : matrice 2D de cubelets
# sens : True pour horaire
# double : True pour 180°
def appliquer_rotation(rubik, face, sens=True, double=False):
	
	if face=="F":
		F = extraire(rubik,"F")
		for x in range(TAILLE):
			for z in range(TAILLE):
				rubik[x][0][z] = F[x][TAILLE-1-z]
		for x in range(TAILLE):
			for z in range(TAILLE):
				rubik[x][0][z] = rubik[x][0][z][2:]+rubik[x][0][z][1:2]+rubik[x][0][z][:1]
    
	if face=="L":
		F = extraire(rubik,"L")
		for y in range(TAILLE):
			for z in range(TAILLE):
				rubik[0][TAILLE-1-y][TAILLE-1-z] = F[TAILLE-1-z][y]
		for y in range(TAILLE):
			for z in range(TAILLE):
				rubik[0][y][z] = rubik[0][y][z][1:2]+rubik[0][y][z][:1]+rubik[0][y][z][2:]
				
	if face=="R":
		F = extraire(rubik,"R")
		for y in range(TAILLE):
			for z in range(TAILLE):
				rubik[TAILLE-1][y][z] = F[TAILLE-1-z][y]
		for y in range(TAILLE):
			for z in range(TAILLE):
				rubik[TAILLE-1][y][z] = rubik[TAILLE-1][y][z][1:2]+rubik[TAILLE-1][y][z][:1]+rubik[TAILLE-1][y][z][2:]
				
	if face=="U":
		F = extraire(rubik,"U")
		for x in range(TAILLE):
			for y in range(TAILLE):
				rubik[TAILLE-1-x][TAILLE-1-y][TAILLE-1] = F[y][TAILLE-1-x]
		for x in range(TAILLE):
			for y in range(TAILLE):
				rubik[x][y][TAILLE-1] = rubik[x][y][TAILLE-1][:1]+rubik[x][y][TAILLE-1][2:]+rubik[x][y][TAILLE-1][1:2]
				
	if face=="D":
		F = extraire(rubik,"D")
		for x in range(TAILLE):
			for y in range(TAILLE):
				rubik[x][y][0] = F[y][TAILLE-1-x]
		for x in range(TAILLE):
			for y in range(TAILLE):
				rubik[x][y][0] = rubik[x][y][0][:1]+rubik[x][y][0][2:]+rubik[x][y][0][1:2]
						
	if face=="B":
		F = extraire(rubik,"B")
		for x in range(TAILLE):
			for z in range(TAILLE):
				rubik[x][TAILLE-1][z] = F[z][TAILLE-1-x]
		for x in range(TAILLE):
			for z in range(TAILLE):
				rubik[x][TAILLE-1][z] = rubik[x][TAILLE-1][z][2:]+rubik[x][TAILLE-1][z][1:2]+rubik[x][TAILLE-1][z][:1]
    
# renvoie True si la face est terminée
# face : matrice 2D de cubelets
# f : caractère (U,L,F,R,B,D)
def face_terminee(face,f):
	
	# TODO			
	return False
	
# renvoie True si le cube est terminé
def victoire(rubik):
	
	# TODO
	return False
	
# renvoie un tuple (face, sens, double) correspondant au mouvement m
# m : chaîne de caractères représentant un mouvement
# exemples: "F" renvoie ('F',True,False), "R'" renvoie ('R',False,False), "L2" renvoie ('L',False,True)
# m DOIT être valide
def mouv(m):
	
	# TODO	
	return

# renvoie une liste de tuples correspondants aux mouvements ms
# ms : chaîne de caractères représentant des mouvements (scramble)
# exemple: "F R' L2" renvoie [('F',True,False),('R',False,False),('L',False,True)]
# ms DOIT être valide
def mouvements(ms):
	
	# TODO	
	return
	
# applique les mouvements ms au cube rubik
# ms : chaîne de caractères représentant des mouvements (scramble)
def m(rubik, ms):
	
	# TODO
	return
	
# renvoie une chaîne de caractères correspondant aux mouvements mouvs
# exemple: [('F',True,False),('R',False,False),('L',False,True)] renvoie "F R' L2"
def scramble(mouvs):
	
	# TODO
	return
	
