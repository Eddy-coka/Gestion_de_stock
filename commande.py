import datetime
import sqlite3

import tkinter as tk
from tkinter import messagebox

import customtkinter

from BD import ajouter, modifier


class commande(tk.Frame):
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

        # forcer entrer chiffre
        # Fonction de validation
        def verifier_entree(P):
            return P.isdigit() or (P and P[0] == '-' and P[1:].isdigit())

        validate_cmd = self.register(verifier_entree)

        # validatecommand = (validate_cmd, "%P")

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

        def hitady():
            from Hitady import Hitady
            self.pack_forget()
            stockage = Hitady(parent, accueil_frame)
            stockage.pack(fill='both', expand=True)

        def stockage():
            from Stockage import stockagecl
            self.pack_forget()
            stockage = stockagecl(parent, accueil_frame)
            stockage.pack(fill='both', expand=True)

        # boutton
        hampiditra = tk.Button(self.menu_frame, text="Hampiditra", width=10, command=hampiditra)
        hampiditra.place(relx=0.5, rely=0.26, anchor='center')
        Hanovab = tk.Button(self.menu_frame, text="Hanova", width=10, command=hanova)
        Hanovab.place(relx=0.5, rely=0.36, anchor='center')
        hitady = tk.Button(self.menu_frame, text="Hitady", width=10, command=hitady)
        hitady.place(relx=0.5, rely=0.46, anchor='center')
        hitady = tk.Button(self.menu_frame, text="Commande", width=10)
        hitady.place(relx=0.5, rely=0.56, anchor='center')
        hitady = tk.Button(self.menu_frame, text="Stockage", width=10, command=stockage)
        hitady.place(relx=0.5, rely=0.66, anchor='center')

        # commande
        self.Nom_cl = customtkinter.CTkEntry(self, placeholder_text_color="#a3a3a3",
                                             text_color='#fff', fg_color='#001a2e',
                                             border_color='#004780',
                                             border_width=2, width=200, height=35, corner_radius=35,
                                             placeholder_text='Nom de client')
        self.Nom_cl.place(relx=0.5, rely=0.3, anchor="center")
        self.liste = []
        self.EntrerDesgination = customtkinter.CTkEntry(self, placeholder_text_color="#a3a3a3",
                                                        text_color='#fff', fg_color='#001a2e',
                                                        border_color='#004780',
                                                        border_width=2, width=200, height=35, corner_radius=35,
                                                        placeholder_text='Designation')
        self.EntrerDesgination.place(relx=0.5, rely=0.36, anchor="center")
        self.EntrerDesgination.bind("<KeyRelease>", self.rech)

        self.Qt = customtkinter.CTkEntry(self, placeholder_text_color="#a3a3a3",
                                         text_color='#fff', fg_color='#001a2e',
                                         border_color='#004780', validate="key",
                                         border_width=2, width=200, height=35, corner_radius=35,
                                         placeholder_text='Quantité', validatecommand=(validate_cmd, "%P"))
        self.Qt.place(relx=0.5, rely=0.42, anchor="center")

        self.Qt.bind("<KeyRelease>", self.rech)

        self.Qt.bind("<KeyRelease>", self.aff)

    def go_back(self):
        self.pack_forget()
        self.accueil_frame.pack(fill='both', expand=True)

    def rech(self, event):
        # Récupérer la valeur saisie dans EntrerDesgination
        des = self.EntrerDesgination.get()
        client = self.Nom_cl.get()
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
                self.label = tk.Label(self, font=16)
                self.label.config(text=f"PU:{selected[1]} Ar")
                self.label.place(relx=0.3, rely=0.48, anchor="center")

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
            tree.place(relx=0.8, rely=0.4, anchor='center', width=100, height=150)
        else:
            tree.place_forget()
        for i in raw:
            anarana = i[1]
            prixa = i[2]
            self.isanya = i[3]

            tree.insert('', 'end', values=(anarana, prixa, self.isanya))
            if anarana == des:
                anarana = i[1]
                self.prix = i[2]

            if anarana == des:
                ajouter_pan = tk.Button(self, text="Commande", width=10, command=self.panier)
                ajouter_pan.place(relx=0.4, rely=0.6, anchor="center")

    # fonction
    import tkinter as tk
    from tkinter import ttk

    def facture(self, tab):
        client = self.Nom_cl.get()
        print(client)

        # Créer une nouvelle fenêtre
        frame = tk.Tk()
        frame.title("Facture")

        style = ttk.Style()
        style.configure("Custom.Treeview",
                        background='#001a2e',
                        foreground='#ffffff',  # Couleur du texte
                        rowheight=25,
                        fieldbackground="#001a2e",
                        bordercolor="#001a2e",
                        borderwidth=6,
                        font=('Helvetica', 12, 'bold'))
        style.map("Custom.Treeview",
                  background=[('selected', '#068962')],
                  foreground=[('selected', '#ffffff')])

        # Créer un cadre pour le Treeview et les barres de défilement
        tree_frame = tk.Frame(frame)
        tree_frame.pack(expand=True, fill='both')

        # Ajouter le nom du client en tant qu'en-tête
        header = tk.Label(tree_frame, text=f"Facture pour : {client}", font=('Helvetica', 16, 'bold'))
        header.grid(row=0, column=0, columnspan=2, pady=10)

        # Créer le Treeview avec le style personnalisé
        tree = ttk.Treeview(tree_frame, show='headings', style='Custom.Treeview')
        tree['columns'] = ['Qt', 'Designation', 'PU', 'Total']
        for column in tree['columns']:
            tree.heading(column, text=column)
        tree.column('Qt', width=100, anchor='center')
        tree.column('Designation', width=200, anchor='w')
        tree.column('PU', width=100, anchor='center')
        tree.column('Total', width=100, anchor='e')

        # Créer les barres de défilement
        vsb = tk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        hsb = tk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
        tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        # Disposer le Treeview et les barres de défilement
        tree.grid(row=1, column=0, sticky='nsew')
        vsb.grid(row=1, column=1, sticky='ns')
        hsb.grid(row=2, column=0, sticky='ew')

        # Ajouter un texte de pied de page
        total = 0
        for raw in tab:
            tree.insert('', 'end', values=(raw[0], raw[1], raw[2], raw[3]))
            total += raw[3]

        footer_text = tk.Label(tree_frame, text=f"Total={total}", font=('Helvetica', 12, 'italic'))
        footer_text.grid(row=3, column=0, pady=10, sticky='w')

        # Configurer les poids pour que le Treeview redimensionne correctement
        tree_frame.grid_rowconfigure(1, weight=1)
        tree_frame.grid_columnconfigure(0, weight=1)

        # Calculer le total et créer le bouton d'impression
        isany = int(self.Qt.get())
        tot = isany * self.prix
        des = self.EntrerDesgination.get()

        imprim = tk.Button(tree_frame, text="Imprimer", width=10,
                           command=lambda: self.confirmer_action(self.Nom_cl.get(), self.Qt.get(), des,
                                                                 self.prix, tot))
        imprim.grid(row=4, column=0, pady=10, sticky='e')

        frame.mainloop()

    def confirmer_action(self, nom, isany, entana, pu, tot):
        def imprimer(nom, isany, entana, pu, tot):
            date = datetime.datetime.today()
            conn = sqlite3.connect("commande.db")
            curs = conn.cursor()
            curs.execute(f'''
                        CREATE TABLE IF NOT EXISTS {nom} (
                        isany TEXT,
                        entana INTEGER,
                        pu INTEGER,
                        pt TEXT,
                        Date DATETIME
                                           )
                                       ''')

            curs.execute(f"SELECT * FROM {nom} WHERE entana=?", (entana,))
            if curs.fetchone():
                curs.execute(f'''
                           UPDATE {nom} SET  isany=?,  pu=? ,pt =?,Date=? WHERE entana=?
                       ''', (isany, pu, tot, date, entana,))
            else:

                curs.execute(f'INSERT INTO {nom} (isany,entana,pu,pt,Date) VALUES (?,?,?,?,?)',
                             (isany, entana, pu, tot, date))

            conn.commit()
            conn.close()

        reponse = messagebox.askyesno("Confirmation",
                                      "Impression?")
        print(self.liste)
        if reponse:
            for raw in self.liste:
                isanya = self.isanya - isany
                print(self.isanya, isany, isanya)
                if isanya > 0:
                    date = datetime.datetime.today()
                    modifier(entana, pu, isanya, date)
                    imprimer(nom, isany, entana, pu, tot)
                else:
                    messagebox.showinfo("Imposible", "insuffisance des données")

        else:
            messagebox.showwarning("Annulation", "Action annulée.")

    def panier(self):
        client = self.Nom_cl.get()
        if client:
            test = False

            entana = self.EntrerDesgination.get()
            pu = self.prix
            qt = int(self.Qt.get())
            pt = qt * pu
            for index, i in enumerate(self.liste):
                if i[1] == entana:
                    test = True
                if test:
                    pt = pt + i[3]
                    qt = qt + i[0]
                    self.liste[index] = (qt, entana, pu, pt)

            if not test: self.liste.append((qt, entana, pu, pt))
            print(self.liste)
            self.EntrerDesgination.delete(0, tk.END)

            self.label = tk.Label(self, font=16)
            self.label.config(text=f"PU:{0} Ar")
            self.label.config(text=f"Pt:0 Ar")
            self.label.place(relx=0.5, rely=0.48, anchor="center")
            facture = tk.Button(self, text="Facture", width=10, command=lambda: self.facture(self.liste))
            facture.place(relx=0.55, rely=0.6, anchor="center")
        else:
            messagebox.showwarning("Alert", "VEUILLEZ ENTRER LE NOM ")

    def aff(self, event):
        qt = int(self.Qt.get())
        tot = qt * self.prix
        self.label = tk.Label(self, font=16)
        self.label.config(text=f"Pt:{tot}Ar")
        self.label.place(relx=0.5, rely=0.48, anchor="center")


root = tk.Tk()
root.minsize(600, 600)
root.title("Varotra")
accueil_frame = tk.Frame(root)
mapage_frame = commande(root, accueil_frame)
mapage_frame.pack(fill='both', expand=True)
root.mainloop()
