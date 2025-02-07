class Posto:
    def __init__(self, numero, fila):
        self.__numero = numero
        self.__fila = fila
        self.__occupato = False
        
    def prenota(self):
        if(self._occupato):
            print(f"Il posto {self._fila}{self._numero} è già occupato.")
        else:
            self._occupato = True
            print(f"Posto {self._fila}{self._numero} ora prenotato.")
            
    def libera(self):
        if self._occupato:
            self._occupato = False
            print(f"Posto {self._fila}{self._numero} appena liberato.")
        else:
            print(f"Errore: Il posto {self._fila}{self._numero} non era prenotato.")
            
    def get_numero(self):
        return self._numero

    def get_fila(self):
        return self._fila

    def get_occupato(self):
        return self._occupato
 
    
    
class PostoVIP(Posto):
    def __init__(self, numero, fila):
        super().__init__(numero, fila)
        self.servizi_extra = ["Accesso al lunge", "Servizio al posto"]
    
    def prenota(self):
        if(self.__occupato):
            print(f"Il posto {self.__fila}{self.__numero} è già occupato.")
        else:
            self._occupato = True
            print(f"Posto {self.__fila}{self.__numero} ora prenotato") 
            print(f"Ed hai aggiunto i seguenti servizi extra: {', '.join(self.servizi_extra)}")   
 
        
class PostoStandard(Posto):
    def __init__(self, numero: int, fila: str, costo_prenotazione_online: float):
        super().__init__(numero, fila)
        self.costo_prenotazione_online = costo_prenotazione_online
        
    def prenota(self):
        if(self.__occupato):
            print(f"Il posto {self.__fila}{self.__numero} è già occupato.")
        else:
            self.__occupato = True
            print(f"Posto {self.__fila}{self.__numero} ora prenotato") 
            print(f"Grazie per aver acquistato il tuo posto al costo di: {self.costo_prenotazione_online}")
            
            
class Teatro():
    def __init__(self):
        self.lista_posti = []
        
    def aggiungi_posto(self):
        num_posti_totali = int(input("Quanti posti ci sono?"))
        for x in range(1, num_posti_totali + 1): 
            num_VIP = int(input("Quanti posti VIP ci sono?"))
            num_Standard = int(input("E quanti Standard"))
            tot = Teatro(num_VIP, num_Standard)
            self.lista_posti.append(tot) 
            print(self.lista_posti)
    
    def prenota_posto(self, numero, fila):
        for x in self.lista_posti:
            if x.get_numero() == numero and x.get_fila() == fila:
                return
        else:
             print(f"Il posto {fila}{numero} non c'è")
    
    def stampa_posti_occupati():
        pass
    
t1 = Teatro()
t1.aggiungi_posto()
t1.prenota_posto()
t1.stampa_posti_occupati()   
