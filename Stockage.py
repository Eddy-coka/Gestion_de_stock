import sqlite3
import tkinter as tk
from tkinter import ttk


class stockagecl(tk.Frame):
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

        def hampiditra():
            from Hampiditra import Hampiditra
            self.pack_forget()
            hampiditraP = Hampiditra(parent, accueil_frame)
            hampiditraP.pack(fill='both', expand=True)

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
        hitady = tk.Button(self.menu_frame, text="Stockage", width=10)
        hitady.place(relx=0.5, rely=0.66, anchor='center')
        # affichage
        style = ttk.Style()
        style.configure("Custom.Treeview", background='#E2F5E7', foreground='#068962', rowheight=25,
                        fieldbackground="#012705", bordercolor="#001a2e", borderwidth=6,
                        font=('Helvetica', 12, 'bold'))
        style.map("Custom.Treeview", background=[('selected', '#068962')], foreground=[('selected', '#001a2e')])

        # Création du Treeview
        tree = ttk.Treeview(self, show='headings', style='Custom.Treeview')
        tree['columns'] = ['Anarany', 'Vidiny', 'Isany']
        tree.column("Anarany", width=100)
        tree.column("Vidiny", width=100)
        tree.column("Isany", width=100)
        for column in tree['columns']:
            tree.heading(column, text=column)
        tree.place(relx=0.55, rely=0.45, anchor='center', width=450, height=450)
        conn = sqlite3.connect("ma_bd.db")
        curs = conn.cursor()
        curs.execute("SELECT * FROM Entana")
        raw = curs.fetchall()
        for i in raw:
            anarana = i[1]
            prix = i[2]
            isany = i[3]
            tree.insert('', 'end', values=(anarana, prix, isany))

    def go_back(self):
        self.pack_forget()
        self.accueil_frame.pack(fill='both', expand=True)


"""root = tk.Tk()
root.minsize(600, 600)
root.title("Varotra")
accueil_frame = tk.Frame(root)
mapage_frame = stockagecl(root, accueil_frame)
mapage_frame.pack(fill='both', expand=True)
root.mainloop()
"""
