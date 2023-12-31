import csv
import time

#from src.Funciones import *
from src.cHospital import *



def main() -> None:
  lista_p = []
  with open("Triage (3).csv", newline='') as csvfile:
    lector = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(csvfile, None)
    for row in lector:
      try:
        aux = Paciente(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        lista_p.append(aux)
      except Exception as e:
        print(str(e))
    mi_hospital = Hospital()
    mi_consultorio1=Consultorio(1) #turno 23 a 6 (un solo enfermero)
    mi_consultorio2=Consultorio(2) #turno 6 a 10 (2 enfermeros)
    mi_consultorio3=Consultorio(2)
    mi_consultorio4=Consultorio(3) #turno 10 a 16 (3 enfermeros
    mi_consultorio5=Consultorio(3)
    mi_consultorio6=Consultorio(3)
    mi_consultorio7=Consultorio(4) #turno 16 a 23 (4 enfermeros)
    mi_consultorio8=Consultorio(4)
    mi_consultorio9=Consultorio(4)
    mi_consultorio10=Consultorio(4)
    mi_hospital.agregar_consultorio(mi_consultorio1)
    mi_hospital.agregar_consultorio(mi_consultorio2)
    mi_hospital.agregar_consultorio(mi_consultorio3)
    mi_hospital.agregar_consultorio(mi_consultorio4)
    mi_hospital.agregar_consultorio(mi_consultorio5)
    mi_hospital.agregar_consultorio(mi_consultorio6)
    mi_hospital.agregar_consultorio(mi_consultorio7)
    mi_hospital.agregar_consultorio(mi_consultorio8)
    mi_hospital.agregar_consultorio(mi_consultorio9)
    mi_hospital.agregar_consultorio(mi_consultorio10)

    tiempo_inicio = datetime.now()
    i=0
    aux=0
    hora_actual = datetime.now()
    print(hora_actual)
    cont_ingreso_h=2
    while True:
        horaglobal=hora_actual
        print((hora_actual))
        if cont_ingreso_h == 2: #cada 2 minutos agrego un paciente
            mi_hospital.agregar_persona(lista_p[i])
            mi_hospital.ordenar_color() #ordena la cola por color del triage
            cont_ingreso_h=0
        print(mi_hospital.imprimir_colaROJO())
        print(mi_hospital.imprimir_colaAMARILLO())
        print(mi_hospital.imprimir_colaAZUL())
        print(mi_hospital.imprimir_colaVERDE())
        print(mi_hospital.imprimir_colaNARANJA())
        mi_hospital.atender()
        time.sleep(3) # Pausa entre cada iteración para simular el paso del tiempo
        #manejo de tiempo:
        hora=hora_actual.hour
        dia=hora_actual.day
        minuto=hora_actual.minute + 1
        cont_ingreso_h= cont_ingreso_h+1
        if minuto>=59:
          hora_actual=hora_actual.replace(hour=hora+1,minute=0)
        else:
          hora_actual=hora_actual.replace(minute=minuto) #el tiempo pasa cada 10 minutos
        if hora==23:
          print(hora_actual)
          hora_actual = hora_actual.replace(day=dia+1,hour=0, minute=0)
        #print(hora_actual)
        i=i+1
        if i >= len(lista_p):
            break

  print("hora inicio: ",tiempo_inicio)





if __name__ == "__main__":
  main()
