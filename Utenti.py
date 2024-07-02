# Questo file gestisce le operazioni relative agli utenti

import sqlite3

class Utente:
    def __init__(self,nome,user_id):
        self.nome = nome
        self.user_id = user_id

class Gestore_Utenti :
    def __init__(self,db_path = 'biblioteca.db'):
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
    
    def Aggiungi_Utente(self,utente):
        self.c.execute("INSERT INTO utenti VALUES(?,?)",(utente.nome,utente.user_id)) 
        self.conn.commit()   
    
    def Rimuovi_Utente(self,user_id):
        self.c.execute("DELETE FROM utenti WHERE user_id = ?",(user_id))
        self.conn.commit()
    
    def Cerca_Utenti(self,nome = None): 
        query ="SELECT * FROM  utenti WHERE 1=1" 
        params = []
        if nome:
            query += "AND nome LIKE ?"
            params.append(f"%{nome}%")
            self.c.execute(query,params)
            risultati = self.c.fetchall()
            return risultati
    
    def Chiudi(self):
        self.conn.close()    
        
                     
    