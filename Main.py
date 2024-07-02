# Questo file funge da interfaccia principale per interagire con il sistema

from Libri import Libro , Biblioteca
from Utenti import Utente , Gestore_Utenti

def main():
    biblioteca = Biblioteca()
    gestore_utenti = Gestore_Utenti()
    
# Aggiungi libri alla biblioteca

Biblioteca.aggiungi_libro(Libro("Il Signore degli Anelli","J.R.R.Tolkien",1954,"1356427905"))

Biblioteca.aggiungi_libro(Libro("Le due Torri","J.R.R. Tolkien",1954,"7890254174"))

# Aggiungi Utenti

Gestore_Utenti.aggiungi_utente(Utente("Kristopher Volkov","001"))

Gestore_Utenti.aggiungi_utente(Utente("Andrea Rossi","002"))

# Ricerchiamo i libri

libri_trovati = Biblioteca.cerca_libri(autore="Tolkien")

for libro in libri_trovati:
    print(f"Libro trovato: {libro[0]} di{libro[1]}")
    
#Ricerchiamo gli utenti

utenti_trovati = Gestore_Utenti.Cerca_Utenti(nome="Kristopher") 

for utente in utenti_trovati:
    print("Utente trovato: {utente[0]} con ID {utente[1]}")

if __name__ == "__main__":
    main() 
    
    


