import datetime
from src.eColor import Color

class Paciente(object):
    
    def __init__(self, DNI, nombre:str, apellido:str, edad:int, genero:str,Enfermedad:str, color:Color, contador:int):
        self.verifico_dni(int(DNI))
        self.verifico_palabra(nombre, apellido)
        self.verificar_edad(int(edad))
        self.verifico_genero(genero)
        self.verifico_palabra_e(Enfermedad)
         
         
    def triage(self,Enfermedad):
        if Enfermedad == "politraumatismo" or Enfermedad == "neumonia":
            self.color = 2
            self.contador = 0
        elif Enfermedad == "bronquitis" or Enfermedad == "hemorragia digestiva" or Enfermedad == "isquemia" or Enfermedad == "convulsiones" or Enfermedad == "coma":
            self.color = 3
            self.contador = 10
        elif Enfermedad == "dolor de estomago" or Enfermedad == "sinusitis" or Enfermedad == "alergias" or Enfermedad == "asma" or Enfermedad == "hipertension" or Enfermedad == "urgencias psiquiatricas" or Enfermedad == "artritis":
            self.color = 4
            self.contador = 60
        elif Enfermedad == "esguince" or Enfermedad == "dolor de espalda" or Enfermedad == "migraña" or Enfermedad == "dolor de muela" or Enfermedad == "infeccion de oido" or Enfermedad == "nauseas":
            self.color = 5
            self.contador = 120
        else:
            self.color = 6 #Si no es ninguno de las lista pertenece al color azul
            self.contador = 240
            
    def verifico_dni(self, dni):
        if type(dni) != int:
            raise Exception(f"El DNI no es un numero entero ")
        elif dni < 0:
            raise Exception(f"El DNI es menor a 0")
        else:
            self.dni = dni
        
    def verifico_palabra(self, nombre, apellido):
        if type(nombre and apellido) != str: 
            raise Exception(f"EL Nombre y/o Apellido es invalido")
        elif (nombre and apellido) == "!#$%&(/)=?¡¬|°[]+*":
            raise Exception(f"EL Nombre y/o Apellido es invalido")
        else:
            self.nombre = nombre
            self.apellido = apellido

    def verificar_edad(self, edad):
        if type(edad) != int:
            raise Exception(f"La edad no es un numero entero ")
        elif edad <= 100 and edad > 0:
            self.edad = edad
        else:
            raise Exception(f"La edad esta fuera de rango")

    def verifico_genero(self,genero):
        if genero == 'F':
            self.genero = genero
        elif genero == 'M':
            self.genero = genero
        else:
            raise Exception(f"El genero es ivalido")
            

    def verifico_palabra_e(self, Enfermedad):
        if type(Enfermedad) != str or ( Enfermedad) == "!#$%&(/)=?¡¬|°[]+*":
            raise Exception(f"La enfermedad no puede ser leida")
        else:
            self.Enfermedad = Enfermedad
            self.triage(Enfermedad)