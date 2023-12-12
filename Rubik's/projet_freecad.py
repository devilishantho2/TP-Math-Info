## le projet Rubik sous forme de macro FreeCAD ##

from constantes import *
from fonctions_logique import *

# API pour les animations
import Draft # voir la méthode Draft.rotate()

# API pour l'Interface Utilisateur
from PySide2 import QtCore, QtGui, QtWidgets

doc = FreeCAD.ActiveDocument
doc = FreeCAD.newDocument()

rubik = generer_rubik_termine()
clr = {"R":(1.0,0.0,0.0),"G":(0.0,1.0,0.0),"B":(0.0,0.0,1.0),"Y":(1.0,0.835,0.0),"O":(1.0,0.349,0.0),"W":(1.0,1.0,1.0),"N":(0.0,0.0,0.0)}

rubik_3d,rubik_3d_copie = [],[]
v = 6
			
def init_rubik(rubik):
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
	
def update_rubik(rubik):
	for x in range(TAILLE):
		for y in range(TAILLE):
			for z in range(TAILLE):
				#GaucheDroiteAvantArriereBasHaut
				HautBas = rubik[x][y][z][0]
				AvantArriere = rubik[x][y][z][1]
				GaucheDroite = rubik[x][y][z][2]
				rubik_3d[x][y][z][0].ViewObject.DiffuseColor=[clr[GaucheDroite],clr[GaucheDroite],clr[AvantArriere],clr[AvantArriere],clr[HautBas],clr[HautBas]]

init_rubik(rubik)
update_rubik(rubik)

def copier_rubik_3d(rubik_3d):
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
# rubik_objects : les objets FreeCAD du cube 3D
# mouv : tuple (f, sens, double) du mouvement à effectuer
# animation : True pour afficher l'animation correspondante
def appliquer_mouvement_3D(rubik_3d,mouv,animation=True):
	
	if mouv[0] == "U":

		for m in range(1+mouv[2]*1):
			for r in range(3-2*mouv[1]):
				appliquer_rotation(rubik,"U")
	
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
	
			copie = copier_rubik_3d(rubik_3d)
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
	
			update_rubik(rubik)

	if mouv[0] == "D":

		for m in range(1+mouv[2]*1):
			for r in range(3-2*mouv[1]):
				appliquer_rotation(rubik,"D")
	
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
	
			copie = copier_rubik_3d(rubik_3d)
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
	
			update_rubik(rubik)

	if mouv[0] == "F":

		for m in range(1+mouv[2]*1):
			for r in range(3-2*mouv[1]):
				appliquer_rotation(rubik,"F")

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
	
			copie = copier_rubik_3d(rubik_3d)
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
	
			update_rubik(rubik)

	if mouv[0] == "B":

		for m in range(1+mouv[2]*1):
			for r in range(3-2*mouv[1]):
				appliquer_rotation(rubik,"B")
	
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
	
			copie = copier_rubik_3d(rubik_3d)
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
	
			update_rubik(rubik)

	if mouv[0] == "L":

		for m in range(1+mouv[2]*1):
			for r in range(3-2*mouv[1]):
				appliquer_rotation(rubik,"L")
	
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
	
			copie = copier_rubik_3d(rubik_3d)
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
	
			update_rubik(rubik)

	if mouv[0] == "R":

		for m in range(1+mouv[2]*1):
			for r in range(3-2*mouv[1]):
				appliquer_rotation(rubik,"R")
	
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
	
			copie = copier_rubik_3d(rubik_3d)
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
	
			update_rubik(rubik)

# Un exemple basique d'interface utilisateur
class Widget(object):

	# initialiser l'IU
	def init(self,parent):
		parent.setWindowTitle("Test IU")
		
		self.w = QtWidgets.QWidget(parent)
		self.w.setGeometry(QtCore.QRect(0, 25, 400, 200))

		# QT fonctionne sur le principe des layouts pour la présentation des éléments (voir doc)
		# ici un layout vertical ordonne les éléments en colonne
		self.vlExemple = QtWidgets.QGridLayout(self.w)

		# un label est un texte affiché
		self.lbExemple = QtWidgets.QLabel(self.w)
		self.lbExemple.setText("Rotations")
		self.vlExemple.addWidget(self.lbExemple,0,0)
		
		#ROTATIONS
		self.TurnUpB= QtWidgets.QPushButton(self.w)
		self.TurnUpB.setEnabled(True)
		self.TurnUpB.setText("U")
		self.TurnUpB.clicked.connect(self.TurnUp)
		self.vlExemple.addWidget(self.TurnUpB,1,0)

		self.TurnDownB= QtWidgets.QPushButton(self.w)
		self.TurnDownB.setEnabled(True)
		self.TurnDownB.setText("D")
		self.TurnDownB.clicked.connect(self.TurnDown)
		self.vlExemple.addWidget(self.TurnDownB,1,1)

		self.TurnFrontB= QtWidgets.QPushButton(self.w)
		self.TurnFrontB.setEnabled(True)
		self.TurnFrontB.setText("F")
		self.TurnFrontB.clicked.connect(self.TurnFront)
		self.vlExemple.addWidget(self.TurnFrontB,1,2)

		self.TurnBackB= QtWidgets.QPushButton(self.w)
		self.TurnBackB.setEnabled(True)
		self.TurnBackB.setText("B")
		self.TurnBackB.clicked.connect(self.TurnBack)
		self.vlExemple.addWidget(self.TurnBackB,1,3)

		self.TurnLeftB= QtWidgets.QPushButton(self.w)
		self.TurnLeftB.setEnabled(True)
		self.TurnLeftB.setText("L")
		self.TurnLeftB.clicked.connect(self.TurnLeft)
		self.vlExemple.addWidget(self.TurnLeftB,1,4)

		self.TurnRightB= QtWidgets.QPushButton(self.w)
		self.TurnRightB.setEnabled(True)
		self.TurnRightB.setText("R")
		self.TurnRightB.clicked.connect(self.TurnRight)
		self.vlExemple.addWidget(self.TurnRightB,1,5)

		#ROTATIONS INVERSE
		self.TurnUpB= QtWidgets.QPushButton(self.w)
		self.TurnUpB.setEnabled(True)
		self.TurnUpB.setText("U'")
		self.TurnUpB.clicked.connect(self.TurnUpI)
		self.vlExemple.addWidget(self.TurnUpB,2,0)

		self.TurnDownB= QtWidgets.QPushButton(self.w)
		self.TurnDownB.setEnabled(True)
		self.TurnDownB.setText("D'")
		self.TurnDownB.clicked.connect(self.TurnDownI)
		self.vlExemple.addWidget(self.TurnDownB,2,1)

		self.TurnFrontB= QtWidgets.QPushButton(self.w)
		self.TurnFrontB.setEnabled(True)
		self.TurnFrontB.setText("F'")
		self.TurnFrontB.clicked.connect(self.TurnFrontI)
		self.vlExemple.addWidget(self.TurnFrontB,2,2)

		self.TurnBackB= QtWidgets.QPushButton(self.w)
		self.TurnBackB.setEnabled(True)
		self.TurnBackB.setText("B'")
		self.TurnBackB.clicked.connect(self.TurnBackI)
		self.vlExemple.addWidget(self.TurnBackB,2,3)

		self.TurnLeftB= QtWidgets.QPushButton(self.w)
		self.TurnLeftB.setEnabled(True)
		self.TurnLeftB.setText("L'")
		self.TurnLeftB.clicked.connect(self.TurnLeftI)
		self.vlExemple.addWidget(self.TurnLeftB,2,4)

		self.TurnRightB= QtWidgets.QPushButton(self.w)
		self.TurnRightB.setEnabled(True)
		self.TurnRightB.setText("R'")
		self.TurnRightB.clicked.connect(self.TurnRightI)
		self.vlExemple.addWidget(self.TurnRightB,2,5)

		#ROTATIONS DOUBLE
		self.TurnUpB= QtWidgets.QPushButton(self.w)
		self.TurnUpB.setEnabled(True)
		self.TurnUpB.setText("U2")
		self.TurnUpB.clicked.connect(self.TurnUp2)
		self.vlExemple.addWidget(self.TurnUpB,3,0)

		self.TurnDownB= QtWidgets.QPushButton(self.w)
		self.TurnDownB.setEnabled(True)
		self.TurnDownB.setText("D2")
		self.TurnDownB.clicked.connect(self.TurnDown2)
		self.vlExemple.addWidget(self.TurnDownB,3,1)

		self.TurnFrontB= QtWidgets.QPushButton(self.w)
		self.TurnFrontB.setEnabled(True)
		self.TurnFrontB.setText("F2")
		self.TurnFrontB.clicked.connect(self.TurnFront2)
		self.vlExemple.addWidget(self.TurnFrontB,3,2)

		self.TurnBackB= QtWidgets.QPushButton(self.w)
		self.TurnBackB.setEnabled(True)
		self.TurnBackB.setText("B2")
		self.TurnBackB.clicked.connect(self.TurnBack2)
		self.vlExemple.addWidget(self.TurnBackB,3,3)

		self.TurnLeftB= QtWidgets.QPushButton(self.w)
		self.TurnLeftB.setEnabled(True)
		self.TurnLeftB.setText("L2")
		self.TurnLeftB.clicked.connect(self.TurnLeft2)
		self.vlExemple.addWidget(self.TurnLeftB,3,4)

		self.TurnRightB= QtWidgets.QPushButton(self.w)
		self.TurnRightB.setEnabled(True)
		self.TurnRightB.setText("R2")
		self.TurnRightB.clicked.connect(self.TurnRight2)
		self.vlExemple.addWidget(self.TurnRightB,3,5)

	# la méthode appelée lors d'un clD(ic sur le bouton exemple
	def TurnUp(self):
		appliquer_mouvement_3D(rubik_3d,("U",True,False),True)

	def TurnDown(self):
		appliquer_mouvement_3D(rubik_3d,("D",True,False),True)

	def TurnFront(self):
		appliquer_mouvement_3D(rubik_3d,("F",True,False),True)

	def TurnBack(self):
		appliquer_mouvement_3D(rubik_3d,("B",True,False),True)

	def TurnLeft(self):
		appliquer_mouvement_3D(rubik_3d,("L",True,False),True)

	def TurnRight(self):
		appliquer_mouvement_3D(rubik_3d,("R",True,False),True)


	def TurnUpI(self):
		appliquer_mouvement_3D(rubik_3d,("U",False,False),True)

	def TurnDownI(self):
		appliquer_mouvement_3D(rubik_3d,("D",False,False),True)

	def TurnFrontI(self):
		appliquer_mouvement_3D(rubik_3d,("F",False,False),True)

	def TurnBackI(self):
		appliquer_mouvement_3D(rubik_3d,("B",False,False),True)

	def TurnLeftI(self):
		appliquer_mouvement_3D(rubik_3d,("L",False,False),True)

	def TurnRightI(self):
		appliquer_mouvement_3D(rubik_3d,("R",False,False),True)


	def TurnUp2(self):
		appliquer_mouvement_3D(rubik_3d,("U",True,True),True)

	def TurnDown2(self):
		appliquer_mouvement_3D(rubik_3d,("D",True,True),True)

	def TurnFront2(self):
		appliquer_mouvement_3D(rubik_3d,("F",True,True),True)

	def TurnBack2(self):
		appliquer_mouvement_3D(rubik_3d,("B",True,True),True)

	def TurnLeft2(self):
		appliquer_mouvement_3D(rubik_3d,("L",True,True),True)

	def TurnRight2(self):
		appliquer_mouvement_3D(rubik_3d,("R",True,True),True)

# exemple de création d'un dock QT contenant notre IU
# voir la documentation FreeCAD / QT-GUI
dock = QtWidgets.QDockWidget() 
ui = Widget()
ui.init(dock)
window = QtWidgets.QApplication.activeWindow()
window.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)

Gui.ActiveDocument.ActiveView.viewIsometric()
Gui.SendMsgToActiveView("ViewFit")