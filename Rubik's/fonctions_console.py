## fonctions pour l'interface utilisateur en console ##

from fonctions_logique import *

# affiche un rubik en console
# le rubik est affiché en mode "déplié"
# exemple :
    # ~ WWW
    # ~ WWW
    # ~ YYY
    # ~  U

# ~ OOR GGG ORR  BBB
# ~ OOR GGG ORR  BBB
# ~ OOR GGG ORR  BBB
 # ~ L   F   R	  B

    # ~ WWW
    # ~ YYY
    # ~ YYY
    # ~  D

def afficher_rubik(rubik,TAILLE):
    
    haut = []
    for y in range(TAILLE-1,-1,-1):
        ligne = ""
        for x in range(TAILLE):
            ligne = ligne+rubik[x][y][TAILLE-1][0]
        haut.append(ligne)

    gauche = []
    for z in range(TAILLE-1,-1,-1):
        ligne = ""
        for y in range(TAILLE-1,-1,-1):
            ligne = ligne+rubik[0][y][z][2]
        gauche.append(ligne)
        
    devant = []
    for z in range(TAILLE-1,-1,-1):
        ligne = ""
        for x in range(TAILLE):
            ligne = ligne+rubik[x][0][z][1]
        devant.append(ligne)
        
    droite = []
    for z in range(TAILLE-1,-1,-1):
        ligne = ""
        for y in range(TAILLE):
            ligne = ligne+rubik[TAILLE-1][y][z][2]
        droite.append(ligne)
        
    derriere = []
    for z in range(TAILLE-1,-1,-1):
        ligne = ""
        for x in range(TAILLE-1,-1,-1):
            ligne = ligne+rubik[x][TAILLE-1][z][1]
        derriere.append(ligne)
        
    bas = []
    for y in range(TAILLE):
        ligne = ""
        for x in range(TAILLE):
            ligne = ligne+rubik[x][y][0][0]
        bas.append(ligne)
        
    rubik_text = ''
    for k in range(TAILLE-1):
        rubik_text += '    '+str(haut[k])+'\n'
    rubik_text += '    '+str(haut[TAILLE-1])+'\n     U\n'
    
    for k in range(TAILLE):
        rubik_text += str(gauche[k])+' '+str(devant[k])+' '+str(droite[k])+' '+str(derriere[k])+'\n'
    rubik_text += ' L   F   R   B\n'
    
    for k in range(TAILLE-1):
        rubik_text += '    '+str(bas[k])+'\n'
    rubik_text += '    '+str(bas[TAILLE-1])+'\n     D\n'
    
    print(rubik_text)


# retourne True si le saisie est un mouvement valide
# les mouvements valides sont une chaine de caractères sous la forme (F|L|R|U|D|B['|2])

def saisie_valide(saisie):
    
    if len(saisie)<4:
        if len(saisie)==1 and (saisie=='F' or saisie=='L' or saisie=='R' or saisie=='U' or saisie=='D' or saisie=='B'):
            return True
        if len(saisie)==2 and (saisie[0]=='F' or saisie[0]=='L' or saisie[0]=='R' or saisie[0]=='U' or saisie[0]=='D' or saisie[0]=='B') and saisie[1]=="'":
            return True
        if len(saisie)==3 and (saisie[0]=='F' or saisie[0]=='L' or saisie[0]=='R' or saisie[0]=='U' or saisie[0]=='D' or saisie[0]=='B') and saisie[1]=="'" and saisie[2]=="2":
            return True
    
# permet la saisie d'un mouvement à effectuer
# sous la forme (F|L|R|U|D|B['|2])
# lettre = face
# ' = anti-horaire
# 2 = 180°				
# renvoie toujours un tuple valide (f, sens, double) : l'utilisateur est invité à recommencer sa saisie tant que celle-ci est invalide

def saisie_mouvement(rubik,TAILLE):
    
    m = input('Entrez la rotation à effectuer (F|L|R|U|D|B)') #F'2 ou F2 ou F
    
    if saisie_valide(m):
        
        if len(m)==1:
            appliquer_rotation(rubik,m,TAILLE)
            
        if len(m)==2:
            if m[1]=="'":
                for k in range(3): appliquer_rotation(rubik,m[0],TAILLE) 
            if m[1]=='2':
                for k in range(2): appliquer_rotation(rubik,m[0],TAILLE)
            
        if len(m)==3:
            for k in range(2): appliquer_rotation(rubik,m[0],TAILLE)
            
        afficher_rubik(rubik,TAILLE)


# permet la saisie d'une suite de mouvements à effectuer		
# renvoie toujours une liste de tuples valide (f, sens, double) : l'utilisateur est invité à recommencer sa saisie tant que celle-ci est invalide
def saisie_mouvements(rubik,TAILLE):

    m = input('Entrez la rotation à effectuer (F|L|R|U|D|B)') #F'2 ou F2 ou F
    L = m.split(" ")

    for e in L:
        
        if saisie_valide(e):
            
            if len(e)==1:
                appliquer_rotation(rubik,e,TAILLE)
                
            if len(e)==2:
                if e[1]=="'":
                    for k in range(3): appliquer_rotation(rubik,e[0],TAILLE) 
                if e[1]=='2':
                    for k in range(2): appliquer_rotation(rubik,e[0],TAILLE)
            
            if len(e)==3:
                for k in range(2): appliquer_rotation(rubik,e[0],TAILLE)
                
        afficher_rubik(rubik,TAILLE)