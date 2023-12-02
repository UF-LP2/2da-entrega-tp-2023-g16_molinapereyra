#from eColor import horaglobal
from src.cPaciente import *

def _init_(self, Turno):
    self.PacienteAtendido = None
    self.abierto = False
    self.turno = Turno  # turno1,2,3,4


def ingresaPaciente(self, Paciente_aux):
    self.PacienteAtendido = Paciente_aux
    self.PacienteAtendido.contador_atendido = self.PacienteAtendido.contador_atendido - 1  # disminuimos el contador


def revisar_hora(self):
    if self.Turno == 1:
        # 23 a 6
        if horaglobal >= 2300 and horaglobal <= 600:
            abierto = True
        else:
            abierto = False
    if self.Turno == 2:
        # 6 a 10
        if horaglobal >= 600 and horaglobal <= 1000:
            abierto = True
        else:
            abierto = False
    if self.Turno == 3:
        # 10 a 16
        if horaglobal >= 1000 and horaglobal <= 1600:
            abierto = True
        else:
            abierto = False
    if self.Turno == 4:
        # 16 a 23
        if horaglobal > 1600 and horaglobal <= 2300:
            abierto = True
        else:
            abierto = False
            # llama chequeartiempodeespera()
        # exception si supera el tiempo de espera de su correspondiente color
        # lo atendemos igual? o descartamos paciente
        # si esta el horario -> sumar tiempo de consulta a hora global y eliminar paciente de cola
        # llamamos funcion desencolar()