import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QListWidget, QTextEdit, QGroupBox)
from PyQt6.QtCore import Qt, QDateTime, QTimer
from main import *


class VentanaHospital(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):

        #mostrar la hora
        hora=horaglobal.hour
        minutos=horaglobal.minute
        layout = QVBoxLayout()

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setText(f'Hora: {hora:02d}:{minutos:02d}')  # Formatear el texto
        layout.addWidget(self.label)

        self.setLayout(layout)
        #sys.exit(app.exec())

        #mostrar la lista
        #layout = QVBoxLayout()

        # Crear un QTextEdit para mostrar la información de los pacientes
        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)
        self.setLayout(layout)
        pacientes = self.leer_pacientes_desde_archivo()
        self.mostrar_pacientes(pacientes)

    def leer_pacientes_desde_archivo(self):
        pacientes = []
        with open("Triage (3).csv", newline='') as csvfile:
            lector = csv.reader(csvfile, delimiter=',', quotechar='|')
            next(csvfile, None)
            for row in lector:
                try:
                    paciente_info = Paciente(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
                    pacientes.append(paciente_info)
                except Exception as e:
                    print(str(e))
            return pacientes

    def mostrar_pacientes(self, pacientes):
        # Mostrar la información de los pacientes en el QTextEdit
        self.text_edit.clear()
        for paciente in pacientes:
            paciente.asignar_color()
            self.text_edit.append(str(paciente))

    def create_paciente_group_box(self, paciente_info):
        grupo_box = QGroupBox()
        layout = QVBoxLayout()
        label = QLabel(paciente_info)
        layout.addWidget(label)
        grupo_box.setLayout(layout)
        return grupo_box





    # nombre del archivo
#class PatientManager(QWidget):
#    def __init__(self):
#         super().__init__()
#         self.setWindowTitle('Hospital')
#
#         self.patients_list = QListWidget()

  #       layout = QVBoxLayout()
  #       layout.addWidget(self.patients_list)

   #      self.setLayout(layout)

         # Configurar un temporizador para leer los pacientes cada 5 segundos (5000 milisegundos)
    #     self.timer = QTimer(self)
    #     self.timer.timeout.connect(self.load_patients)
    #     self.timer.start(5000)  # Tiempo en milisegundos (5 segundos)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaHospital()
    ventana.show()
    ventana.setGeometry(100, 100, 400, 300)
    sys.exit(app.exec())
