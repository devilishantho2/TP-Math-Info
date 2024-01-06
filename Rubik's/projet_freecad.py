## le projet Rubik sous forme de macro FreeCAD ##

from fonctions_logique import *

# API pour les animations
import Draft # voir la méthode Draft.rotate()

# API pour l'Interface Utilisateur
from PySide import QtCore, QtGui, QtWidgets
import FreeCADGui

#Pour la sauvegarde
import json

doc = FreeCAD.ActiveDocument
doc = FreeCAD.newDocument()

TAILLE = 3
rubik = generer_rubik_termine(TAILLE)
clr = {"R":(1.0,0.0,0.0),"G":(0.0,1.0,0.0),"B":(0.0,0.0,1.0),"Y":(1.0,0.835,0.0),"O":(1.0,0.349,0.0),"W":(1.0,1.0,1.0),"N":(0.0,0.0,0.0)}

rubik_3d,rubik_3d_copie = [],[]
v = 6
n_melange = 0

def save():
	dico = {"R" : rubik, "T" : TAILLE}
	with open('data.json', 'w') as mon_fichier:
		json.dump(dico, mon_fichier)

def load():
	global rubik, rubik_3d,TAILLE
	rubik,rubik_3d = [], []
	with open('data.json') as mon_fichier:
    		dico = json.load(mon_fichier)
	rubik = dico["R"]
	TAILLE = dico["T"]
	for obj in doc.Objects:
		doc.removeObject(obj.Name)
	init_rubik(rubik,TAILLE)
	update_rubik(rubik,TAILLE)
		
def init_rubik(rubik,TAILLE):
	for z in range(TAILLE):
		rubik_3d.append([])
	for y in range(TAILLE):
		for z in range(TAILLE):
			rubik_3d[y].append([])
	for x in range(TAILLE):
		for y in range(TAILLE):
			for z in range(TAILLE):
				rubik_3d[x][y].append([doc.addObject("Part::Box","cubelet"+str(x)+str(y)+str(z)),(x,y,z)])
				rubik_3d[x][y][z][0].Length = 1
				rubik_3d[x][y][z][0].Width = 1
				rubik_3d[x][y][z][0].Height = 1
				rubik_3d[x][y][z][0].Placement = App.Placement(App.Vector(x,y,z),App.Rotation(0,0,0,1))
				rubik_3d[x][y][z][0].ViewObject.LineWidth = 5
				rubik_3d[x][y][z][0].ViewObject.LineColor = (0,0,0)
	
def update_rubik(rubik,TAILLE):
	for x in range(TAILLE):
		for y in range(TAILLE):
			for z in range(TAILLE):
				#GaucheDroiteAvantArriereBasHaut
				HautBas = rubik[x][y][z][0]
				AvantArriere = rubik[x][y][z][1]
				GaucheDroite = rubik[x][y][z][2]
				rubik_3d[x][y][z][0].ViewObject.DiffuseColor=[clr[GaucheDroite],clr[GaucheDroite],clr[AvantArriere],clr[AvantArriere],clr[HautBas],clr[HautBas]]

init_rubik(rubik,TAILLE)
update_rubik(rubik,TAILLE)

def copier_rubik_3d(rubik_3d,TAILLE):
	copie = []
	for x in range(TAILLE):
		copie.append([])
		for y in range(TAILLE):
			copie[x].append([])
			for z in range(TAILLE):
				copie[x][y].append([])
				for i in [0,1]:
					copie[x][y][z].append(rubik_3d[x][y][z][i])
	return copie

# applique un mouvement sur une face du cube (logique + objets 3D)
# rubik : le cube logique
# rubik_3ds : les objets FreeCAD du cube 3D
# mouv : tuple (f, sens, double) du mouvement à effectuer
# animation : True pour afficher l'animation correspondante
def appliquer_mouvement_3D(rubik_3d,mouv,animation=True):
	
	if mouv[0] == "U":

		for m in range(1+mouv[2]*1):
			for r in range(3-2*mouv[1]):
				appliquer_rotation(rubik,"U",TAILLE)
	
			if animation == True:		
				for i in range(90//v):
					for x in range(TAILLE):
						for y in range(TAILLE):
							Draft.rotate(rubik_3d[x][y][TAILLE-1][0],(1-2*mouv[1])*v,center=App.Vector(TAILLE/2,TAILLE/2,TAILLE-0.5),axis=App.Vector(0,0,1),copy=False)
					FreeCADGui.updateGui()
			else:
				for x in range(TAILLE):
					for y in range(TAILLE):
						Draft.rotate(rubik_3d[x][y][TAILLE-1][0],(1-2*mouv[1])*90,center=App.Vector(TAILLE/2,TAILLE/2,TAILLE-0.5),axis=App.Vector(0,0,1),copy=False)
				FreeCADGui.updateGui()
	
			copie = copier_rubik_3d(rubik_3d,TAILLE)
			if mouv[1]==True:
				for x in range(TAILLE):
					for y in range(TAILLE):	
						rubik_3d[x][y][TAILLE-1][0] = copie[TAILLE-1-y][x][TAILLE-1][0]
			else:
				for x in range(TAILLE):
					for y in range(TAILLE):	
						rubik_3d[x][y][TAILLE-1][0] = copie[y][TAILLE-1-x][TAILLE-1][0]

			for x in range(TAILLE):
				for y in range(TAILLE):
					pos = rubik_3d[x][y][TAILLE-1][1]
					Draft.rotate(rubik_3d[x][y][TAILLE-1][0],90,center=App.Vector(pos[0]+0.5,pos[1]+0.5,TAILLE+0.5),axis=App.Vector(0,0,1),copy=False)	
	
			update_rubik(rubik,TAILLE)

	if mouv[0] == "D":

		for m in range(1+mouv[2]*1):
			for r in range(3-2*mouv[1]):
				appliquer_rotation(rubik,"D",TAILLE)
	
			if animation == True:		
				for i in range(90//v):
					for x in range(TAILLE):
						for y in range(TAILLE):
							Draft.rotate(rubik_3d[x][y][0][0],(2*mouv[1]-1)*v,center=App.Vector(TAILLE/2,TAILLE/2,TAILLE-0.5),axis=App.Vector(0,0,1),copy=False)
					FreeCADGui.updateGui()
			else:
				for x in range(TAILLE):
					for y in range(TAILLE):
						Draft.rotate(rubik_3d[x][y][0][0],(2*mouv[1]-1)*90,center=App.Vector(TAILLE/2,TAILLE/2,TAILLE-0.5),axis=App.Vector(0,0,1),copy=False)
				FreeCADGui.updateGui()
	
			copie = copier_rubik_3d(rubik_3d,TAILLE)
			if mouv[1]==False:
				for x in range(TAILLE):
					for y in range(TAILLE):	
						rubik_3d[x][y][0][0] = copie[TAILLE-1-y][x][0][0]
			else:
				for x in range(TAILLE):
					for y in range(TAILLE):	
						rubik_3d[x][y][0][0] = copie[y][TAILLE-1-x][0][0]

			for x in range(TAILLE):
				for y in range(TAILLE):
					pos = rubik_3d[x][y][0][1]
					Draft.rotate(rubik_3d[x][y][0][0],90,center=App.Vector(pos[0]+0.5,pos[1]+0.5,0.5),axis=App.Vector(0,0,1),copy=False)	
	
			update_rubik(rubik,TAILLE)

	if mouv[0] == "F":

		for m in range(1+mouv[2]*1):
			for r in range(3-2*mouv[1]):
				appliquer_rotation(rubik,"F",TAILLE)

			if animation == True:		
				for i in range(90//v):
					for x in range(TAILLE):
						for z in range(TAILLE):
							Draft.rotate(rubik_3d[x][0][z][0],(2*mouv[1]-1)*v,center=App.Vector(TAILLE/2,0,TAILLE/2),axis=App.Vector(0,1,0),copy=False)
					FreeCADGui.updateGui()
			else:
				for x in range(TAILLE):
					for z in range(TAILLE):
						Draft.rotate(rubik_3d[x][0][z][0],(2*mouv[1]-1)*90,center=App.Vector(TAILLE/2,0,TAILLE/2),axis=App.Vector(0,1,0),copy=False)
				FreeCADGui.updateGui()
	
			copie = copier_rubik_3d(rubik_3d,TAILLE)
			if mouv[1]==True:
				for x in range(TAILLE):
					for z in range(TAILLE):	
						rubik_3d[x][0][z][0] = copie[TAILLE-1-z][0][x][0]
			else:
				for x in range(TAILLE):
					for z in range(TAILLE):	
						rubik_3d[x][0][z][0] = copie[z][0][TAILLE-1-x][0]

			for x in range(TAILLE):
				for z in range(TAILLE):
					pos = rubik_3d[x][0][z][1]
					Draft.rotate(rubik_3d[x][0][z][0],90,center=App.Vector(pos[0]+0.5,0.5,pos[2]+0.5),axis=App.Vector(0,1,0),copy=False)	
	
			update_rubik(rubik,TAILLE)

	if mouv[0] == "B":

		for m in range(1+mouv[2]*1):
			for r in range(3-2*mouv[1]):
				appliquer_rotation(rubik,"B",TAILLE)
	
			if animation == True:		
				for i in range(90//v):
					for x in range(TAILLE):
						for z in range(TAILLE):
							Draft.rotate(rubik_3d[x][TAILLE-1][z][0],(1-2*mouv[1])*v,center=App.Vector(TAILLE/2,TAILLE-0.5,TAILLE/2),axis=App.Vector(0,1,0),copy=False)
					FreeCADGui.updateGui()
			else:
				for x in range(TAILLE):
					for z in range(TAILLE):
						Draft.rotate(rubik_3d[x][TAILLE-1][z][0],(1-2*mouv[1])*90,center=App.Vector(TAILLE/2,TAILLE-0.5,TAILLE/2),axis=App.Vector(0,1,0),copy=False)
				FreeCADGui.updateGui()
	
			copie = copier_rubik_3d(rubik_3d,TAILLE)
			if mouv[1]==False:
				for x in range(TAILLE):
					for z in range(TAILLE):	
						rubik_3d[x][TAILLE-1][z][0] = copie[TAILLE-1-z][TAILLE-1][x][0]
			else:
				for x in range(TAILLE):
					for z in range(TAILLE):	
						rubik_3d[x][TAILLE-1][z][0] = copie[z][TAILLE-1][TAILLE-1-x][0]

			for x in range(TAILLE):
				for z in range(TAILLE):
					pos = rubik_3d[x][TAILLE-1][z][1]
					Draft.rotate(rubik_3d[x][TAILLE-1][z][0],90,center=App.Vector(pos[0]+0.5,TAILLE-0.5,pos[2]+0.5),axis=App.Vector(0,1,0),copy=False)	
	
			update_rubik(rubik,TAILLE)

	if mouv[0] == "L":

		for m in range(1+mouv[2]*1):
			for r in range(3-2*mouv[1]):
				appliquer_rotation(rubik,"L",TAILLE)
	
			if animation == True:		
				for i in range(90//v):
					for y in range(TAILLE):
						for z in range(TAILLE):
							Draft.rotate(rubik_3d[0][y][z][0],(2*mouv[1]-1)*v,center=App.Vector(0.5,TAILLE/2,TAILLE/2),axis=App.Vector(1,0,0),copy=False)
					FreeCADGui.updateGui()
			else:
				for y in range(TAILLE):
					for z in range(TAILLE):
						Draft.rotate(rubik_3d[0][y][z][0],(2*mouv[1]-1)*90,center=App.Vector(0.5,TAILLE/2,TAILLE/2),axis=App.Vector(1,0,0),copy=False)
				FreeCADGui.updateGui()
	
			copie = copier_rubik_3d(rubik_3d,TAILLE)
			if mouv[1]==True:
				for y in range(TAILLE):
					for z in range(TAILLE):	
						rubik_3d[0][y][z][0] = copie[0][z][TAILLE-1-y][0]
			else:
				for y in range(TAILLE):
					for z in range(TAILLE):	
						rubik_3d[0][y][z][0] = copie[0][TAILLE-1-z][y][0]

			for y in range(TAILLE):
				for z in range(TAILLE):
					pos = rubik_3d[0][y][z][1]
					Draft.rotate(rubik_3d[0][y][z][0],90,center=App.Vector(0.5,pos[1]+0.5,pos[2]+0.5),axis=App.Vector(1,0,0),copy=False)	
	
			update_rubik(rubik,TAILLE)

	if mouv[0] == "R":

		for m in range(1+mouv[2]*1):
			for r in range(3-2*mouv[1]):
				appliquer_rotation(rubik,"R",TAILLE)
	
			if animation == True:		
				for i in range(90//v):
					for y in range(TAILLE):
						for z in range(TAILLE):
							Draft.rotate(rubik_3d[TAILLE-1][y][z][0],(1-2*mouv[1])*v,center=App.Vector(TAILLE-0.5,TAILLE/2,TAILLE/2),axis=App.Vector(1,0,0),copy=False)
					FreeCADGui.updateGui()
			else:
				for y in range(TAILLE):
					for z in range(TAILLE):
						Draft.rotate(rubik_3d[TAILLE-1][y][z][0],(1-2*mouv[1])*90,center=App.Vector(TAILLE-0.5,TAILLE/2,TAILLE/2),axis=App.Vector(1,0,0),copy=False)
				FreeCADGui.updateGui()
	
			copie = copier_rubik_3d(rubik_3d,TAILLE)
			if mouv[1]==False:
				for y in range(TAILLE):
					for z in range(TAILLE):	
						rubik_3d[TAILLE-1][y][z][0] = copie[TAILLE-1][z][TAILLE-1-y][0]
			else:
				for y in range(TAILLE):
					for z in range(TAILLE):	
						rubik_3d[TAILLE-1][y][z][0] = copie[TAILLE-1][TAILLE-1-z][y][0]

			for y in range(TAILLE):
				for z in range(TAILLE):
					pos = rubik_3d[TAILLE-1][y][z][1]
					Draft.rotate(rubik_3d[TAILLE-1][y][z][0],90,center=App.Vector(TAILLE-0.5,pos[1]+0.5,pos[2]+0.5),axis=App.Vector(1,0,0),copy=False)	
	
			update_rubik(rubik,TAILLE)



class TestDialog(QtGui.QDialog):

    def generer(self):
        global TAILLE, init_rubik, update_rubik, rubik, generer_rubik_termine
        rubik = generer_rubik_termine(TAILLE)
        init_rubik(rubik,TAILLE)
        update_rubik(rubik,TAILLE)
        Gui.SendMsgToActiveView("ViewFit")
        Gui.ActiveDocument.ActiveView.viewIsometric()

    def supprimer(self):
        global rubik, rubik_3d
        rubik = []
        for obj in doc.Objects:
            doc.removeObject(obj.Name)
        rubik_3d = []

    def TailleChanged(self,t):
        global TAILLE
        TAILLE = t

    def NMChanged(self,n):
        global n_melange
        n_melange = n

    def scramble(self):
        melange,melange_texte = melanger(n_melange)
        print(melange_texte)
        for e in melange:
            appliquer_mouvement_3D(rubik_3d,e,True)

    def __init__(self):

        super(TestDialog, self).__init__()

        # Créer un QTabWidget
        tab_widget = QtGui.QTabWidget(self)

        # Onglet 1
        tab1 = QtGui.QWidget()

        # Créer un layout vertical dans l'onglet 1
        vertical_layout1 = QtGui.QVBoxLayout(tab1)

        # Créer une QGroupBox pour accueillir le layout vertical
        generation_group_box = QtGui.QGroupBox('Génération', self)

        # Créer un layout vertical dans la QGroupBox
        generation_layout = QtGui.QVBoxLayout()

        # HLayout avec un label "Taille" et une spinbox
        hlayout1 = QtGui.QHBoxLayout()
        label1 = QtGui.QLabel('Taille', self)
        spinbox1 = QtGui.QSpinBox(self)
        spinbox1.setMinimum(0)
        spinbox1.valueChanged.connect(lambda: self.TailleChanged(spinbox1.value()))

        hlayout1.addWidget(label1)
        hlayout1.addWidget(spinbox1)
        generation_layout.addLayout(hlayout1)

        # Label "Mélange"
        label2 = QtGui.QLabel('Mélange', self)
        generation_layout.addWidget(label2)

        # HLayout avec un label "Nombre de mouvements" et une spinbox
        hlayout2 = QtGui.QHBoxLayout()
        label3 = QtGui.QLabel('Nombre de mouvements', self)
        spinbox2 = QtGui.QSpinBox(self)
        spinbox2.setMinimum(0)
        spinbox2.valueChanged.connect(lambda: self.NMChanged(spinbox2.value()))
        hlayout2.addWidget(label3)
        hlayout2.addWidget(spinbox2)
        generation_layout.addLayout(hlayout2)

        # HLayout avec un label "ou scramble" et une zone de texte
        hlayout3 = QtGui.QHBoxLayout()
        label4 = QtGui.QLabel('ou scramble', self)
        line_edit = QtGui.QLineEdit(self)
        hlayout3.addWidget(label4)
        hlayout3.addWidget(line_edit)
        generation_layout.addLayout(hlayout3)

        # Trois boutons avec les nouveaux noms
        button1 = QtGui.QPushButton('Générer le cube', self)
        button1.clicked.connect(lambda: self.generer())
        button2 = QtGui.QPushButton('Scramble', self)
        button2.clicked.connect(lambda: self.scramble())
        button3 = QtGui.QPushButton('Supprimer le cube', self)
        button3.clicked.connect(lambda: self.supprimer())

        # HLayout pour les boutons "Save" et "Load"
        hlayout_buttons = QtGui.QHBoxLayout()
        button_save = QtGui.QPushButton('Save', self)
        button_save.clicked.connect(lambda: save())
        button_load = QtGui.QPushButton('Load', self)
        button_load.clicked.connect(lambda: load())
        hlayout_buttons.addWidget(button_save)
        hlayout_buttons.addWidget(button_load)

        generation_layout.addWidget(button1)        
        generation_layout.addWidget(button3)
        generation_layout.addWidget(button2)
        generation_layout.addLayout(hlayout_buttons)



        # Ajouter le layout vertical à la QGroupBox
        generation_group_box.setLayout(generation_layout)

        # Ajouter la QGroupBox au layout vertical de l'onglet 1
        vertical_layout1.addWidget(generation_group_box)

        # Créer une QGroupBox pour les "Mouvements"
        movements_group_box = QtGui.QGroupBox('Mouvements', self)

        # Créer un layout grid de 6 colonnes et 3 lignes
        grid_layout = QtGui.QGridLayout()
        
        #TOUT LES BOUTONS ALED
        #Normal
        b1 = QtGui.QPushButton("L", self)
        b1.clicked.connect(lambda: appliquer_mouvement_3D(rubik_3d,("L",True,False),True))
        grid_layout.addWidget(b1, 0, 0)
        
        b2 = QtGui.QPushButton("F", self)
        b2.clicked.connect(lambda: appliquer_mouvement_3D(rubik_3d,("F",True,False),True))
        grid_layout.addWidget(b2, 0, 1)

        b3 = QtGui.QPushButton("R", self)
        b3.clicked.connect(lambda: appliquer_mouvement_3D(rubik_3d,("R",True,False),True))
        grid_layout.addWidget(b3, 0, 2)

        b4 = QtGui.QPushButton("U", self)
        b4.clicked.connect(lambda: appliquer_mouvement_3D(rubik_3d,("U",True,False),True))
        grid_layout.addWidget(b4, 0, 3)

        b5 = QtGui.QPushButton("D", self)
        b5.clicked.connect(lambda: appliquer_mouvement_3D(rubik_3d,("D",True,False),True))
        grid_layout.addWidget(b5, 0, 4)

        b6 = QtGui.QPushButton("B", self)
        b6.clicked.connect(lambda: appliquer_mouvement_3D(rubik_3d,("B",True,False),True))
        grid_layout.addWidget(b6, 0, 5)

        #Inverse
        b7 = QtGui.QPushButton("L'", self)
        b7.clicked.connect(lambda: appliquer_mouvement_3D(rubik_3d,("L",False,False),True))
        grid_layout.addWidget(b7, 1, 0)
        
        b8 = QtGui.QPushButton("F'", self)
        b8.clicked.connect(lambda: appliquer_mouvement_3D(rubik_3d,("F",False,False),True))
        grid_layout.addWidget(b8, 1, 1)

        b9 = QtGui.QPushButton("R'", self)
        b9.clicked.connect(lambda: appliquer_mouvement_3D(rubik_3d,("R",False,False),True))
        grid_layout.addWidget(b9, 1, 2)

        b10 = QtGui.QPushButton("U'", self)
        b10.clicked.connect(lambda: appliquer_mouvement_3D(rubik_3d,("U",False,False),True))
        grid_layout.addWidget(b10, 1, 3)

        b11 = QtGui.QPushButton("D'", self)
        b11.clicked.connect(lambda: appliquer_mouvement_3D(rubik_3d,("D",False,False),True))
        grid_layout.addWidget(b11, 1, 4)

        b12 = QtGui.QPushButton("B'", self)
        b12.clicked.connect(lambda: appliquer_mouvement_3D(rubik_3d,("B",False,False),True))
        grid_layout.addWidget(b12, 1, 5)

        #Double
        b13 = QtGui.QPushButton("L2", self)
        b13.clicked.connect(lambda: appliquer_mouvement_3D(rubik_3d,("L",True,True),True))
        grid_layout.addWidget(b13, 2, 0)
        
        b14 = QtGui.QPushButton("F2", self)
        b14.clicked.connect(lambda: appliquer_mouvement_3D(rubik_3d,("F",True,True),True))
        grid_layout.addWidget(b14, 2, 1)

        b15 = QtGui.QPushButton("R2", self)
        b15.clicked.connect(lambda: appliquer_mouvement_3D(rubik_3d,("R",True,True),True))
        grid_layout.addWidget(b15, 2, 2)

        b16 = QtGui.QPushButton("U2", self)
        b16.clicked.connect(lambda: appliquer_mouvement_3D(rubik_3d,("U",True,True),True))
        grid_layout.addWidget(b16, 2, 3)

        b17 = QtGui.QPushButton("D2", self)
        b17.clicked.connect(lambda: appliquer_mouvement_3D(rubik_3d,("D",True,True),True))
        grid_layout.addWidget(b17, 2, 4)

        b18 = QtGui.QPushButton("B2", self)
        b18.clicked.connect(lambda: appliquer_mouvement_3D(rubik_3d,("B",True,True),True))
        grid_layout.addWidget(b18, 2, 5)

        # Ajouter le layout grid à la QGroupBox des "Mouvements"
        movements_group_box.setLayout(grid_layout)

        # Ajouter la QGroupBox des "Mouvements" au layout vertical de l'onglet 1
        vertical_layout1.addWidget(movements_group_box)

        # Ajouter l'onglet 1 au QTabWidget
        tab_widget.addTab(tab1, "Cube")

        # Onglet 2
        tab2 = QtGui.QWidget()

        # Créer un layout vertical dans l'onglet 2
        vertical_layout2 = QtGui.QVBoxLayout(tab2)

        # Ajouter un label à l'onglet 2
        label = QtGui.QLabel('Ceci est l\'onglet Aide', self)
        vertical_layout2.addWidget(label, alignment=QtCore.Qt.AlignTop)  # Aligner vers le haut

        # Ajouter l'onglet 2 au QTabWidget
        tab_widget.addTab(tab2, "Aide")

        # Ajouter le QTabWidget au layout vertical principal
        main_layout = QtGui.QVBoxLayout(self)
        main_layout.addWidget(tab_widget)

        # Redimensionner la fenêtre
        self.resize(500, 300)

# Fonction pour créer et afficher le dock
def show_dock_widget():
    # Créer une instance de la classe TestDialog
    dialog = TestDialog()

    # Créer un widget de dock
    dock_widget = QtGui.QDockWidget("Rubik's cube", FreeCADGui.getMainWindow())
    dock_widget.setWidget(dialog)

    # Ajouter le widget de dock à FreeCAD
    FreeCADGui.getMainWindow().addDockWidget(QtCore.Qt.RightDockWidgetArea, dock_widget)

    # Afficher le widget de dock
    dock_widget.show()

show_dock_widget()

Gui.ActiveDocument.ActiveView.viewIsometric()
Gui.SendMsgToActiveView("ViewFit")