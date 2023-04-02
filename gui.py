import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
import json

# Чтение данных из файла sorted_hero_winrates.json
with open('sorted_hero_winrates.json', 'r') as file:
    sorted_hero_winrates = json.load(file)

class TableWidget(QTableWidget):
    def __init__(self, data):
        super().__init__()
        self.data = data
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Сортировка героев по винрейту")
        self.setRowCount(len(self.data))
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(["Герой", "Винрейт"])
        self.horizontalHeader().setStretchLastSection(True)
        row = 0
        for hero, winrate in self.data.items():
            hero_item = QTableWidgetItem(hero)
            winrate_item = QTableWidgetItem(str(winrate) + "%")
            self.setItem(row, 0, hero_item)
            self.setItem(row, 1, winrate_item)
            row += 1

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.table_widget = TableWidget(sorted_hero_winrates)
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.table_widget)
        self.setLayout(self.layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec_())
