import datetime
import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk
import customtkinter
from BD import modifier
from Stockage import stockagecl


class Hanova(tk.Frame):
    def __init__(self, parent, accueil_frame):
        super().__init__(parent)
        self.accueil_frame = accueil_frame
        self.config(bg="lightgray")


        # retour
        self.button = tk.Button(self, text="Go Back", command=self.go_back)
        self.button.place(relx=0.9, rely=0.9, anchor="sw")
        # button @sisiny
        self.menu_frame = tk.Frame(self, bg="#001a2e", width=100)
        self.menu_frame.pack(fill=tk.Y, side=tk.LEFT)

        # func button
        def hampiditra():
            from Hampiditra import Hampiditra
            self.pack_forget()
            mapage_frame = Hampiditra(parent, accueil_frame)
            mapage_frame.pack(fill='both', expand=True)

        def stockage():
            self.pack_forget()
            mapage_frame = stockagecl(parent, accueil_frame)
            mapage_frame.pack(fill='both', expand=True)

        def hitady():
            from Hitady import Hitady
            self.pack_forget()
            stockage = Hitady(parent, accueil_frame)
            stockage.pack(fill='both', expand=True)

        def commmande():
                from commande import commande
                self.pack_forget()
                stockage = commande(parent, accueil_frame)
                stockage.pack(fill='both', expand=True)

        # boutton
        hampiditra = tk.Button(self.menu_frame, text="Hampiditra", width=10, command=hampiditra)
        hampiditra.place(relx=0.5, rely=0.26, anchor='center')
        Hanovab = tk.Button(self.menu_frame, text="Hanova", width=10)
        Hanovab.place(relx=0.5, rely=0.36, anchor='center')
        hitady = tk.Button(self.menu_frame, text="Hitady", width=10,command=hitady)
        hitady.place(relx=0.5, rely=0.46, anchor='center')
        hitady = tk.Button(self.menu_frame, text="Commande", width=10,command=commmande)
        hitady.place(relx=0.5, rely=0.56, anchor='center')
        hitady = tk.Button(self.menu_frame, text="Stockage", width=10, command=stockage)
        hitady.place(relx=0.5, rely=0.66, anchor='center')
        # manova
        self.EntrerDesgination = customtkinter.CTkEntry(self, placeholder_text_color="#a3a3a3",
                                                        text_color='#fff', fg_color='#001a2e',
                                                        border_color='#004780',
                                                        border_width=2, width=200, height=35, corner_radius=35,
                                                        placeholder_text='Designation')
        self.EntrerDesgination.place(relx=0.5, rely=0.3, anchor="center")
        self.EntrerDesgination.bind("<KeyRelease>", self.rech)
        var = tk.IntVar
        self.Prix = customtkinter.CTkEntry(self, placeholder_text_color="#a3a3a3",
                                           text_color='#fff', fg_color='#001a2e',
                                           border_color='#004780',
                                           border_width=2, width=200, height=35, corner_radius=35,
                                           placeholder_text='Prix', )
        self.Prix.place(relx=0.5, rely=0.36, anchor="center")
        self.Quantite = customtkinter.CTkEntry(self, placeholder_text_color="#a3a3a3",
                                               text_color='#fff', fg_color='#001a2e',
                                               border_color='#004780',
                                               border_width=2, width=200, height=35, corner_radius=35,
                                               placeholder_text='Quantités')
        self.Quantite.place(relx=0.5, rely=0.42, anchor="center")
        # boutton

        hovaina = tk.Button(self, text="Hovaina", width=10, command=self.mod)
        hovaina.place(relx=0.39, rely=0.6, anchor='center')

        fafana = tk.Button(self, text="Fafana", width=10, command=self.fafana)
        fafana.place(relx=0.59, rely=0.6, anchor='center')

    def fafana(self):
        self.EntrerDesgination.delete(0, tk.END)
        self.Prix.delete(0, tk.END)
        self.Quantite.delete(0, tk.END)

    def mod(self):
        # maka
        global des, pr, qt, test
        desentr = self.EntrerDesgination.get()
        prixent = int(self.Prix.get())
        qtsent = (self.Quantite.get())
        # mande @bd
        bd = sqlite3.connect("ma_bd.db")
        curs = bd.cursor()
        curs.execute("SELECT * FROM Entana")
        tab = curs.fetchall()
        date = datetime.datetime.today()
        test = "inconnu"
        for raw in tab:
            id, des, pr, qt, dt = raw
            if des == desentr:
                test = des
        if test == "inconnu":
            messagebox.showinfo("Pas dans bd", f"{desentr} n'est pas dans bd.")
        elif qtsent:
            self.confirmer_action(des, prixent, pr, qtsent, qt, date)
        else:
            messagebox.showinfo("Pas dans bd", "Veuillez completer.")
        bd.commit()
        bd.close()

    def confirmer_action(self, entana, prixent, prixbd, qtent, qtbd, date):
        reponse = messagebox.askyesno("Confirmation",
                                      f"Êtes-vous sûr de vouloir changer le prix de {entana} de {prixbd} en {prixent} et {qtbd} en {qtent}?")
        if reponse:
            modifier(entana, prixent, qtent, date)
            messagebox.showinfo("Action confirmée", "Action exécutée.")
        else:
            messagebox.showwarning("Annulation", "Action annulée.")

    def go_back(self):
        self.pack_forget()
        self.accueil_frame.pack(fill='both', expand=True)  # Close the current window

    def rech(self, event):
        # Récupérer la valeur saisie dans EntrerDesgination
        des = self.EntrerDesgination.get()
        pr = self.Prix.get()
        qt = self.Quantite.get()
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
                self.Prix.delete('0', tk.END)
                self.Prix.insert('end', selected[1])

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
            tree.pack_forget()
        for i in raw:
            anarana = i[1]
            prix = i[2]
            isany = i[3]
            tree.insert('', 'end', values=(anarana, prix, isany))


"""root = tk.Tk()
root.minsize(600, 600)
root.title("Varotra")
accueil_frame = tk.Frame(root)
mapage_frame = Hanova(root, accueil_frame)
mapage_frame.pack(fill='both', expand=True)
root.mainloop()"""
