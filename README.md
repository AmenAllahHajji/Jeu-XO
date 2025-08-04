# 🎮 Jeu XO (Tic-Tac-Toe) en Python avec Tkinter

## Description
Ce projet est une version simple du jeu **XO (ou Tic-Tac-Toe)** développée en Python avec **Tkinter** pour l'interface graphique.

L'application propose deux modes de jeu :
- 🔹 **Contre un ami** (2 joueurs humains)
- 🔹 **Contre l'ordinateur**

## Fonctionnalités
- Interface conviviale développée avec Tkinter
- Menu principal avec deux boutons : "Jouer contre un ami" et "Jouer contre l’ordinateur"
- Affichage du gagnant ou d’une égalité
- Redémarrage d'une partie facilement

## Bibliothèques utilisées
1. **subprocess**  
   Permet de lancer des processus externes depuis un script Python.  
   Utilisée ici pour appeler d’autres interfaces ou scripts selon le mode de jeu choisi.

2. **sys**  
   Fournit des outils pour interagir avec l’environnement Python, notamment pour récupérer le chemin de l’interpréteur Python, ce qui facilite le lancement des autres scripts.
   
4. **Pillow (PIL)**  
   Bibliothèque Python pour ouvrir, manipuler, et enregistrer des images dans différents formats.  
   Utilisée ici pour charger et afficher des images dans l’interface graphique, notamment via les modules `Image` et `ImageTk` pour Tkinter.

