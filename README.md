[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/LcojlfsQ)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-7f7980b617ed060a017424585567c406b6ee15c891e84e1186181d67ecf80aa0.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=12558224)
# G***NroGrupo***_***Apellido1******Apellido2***_TP***1/2/../Final***
#G***16***_***Datenis******Molina******Pereyra2***_TP***1/2/../Final***
  "Breve descripción del trabajo"
En este trabajo intentamos resolver el problema de sistema de atencion de Triage de hospital.Para resolverlo nosotros planteamos un paciente con 4 sintomas: dolor, respira, movilidad, perdida de conciencia.Tenemos un hospital que con una cierta frecuencia van entrando los pacientes, se le realiza el Triage utilizando un arbol de desicion para colocarle su color.Luego lo separamos en colas de acuerdo al color.Por ultimo atendemos los pacientes, en orden, primero los rojo, si no hay rojos continuo con la proxima cola de acuerdo a la gravedad.Para atender al paciente nos fijamos que consultorios se encuentran abierto segun el turno y que este vacio para que pueda entrar al consultorio.Los pacientes van tardar 10 minutos dentro del consultorio excepto los rojo que entran y salen, debido a su complejidad son trasladados a otra parte.
Si llega un paciente rojo que es de atencion inmediata y todos los consultorios estan ocupados.Colocamos al paciente que estaba en el consultorio en espera, y atendemos al rojo.Una vez que sale el rojo, continuamos atendiendo al paciente en espera.
## Integrantes
- Lucas Datenis
- Lucia Molina Pavlicka
- Maria Pereyra

## Objetivo del proyecto
"Descripción del problema y el objetivo del desarrollo del proyecto"
El problema que resolvemos en este proyecto es sistema de atencion en Triage de hospital. El objetivo es un sistema eficiente, donde los pacientes no esperen mas de lo indicado segun su triage y que no haya sala de espera ociosa.Los enfermeros son clones, todos tienen la misma velocidad y capacidad para realizar el triage

## Requisitos
"Explicación de requisitos, librerias y explicaciones de uso"
Librerias utilizadas time,deque,enum, datetime
_ enum import Enum
Utilizada para crear la clase Color de Enum, vamos a tener los distintos colores posibles de acuerdo al triage.El color de triage se va a elegir de acuerdo a los sintomas que presenta el paciente
_ from collections import deque
Usada para manejo de colas en el proyecto, nos permite agregar al frente con appendleft() y eliminar por el otro extremo utilzando pop().Tenemos colas de cada color, cola de pacientes.
_from datetime import *
_import time
Esta libreria la usamos para manejar el tiempo, nos permite obtener  un objeto con la hora actual(day,minute, hour) para manejar la hora global.Luego a esta hora global le modificamos los minutos de esa hora para indicar el paso del tiempo.Tambien la usamos para obtener la hora de ingreso del paciente.Calcular  la diferencia  entre el ingreso y la hora actual y ver si supero su tiempo de espera segun el color de Triage.


---
##### UF-FICEN LP2 2023 - GNU General Public License v3.0
