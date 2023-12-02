import csv
from Funciones import simulacion
from src.cHospital import *
#from src.cPaciente import Paciente
#from src.Funciones import simulacion



def main() -> None:
  lista_p = []
  with open("Triage.csv", newline='') as csvfile:
    lector = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(csvfile, None)
    for row in lector:
      try:
        aux = Paciente(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
        lista_p.append(aux)
      except Exception as e:
        print(str(e))
  simulacion(lista_p)
  #for i in range(len(lista_p)):
  #  print(str(lista_p[i]))
  
  
if __name__ == "__main__":
  main()
