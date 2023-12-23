## le projet Rubik en interaction console (script executable) ##

from fonctions_logique import *
from fonctions_console import *
from fonctions_debug import *

TAILLE = 3
run = True

rubik = generer_rubik_termine(TAILLE)
afficher_rubik(rubik,TAILLE)

while run:
    saisie_mouvements(rubik,TAILLE)