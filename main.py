import csv
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn import preprocessing
from src.cPaciente import Paciente
from src.Funciones import simulacion



def main() -> None:
  # with open("tabla_pacientes.csv", newline='') as csvfile:
  #    lector = csv.reader(csvfile, delimiter=',', quotechar='|')
  #    next(csvfile, None)
  #    for row in lector:
  #       try:
  #         aux = Paciente(row[0], row[1], row[2], row[3], row[4], row[5], 1, 0)
  #         lista_p.append(aux)
  #       except Exception as e:
  #         print(str(e))
          
  # for i in range(len(lista_p)):
  #   print(lista_p[i])
  
  datos = pd.read_csv("tabla_pacientes.csv", delimiter=',')
  datos[0:5]
  print("Datos: \n", datos)
  
  #Leo las enfermedades que hay y cuantas veces se repite
  Enfermedad = datos['Enfermedad'].value_counts()
  print("Enfermedad: \n", Enfermedad)
  
  #Creo la lista de datos de forma indepeniente
  x = datos[['DNI-1', 'first_name', 'Last_name', 'edad', 'gender']].values
  x[0:5]
  print("Lista: \n", x)
  
  #Convierto las varibles categoricas a varibles continuas
  genero = preprocessing.LabelEncoder() #Guarda la codificacion para la tranformacion
  genero.fit(datos['gender']) #Selecciona las posibles variables
  x[:,4] = genero.transform(datos['gender']) #Transforma toda la columna de gender
  
  x[0:5]
  #print("Pacientes: \n", x)
  
  lista_p = []
  
  for i in range(len(x)):
    aux = x[i]
    Paciente = aux
    lista_p.append(Paciente)
  
  print("Pacientes: \n", lista_p)
  #print("lista grabada")
  
  
if __name__ == "__main__":
  main()
