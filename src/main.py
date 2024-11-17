# main.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from critmass_calculator.calculator_window import CalculatorWindow
from team_builder.team_builder_window import TeamBuilderWindow  # Import TeamBuilderWindow
from main_menu_ui import Ui_MainMenuWindow


class MainMenu(QMainWindow, Ui_MainMenuWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calculatorButton.clicked.connect(self.open_calculator)
        self.teamBuilderButton.clicked.connect(self.open_team_builder)
        self.dropCalculatorButton.clicked.connect(self.open_drop_calculator)
        # TODO: Connect artifact analyzer when implemented

    def open_calculator(self):
        self.calculator = CalculatorWindow()
        self.calculator.show()

    def open_team_builder(self):
        self.team_builder = TeamBuilderWindow()
        self.team_builder.show()

    def open_drop_calculator(self):
        # Placeholder for Artifact Drop Calculator Window
        # self.drop_calculator = DropCalculatorWindow()
        # self.drop_calculator.show()
        QMessageBox.information(self, "Coming Soon", "Artifact Drop Calculator module is not yet implemented.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    sys.exit(app.exec_())
