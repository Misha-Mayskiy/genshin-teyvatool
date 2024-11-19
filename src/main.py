import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from critmass_calculator.calculator_window import CalculatorWindow
from team_builder.team_builder_window import TeamBuilderWindow
from artifact_analyzer.artifact_analyzer_window import ArtifactAnalyzerWindow
from main_menu_ui import Ui_MainMenuWindow


class MainMenu(QMainWindow, Ui_MainMenuWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calculatorButton.clicked.connect(self.open_calculator)
        self.teamBuilderButton.clicked.connect(self.open_team_builder)
        self.dropCalculatorButton.clicked.connect(self.open_drop_calculator)

        # Connect info buttons
        self.calculatorInfoButton.clicked.connect(self.show_calculator_info)
        self.teamBuilderInfoButton.clicked.connect(self.show_team_builder_info)
        self.dropCalculatorInfoButton.clicked.connect(self.show_drop_calculator_info)

    def open_calculator(self):
        self.calculator = CalculatorWindow()
        self.calculator.show()

    def open_team_builder(self):
        self.team_builder = TeamBuilderWindow()
        self.team_builder.show()

    def open_drop_calculator(self):
        self.artifact_analyzer = ArtifactAnalyzerWindow()
        self.artifact_analyzer.show()

    # Info button slots
    def show_calculator_info(self):
        QMessageBox.information(self, "Info",
                                "Calculate the critical mass of your character's artifacts.\n"
                                "Input your current artifact crit stats to see calculated crit mass and evaluation.")

    def show_team_builder_info(self):
        QMessageBox.information(self, "Info",
                                "Build potentially perfect teams from your available characters.\n"
                                "Choose your team from available character's and see real potential damage.")

    def show_drop_calculator_info(self):
        QMessageBox.information(self, "Info",
                                "Calculate the chance of obtaining an artifact with preferred sub-stats.\n"
                                "Select your artifact rare and wanted sub-stats to see chances on perfect artifact.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_menu = MainMenu()
    main_menu.show()
    sys.exit(app.exec_())
