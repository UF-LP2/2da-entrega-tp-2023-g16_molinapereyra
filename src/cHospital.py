import cPaciente
import random
from src.eColor import Color
import time
from collections import deque
class Hospital:
    def __init__(self, velocidad_salida):
        self.cola_pac= deque()
        self.velocidad_salida=velocidad_salida#ver
        self.hora_inicio=time.time()#ver
        self.cola_rojo=[]
        self.cola_naranja=[]
        self.cola_amarillo=[]
        self.cola_verde=[]
        self.cola_azul=[]
        self.listaconsult=[]
    def agregar_consultorio(self,consultorio):
        self.listaconsult.append(consultorio)
    def agregar_persona(self, paciente):
        self.cola_pac.append(paciente)

    def ordenar_color(self):
        paciente_aux=self.cola_pac.popleft()
        if paciente_aux.Triage==Color.Rojo:
            self.cola_rojo.append(paciente_aux)
        if paciente_aux.Triage == Color.Naranja:
            self.cola_naranja.append(paciente_aux)
        if paciente_aux.Triage == Color.Amarillo:
            self.cola_amarillo.append(paciente_aux)
        if paciente_aux.Triage == Color.Verde:
            self.cola_verde.append(paciente_aux)
        if paciente_aux.Triage == Color.Azul:
            self.cola_azul.append(paciente_aux)
    def chequearabierto(self,paciente_aux):
        for i in range(len(self.listaconsult)):
              self.listaconsult[i].revisar_hora()
              if self.listaconsult[i].abierto==True:
                  self.listaconsult[i].ingresaPaciente(paciente_aux)

    def procesar_personas(self):
        while self.cola_pac:
             paciente = self.cola_pac.popleft()
             tiempo_espera = (time.time() / 60) - paciente.horario_ingreso
             print(f"Persona entrada a las {paciente.horario_ingreso} esperó {tiempo_espera:.2f} minutos.")
             time.sleep(random.uniform(1, self.velocidad_salida))
             if paciente.Triage == Color.Naranja and tiempo_espera > 10:
                 raise Exception(f"Tiempo de espera SUPERADO")
             if paciente.Triage == Color.Amarillo and tiempo_espera > 60:
                 raise Exception(f"Tiempo de espera SUPERADO")
             if paciente.Triage == Color.Verde and tiempo_espera > 120:
                 raise Exception(f"Tiempo de espera SUPERADO")
             if paciente.Triage == Color.Azul and tiempo_espera > 240:
                 raise Exception(f"Tiempo de espera SUPERADO")

    def atender(self):
        if self.cola_rojo == None:
             if self.cola_naranja == None:
                 if self.cola_amarillo == None:
                     if self.cola_verde == None:
                         if self.cola_azul == None:
                             return
                         else:
                             # revisar hora del consutorio, si esta abierto
                             self.chequearabierto(self.cola_azul[0])  # mando al paciente al consultorio
                             for i in range(len(self.cola_azul) - 1):
                                 self.cola_rojo[i] = self.cola_azul[
                                     i + 1]  # reorganizamos la cola, movemos los pacientes
                             return
                     else:
                         self.chequearabierto(self.cola_verde[0])  # mando al paciente al consultorio
                         for i in range(len(self.cola_verde) - 1):
                             self.cola_rojo[i] = self.cola_verde[
                                 i + 1]  # reorganizamos la cola, movemos los pacientes
                         return
                 else:
                     self.chequearabierto(self.cola_amarillo[0])  # mando al paciente al consultorio que este abierto
                     for i in range(len(self.cola_amarillo) - 1):
                         self.cola_rojo[i] = self.cola_amarillo[i + 1]  # reorganizamos la cola, movemos los pacientes
                     return
             else:
                 self.chequearabierto(self.cola_naranja[0])  # mando al paciente al consultorio
                 for i in range(len(self.cola_naranja) - 1):
                     self.cola_rojo[i] = self.cola_naranja[i + 1]  # reorganizamos la cola, movemos los pacientes
                 return

        else:
             self.chequearabierto(self.cola_rojo[0])  # mando al paciente al consultorio que este abierto
             for i in range(len(self.cola_rojo) - 1):
                 self.cola_rojo[i] = self.cola_rojo[i + 1]  # reorganizamos la cola, movemos los pacientes
             return

             #falta defprocesarpersonas y atender