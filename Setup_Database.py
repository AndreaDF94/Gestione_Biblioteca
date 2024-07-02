# Questo file crea il database e le tabelle necessarie

import sqlite3

def setup_database():
    conn = sqlite3.connect('biblioteca.db')
    c = conn.cursor()
    
    c.execute(''' CREATE TABLE IF NOT EXIST libri(titolo TEXT,autore TEXT,anno INTEGER, isbn TEXT PRIMARY KEY)''')
    
    c.execute(''' CREATE TABLE IF NOT EXIST utenti(nome TEXT,user_id TEXT PRIMARY KEY)''')
    
    c.execute(''' CREATE TABLE IF NOT EXIST prestiti(user_id TEXT ,isbn_libro TEXT, FOREING KEY(user_id)REFERENCES utenti(user_id),
              FOREIGN KEY(isbn_libro)REFERENCES  libri(isbn))''')
    
    conn.commit()
    conn.close()
    
if __name__ == "__main__":
    setup_database()
    