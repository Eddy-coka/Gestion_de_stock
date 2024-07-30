import sqlite3
from tkinter import messagebox


def confirmer_action(entana, prixent, prixbd, qtent, qtbd, date):
    reponse = messagebox.askyesno("Confirmation",
                                  f"Êtes-vous sûr de vouloir changer le prix de {entana} de {prixbd} en {prixent} et {qtbd} en {qtent}?")
    if reponse:
        modifier(entana, prixent, qtent, date)
        messagebox.showinfo("Action confirmée", "Action exécutée.")
    else:
        messagebox.showwarning("Annulation", "Action annulée.")


def ajouter(designation, prix, qt, date):
    bd = sqlite3.connect("ma_bd.db")
    curs = bd.cursor()
    curs.execute(f'''
                CREATE TABLE IF NOT EXISTS Entana (
                id INTEGER PRIMARY KEY,
                Designation TEXT,
                Prix INTEGER,
                Quantité INTEGER,
                Date TEXT
            )
        ''')
    curs.execute("SELECT * FROM Entana")
    raw = curs.fetchall()
    nb = 0
    pr = 0
    qtb = 0
    for raw in raw:
        id, des, pr, qtb, dt = raw
        if raw[1] == designation:
            nb = nb + 1
            pr = pr
            qtb = qtb
    if nb == 1:
        confirmer_action(designation, prix, pr, qt, qtb, date)

    else:
        curs.execute(
            f'INSERT INTO Entana (Designation,Prix,Quantité,Date) VALUES (?,?,?,?)',
            (designation, prix, qt, date))
        messagebox.showinfo("Ok", "Enregistrer avec succès")
    bd.commit()
    bd.close()


# ajouter("kkaoo",4,4,4)
def modifier(designation, prix, qt, date):
    conn = sqlite3.connect("ma_bd.db")
    cursor = conn.cursor()

    # Exécuter la requête UPDATE
    cursor.execute("UPDATE Entana SET Designation=?, Prix=?, Quantité=?, Date=? WHERE Designation=?",
                   (designation, prix, qt, date, designation))
    messagebox.showinfo("Changement", "Changement avec enregistrement avec succès")
    # Commit des modifications
    conn.commit()
    conn.close()
