from src.eColor import Color
#horaglobal=0 #cambiar
#import time
#aux = time.localtime()
#horaglobal = aux.tm_hour*100+aux.tm_min
#print(horaglobal)

class Paciente(object):
    
    def __init__(self, DNI, Nombre:str, Apellido:str, Edad:int, Genero:str,Perdida_de_Conciencia:bool,Respira:bool,Movilidad:bool,Dolor:bool):
        self.verifico_dni(int(DNI))
        self.verifico_palabra(Nombre, Apellido)
        self.verificar_edad(int(Edad))
        self.verifico_genero(Genero)
        self.perdidaconciencia = Perdida_de_Conciencia
        self.respira=Respira
        self.movilidad=Movilidad
        self.dolor=Dolor
        self.Triage=Color.Blanco
        self.asignar_color()
        self.contar_atendido=10#por defecto todos tienen ese tiempo para ser atendidos en consult
        self.horario_ingreso=horaglobal
     
         
    def __str__(self):
        return(f"{self.dni}, {self.apellido}, {self.nombre}, {self.edad}, {self.genero}, {str(self.color)}, {self.contador}")
      
         

    def verifico_dni(self, dni):
        if type(dni) != int:
            raise Exception(f"El DNI no es un numero entero ")
        elif dni < 0:
            raise Exception(f"El DNI es menor a 0")
        else:
            self.dni = dni
    def asignar_color(self):
        if self.respira==False:
            self.Triage=Color.Rojo
        else:
            if self.perdidaconciencia==True:
                if self.movilidad==False:
                    self.Triage=Color.Naranja
                else:
                    if self.dolor==True:
                        self.Triage=Color.Amarillo
                    else:
                        self.Triage=Color.Verde
            else:
                if self.movilidad==False:
                    if self.dolor==True:
                        self.Triage=Color.Naranja
                    else:
                        self.Triage=Color.Azul



            
        
         
       
        
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
        if genero == 'F' or genero == 0:
            self.genero = genero
        elif genero == 'M' or genero == 1: #Al convertir los datos M paso a tener valores de 1 y F valores de 0
            self.genero = genero
        else:
            raise Exception(f"El genero es ivalido")
            

    def verifico_palabra_e(self, Enfermedad):
        if type(Enfermedad) != str or ( Enfermedad) == "!#$%&(/)=?¡¬|°[]+*":
            raise Exception(f"La enfermedad no puede ser leida")
        else:
            self.Enfermedad = Enfermedad
            self.triage(Enfermedad)