# # I Satck de 2 pages
# #___________________________________________________________________________
# #___________________________________________________________________________
#
# from PySide2.QtWidgets import QGridLayout, QLineEdit, QFormLayout, QWidget, QStackedLayout, QComboBox, QVBoxLayout, \
#     QPushButton, QTextEdit
# from PySide2 import QtWidgets
#
# from package.api.crypto import Crypter
#
# class MainWindow(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Cryptool 2S3")  # a voire
#         self.setup_ui()
#
#     def setup_ui(self):
#         self.create_widgets()
#         self.create_layouts()
#
#     def create_widgets(self):
#         layout = QVBoxLayout()
#         self.setLayout(layout)
#
#         #Creation et connection du switch
#         self.pageCombo = QComboBox()
#         self.pageCombo.addItems(["Cryper", "Decrypter"])
#         self.pageCombo.activated.connect(self.switchPage)
#
#         # Creation stack
#         self.stackedLayout = QStackedLayout()
#
#         # Page 1
#         self.page1 = QWidget()
#         self.page1Layout = QFormLayout()
#         self.page1Layout.addRow(" Saisir la chaine à crypter :", QTextEdit())
#         self.page1Layout.addRow("   Saisir key entre 1 et 42 :", QLineEdit())
#         self.page1Layout.addRow("                      Crypter :", QPushButton("Cliquer"))
#         self.page1Layout.addRow("        Votre chaine crypté :", QTextEdit())
#         self.page1.setLayout(self.page1Layout)
#         self.stackedLayout.addWidget(self.page1)
#
#         # Page 2
#         self.page2 = QWidget()
#         self.page2Layout = QFormLayout()
#         self.page2Layout.addRow("Saisir la chaine à décrypter :", QTextEdit())
#         self.page2Layout.addRow("    Saisir key entre 1 et 42 :", QLineEdit())
#         self.page2Layout.addRow("                     Decrypter :", QPushButton("Cliquer"))
#         self.page2Layout.addRow("       Votre chaine décrypté :", QTextEdit())
#         self.page2.setLayout(self.page2Layout)
#         self.stackedLayout.addWidget(self.page2)
#
#         layout.addWidget(self.pageCombo)
#         layout.addLayout(self.stackedLayout)
#
#     def switchPage(self):
#         self.stackedLayout.setCurrentIndex(self.pageCombo.currentIndex())
#
#     def create_layouts(self):
#         self.main_layout = QGridLayout(self)
#
#     def valide_crypt(self):
#         message_box = QtWidgets.QMessageBox()           # QMB message qui va s'afficher
#         message_box.setWindowTitle("Key Generator")
#         message_box.setText("La clé est generé !")
#         message_box.exec_()
#
#     def generate_crypt(self): # Connection LineEdite !!!!
#         chaine_a_crypter = self.text_box.toPlainText()  # Plain pour textEdit
#         key_crypto = self.key_box.text()                # text pour un line edit
#         crypt_affiche = Crypter(chaine_a_crypter, int(key_crypto)).crypter()
#         if crypt_affiche:
#             self.afficher_crypt(crypt_affiche)
#
#     def afficher_crypt(self, note):
#         self.crypt_box.setText(note)  # Set text pour changer le text from PySide2 import QtWidgets


# II Layout crypter           salute    key : 5
#___________________________________________________________________________
#___________________________________________________________________________
#
#
# from PySide2.QtWidgets import QGridLayout
# from PySide2 import QtWidgets
#
# from package.api.crypto import Crypter, Decrypter
#
# class MainWindow(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Cryptool 2S3")  # a voire
#         self.setup_ui()
#
#     def setup_ui(self):
#         self.create_widgets()
#         self.create_layouts()
#         self.add_widgets_to_layouts()
#         self.setup_connections()
#
#     def create_widgets(self):
#         self.text_box = QtWidgets.QTextEdit()
#         self.text_box.setPlaceholderText("Saisir la chaine à crypter")
#
#         self.key_box = QtWidgets.QLineEdit()
#         self.key_box.setPlaceholderText("Saisir key entre 1 et 42")
#
#         self.btn_clique = QtWidgets.QPushButton("Crypter")
#
#         self.crypt_box = QtWidgets.QTextEdit()
#
#
#     def create_layouts(self):
#         self.main_layout = QGridLayout(self)
#
#     def add_widgets_to_layouts(self):
#         self.main_layout.addWidget(self.text_box, 0, 0, 2, 5)
#         self.main_layout.addWidget(self.btn_clique, 2, 0, 1, 3)
#         self.main_layout.addWidget(self.key_box, 2, 4, 1, 1)
#         self.main_layout.addWidget(self.crypt_box, 3, 0, 2, 5)
#
#     def setup_connections(self):
#         self.btn_clique.clicked.connect(self.generate_crypt)
#         self.btn_clique.clicked.connect(self.valide_crypt)
#
#     def valide_crypt(self):
#         message_box = QtWidgets.QMessageBox()           # QMB message qui va s'afficher
#         message_box.setWindowTitle("Key Generator")
#         message_box.setText("La chaine est generé !")
#         message_box.exec_()
#
#     def generate_crypt(self): # Connection LineEdite !!!!
#         chaine_a_crypter = self.text_box.toPlainText()  # Plain pour textEdit
#         key_crypto = self.key_box.text()                # text pour un line edit
#         crypt_affiche = Crypter(chaine_a_crypter, int(key_crypto)).crypter()
#         if crypt_affiche:
#             self.afficher_crypt(crypt_affiche)
#
#     def afficher_crypt(self, note):
#         self.crypt_box.setText(note)  # Set text pour changer le text from PySide2 import QtWidgets

# #
# # III Layout decrypter       xg_fa2q;£z5èy_5jt}       key : 5
# #___________________________________________________________________________
# #___________________________________________________________________________
#
#
# from PySide2.QtWidgets import QGridLayout
# from PySide2 import QtWidgets
#
# from package.api.crypto import Crypter, Decrypter
#
#
# class MainWindow(QtWidgets.QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Cryptool 2S3")  # a voire
#         self.setup_ui()
#
#     def setup_ui(self):
#         self.create_widgets()
#         self.create_layouts()
#         self.add_widgets_to_layouts()
#         self.setup_connections()
#
#     def create_widgets(self):
#         self.text_box = QtWidgets.QTextEdit()
#         self.text_box.setPlaceholderText("Saisir la chaine à decrypter")
#
#         self.key_box = QtWidgets.QLineEdit()
#         self.key_box.setPlaceholderText("Saisir key entre 1 et 42")
#
#         self.btn_clique = QtWidgets.QPushButton("Derypter")
#
#         self.crypt_box = QtWidgets.QTextEdit()
#
#
#     def create_layouts(self):
#         self.main_layout = QGridLayout(self)
#
#     def add_widgets_to_layouts(self):
#         self.main_layout.addWidget(self.text_box, 0, 0, 2, 5)
#         self.main_layout.addWidget(self.btn_clique, 2, 0, 1, 3)
#         self.main_layout.addWidget(self.key_box, 2, 4, 1, 1)
#         self.main_layout.addWidget(self.crypt_box, 3, 0, 2, 5)
#
#     def setup_connections(self):
#         self.btn_clique.clicked.connect(self.generate_crypt)
#         self.btn_clique.clicked.connect(self.valide_crypt)
#
#     def valide_crypt(self):
#         message_box = QtWidgets.QMessageBox()           # QMB message qui va s'afficher
#         message_box.setWindowTitle("Key Generator")
#         message_box.setText("La chaine est reconstruite !")
#         message_box.exec_()
#
#     def generate_crypt(self): # Connection LineEdite !!!!
#         chaine_a_crypter = self.text_box.toPlainText()  # Plain pour textEdit
#         key_crypto = self.key_box.text()                # text pour un line edit
#         crypt_affiche = Decrypter(chaine_a_crypter, int(key_crypto)).decryptage()
#         if crypt_affiche:
#             self.afficher_crypt(crypt_affiche)
#
#     def afficher_crypt(self, note):
#         self.crypt_box.setText(note)  # Set text pour changer le text from PySide2 import QtWidgets
#

# #
# # IV Deux sur meme page
# #___________________________________________________________________________
# #___________________________________________________________________________


from PySide2.QtWidgets import QGridLayout
from PySide2 import QtWidgets

from package.api.crypto import Crypter, Decrypter

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cryptool 2S3")
        self.setup_ui()
        self.setStyleSheet("""
                                    background-color : rgb(20,20,20);
                                    color : rgb(220,220,220);
                                    font-size: 12px;
                                   """)

    def setup_ui(self):
        self.create_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        self.text_box = QtWidgets.QTextEdit()
        self.text_box.setPlaceholderText("Saisir la chaine à crypter")
        self.key_box = QtWidgets.QLineEdit()
        self.key_box.setPlaceholderText("Saisir key entre 1 et 10")
        self.btn_clique = QtWidgets.QPushButton("Crypter")
        self.crypt_box = QtWidgets.QTextEdit()


        self.text_box_2 = QtWidgets.QTextEdit()
        self.text_box_2.setPlaceholderText("Saisir la chaine à decrypter")
        self.key_box_2 = QtWidgets.QLineEdit()
        self.key_box_2.setPlaceholderText("Saisir key entre 1 et 10")
        self.btn_clique_2 = QtWidgets.QPushButton("Derypter")
        self.crypt_box_2 = QtWidgets.QTextEdit()

        self.info()


    def create_layouts(self):
        self.main_layout = QGridLayout(self)

    def add_widgets_to_layouts(self):
        self.main_layout.addWidget(self.text_box, 0, 0, 2, 5)
        self.main_layout.addWidget(self.btn_clique, 2, 0, 1, 3)
        self.main_layout.addWidget(self.key_box, 2, 4, 1, 1)
        self.main_layout.addWidget(self.crypt_box, 3, 0, 2, 5)

        self.main_layout.addWidget(self.text_box_2, 6, 0, 2, 5)
        self.main_layout.addWidget(self.btn_clique_2, 8, 0, 1, 3)
        self.main_layout.addWidget(self.key_box_2, 8, 4, 1, 1)
        self.main_layout.addWidget(self.crypt_box_2, 9, 0, 2, 5)

    def setup_connections(self):
        self.btn_clique.clicked.connect(self.generate_crypt)
        self.btn_clique.clicked.connect(self.valide_crypt)

    def valide_crypt(self):
        message_box = QtWidgets.QMessageBox()
        message_box.setWindowTitle("Key Generator")
        message_box.setText("Generé sans erreur  !")
        message_box.exec_()

    def info(self):
        message_box = QtWidgets.QMessageBox()
        message_box.setWindowTitle("Information")
        message_box.setText("""
                Application en cours de construction :
                         
    Bien saisir une clé entre 1 et 10 sinon des erreurs vont etre generé !
               Appuyer sur ok pour lancerl'application...
                
                                   Kiss la famille
        """)
        message_box.exec_()

    def generate_crypt(self):
        chaine_a_crypter = self.text_box.toPlainText()
        key_crypto = self.key_box.text()
        crypt_affiche = Crypter(chaine_a_crypter, int(key_crypto)).crypter()
        if crypt_affiche:
            self.afficher_crypt(crypt_affiche)

    def generate_decrypt(self):
        chaine_a_crypter = self.text_box_2.toPlainText()
        key_crypto = self.key_box_2.text()
        decrypt_affiche = Decrypter(chaine_a_crypter, int(key_crypto)).decryptage()
        if decrypt_affiche:
            self.afficher_decrypt(decrypt_affiche)

    def afficher_crypt(self, note):
        self.crypt_box.setText(note)

    def afficher_decrypt(self, note):
        self.crypt_box_2.setText(note)
    def setup_connections(self):
        self.btn_clique.clicked.connect(self.generate_crypt)
        self.btn_clique.clicked.connect(self.valide_crypt)
        self.btn_clique_2.clicked.connect(self.generate_decrypt)
        self.btn_clique_2.clicked.connect(self.valide_crypt)



