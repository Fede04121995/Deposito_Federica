lista_utenti=[]
id = 0
aggiunte= int(input("quantiutenti vuoi aggiungere"))
              
while(len(lista_utenti)<=aggiunte):
    utente2=[]
    nome = input("isneriscituo nome")
    utente2.append(nome)
    password =input("isnerisci lapassword")
    utente2.append(password)
    id +=1
    utente2.append(id)

    lista_utenti.append(utente2)
    print(utente2)
    print(lista_utenti)

print(lista_utenti)