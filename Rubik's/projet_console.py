## le projet Rubik en interaction console (script executable) ##

from constantes import *
from fonctions_logique import *
from fonctions_console import *

run = True

rubik = generer_rubik_termine()
print(afficher_rubik(rubik))

while run:
	saisie_mouvements(rubik)