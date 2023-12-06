import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QHBoxLayout
from PyQt6.QtCore import QTimer

class ColorSorter(QWidget):
    def __init__(self):
        super().__init__()

        self.colors = []
        self.colors_count = {'red': 0, 'orange': 0, 'yellow': 0, 'green': 0, 'blue': 0}

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Color Sorter')

        main_layout = QHBoxLayout()

        for color in self.colors_count:
            button_layout = QVBoxLayout()
            main_layout.addLayout(button_layout)

            button = QPushButton(color.title())
            button.setStyleSheet(f"background-color: {color};")
            button_layout.addWidget(button)

        self.setLayout(main_layout)
        self.show()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.add_color)
        self.timer.start(1000)

    def add_color(self):
        new_colors = ['red', 'orange', 'yellow', 'yellow', 'yellow', 'green', 'green', 'blue', 'blue', 'blue']
        new_color = random.choice(new_colors)
        self.colors.append(new_color)
        self.colors_count[new_color] += 1

        for layout_idx, (color, count) in enumerate(self.colors_count.items()):
            button_layout = self.layout().itemAt(layout_idx)
            while button_layout.count() > 1:
                widget = button_layout.itemAt(1).widget()
                button_layout.removeWidget(widget)
                widget.setParent(None)

            for _ in range(count):
                button = QPushButton(color.title())
                button.setStyleSheet(f"background-color: {color};")
                button_layout.addWidget(button)

def main():
    app = QApplication(sys.argv)
    ex = ColorSorter()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
