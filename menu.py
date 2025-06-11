import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
import sys
def jouer_avec_ami():
    subprocess.Popen([sys.executable, "XO-entre-amis.py"])
    root.destroy()
def jouer_contre_ordi():
    subprocess.Popen([sys.executable, "XO-vs-ordinateur.py"])
    root.destroy()
    
root=tk.Tk()
root.title("Jeu XO - Menu")
root.geometry("600x710")

image = Image.open("xo.jpg")
image= image.resize((600, 500))
image_tk = ImageTk.PhotoImage(image)
label_image = tk.Label(root, image=image_tk, bg="#f0f0f0")
label_image.pack(pady=10)

label_titre=tk.Label(root,text="Bienvenue au jeu XO",font=("Arial",18),bg="#f0f0f0")
label_titre.pack(pady=10)
btn_ami = tk.Button(root, text="Jouer avec un ami", font=("Arial", 14), bg="#007BFF", fg="white", command=jouer_avec_ami)
btn_ami.pack(pady=10, ipadx=10, ipady=5)
btn_ordi = tk.Button(root, text="Contre l’ordinateur", font=("Arial", 14),bg="#28a745", fg="white", command=jouer_contre_ordi)
btn_ordi.pack(pady=10, ipadx=10, ipady=5)

root.mainloop()