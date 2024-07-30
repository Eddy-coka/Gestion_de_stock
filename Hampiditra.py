import datetime
import sqlite3

import tkinter as tk
from tkinter import messagebox

import customtkinter

from BD import ajouter, modifier
from commande import commande


class Hampiditra(tk.Frame):
    def __init__(self, parent, accueil_frame):
        super().__init__(parent)
        self.accueil_frame = accueil_frame
        self.config(bg="lightgray")
        # retour

        self.button = tk.Button(self, text="Go Back", command=self.go_back)
        self.button.place(relx=0.9, rely=0.9, anchor="sw")
        # button @sisiny
        self.menu_frame = tk.Frame(self, width=100, bg='#001a2e')
        self.menu_frame.pack(fill=tk.Y, side=tk.LEFT)

        # func button

        def hanova():
            from Hanova import Hanova
            self.pack_forget()
            hampiditraP = Hanova(parent, accueil_frame)
            hampiditraP.pack(fill='both', expand=True)

        def stockage():
            from Stockage import stockagecl
            self.pack_forget()
            stockage = stockagecl(parent, accueil_frame)
            stockage.pack(fill='both', expand=True)

        def hitady():
            from Hitady import Hitady
            self.pack_forget()
            stockage = Hitady(parent, accueil_frame)
            stockage.pack(fill='both', expand=True)

        def commmande():

            self.pack_forget()
            stockage = commande(parent, accueil_frame)
            stockage.pack(fill='both', expand=True)
        # boutton
        hampiditra = tk.Button(self.menu_frame, text="Hampiditra", width=10)
        hampiditra.place(relx=0.5, rely=0.26, anchor='center')
        Hanovab = tk.Button(self.menu_frame, text="Hanova", width=10, command=hanova)
        Hanovab.place(relx=0.5, rely=0.36, anchor='center')
        hitady = tk.Button(self.menu_frame, text="Hitady", width=10,command=hitady)
        hitady.place(relx=0.5, rely=0.46, anchor='center')
        hitady = tk.Button(self.menu_frame, text="Commande", width=10,command=commmande)
        hitady.place(relx=0.5, rely=0.56, anchor='center')
        hitady = tk.Button(self.menu_frame, text="Stockage", width=10, command=stockage)
        hitady.place(relx=0.5, rely=0.66, anchor='center')
        # mampiditra

        self.EntrerDesgination = customtkinter.CTkEntry(self, placeholder_text_color="#a3a3a3",
                                                        text_color='#fff', fg_color='#001a2e',
                                                        border_color='#004780',
                                                        border_width=2, width=200, height=35, corner_radius=35,
                                                        placeholder_text='Designation')
        self.EntrerDesgination.place(relx=0.5, rely=0.3, anchor="center")
        self.EntrerDesgination.bind("<Return>", self.ajouter)  # mipotsika boutton entrer
        self.Prix = customtkinter.CTkEntry(self, placeholder_text_color="#a3a3a3",
                                           text_color='#fff', fg_color='#001a2e',
                                           border_color='#004780',
                                           border_width=2, width=200, height=35, corner_radius=35,
                                           placeholder_text='Prix')
        self.Prix.place(relx=0.5, rely=0.36, anchor="center")
        self.Prix.bind("<Return>", self.ajouter)  # mipotsika boutton entrer
        self.Quantite = customtkinter.CTkEntry(self, placeholder_text_color="#a3a3a3",
                                               text_color='#fff', fg_color='#001a2e',
                                               border_color='#004780',
                                               border_width=2, width=200, height=35, corner_radius=35,
                                               placeholder_text='Quantités')
        self.Quantite.place(relx=0.5, rely=0.42, anchor="center")
        self.Quantite.bind("<Return>", self.ajouter)#mipotsika boutton entrer

        # boutton

        ampidirina = tk.Button(self, text="Ampidirina", width=10, command=lambda: self.ajouter)
        ampidirina.place(relx=0.39, rely=0.6, anchor='center')

        fafana = tk.Button(self, text="Fafana", width=10, command=self.fafana)
        fafana.place(relx=0.59, rely=0.6, anchor='center')

    def go_back(self):
        self.pack_forget()
        self.accueil_frame.pack(fill='both', expand=True)

    def fafana(self):
        self.EntrerDesgination.delete(0, tk.END)
        self.Prix.delete(0, tk.END)
        self.Quantite.delete(0, tk.END)

    def ajouter(self,event):
        date = datetime.datetime.today()
        print(date)
        des = self.EntrerDesgination.get()
        prix = self.Prix.get()
        qt = self.Quantite.get()
        if des:
            if qt:
                if prix:
                    ajouter(des, prix, qt, date)
                    self.fafana()
        else:
            messagebox.showinfo("Données manquée", "Veuillez completer tous")


"""root = tk.Tk()
root.minsize(600, 600)
root.title("Varotra")
accueil_frame = tk.Frame(root)
mapage_frame = Hampiditra(root, accueil_frame)
mapage_frame.pack(fill='both', expand=True)
root.mainloop()"""
