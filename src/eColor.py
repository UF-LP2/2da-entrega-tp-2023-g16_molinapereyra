from enum import Enum
from datetime import *
import time
import random
from collections import deque
class Color(Enum):
    Blanco = 1 #Color previo a triage
    Rojo = 2
    Naranja = 3
    Amarillo = 4
    Verde = 5
    Azul = 6
    def __str__(self):
        return self.name