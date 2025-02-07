class Posto:
    def __init__(self, numero, fila):
        self.__numero = numero
        self.__fila = fila
        self.__occupato = False
        
    def prenota(self):
        if(self.__occupato):
            print(f"Il posto {self.__fila}{self.__numero} è già occupato.")
        else:
            self.__occupato = True  
            print(f"Posto {self.__fila}{self.__numero} ora prenotato.")
            
    def libera(self):
        if(self.__occupato):
            self.__occupato = False  
            print(f"Posto {self.__fila}{self.__numero} appena liberato.")
        else:
            print(f"Errore: Il posto {self.__fila}{self.__numero} non era prenotato.")
            
    def get_numero(self):
        return self.__numero

    def get_fila(self):
        return self.__fila

    def get_occupato(self):
        return self.__occupato

    
class PostoVIP(Posto):
    def __init__(self, numero, fila):
        super().__init__(numero, fila)
        self.servizi_extra = ["Accesso al lounge", "Servizio al posto"]
    
    def prenota(self):
        if(self.get_occupato()):  
            print(f"Il posto {self.get_fila()}{self.get_numero()} è già occupato.")
        else:
            super().prenota()  
            print(f"Ed hai aggiunto i seguenti servizi extra: {', '.join(self.servizi_extra)}")
 

class PostoStandard(Posto):
    def __init__(self, numero, fila):
        super().__init__(numero, fila)
        
    def prenota(self):
        if(self.get_occupato()):  
            print(f"Il posto {self.get_fila()}{self.get_numero()} è già occupato.")
        else:
            super().prenota()  
            print("Grazie per aver acquistato il tuo posto al costo di")


class Teatro:
    def __init__(self):
        self.lista_posti = []
        
    def aggiungi_posto(self):
        num_posti_totali = int(input("Quanti posti totali ci sono? "))
        num_VIP = int(input("Quanti posti VIP ci sono? "))
        num_Standard = int(input("E quanti Standard? "))
        
        if(num_VIP + num_Standard != num_posti_totali):
            print("Errore: La somma dei posti VIP e Standard non corrisponde al numero totale di posti.")
            return  # Esce dal metodo, quindi l'inserimento dei posti non prosegue
        else:
            print("Numero di posti corretto. Procediamo con l'inserimento dei posti.")
            
        for y in range(1, num_VIP + 1):
            fila_VIP = input(f"Qual è la fila dei posti VIP? {y}: ")
            numero_VIP = int(input(f"E il numero posto VIP? {y}: "))
            posto_vip = PostoVIP(numero_VIP, fila_VIP)
            self.lista_posti.append(posto_vip)
            
        for z in range(1, num_Standard + 1):
            fila_Standard = input(f"Qual è la fila dei posti Standard? {z}: ")
            numero_Standard = int(input(f"E il numero posto Standard? {z}: "))
            posto_Standard = PostoStandard(numero_Standard, fila_Standard)
            self.lista_posti.append(posto_Standard)
            
    def prenota_posto(self):
        fila = input("Inserisci la fila del posto che vuoi prenotare: ")
        numero = int(input("Inserisci il numero del posto che vuoi prenotare: "))
        
        for posto in self.lista_posti:
            if posto.get_numero() == numero and posto.get_fila() == fila:
                posto.prenota()
                break
        else:
            print(f"Il posto {fila}{numero} non è stato trovato.")
    
    def stampa_posti_occupati(self):
        for posto in self.lista_posti:
            if posto.get_occupato():  # Usando il getter
                print(f"Posto {posto.get_fila()}{posto.get_numero()} è occupato.")
            else:
                print(f"Posto {posto.get_fila()}{posto.get_numero()} è libero.")
                
t1 = Teatro()
t1.aggiungi_posto()  
t1.prenota_posto()  
t1.stampa_posti_occupati() 