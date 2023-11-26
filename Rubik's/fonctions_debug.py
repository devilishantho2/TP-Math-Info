## fonctions utiles au debug programme pendant son développement ##
## ces fonctions ne font pas partie du projet final ##
## ne les implémentez que si cela vous est utile, vous pouvez évidemment en ajouter d'autres ##

from constantes import *
from fonctions_logique import *

# affiche un rubik en console en mode debug
# par exemple, affichage des 3 couleurs des cubelets :
             # ~ YGO|WBN|WBR|
             # ~ YNO|WNN|WNR|
             # ~ YBO|WGN|WGR|
                  # ~ U

# ~ YGO|YNO|YBO| YBO|WGN|WGR| WGR|WNR|WBR|   WBR|WBN|YGO|
# ~ NGO|NNO|NBO| NBO|NGN|NGR| NGR|NNR|NBR|   NBR|NBN|NGO|
# ~ WGO|WNO|WBO| WBO|YGN|YGR| YGR|YNR|YBR|   YBR|YBN|WGO|
     # ~ L            F           R               B

             # ~ WBO|YGN|YGR|
             # ~ WNO|YNN|YNR|
             # ~ WGO|YBN|YBR|
                  # ~ D
def debug_rubik(rubik):
			
    haut = []
    for y in range(TAILLE-1,-1,-1):
        ligne = ""
        for x in range(TAILLE):
            ligne = ligne+rubik[x][y][TAILLE-1]+"|"
        haut.append(ligne)

    gauche = []
    for z in range(TAILLE-1,-1,-1):
        ligne = ""
        for y in range(TAILLE-1,-1,-1):
            ligne = ligne+rubik[0][y][z]+"|"
        gauche.append(ligne)
        
    devant = []
    for z in range(TAILLE-1,-1,-1):
        ligne = ""
        for x in range(TAILLE):
            ligne = ligne+rubik[x][0][z]+"|"
        devant.append(ligne)
        
    droite = []
    for z in range(TAILLE-1,-1,-1):
        ligne = ""
        for y in range(TAILLE):
            ligne = ligne+rubik[TAILLE-1][y][z]+"|"
        droite.append(ligne)
        
    derriere = []
    for z in range(TAILLE-1,-1,-1):
        ligne = ""
        for x in range(TAILLE-1,-1,-1):
            ligne = ligne+rubik[x][TAILLE-1][z]+"|"
        derriere.append(ligne)
        
    bas = []
    for y in range(TAILLE):
        ligne = ""
        for x in range(TAILLE):
            ligne = ligne+rubik[x][y][0]+"|"
        bas.append(ligne)
        
    rubik_text = ''
    for k in range(TAILLE-1):
        rubik_text += '             '+str(haut[k])+'\n'
    rubik_text += '             '+str(haut[TAILLE-1])+'\n                  U\n'
    
    for k in range(TAILLE):
        rubik_text += str(gauche[k])+' '+str(devant[k])+' '+str(droite[k])+' '+str(derriere[k])+'\n'
    rubik_text += '     L            F            R            B\n'
    
    for k in range(TAILLE-1):
        rubik_text += '             '+str(bas[k])+'\n'
    rubik_text += '             '+str(bas[TAILLE-1])+'\n                  D\n'
    
    print(rubik_text)

# affiche une face en mode debug
# par exemple :
# ~ YGO|WBN|WBR|
# ~ YNO|WNN|WNR|
# ~ YBO|WGN|WGR|
def debug_face(face):
	
	# TODO
	return
		
