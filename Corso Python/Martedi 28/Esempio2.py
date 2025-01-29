nome = ""
password = ""

print("Registrati inserendo un Nome Utente e una Password")

nome = input("Nome Utente")
password = input("Password")

print("Ottimo! Ti sei appena registrato!")

if(nome != "" and password != ""): 
    nome_utente = input("Inserisci il tuo Nome Utente per Login")
    password_utente = input("Inserisci la tua password per Login") 
elif(nome_utente == nome and password_utente == password):
    print("Benvenuto nel tuo nuovo account!")
else:
    print("Mi dispiace, password o nome utente sono errati.")