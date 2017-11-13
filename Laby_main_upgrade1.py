# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 20:26:03 2017

@author: Grim

Laby : structure principale du jeu Labyrinthe
Jeu dans lequel on doit déplacer un personnage jusqu'a des bananes 

Script Python
Fichiers : laby_main.py, laby_classes.py, laby_constantes.py, n1, n2 + images
Table : laby_table.py

"""

import pygame
from pygame.locals import *

from laby_classes import *
from laby_constances import *

pygame.init()

#Ouverture de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((cote_fenetre, cote_fenetre), RESIZABLE)
#Icone
icone = pygame.image.load(image_icone)
pygame.display.set_icon(icone)
#Titre
pygame.display.set_caption(titre_fenetre)
#Sons 
bruit_choix = pygame.mixer.Sound(son_choix)
bruit_victoire = pygame.mixer.Sound(son_victoire)
bruit_mur = pygame.mixer.Sound(son_mur)

# Score
score = 100

#BOUCLE PRINCIPALE
continuer = 1
joue_choix = 0 #1 si le son a été mis en pause
joue_victoire= 0 
joue_mur = 0

# Ecritures 
myfont = pygame.font.SysFont('iskoolapota', 30)

while continuer:	
	#Chargement et affichage de l'écran d'accueil
	accueil = pygame.image.load(image_entree).convert()
	fenetre.blit(accueil, (0,0))
	welcome = myfont.render('WELCOME', False, (0,0,0))
	fenetre.blit(welcome,(150,100))
	enter=myfont.render('PRESS START TO PLAY', False, (0,0,0))
	fenetre.blit(enter,(80,150))

	#Rafraichissement
	pygame.display.flip()

	#On remet ces variables à 1 à chaque tour de boucle
	continuer_jeu = 1
	continuer_accueil = 1
	ecran_victoire = 0
	ecran_defaite = 0
 
 
	#BOUCLE D'ACCUEIL
	while continuer_accueil:
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met les variables 
			#de boucle à 0 pour n'en parcourir aucune et fermer
			if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
				continuer_accueil = 0
				continuer_jeu = 0
				continuer = 0
				#Variable de choix du niveau
				choix = 0
				
			elif event.type == KEYDOWN:
				if event.key == K_RETURN: # Presser entrer pour commencer le jeu 
    				    continuer_accueil= 0 # on quitte l'accueil
    				    choix ='n1'
    				    bruit_choix.play()
				#Lancement du niveau 1
#				if event.key == K_F1:
#					continuer_accueil = 0	#On quitte l'accueil
#					choix = 'n1'		#On définit le niveau à charger
#					bruit_choix.play()
#				#Lancement du niveau 2
#				elif event.key == K_F2:
#					continuer_accueil = 0
#					choix = 'n2'
#					bruit_choix.play()
#                        # Lancement du niveau 3
#				elif event.key == K_F3:
#					continuer_accueil = 0
#					choix = 'n3'
#					bruit_choix.play()
			
	#on vérifie que le joueur a bien fait un choix de niveau
	#pour ne pas charger s'il quitte
	if choix != 0:
		#Chargement du fond
		fond = pygame.image.load(image_fond).convert()

		#Génération d'un niveau à partir d'un fichier
		niveau = Niveau(choix)
		niveau.generer()
		niveau.afficher(fenetre)

		#Création de Donkey Kong
		dk = Perso("images/dk_droite.png", "images/dk_gauche.png", 
		"images/dk_haut.png", "images/dk_bas.png", niveau, bruit_mur,score)

	pygame.key.set_repeat(400, 30)			
	#BOUCLE DE JEU
	while continuer_jeu:
	
		#Limitation de vitesse de la boucle
		pygame.time.Clock().tick(30)
	
		for event in pygame.event.get():
		
			#Si l'utilisateur quitte, on met la variable qui continue le jeu
			#ET la variable générale à 0 pour fermer la fenêtre
			if event.type == QUIT:
				continuer_jeu = 0
				continuer = 0
		
			elif event.type == KEYDOWN:
				#Si l'utilisateur presse Echap ici, on revient seulement au menu
				if event.key == K_ESCAPE:
					continuer_jeu = 0
					
				#Touches de déplacement de Donkey Kong
				elif event.key == K_RIGHT:
					myfont = pygame.font.SysFont("monospace", 20)
					score_display = myfont.render(str(score), 10, (0,255,0))
					fenetre.blit(score_display, (50, 50))
					pygame.display.flip()
					score = dk.deplacer('droite')
				elif event.key == K_LEFT:
					myfont = pygame.font.SysFont("monospace", 20)
					score_display = myfont.render(str(score), 10, (0,255,0))
					fenetre.blit(score_display, (50,50))
					pygame.display.flip()
					score = dk.deplacer('gauche')
				elif event.key == K_UP:
					score = dk.deplacer('haut')
				elif event.key == K_DOWN:
					score = dk.deplacer('bas')
				print(str(score))
			elif event.type == VIDEORESIZE: # si la taille de la fênetre dépasse 500pxl le jeu s'arrête
				if event.w > 500 or event.h > 500:
					continuer = 0

			
		#Affichages aux nouvelles positions
		fenetre.blit(fond, (0,0))
		niveau.afficher(fenetre)
		fenetre.blit(dk.direction, (dk.x, dk.y)) #dk.direction = l'image dans la bonne direction
		pygame.display.flip()
  
  
           # Si score négatif , fin de jeu
		if  score == 0: 
			print('je suis là1')
			ecran_defaite = 1 
			#Rafraichissement
			while ecran_defaite: 
        			fenetre.fill(pygame.Color("black"))
        			print('je suis là2')
        			defaite = pygame.image.load(image_defaite).convert()
        			fenetre.blit(defaite, (0,0))
        			gameover = myfont.render('GAME OVER', False, (0,0,0))
        			fenetre.blit(gameover,(150,100))
        			pygame.time.delay(1000)
           
        			continuer_accueil = 0
        			print('je suis là3')
        			ecran_defaite = 0
   
    
		#Victoire -> Niveau suivant et si dernier niveau alors accueil
		elif niveau.structure[dk.case_y][dk.case_x] == 'a':
			bruit_victoire.play()
			continuer_jeu = 0 
#			ecran_victoire = 1                         
		


#		# BOUCLE POUR !GAME OVER           
#		while ecran_defaite: 
#			
#                  
#        		#Limitation de vitesse de la boucle
#			pygame.time.Clock().tick(30)	
#			for event in pygame.event.get():
#        		
#			#Si l'utilisateur quitte, on met la variable qui continue le jeu
##			ET la variable générale à 0 pour fermer la fenêtre
#			    if event.type == QUIT:
#			        continuer_jeu = 0
#			        continuer = 0
#        		
#			    elif event.type == KEYDOWN:
#			    #Si l'utilisateur presse Echap ici, on revient seulement au menu
#			        if event.key == K_ESCAPE:
#			            ecran_defaite = 0
#			            continuer_accueil = 1
           

pygame.quit()
print("END")