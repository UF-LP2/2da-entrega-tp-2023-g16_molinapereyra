import csv
from src.cPaciente import Paciente
from src.Funciones import simulacion



def main() -> None:
  lista_p = []
  with open("tabla_pacientes.csv", newline='') as csvfile:
     lector = csv.reader(csvfile, delimiter=',', quotechar='|')
     next(csvfile, None)
     for row in lector:
        try:
          aux = Paciente(row[0], row[1], row[2], row[3], row[4], row[5], 1, 0)
          lista_p.append(aux)
        except Exception as e:
          print(str(e))
          
  for i in range(len(lista_p)):
    print(lista_p[i])
          
  print("lista grabada")
  
  
if __name__ == "__main__":
  main()
