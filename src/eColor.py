from enum import Enum

class Color(Enum):
    Blanco = 1 #Color previo a triage
    Rojo = 2
    Naranja = 3
    Amarillo = 4
    Verde = 5
    Azul = 6
    
    def __str__(num):
        if num == 2:
            return "ROJO"
        elif num == 3:
            return "NARANJA"
        elif num == 4:
            return "AMARILLO"
        elif num == 5:
            return "VERDE"
        else:
            return "AZUL"