#from eColor import horaglobal
from src.cPaciente import *
class Consultorio:
    def __init__(self,Turno:int):
        self.PacienteAtendido = None
        self.abierto = False
        self.turno = Turno  # turno1,2,3,4

    def getAbierto(self):
        return self.abierto

    def ingresaPaciente(self, Paciente_aux):
        self.PacienteAtendido = Paciente_aux


    def atenderPac(self):
        if self.PacienteAtendido ==None:
            return #el consultorio esta vacio, no se tiene que disminuir el tiempo
        if self.PacienteAtendido.contar_atendido != 0:
            self.PacienteAtendido.contar_atendido = self.PacienteAtendido.contar_atendido - 1  # disminuimos el contador
            return
        else:
            self.PacienteAtendido= None #elimino el paciente porque ya esta atendido

    def revisar_hora(self):
        hora=horaglobal.hour

        if self.turno == 1:
        # 23 a 6
            if hora >= 23 and hora <= 6:
                abierto = True
                return True
            else:
                abierto = False
                return False
        if self.turno == 2:
        # 6 a 10
            if hora >= 6 and hora <= 10:
                abierto = True
                return True
            else:
                abierto = False
                return False
        if self.turno == 3:
        # 10 a 16
            if hora >= 10 and hora <= 16:
                abierto = True
                return True
            else:
                abierto = False
                return False
        if self.turno == 4:
        # 16 a 23
            if hora > 16 and hora <= 23:
                abierto = True
                return True
            else:
                abierto = False
                return False
            # llama chequeartiempodeespera()
        # exception si supera el tiempo de espera de su correspondiente color
        # lo atendemos igual? o descartamos paciente
        # si esta el horario -> sumar tiempo de consulta a hora global y eliminar paciente de cola
        # llamamos funcion desencolar()