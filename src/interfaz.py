import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QComboBox

class ObjectManager(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Object Manager')

        self.objects_list = QListWidget()
        self.colors_combo = QComboBox()
        self.colors_combo.addItems(['Red', 'Blue', 'Green'])  # Colores disponibles
        self.move_button = QPushButton('Move Selected')

        layout = QVBoxLayout()
        objects_layout = QHBoxLayout()
        objects_layout.addWidget(self.objects_list)
        objects_layout.addWidget(self.colors_combo)
        layout.addLayout(objects_layout)
        layout.addWidget(self.move_button)

        self.setLayout(layout)

        self.move_button.clicked.connect(self.move_selected_objects)

    def move_selected_objects(self):
        selected_items = self.objects_list.selectedItems()
        selected_color = self.colors_combo.currentText()

        # Mover los objetos seleccionados a otra lista o realizar acciones basadas en el color seleccionado
        for item in selected_items:
            # Aquí puedes agregar lógica para mover elementos a otra lista según el color seleccionado
            # Por ejemplo, puedes tener otras QListWidget y agregar elementos según el color a esas listas
            print(f"Objeto: {item.text()}, Color: {selected_color}")
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ObjectManager()
    window.setGeometry(100, 100, 400, 300)
    window.show()
    #sys.exit(app.exec_())