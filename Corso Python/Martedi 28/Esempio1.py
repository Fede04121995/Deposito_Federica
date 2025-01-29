#creiamo un sistema di if che ci permetta di riempire dei dati(Nome,eta,cap e un booleano di riferimento)

nome = ""
eta = 0
cap = 0
boolRif = False


if nome == "" and eta == 0 and cap == 0 and boolRif == False :
    nome = input("Inserisci il nome")
    if nome != "" and eta == 0 and cap == 0 and boolRif == False:
        eta = int(input("Inserisci l'età"))
        if nome != "" and eta > 0 and cap == 0 and boolRif == False:
             cap(input("Inserisci il tuo cap"))
             if nome != "" and eta > 0 and cap != 0 and boolRif == False:
                 # boolRif = True
                 
                 riferimento = int(input("Inserisci o 1 o 0"))
                 if (eiferimento > 0):
                     boolRif = False
                     print(nome, eta, cap, boolRif)
                 elif(riferimento <= 0):
                     boolRif = True
                     print(nome, eta, cap, boolRif)
                 else:
                     print("Pippo hai sbagliato")         