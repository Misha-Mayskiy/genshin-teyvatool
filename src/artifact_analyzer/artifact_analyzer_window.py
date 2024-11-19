import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from .artifact_analyzer_ui import Ui_ArtifactAnalyzerWindow  # Import the UI class


class ArtifactAnalyzerWindow(QMainWindow, Ui_ArtifactAnalyzerWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect signals
        self.calculateButton.clicked.connect(self.calculateProbability)

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
                      f"<b>{probability:.6f}%</b>"
        self.resultLabel.setText(result_text)

    def computeArtifactProbability(self, rarity, preferred_substats):
        from math import comb

        # All possible substats
        all_substats = ["HP%", "ATK%", "DEF%", "Energy Recharge%", "Elemental Mastery",
                        "Crit Rate%", "Crit Damage%", "Flat HP", "Flat ATK", "Flat DEF"]

        total_substats = len(all_substats)
        desired_substat_count = len(preferred_substats)

        # Initial substat count probabilities for simplicity
        initial_substat_probabilities = {
            3: 0.5,
            4: 0.5
        }

        total_probability = 0.0

        for initial_substat_count, init_prob in initial_substat_probabilities.items():
            # Probability calculations
            possible_substats = comb(total_substats, initial_substat_count)
            desired_in_initial = min(desired_substat_count, initial_substat_count)

            prob_desired_initial = (
                    comb(desired_substat_count, desired_in_initial) *
                    comb(total_substats - desired_substat_count, initial_substat_count - desired_in_initial) /
                    possible_substats
            )

            remaining_preferred = desired_substat_count - desired_in_initial
            total_upgrades = 4 if rarity == 4 else 5
            available_substats_pool = total_substats - initial_substat_count

            if remaining_preferred > total_upgrades:
                prob_desired_upgrades = 0.0
            else:
                prob_desired_upgrades = comb(total_upgrades, remaining_preferred) * \
                                        (desired_substat_count - desired_in_initial) ** remaining_preferred * \
                                        (available_substats_pool - (desired_substat_count - desired_in_initial)) ** (
                                                total_upgrades - remaining_preferred) / \
                                        (available_substats_pool ** total_upgrades)

            total_prob = init_prob * prob_desired_initial * prob_desired_upgrades * 100.0
            total_probability += total_prob

        return total_probability


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ArtifactAnalyzerWindow()
    window.show()
    sys.exit(app.exec_())
