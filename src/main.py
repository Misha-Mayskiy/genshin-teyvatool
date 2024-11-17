import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from critmass_calculator.calculator_window import CalculatorWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calculator_window = CalculatorWindow()
        self.setWindowTitle("Genshin Impact Toolkit")
        self.setGeometry(100, 100, 800, 600)
        # Здесь можно добавить меню или кнопки для открытия различных модулей


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorWindow()  # Или MainWindow, если есть главное меню
    window.show()
    sys.exit(app.exec_())
