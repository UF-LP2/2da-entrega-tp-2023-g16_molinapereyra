import csv
from src.Funciones import *
from src.cHospital import *
#from src.cPaciente import Paciente
#from src.Funciones import simulacion



def main() -> None:
  lista_p = []
  with open("Triage (1).csv", newline='') as csvfile:
    lector = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(csvfile, None)
    for row in lector:
      try:
        aux = Paciente(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        lista_p.append(aux)
      except Exception as e:
        print(str(e))
        
    #hospital = Hospital()
    #simulación de la cola del triage
    
  
  #start_time = simulacion(lista_p)
  #print("Hora en datetime: ", str(horaglobal))
  print("Hora global modificada: ", timestamp)
  #for i in range(len(lista_p)):
  #  print(str(lista_p[i]))
  
  
if __name__ == "__main__":
  main()
