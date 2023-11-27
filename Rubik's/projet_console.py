## le projet Rubik en interaction console (script executable) ##

from constantes import *
from fonctions_logique import *
from fonctions_console import *
from fonctions_debug import *

run = True

rubik = generer_rubik_termine()
afficher_rubik(rubik)

while run:
    saisie_mouvements(rubik)