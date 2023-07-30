#Created by Sadek Adel
import tkinter as tk
import winsound
from tkinter import messagebox
hertz = 440
temps_son = 100



# Fonction pour déplacer la balle
def deplacer_droite_raquette1(event):
    canvas.move(raquette1,0,10)
def deplacer_gauche_raquette1(event):
    canvas.move(raquette1, 0, -10)

def deplacer_droite_raquette2(event):
    canvas.move(raquette2,0,10)
def deplacer_gauche_raquette2(event):
    canvas.move(raquette2, 0, -10)
# Variables pour les scores
score_joueur1 = 0
score_joueur2 = 0

test = 0
def deplacer_balle():
    global dx, dy  # Déclarer dx et dy comme variables globales
    global test
    global score_joueur1, score_joueur2
    canvas.move(balle, dx, dy)
    position = canvas.coords(balle)  # Récupérer les nouvelles coordonnées de la balle
    x, y = position[0], position[1]
    letesteur = test
    print("LE TESTEUR : " + str(score_joueur2+score_joueur1))



    # Vérifier si la balle touche les bords de la fenêtre
    if x <= 0 :
        # Inverser la direction horizontale (changer de dx)
        dx = -dx
        canvas.move(balle, (largeur - diametre) / 2 - x, (hauteur - diametre) / 2 - y)
        messagebox.showinfo("Message", "La balle a touché le bord gauche.")
        score_joueur2 = score_joueur2 + 1
        label_joueur2.configure(text=f"Joueur 2 : {score_joueur2}")

    elif x >= largeur - diametre:
        dx = -dx
        messagebox.showinfo("Message", "La balle a touché le bord droit.")
        canvas.move(balle, (largeur - diametre) / 2 - x, (hauteur - diametre) / 2 - y)
        #Jouer un son lors de l'impact
        winsound.Beep(hertz, temps_son)
        score_joueur1 = score_joueur1 + 1
        label_joueur1.configure(text=f"Joueur 1 : {score_joueur1}")


    if y <= 0 or y >= hauteur - diametre:
        # Inverser la direction verticale (changer de dy)
        dy = -dy
        winsound.Beep(hertz, temps_son)

    if len((canvas.find_overlapping(canvas.coords(raquette1)[0],canvas.coords(raquette1)[1],canvas.coords(raquette1)[2],canvas.coords(raquette1)[3]))) > 1:
        print("COLLISION")
        dx = -dx
        winsound.Beep(hertz, temps_son)
    elif len((canvas.find_overlapping(canvas.coords(raquette2)[0],canvas.coords(raquette2)[1],canvas.coords(raquette2)[2],canvas.coords(raquette2)[3]))) > 1:
        print("COLLISION")
        dx = -dx

    # Appeler la fonction de déplacement après un délai (en millisecondes)
    fenetre.after(delai_millis, deplacer_balle)

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Jeu de Ping Pong")





# Dimensions de la fenêtre
largeur, hauteur = 800, 600
fenetre.geometry(f"{largeur}x{hauteur}")

# Création d'un widget Canvas pour dessiner la balle
canvas = tk.Canvas(fenetre, width=largeur, height=hauteur, bg="black")
canvas.pack()



# Paramètres de la balle
diametre = 20
x, y = (largeur - diametre) / 2, (hauteur - diametre) / 2
dx, dy = 10, 10
# Vitesse de déplacement de la balle (en pixels)

# Dessiner la balle
balle = canvas.create_oval(x, y, x + diametre, y + diametre, fill="purple")

# Démarrer le déplacement de la balle
delai_millis = 30  # Délai entre chaque déplacement (en millisecondes)


# Paramètres des raquettes
raquette_largeur, raquette_hauteur = 10, 80
raquette1_x, raquette1_y = 20, (hauteur - raquette_hauteur) / 2
raquette2_x, raquette2_y = largeur - 20 - raquette_largeur, (hauteur - raquette_hauteur) / 2

# Dessiner les raquettes
raquette1 = canvas.create_rectangle(raquette1_x, raquette1_y, raquette1_x + raquette_largeur, raquette1_y + raquette_hauteur, fill="blue")
raquette2 = canvas.create_rectangle(raquette2_x, raquette2_y, raquette2_x + raquette_largeur, raquette2_y + raquette_hauteur, fill="green")

canvas.bind_all('<Right>', deplacer_droite_raquette1)
canvas.bind_all('<Left>', deplacer_gauche_raquette1)

canvas.bind_all('<s>', deplacer_droite_raquette2)
canvas.bind_all('<z>', deplacer_gauche_raquette2)

# Création d'un widget Label pour afficher les scores
label_joueur1 = tk.Label(fenetre, text=f"Joueur 1 : {score_joueur1}", font=("Arial", 18))
label_joueur1.pack(side=tk.TOP, padx=20)

label_joueur2 = tk.Label(fenetre, text=f"Joueur 2 : {score_joueur2}", font=("Arial", 18))
label_joueur2.pack(side=tk.TOP, padx=20)


deplacer_balle()


# Lancement de la boucle principale de l'application
fenetre.mainloop()
