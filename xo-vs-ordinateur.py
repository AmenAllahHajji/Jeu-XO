import tkinter as tk
from functools import partial
from tkinter import messagebox
from  random import *
root = tk.Tk()
root.title("Jeu XO")
root.geometry("600x600")
root.configure(bg="#ADD8E6")
joueur_humain = "X"
joueur_ordi = "O"
joueur_courant = joueur_humain
cadre = tk.Frame(root)
cadre.pack(expand=True)
def tour_ordi():
    global joueur_courant
    liste=[(i, j) for i in range(3) for j in range(3) if boutons[i][j]["text"] == ""]
    if liste:
        i, j =choice(liste)
        boutons[i][j].config(text=joueur_courant,fg="red")
        if verif_gagnant('O'):
            messagebox.showinfo("Fin du jeu", f"L'ordinateur a gagné !")
            desactiver_grille()
        elif grille_pleine():
            messagebox.showinfo("Fin du jeu", "Match nul !")
        joueur_courant = joueur_humain
def colorier_gagnant(liste):
    for i, j in liste:
        boutons[i][j].config(bg="green")
def verif_gagnant(c):
    for i in range(3):
        if boutons[i][0]["text"] == boutons[i][1]["text"] == boutons[i][2]["text"]==c:
            colorier_gagnant([(i,0), (i,1), (i,2)])
            return True
        if boutons[0][i]["text"] == boutons[1][i]["text"] == boutons[2][i]["text"]==c:
            colorier_gagnant([(0,i), (1,i), (2,i)])
            return True
    if boutons[0][0]["text"] == boutons[1][1]["text"] == boutons[2][2]["text"]==c:
        colorier_gagnant([(0,0), (1,1), (2,2)])
        return True
    if boutons[0][2]["text"] == boutons[1][1]["text"] == boutons[2][0]["text"]==c:
        colorier_gagnant([(0,2), (1,1), (2,0)])
        return True
    return False

def grille_pleine():
    for ligne in boutons:
        for btn in ligne:
            if btn["text"] == "":
                return False
    return True

def desactiver_grille():
    for ligne in boutons:
        for btn in ligne:
            btn.config(state="disabled")

def clic_case(i, j):
    global joueur_courant 
    bouton = boutons[i][j]
    if bouton["text"] == "" and joueur_courant == joueur_humain:
        bouton.config(text=joueur_courant,fg="blue")
        if verif_gagnant('X'):
            messagebox.showinfo("Fin du jeu","Le joueur "+joueur_courant+" a gagné !")
            desactiver_grille()
        elif grille_pleine():
            messagebox.showinfo("Fin du jeu", "Match nul !")
        joueur_courant = joueur_ordi
        root.after(500, tour_ordi)

def reinitialiser():
    global joueur_courant
    joueur_courant = "X"
    for ligne in boutons:
        for btn in ligne:
            btn.config(text="", state="normal",bg="white")

boutons = []
for i in range(3):
    ligne = []
    for j in range(3):
        btn = tk.Button(cadre, text="", font=("Arial", 24), width=5, height=2)
        btn.config(command=partial(clic_case, i, j))
        btn.grid(row=i, column=j)
        ligne.append(btn)
    boutons.append(ligne)

btn_reset = tk.Button(root, text="Rejouer", font=("Arial", 12), command=reinitialiser,bg="#ADD8E6")
btn_reset.pack(pady=10)
root.mainloop()

