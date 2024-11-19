import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                             QWidget, QVBoxLayout, QHBoxLayout, QComboBox,
                             QCheckBox, QMessageBox, QGridLayout)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class ArtifactAnalyzerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ArteFactor - Artifact Analyzer")
        self.setWindowIcon(QIcon("resources/icons/drop_calculator_icon.png"))
        self.setFixedSize(600, 500)

        # Initialize UI Elements
        self.initUI()

        # Apply Stylesheet
        self.applyStyles()

    def initUI(self):
        # Central Widget
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)

        # Main Layout
        mainLayout = QVBoxLayout()
        self.centralWidget.setLayout(mainLayout)

        # Title Label
        self.titleLabel = QLabel("Artifact Probability Calculator")
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(Qt.AlignCenter)
        mainLayout.addWidget(self.titleLabel)

        # Rarity Selection
        rarityLayout = QHBoxLayout()
        rarityLabel = QLabel("Artifact Rarity:")
        self.rarityComboBox = QComboBox()
        self.rarityComboBox.addItems(["4-Star", "5-Star"])
        rarityLayout.addWidget(rarityLabel)
        rarityLayout.addWidget(self.rarityComboBox)
        mainLayout.addLayout(rarityLayout)

        # Artifact Type Selection
        typeLayout = QHBoxLayout()
        typeLabel = QLabel("Artifact Type:")
        self.typeComboBox = QComboBox()
        self.typeComboBox.addItems(["Flower", "Plume", "Sands", "Goblet", "Circlet"])
        typeLayout.addWidget(typeLabel)
        typeLayout.addWidget(self.typeComboBox)
        mainLayout.addLayout(typeLayout)

        # Preferred Substats Selection
        substatGroupLabel = QLabel("Select Preferred Substats (Up to 4):")
        mainLayout.addWidget(substatGroupLabel)

        self.substatCheckboxes = []
        substatOptions = ["HP%", "ATK%", "DEF%", "Energy Recharge%", "Elemental Mastery",
                          "Crit Rate%", "Crit Damage%", "Flat HP", "Flat ATK", "Flat DEF"]
        substatGridLayout = QGridLayout()
        for i, substat in enumerate(substatOptions):
            checkbox = QCheckBox(substat)
            self.substatCheckboxes.append(checkbox)
            substatGridLayout.addWidget(checkbox, i // 2, i % 2)
        mainLayout.addLayout(substatGridLayout)

        # Calculate Button
        self.calculateButton = QPushButton("Calculate Probability")
        self.calculateButton.clicked.connect(self.calculateProbability)
        mainLayout.addWidget(self.calculateButton)

        # Result Label
        self.resultLabel = QLabel("")
        self.resultLabel.setAlignment(Qt.AlignCenter)
        self.resultLabel.setWordWrap(True)
        mainLayout.addWidget(self.resultLabel)

    def applyStyles(self):
        style = """
        QWidget {
            background-color: #3B4252;
            color: #ECEFF4;
            font-size: 14px;
        }
        QLabel {
            color: #ECEFF4;
        }
        QPushButton {
            background-color: #5E81AC;
            border: none;
            border-radius: 10px;
            color: #ECEFF4;
            height: 40px;
        }
        QPushButton:hover {
            background-color: #81A1C1;
        }
        QComboBox, QCheckBox {
            background-color: #434C5E;
            color: #ECEFF4;
            border: none;
            selection-background-color: #5E81AC;
        }
        """
        self.centralWidget.setStyleSheet(style)

    def calculateProbability(self):
        # Collect user inputs
        rarity = self.rarityComboBox.currentText()
        rarity_value = 4 if rarity == "4-Star" else 5
        artifact_type = self.typeComboBox.currentText()

        # Collect preferred substats
        preferred_substats = [checkbox.text() for checkbox in self.substatCheckboxes if checkbox.isChecked()]
        if len(preferred_substats) == 0 or len(preferred_substats) > 4:
            QMessageBox.warning(self, "Input Error", "Please select between 1 and 4 preferred substats.")
            return

        # Calculate Probability
        probability = self.computeArtifactProbability(rarity_value, preferred_substats)
        result_text = f"The probability of obtaining an artifact with your preferred substats is:\n" \
                      f"{probability:.5f}%"
        self.resultLabel.setText(result_text)

    def computeArtifactProbability(self, rarity, preferred_substats):
        from math import comb

        # All possible substats
        all_substats = ["HP%", "ATK%", "DEF%", "Energy Recharge%", "Elemental Mastery",
                        "Crit Rate%", "Crit Damage%", "Flat HP", "Flat ATK", "Flat DEF"]

        total_substats = len(all_substats)
        desired_substat_count = len(preferred_substats)

        # Initial substat count probabilities for artifacts in Genshin Impact
        # For 4* and 5* artifacts, they can start with 3 or 4 substats
        # Let's assume equal chances for simplicity in this implementation
        initial_substat_counts = [3, 4]
        initial_substat_prob = {3: 0.5, 4: 0.5}  # Simplified assumption

        # Calculate the probability
        total_probability = 0.0

        for initial_count in initial_substat_counts:
            prob_initial_count = initial_substat_prob[initial_count]

            # Calculate the probability of starting with desired substats
            prob_desired_initial = comb(desired_substat_count, min(desired_substat_count, initial_count)) * \
                                   comb(total_substats - desired_substat_count,
                                        initial_count - min(desired_substat_count, initial_count)) / \
                                   comb(total_substats, initial_count)

            # Remaining substats to obtain during upgrades
            remaining_substats_needed = max(0, desired_substat_count - initial_count)
            total_upgrades = 5 if rarity == 5 else 4  # Number of upgrades for 5* and 4* artifacts
            upgrade_chances = total_upgrades

            # Probability of obtaining remaining desired substats during upgrades
            prob_desired_upgrades = 1.0
            for i in range(remaining_substats_needed):
                prob_desired_upgrades *= (desired_substat_count - initial_count - i) / (
                            total_substats - initial_count - i)

            # Combine probabilities
            total_prob = prob_initial_count * prob_desired_initial * prob_desired_upgrades * 100  # As a percentage
            total_probability += total_prob

        return total_probability


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArtifactAnalyzerWindow()
    window.show()
    sys.exit(app.exec_())
