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
clr = {"red":(1.0,0.0,0.0),"green":(0.0,1.0,0.0),"blue":(0.0,0.0,1.0),"yellow":(1.0,0.835,0.0),"orange":(1.0,0.349,0.0),"white":(1.0,1.0,1.0),"black":(0.0,0.0,0.0)}

rubik_3d = []

for z in range(TAILLE):
	rubik_3d.append([])
for y in range(TAILLE):
	for z in range(TAILLE):
		rubik_3d[y].append([])
for x in range(TAILLE):
	for y in range(TAILLE):
		for z in range(TAILLE):
			rubik_3d[x][y].append(doc.addObject("Part::Box","Cube"))
for x in range(TAILLE):
	for y in range(TAILLE):
		for z in range(TAILLE):
			rubik_3d[x][y][z].Length = 1
			rubik_3d[x][y][z].Width = 1
			rubik_3d[x][y][z].Height = 1
			rubik_3d[x][y][z].Placement = App.Placement(App.Vector(x,y,z),App.Rotation(0,0,0,1))
			rubik_3d[x][y][z].ViewObject.DiffuseColor=[clr["yellow"],clr["orange"],clr["green"],clr["white"],clr["blue"],clr["red"]]

# applique un mouvement sur une face du cube (logique + objets 3D)
# rubik : le cube logique
# rubik_objects : les objets FreeCAD du cube 3D
# mouv : tuple (f, sens, double) du mouvement à effectuer
# animation : True pour afficher l'animation correspondante
def appliquer_mouvement_3D(rubik,rubik_objects,mouv,animation):
	
	# TODO
	return

# Un exemple basique d'interface utilisateur
class TestWidget(object):
		
	# la méthode appelée lors d'un clic sur le bouton exemple
	def exemple(self):
		
		print("clic")
		return
		
	# initialiser l'IU
	def init(self, parent):
		parent.setWindowTitle("Test IU")
		
		self.wExemple = QtWidgets.QWidget(parent)
		self.wExemple.setGeometry(QtCore.QRect(0, 25, 200, 200))

		# QT fonctionne sur le principe des layouts pour la présentation des éléments (voir doc)
		# ici un layout vertical ordonne les éléments en colonne
		self.vlExemple = QtWidgets.QVBoxLayout(self.wExemple)

		# un label est un texte affiché
		self.lbExemple = QtWidgets.QLabel(self.wExemple)
		self.lbExemple.setText("Exemple de label")
		self.vlExemple.addWidget(self.lbExemple)
		
		# un bouton est connecté à une méthode (ici, exemple())
		self.btExemple= QtWidgets.QPushButton(self.wExemple)
		self.btExemple.setEnabled(True)
		self.btExemple.setText("Exemple de bouton")
		self.btExemple.clicked.connect(self.exemple)
		self.vlExemple.addWidget(self.btExemple)

		return



# exemple de création d'un dock QT contenant notre IU
# voir la documentation FreeCAD / QT-GUI
dock = QtWidgets.QDockWidget() 
ui = TestWidget()
ui.init(dock)
window = QtWidgets.QApplication.activeWindow()
window.addDockWidget(QtCore.Qt.RightDockWidgetArea, dock)

Gui.SendMsgToActiveView("ViewFit")