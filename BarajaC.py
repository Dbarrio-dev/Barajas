import Baraja

class BarajaC():

    def __init__(self, palos, numeros):
        self.palos = palos
        self.numeros = numeros
        self.mazacote = Baraja.crearBaraja(palos, numeros) 

    def barajar(self):
        Baraja.barajar(self.mazacote)

    def repartir (self, num_jugadores, num_cartas):
        for i in range (num_jugadores):
            jugadores.append([])

            for i in range(num_jugadores*num_cartas):
            jugadores[i].append(self.mazacote[i])
            
        