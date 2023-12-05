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
        self.listaconsult=[]

    def agregar_consultorio(self,consultorio):
        self.listaconsult.append(consultorio)
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
    def chequearabierto(self):
        i=0
        for i in range(len(self.listaconsult)):
              if self.listaconsult[i].revisar_hora() == True and self.listaconsult[i].PacienteAtendido == None:
                  return i #retorna el consultorio a donde va a ingregar el paciente
        return -1

    def chequearAbiertoROJO(self):
        i = 0
        for i in range(len(self.listaconsult)):
            if self.listaconsult[i].revisar_hora() == True:
                return i #siempre va a haber uno abierto

    def procesar_personas(self,paciente):
             diferencia = horaglobal - paciente.hora_ingreso #calculamos diferencia de hora para saber el tiempo de espera
             tsecs= diferencia.total_seconds()
             minutos= tsecs/60
             if paciente.Triage == Color.Naranja and minutos > 10:
                 raise Exception(f"Tiempo de espera SUPERADO")
                 return False # devuelve false si el paciente supero su tiempo de espera
             if paciente.Triage == Color.Amarillo and minutos > 60:
                 raise Exception(f"Tiempo de espera SUPERADO")
                 return False
             if paciente.Triage == Color.Verde and minutos > 120:
                 raise Exception(f"Tiempo de espera SUPERADO")
                 return False
             if paciente.Triage == Color.Azul and minutos > 240:
                 raise Exception(f"Tiempo de espera SUPERADO")
                 return False
    def modificarPAcientes(self):
        i=0
        for i in range(len(self.listaconsult)):
            if self.listaconsult[i].PacienteEnEspera != None: #en caso de que haya un paciente en espero, lo paso a paciente atendido
                self.listaconsult[i].PacienteAtendido = self.listaconsult[i].PacienteEnEspera
                self.listaconsult[i].PacienteEnEspera= None


    def atender(self):
        self.disminuir_tiempo_consult()
        self.modificarPAcientes()
        aux = self.chequearabierto()
        if len(self.cola_rojo) == 0:
             if len(self.cola_naranja) == 0:
                 if len(self.cola_amarillo) == 0:
                     if len(self.cola_verde) == 0:
                         if len(self.cola_azul) == 0:
                             return
                         else:
                             # revisar hora del consutorio, si esta abierto
                              #como supero el tiempo de espera, no se atiende al paciente
                             #si no devuelve false, se atiende al paciente
                             if aux != -1: # mando al paciente al consultorio
                                 paciente = self.cola_azul.pop()
                                 if self.procesar_personas(paciente) == False:
                                     return
                                 self.listaconsult[aux].ingresaPaciente(paciente)
                                # for i in range(len(self.cola_azul) - 1):
                                 #   self.cola_azul[i] = self.cola_azul[i + 1]  # reorganizamos la cola, movemos los pacientes

                                 #return
                             return
                     else:
                         if aux != -1:  # mando al paciente al consultorio
                             paciente = self.cola_verde.pop()
                             if self.procesar_personas(paciente) == False:
                                 return
                             self.listaconsult[aux].ingresaPaciente(paciente)
                             #for i in range(len(self.cola_verde) - 1):
                              #   self.cola_verde[i] = self.cola_verde[i + 1]  # reorganizamos la cola, movemos los pacientes
                             #return
                         return
                 else:
                     if aux != -1:  # mando al paciente al consultorio
                         paciente = self.cola_amarillo.pop()
                         if self.procesar_personas(paciente) == False:
                             return
                         self.listaconsult[aux].ingresaPaciente(paciente)
                        # for i in range(len(self.cola_amarillo) - 1):
                          #   self.cola_amarillo[i] = self.cola_amarillo[i + 1]  # reorganizamos la cola, movemos los pacientes
                         #return
                     return
             else:
                 if aux != -1:  # mando al paciente al consultorio
                     paciente = self.cola_naranja.pop()
                     if self.procesar_personas(paciente) == False:
                         return
                     self.listaconsult[aux].ingresaPaciente(paciente)
                     #for i in range(len(self.cola_naranja) - 1):
                         #self.cola_naranja[i] = self.cola_naranja[i + 1]  # reorganizamos la cola, movemos los pacientes

                     #return
                 return

        else:
            if aux != -1:  # mando al paciente al consultorio
                paciente = self.cola_rojo.pop()
                self.listaconsult[aux].ingresaPaciente(paciente)
                #for i in range(len(self.cola_rojo) - 1):
                 #   self.cola_rojo[i] = self.cola_rojo[i + 1]  # reorganizamos la cola, movemos los pacientes

                return
            else:# en caso que este ocupado, un paciente queda en espera
                aux1=self.chequearAbiertoROJO()
                paciente = self.cola_rojo.pop()
                self.listaconsult[aux1].cambiarPac(paciente)
                #for i in range(len(self.cola_rojo) - 1):
                  #  self.cola_rojo[i] = self.cola_rojo[i + 1]  # reorganizamos la cola, movemos los pacientes

                #return
            return

    def disminuir_tiempo_consult(self):
        i=0
        for i in range(len(self.listaconsult)):
            self.listaconsult[i].atenderPac() #disminuye 1 minuto a todos los pacientes que estan en consultorio

    def imprimir_cola(self):
        for paciente in self.cola_pac:
            print(paciente)

    def imprimir_colaROJO(self):
        print("Cola ROJO")
        for paciente in self.cola_rojo:
            print(paciente)

    def imprimir_colaNARANJA(self):
        print("Cola NARANJA:")
        for paciente in self.cola_naranja:
            print(paciente)

    def imprimir_colaAMARILLO(self):
        print("cola AMARILLO:")
        for paciente in self.cola_amarillo:
            print(paciente)


    def imprimir_colaVERDE(self):
        print("cola VERDE")
        for paciente in self.cola_verde:
            print(paciente)

    def imprimir_colaAZUL(self):
        print("cola AZUL")
        for paciente in self.cola_azul:
            print(paciente)
