# Questo file gestisce le operazioni relative ai prestiti dei libri.

import sqlite3

class Prestito:
    def __init__(self,user_id,isbn_libro):
        self.user_id = user_id
        self.isbn_libro = isbn_libro
        
class Gestore_Prestiti :
    def __init__(self,db_path = 'biblioteca.db') :
         
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
    def presta_libro(self,user_id,isbn_libro):
        self.c.execute ("INSERT INTO prestiti VALUES(?,?)", (user_id,isbn_libro))
        self.conn.commit()   
    def restituisci_libro(self,user_id,isbn_libero):
        self.c.execute("DELETE FROM prestiti WHERE user_id = ? AND isbn_libro = ?", (user_id,isbn_libero)) 
        self.conn.commit()   
    def prestiti_utente(self,user_id):
        self.c.execute("SELECT * FROM prestiti WHERE user_id = ?", (user_id))    
        risultati = self.c.fetchall()
        return risultati
    def chiudi(self):
        self.conn.close