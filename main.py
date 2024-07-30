import tkinter as tk
from Hampiditra import Hampiditra
from Hanova import Hanova
from Hitady import Hitady
from Stockage import stockagecl
from commande import commande


def hampiditra():
    accueil_frame.pack_forget()
    mapage_frame.pack(fill='both', expand=True)

def hitady():
    accueil_frame.pack_forget()
    stockage = Hitady(root, accueil_frame)
    stockage.pack(fill='both', expand=True)
def hanova():
    accueil_frame.pack_forget()
    hampiditraP.pack(fill='both', expand=True)
def stockage():
    accueil_frame.pack_forget()
    stockage=stockagecl(root, accueil_frame)
    stockage.pack(fill='both', expand=True)
def commmande():
    accueil_frame.pack_forget()
    stockage=commande(root, accueil_frame)
    stockage.pack(fill='both', expand=True)





if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(600, 600)
    root.title("Varotra")
    root.config(bg="lightgray")
    accueil_frame = tk.Frame(root)
    #boutton
    hampiditra = tk.Button(accueil_frame, text="Hampiditra", command=hampiditra, width=10)
    hampiditra.place(relx=0.5, rely=0.3, anchor='center')
    Hanovab = tk.Button(accueil_frame, text="Hanova", command=hanova, width=10)
    Hanovab.place(relx=0.5, rely=0.345, anchor='center')
    hitady = tk.Button(accueil_frame, text="Hitady", width=10,command=hitady)
    hitady.place(relx=0.5, rely=0.390, anchor='center')
    hitady = tk.Button(accueil_frame, text="Commande", width=10,command=commmande)
    hitady.place(relx=0.5, rely=0.435, anchor='center')
    hitady = tk.Button(accueil_frame, text="Stockage", width=10,command=stockage)
    hitady.place(relx=0.5, rely=0.480, anchor='center')
    mapage_frame = Hampiditra(root,accueil_frame)
    hampiditraP = Hanova(root, accueil_frame)
    accueil_frame.pack(fill='both', expand=True)
    root.mainloop()
