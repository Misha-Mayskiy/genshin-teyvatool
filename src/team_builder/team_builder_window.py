import json
import os
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore
from .team_builder_ui import Ui_TeamBuilderWindow


class TeamBuilderWindow(QMainWindow, Ui_TeamBuilderWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.load_characters()

        # Connect buttons to their functions
        self.addButton.clicked.connect(self.add_to_team)
        self.removeButton.clicked.connect(self.remove_from_team)
        self.optimizeButton.clicked.connect(self.optimize_team)

    def load_characters(self):
        """
        Load characters from a JSON file into the available characters list.
        """
        try:
            # Get the absolute path to the 'characters.json' file
            script_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.abspath(os.path.join(script_dir, '..', '..'))
            json_path = os.path.join(project_root, 'resources', 'characters.json')

            with open(json_path, 'r', encoding='utf-8') as file:
                characters = json.load(file)

            self.characters = characters  # Store for later use

            for char in characters:
                item_text = f"{char['name']} - {char['role']} - {char['element']}"
                self.availableCharactersList.addItem(item_text)
        except FileNotFoundError:
            QMessageBox.critical(self, "Error",
                                 f"'characters.json' not found at {json_path}. Please ensure the file exists.")
        except json.JSONDecodeError as e:
            QMessageBox.critical(self, "Error", f"Failed to parse 'characters.json': {e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")

    def add_to_team(self):
        """
        Add selected characters from available list to the team list.
        """
        selected_items = self.availableCharactersList.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "No Selection", "Please select at least one character to add.")
            return

        for item in selected_items:
            if self.selectedTeamList.count() >= 4:
                QMessageBox.warning(self, "Team Full", "The team can have a maximum of 4 characters.")
                break
            if not self.selectedTeamList.findItems(item.text(), QtCore.Qt.MatchExactly):
                self.selectedTeamList.addItem(item.text())

    def remove_from_team(self):
        """
        Remove selected characters from the team list.
        """
        selected_items = self.selectedTeamList.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "No Selection", "Please select at least one character to remove.")
            return

        for item in selected_items:
            self.selectedTeamList.takeItem(self.selectedTeamList.row(item))

    def optimize_team(self):
        """
        Optimize the team based on selected characters.
        For simplicity, this will just check for elemental synergies.
        """
        team = [self.selectedTeamList.item(i).text() for i in range(self.selectedTeamList.count())]
        if not team:
            QMessageBox.warning(self, "Empty Team", "Please select at least one character to optimize.")
            return

        elements = [self.get_element(char) for char in team]
        element_set = set(elements)

        # Ensure at least two different elements for better reactions
        if len(element_set) < 2:
            QMessageBox.warning(self, "Weak Synergy",
                                "It's better to have at least two different elements for optimal reactions.")
            return

        QMessageBox.information(self, "Optimized Team", "Your team has good elemental synergies!")

    def get_element(self, character_text):
        """
        Retrieve the element of a character based on the selected list item text.
        """
        name = character_text.split(" - ")[0]
        for char in self.characters:
            if char['name'] == name:
                return char['element']
        return None
