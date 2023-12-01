from enum import Enum
import time
import random
from colletions import deque
horaglobal=0 #cambiar
class Color(Enum):
    Blanco = 1 #Color previo a triage
    Rojo = 2
    Naranja = 3
    Amarillo = 4
    Verde = 5
    Azul = 6
    def __str__(self):
        return self.name