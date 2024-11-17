# calculator_window.py

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import QtCore
from .calculator_ui import Ui_CalculatorWindow  # Import the generated class


class CalculatorWindow(QMainWindow, Ui_CalculatorWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calculateButton.clicked.connect(self.calculate_crit_mass)

    def calculate_crit_mass(self):
        try:
            crit_damage = float(self.critDamageInput.text().replace(',', '.'))
            crit_chance = float(self.critChanceInput.text().replace(',', '.'))
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid numerical values.")
            return

        # Calculate critical mass using the formula: critical_mass = crit_chance * 2 + crit_damage
        crit_mass = crit_chance * 2 + crit_damage
        crit_mass = round(crit_mass, 1)
        self.resultLabel.setText(f"Critical Mass: {crit_mass}")

        # Evaluate the amount of critical mass
        if crit_mass < 50.0:
            evaluation = "You should replace or upgrade your artifacts."
        elif 50.0 <= crit_mass < 90.0:
            evaluation = "Good critical mass for supports."
        elif 90.0 <= crit_mass < 130.0:
            evaluation = "Excellent critical mass for sub-DPS."
        elif 130.0 <= crit_mass < 500.0:
            evaluation = "You have perfect artifacts!"
        else:
            evaluation = "Are you sure you didn't make a mistake?)"

        self.evaluationLabel.setText(f"{evaluation}")

        # Additional checks with improvement tips
        if crit_chance > 100:
            QMessageBox.information(self, "Information",
                                    "Critical Chance is over 100%, consider shifting towards Critical Damage.")

        # Check the ratio of Critical Chance to Critical Damage (1:2 for balance)
        if abs(crit_chance - (crit_damage / 2)) > 15 or (crit_damage / 2 < 100 and crit_chance < 70):  # Allowable deviation
            QMessageBox.information(self, "Information", "Optimal ratio of Critical Chance to Critical Damage is 1:2.")
