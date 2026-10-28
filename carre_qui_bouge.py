from casioplot import *
from random import *

# Taille du côté du carré à attraper
global A
A = 5

# Taille du côté de notre carré
global B
B = 3

# Nombre de points avant la fin
global fin
fin = 10

def game():
    global compteur, coup
    compteur = 0
    coup = 0

    # Positions de depart du carre
    x = 150
    y = 80

    cible_x = randint(8, 379)
    cible_y = randint(8, 184)

    while compteur <= fin:
        # 1. Effaçage de l'écran
        clear_screen()
        draw_string(0, 0, "Score: " + str(compteur))

        # 2. Dessin du carré à attraper
        for dx in range(A):
            for dy in range(A):
                set_pixel(cible_x + dx, cible_y - dy, (255, 0, 0))
        
        # 3. Dessin du carré joueur
        for gx in range(B):
            for gy in range(B):
                set_pixel(x + gx, y - gy, (0, 0, 0))

        # 4. Affichage du dessin
        show_screen()
        
        # 5. Attendre la pression d'une touche
        t = getkey()
        
        # 6. L'action en fonction de la touche préssée
        if t == 14 and y > 8: # Haut
            y = y - 4
            coup += 1
        if t == 34 and y < 184: # Bas
            y = y + 4
            coup += 1
        if t == 23 and x > 8: # Gauche
            x = x - 4
            coup += 1
        if t == 25 and x < 379: # Droite
            x = x + 4
            coup += 1

        # 7. Collision avec le carré rouge
        if (x < cible_x + 3 and x + 3 > cible_x and y - 3 < cible_y and y > cible_y - 3):
            cible_x = randint(8, 379)
            cible_y = randint(8, 184)
            compteur += 1

    # ÉCRAN DE FIN ET MENU 
    choix = 0  # 0 = Rejouer, 1 = Quitter
    
    while True:
        clear_screen()
        
        # Textes de victoire
        draw_string(145, 30, "BIEN JOUE !")
        draw_string(140, 60, "Tu as reussi !")
        draw_string(105, 90, "Total de coups : " + str(coup))
        draw_string(110, 120, "Selectionner avec < >")
        
        # Gestion des couleurs selon le choix actif (Vert si sélectionné, Noir sinon)
        if choix == 0:
            couleur_rejouer = (0, 255, 0)  # Vert
            couleur_quitter = (0, 0, 0)    # Noir
        else:
            couleur_rejouer = (0, 0, 0)    # Noir
            couleur_quitter = (0, 255, 0)  # Vert
            
        # Affichage des boutons du menu
        draw_string(80, 150, "Rejouer", couleur_rejouer)
        draw_string(250, 150, "Quitter", couleur_quitter)
        
        show_screen()
        
        # Lecture des touches
        t_menu = getkey()
        
        if t_menu == 23:  # Flèche Gauche (<)
            choix = 0
        elif t_menu == 25:  # Flèche Droite (>)
            choix = 1
        elif t_menu == 95:  # Touche OK/EXE
            if choix == 0:
                game()  # Relance une partie
                break
            else:
                break   # Quitte complètement le jeu

# Lancement initial du jeu
game()

clear_screen()
draw_string(115, 90, "Appuyer sur : AC")