import datetime
import sqlite3

import tkinter as tk
from tkinter import messagebox, ttk

import customtkinter

from BD import ajouter, modifier


class Hitady(tk.Frame):
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
        def hampiditra():
            from Hampiditra import Hampiditra
            self.pack_forget()
            mapage_frame = Hampiditra(parent, accueil_frame)
            mapage_frame.pack(fill='both', expand=True)

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

        def commmande():
                from commande import commande
                self.pack_forget()
                stockage = commande(parent, accueil_frame)
                stockage.pack(fill='both', expand=True)

        # boutton
        hampiditra = tk.Button(self.menu_frame, text="Hampiditra", width=10, command=hampiditra)
        hampiditra.place(relx=0.5, rely=0.26, anchor='center')
        Hanovab = tk.Button(self.menu_frame, text="Hanova", width=10, command=hanova)
        Hanovab.place(relx=0.5, rely=0.36, anchor='center')
        hitady = tk.Button(self.menu_frame, text="Hitady", width=10)
        hitady.place(relx=0.5, rely=0.46, anchor='center')
        hitady = tk.Button(self.menu_frame, text="Commande", width=10,command=commmande)
        hitady.place(relx=0.5, rely=0.56, anchor='center')
        hitady = tk.Button(self.menu_frame, text="Stockage", width=10, command=stockage)
        hitady.place(relx=0.5, rely=0.66, anchor='center')
        # hitady
        self.EntrerDesgination = customtkinter.CTkEntry(self, placeholder_text_color="#a3a3a3",
                                                        text_color='#fff', fg_color='#001a2e',
                                                        border_color='#004780',
                                                        border_width=2, width=200, height=35, corner_radius=35,
                                                        placeholder_text='Designation')
        self.EntrerDesgination.place(relx=0.5, rely=0.3, anchor="center")
        self.EntrerDesgination.bind("<KeyRelease>", self.rech)
        self.button = tk.Button(self, text="Tadiavina", command=self.rech)
        self.button.place(relx=0.75, rely=0.32, anchor="sw")

    def rech(self, event):
        # Récupérer la valeur saisie dans EntrerDesgination
        des = self.EntrerDesgination.get()
        print("Valeur saisie:", des)
        conn = sqlite3.connect("ma_bd.db")
        curs = conn.cursor()
        curs.execute("SELECT * FROM Entana WHERE Designation LIKE ?", ('%' + des + '%',))
        raw = curs.fetchall()
        style = ttk.Style()

        style.configure("Custom.Treeview", background='#E2F5E7', foreground='#068962', rowheight=25,
                        fieldbackground="#012705", bordercolor="#001a2e", borderwidth=6,
                        font=('Helvetica', 12, 'bold'))
        style.map("Custom.Treeview", background=[('selected', '#068962')], foreground=[('selected', '#001a2e')])

        # Création du Treeview
        tree = ttk.Treeview(self, show='headings', style='Custom.Treeview')
        tree['columns'] = ['Anarany', 'Vidiny', 'Isany']

        def doubleclique(event):
            for s in tree.selection():
                item = tree.item(s)
                selected = item['values']
                print(selected)
                self.EntrerDesgination.delete('0', tk.END)
                self.EntrerDesgination.insert('end', selected[0])

        tree.bind("<Double-1>", doubleclique)
        tree.bind("<Return>", doubleclique)

        tree.column("Anarany", width=100)
        tree.column("Vidiny", width=100)
        tree.column("Isany", width=100)
        # scrool

        # Configuration des colonnes
        for column in tree['columns']:
            tree.heading(column, text=column)

        if des:
            tree.place(relx=0.59, rely=0.52, anchor='center', width=500, height=150)
        else:
            tree.pack_forget()
        for i in raw:
            anarana = i[1]
            prix = i[2]
            isany = i[3]
            tree.insert('', 'end', values=(anarana, prix, isany))

    def go_back(self):
        self.pack_forget()
        self.accueil_frame.pack(fill='both', expand=True)
