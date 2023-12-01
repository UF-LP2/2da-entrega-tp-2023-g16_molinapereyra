import cPaciente

class Hospital:
 def __init__(self, velocidad_salida):
     self.cola_pac=
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
              if self.listaconsult[i].abierto==True
                  self.listaconsult[i].ingresaPaciente(paciente_aux)


      #falta defprocesarpersonas y atender