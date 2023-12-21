import FreeCADGui
from projet_freecad import *
from PySide import QtGui, QtCore
from constantes import *

class TestDialog(QtGui.QDialog):

    def generer(TAILLE):
        print("lol")

    def supprimer():
        rubik = []
        rubik_3d = []

    def __init__(self):
        super(TestDialog, self).__init__()

        # Définir la variable a
        a = 1  # Vous pouvez définir la valeur initiale de "a" ici

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
        
        # Désactiver le spin box si la variable "a" est égale à 1
        spinbox1.setEnabled(a != 1)

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
        button1.clicked.connect(self.generer(TAILLE))
        button2 = QtGui.QPushButton('Afficher le scramble', self)
        button3 = QtGui.QPushButton('Supprimer le cube', self)
        button3.clicked.connect(self.supprimer())
        generation_layout.addWidget(button1)

        # HLayout pour les boutons "Save" et "Load"
        hlayout_buttons = QtGui.QHBoxLayout()
        button_save = QtGui.QPushButton('Save', self)
        button_load = QtGui.QPushButton('Load', self)
        hlayout_buttons.addWidget(button_save)
        hlayout_buttons.addWidget(button_load)
        generation_layout.addLayout(hlayout_buttons)

        generation_layout.addWidget(button2)
        generation_layout.addWidget(button3)

        # Ajouter le layout vertical à la QGroupBox
        generation_group_box.setLayout(generation_layout)

        # Ajouter la QGroupBox au layout vertical de l'onglet 1
        vertical_layout1.addWidget(generation_group_box)

        # Créer une QGroupBox pour les "Mouvements"
        movements_group_box = QtGui.QGroupBox('Mouvements', self)

        # Créer un layout grid de 6 colonnes et 3 lignes
        grid_layout = QtGui.QGridLayout()

        # Ajouter des boutons dans le layout grid
        movements = ['U', 'R', 'F', 'D', 'L', 'B']
        
        for col, move in enumerate(movements):
            # Boutons pour les mouvements possibles
            button = QtGui.QPushButton(move, self)
            grid_layout.addWidget(button, 0, col)
            
            # Boutons pour les mouvements dans le sens anti-horaire
            button_ccw = QtGui.QPushButton(f"{move}'", self)
            grid_layout.addWidget(button_ccw, 1, col)
            
            # Boutons pour les mouvements à 180 degrés
            button_180 = QtGui.QPushButton(f"{move}2", self)
            grid_layout.addWidget(button_180, 2, col)

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