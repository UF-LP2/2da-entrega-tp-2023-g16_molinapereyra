import os
import random
import time
from collections import deque
from src.cConsultorio import *

class Hospital:
    def __init__(self):
        self.cola_pac= deque()
        self.cola_rojo= deque()
        self.cola_naranja=deque()
        self.cola_amarillo=deque()
        self.cola_verde=deque()
        self.cola_azul=deque()
        self.listaconsult=deque()
        self.contar=0
    def agregar_consultorio(self,consultorio):
        self.listaconsult.appendleft(consultorio)
    def agregar_persona(self,aux):
        aux.asignar_color()
        self.cola_pac.appendleft(aux)

    def ordenar_color(self):
        paciente_aux=self.cola_pac.pop()
        if paciente_aux.Triage == Color.Rojo:
            self.cola_rojo.appendleft(paciente_aux)
        if paciente_aux.Triage == Color.Naranja:
            self.cola_naranja.appendleft(paciente_aux)
        if paciente_aux.Triage == Color.Amarillo:
            self.cola_amarillo.appendleft(paciente_aux)
        if paciente_aux.Triage == Color.Verde:
            self.cola_verde.appendleft(paciente_aux)
        if paciente_aux.Triage == Color.Azul:
            self.cola_azul.appendleft(paciente_aux)
    def chequearabierto(self,paciente_aux):
        for i in range(len(self.listaconsult)):
              self.listaconsult[i].revisar_hora()
              if self.listaconsult[i].abierto==True:
                  self.listaconsult[i].ingresaPaciente(paciente_aux)
                  return

    def procesar_personas(self):
        while self.cola_pac:
             paciente = self.cola_pac.pop()
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
        if len(self.cola_rojo) == 0:
             if len(self.cola_naranja) == 0:
                 if len(self.cola_amarillo) == 0:
                     if len(self.cola_verde) == 0:
                         if len(self.cola_azul) == 0:
                             return
                         else:
                             # revisar hora del consutorio, si esta abierto
                             self.chequearabierto(self.cola_azul[0])  # mando al paciente al consultorio
                             for i in range(len(self.cola_azul) - 1):
                                 self.cola_azul[i] = self.cola_azul[i + 1]  # reorganizamos la cola, movemos los pacientes
                             self.contar=self.contar+1
                             return
                     else:
                         self.chequearabierto(self.cola_verde[0])  # mando al paciente al consultorio
                         for i in range(len(self.cola_verde) - 1):
                             self.cola_verde[i] = self.cola_verde[i + 1]  # reorganizamos la cola, movemos los pacientes
                         self.contar = self.contar + 1
                         return
                 else:
                     self.chequearabierto(self.cola_amarillo[0])  # mando al paciente al consultorio que este abierto
                     for i in range(len(self.cola_amarillo) - 1):
                         self.cola_amarillo[i] = self.cola_amarillo[i + 1]  # reorganizamos la cola, movemos los pacientes
                     self.contar = self.contar + 1
                     return
             else:
                 self.chequearabierto(self.cola_naranja[0])  # mando al paciente al consultorio
                 for i in range(len(self.cola_naranja) - 1):
                     self.cola_rojo[i] = self.cola_rojo[i + 1]  # reorganizamos la cola, movemos los pacientes
                 self.contar = self.contar + 1
                 return

        else:
             self.chequearabierto(self.cola_rojo[0])  # mando al paciente al consultorio que este abierto
             for i in range(len(self.cola_rojo) - 1):
                 self.cola_rojo[i] = self.cola_rojo[i + 1]  # reorganizamos la cola, movemos los pacientes
             self.contar = self.contar + 1
             return

    def imprimir_cola(self):
        for paciente in self.cola_pac:
            print(paciente)
        os.system("clear")
    def imprimir_colaROJO(self):
        print("Cola ROJO")
        for paciente in self.cola_rojo:
            print(paciente)
        os.system("clear")

    def imprimir_colaNARANJA(self):
        print("Cola NARANJA:")
        for paciente in self.cola_naranja:
            print(paciente)
        os.system("clear")

    def imprimir_colaAMARILLO(self):
        print("cola AMARILLO:")
        for paciente in self.cola_amarillo:
            print(paciente)
        os.system("clear")


    def imprimir_colaVERDE(self):
        print("cola VERDE")
        for paciente in self.cola_verde:
            print(paciente)
        os.system("clear")

    def imprimir_colaAZUL(self):
        print("cola AZUL")
        for paciente in self.cola_azul:
            print(paciente)
        os.system("clear")
