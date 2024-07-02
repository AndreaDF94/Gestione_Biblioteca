# Questo file gestisce tutte le operazioni relative ai libri

import sqlite3

class Libro :
    def __init__(self,titolo,autore,anno,isbn) :
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.isbn = isbn
        
class Biblioteca :
    def __init__(self,db_path = 'biblioteca.db'):
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        
    def aggiungi_libro(self,libro):
        self.c.execute("INSERT INTO libri VALUES(?,?,?,?)",(libro.titolo,libro.autore,libro.anno,libro.isbn))
        self.conn.commit()
            
    def rimuovi_libro(self,isbn):
        self.c.execute('DELETE FROM  libri WHERE isbn = ?',(isbn))    
        self.conn.commit()
    
    def cerca_libri(self,titolo = None, autore = None) :
        query = "SELECT * FROM libri WHERE 1 = 1" 
        params = []
        if titolo:
            query += " AND titolo LIKE ?"
            params.append(f"%{titolo}%")
        if autore :
            query += "AND autore LIKE ? "  
            params.append(f"%{autore}%")  
            self.c.execute(query,params)
        risultati = self.c.fetchall()
        return risultati
    def chiudi(self):
        self.conn.close()
        