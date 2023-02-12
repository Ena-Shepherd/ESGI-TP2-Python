"""

 Author: Yannis STEFANELLI

 Creation Date: 12-02-2023 20:49:43

 Description :

"""

import random


def surface_sous_courbe(a, b, p):
    a = float(a)
    b = float(b)
    p = float(p)
    S = 0
    n = 0
    while (a + p * n) < b:
        U0 = p * (a + p * n)
        S = U0 + S
        n = n + 1
    return S

def exo1():
    a = input("entrer a : ")
    b = input("entrer b : ")
    p = input("entrer p : ")

    print("Calcul de l’intégrale de la fonction y = x * x avec " + a + "<= x < " + b + " et p = " + p)
    print(surface_sous_courbe(a, b, p))

def afficher_allumettes(n):
    allumettes = "l" * n
    print(allumettes)

def check_perdu(allumettes, piece, nom):
    if piece == 1 and allumettes == 0:
        print("L'Ordi a perdu :-(\n" + nom + " a gagné :-)\n")
        return 1
    elif allumettes == 0:
        print(nom + " a perdu :-(\n" + "L'Ordi a gagné :-)\n")
        return 1
    return 0


def exo2():

    nom = input("Entrez votre nom : ")
    allumettes = int(input("Choisir le nombre d'allumettes de départ : "))
    maxi = int(input("Choisir le nombre d'allumettes max à retirer : "))

    piece = random.randint(0, 1)

    if piece == 1:
        print("L'ordi commence\n")
    else:
        print("Vous commencez\n")

    while allumettes >= 0:
        move = random.randint(1, maxi)
        if move > allumettes:
            move = allumettes

        if maxi > allumettes:
            maxi = allumettes

        if piece == 1:
            afficher_allumettes(allumettes)
            print("L'Ordi enlève : " + str(move) + "\n")
            allumettes -= move
            result = check_perdu(allumettes, piece, nom)
            if result == 1:
                return
            piece = 0
        else:
            afficher_allumettes(allumettes)
            playermove = int(input(nom + " enlève : "))
            if playermove > maxi or playermove == 0:
                print("Vous trichez ! Passez donc votre tour en retirant " + str(maxi) + " allumettes >:)\n")
                allumettes -= maxi
            else:
                allumettes -= playermove
            result = check_perdu(allumettes, piece, nom)
            if result == 1:
                return
            piece = 1

def exo3():
    # Saisir les deux entiers
    x = int(input("Entrez le premier entier : "))
    y = int(input("Entrez le deuxième entier : "))

    # Écrire les entiers dans un fichier binaire
    with open("BDD.bin", "wb") as f:
        f.write(x.to_bytes(4, "big"))
        f.write(y.to_bytes(4, "big"))

    # Écrire les entiers dans un fichier texte
    with open("BDD.txt", "w") as f:
        f.write(str(x) + "\n")
        f.write(str(y) + "\n")

    # Lire les entiers à partir du fichier binaire
    with open("BDD.bin", "rb") as f:
        x_bin = int.from_bytes(f.read(4), "big")
        y_bin = int.from_bytes(f.read(4), "big")

    # Lire les entiers à partir du fichier texte
    with open("BDD.txt", "r") as f:
        x_txt = int(f.readline().strip())
        y_txt = int(f.readline().strip())

    # Afficher les entiers lus à partir des fichiers
    print("Entiers lus à partir de BDD.bin :", x_bin, y_bin)
    print("Entiers lus à partir de BDD.txt :", x_txt, y_txt)

class Livre:
    def __init__(self, nom, auteur, maison_edition, code_barre):
        self.nom = nom
        self.auteur = auteur
        self.maison_edition = maison_edition
        self.code_barre = code_barre
        
    def modification(self, nom=None, auteur=None, maison_edition=None, code_barre=None):
        if nom:
            self.nom = nom
        if auteur:
            self.auteur = auteur
        if maison_edition:
            self.maison_edition = maison_edition
        if code_barre:
            self.code_barre = code_barre
            
    def affichage_infos(self):
        print("Nom du livre:", self.nom)
        print("Auteur:", self.auteur)
        print("Maison d'édition:", self.maison_edition)
        print("Code barre:", self.code_barre)

def exo4():
    livre1 = Livre("L'Étranger", "Albert Camus", "Gallimard", "1234567890123")
    print("Informations du livre avant modification:")
    livre1.affichage_infos()

    livre1.modification(nom="La Peste", auteur="Albert Camus")
    print("\nInformations du livre après modification:")
    livre1.affichage_infos()

class Roman(Livre):
    def __init__(self, nom, auteur, maison_edition, code_barre, type_roman, description):
        Livre.__init__(self, nom, auteur, maison_edition, code_barre)
        self.type_roman = type_roman
        self.description = description
        
    def modification(self, nom, auteur, maison_edition, code_barre, type_roman, description):
        Livre.modification(self, nom, auteur, maison_edition, code_barre)
        self.type_roman = type_roman
        self.description = description
        
    def affichage(self):
        Livre.affichage_infos(self)
        print("Type de roman :", self.type_roman)
        print("Description :", self.description)

def exo5():
    mon_roman = Roman("Commissaire Magret", "David Palermo", "Gallimard", "16574654", "Policier", "Le commissaire Magret est un enquêteur qui apprécie cuisiner à feu doux les suspect avant de leur faire avouer\n comment ils ont fait passer leur victime à la casserolle\n")
    mon_roman.affichage()
    mon_roman.modification("Commissaire Magret, les recettes", "David Palermo", "Gallimard", "16574654", "Recettes", "Best-of des recettes du commissaire Magret\n compilées depuis tous les romans de D.Palermo")
    mon_roman.affichage()

import tkinter as tk

import tkinter as tk

class ModifyWindow:
    def __init__(self, master, livre):
        self.master = master
        self.livre = livre
        self.master.title("Modifier les informations du livre")
        
        self.label_nom = tk.Label(self.master, text="Nom")
        self.label_nom.grid(row=0, column=0)
        self.entry_nom = tk.Entry(self.master)
        self.entry_nom.grid(row=0, column=1)
        self.entry_nom.insert(0, self.livre.nom)
        
        self.label_auteur = tk.Label(self.master, text="Auteur")
        self.label_auteur.grid(row=1, column=0)
        self.entry_auteur = tk.Entry(self.master)
        self.entry_auteur.grid(row=1, column=1)
        self.entry_auteur.insert(0, self.livre.auteur)
        
        self.label_maison_edition = tk.Label(self.master, text="Maison d'édition")
        self.label_maison_edition.grid(row=2, column=0)
        self.entry_maison_edition = tk.Entry(self.master)
        self.entry_maison_edition.grid(row=2, column=1)
        self.entry_maison_edition.insert(0, self.livre.maison_edition)
        
        self.label_code_barre = tk.Label(self.master, text="Code barre")
        self.label_code_barre.grid(row=3, column=0)
        self.entry_code_barre = tk.Entry(self.master)
        self.entry_code_barre.grid(row=3, column=1)
        self.entry_code_barre.insert(0, self.livre.code_barre)
        
        self.modify_button = tk.Button(self.master, text="Modifier", command=self.modify)
        self.modify_button.grid(row=4, column=0, columnspan=2, pady=10)
        
    def modify(self):
        self.livre.nom = self.entry_nom.get()
        self.livre.auteur = self.entry_auteur.get()
        self.livre.maison_edition = self.entry_maison_edition.get()
        self.livre.code_barre = self.entry_code_barre.get()

def exo6():
    livre = Livre("Nom du livre", "Auteur du livre", "Maison d'édition du livre", "Code barre du livre")
    root = tk.Tk()
    app = ModifyWindow(master=root, livre=livre)
    root.mainloop()


while(True):
    try:
        menu = int(input("Quel exercice voulez vous executer ? 1-6 ( 0 pour quitter )\n"))
    except:
        print("Réponse inconnue, à bientôt !\n")
        exit(1)

    match menu:
        case 1:
            exo1()
        case 2:
            exo2()
        case 3:
            exo3()
        case 4:
            exo4()
        case 5:
            exo5()
        case 6:
            exo6()
        case 0:
            print("Je quitte le programme")
            exit(0)
        case _:
            print("Un chiffre entre 1 et 6 !!!")