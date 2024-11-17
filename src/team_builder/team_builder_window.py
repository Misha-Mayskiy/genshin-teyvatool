# team_builder_window.py

import json
import os
import logging
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem, QApplication
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore
from .team_builder_ui import Ui_TeamBuilderWindow

# Configure logging to file
logging.basicConfig(
    filename='logs/team_builder.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


class TeamBuilderWindow(QMainWindow, Ui_TeamBuilderWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Initialize data structures
        self.characters = []
        self.reactions = []

        # Load data
        self.load_characters()
        self.load_reactions()
        self.setup_filters()

        # Connect buttons to their functions
        self.addButton.clicked.connect(self.add_to_team)
        self.removeButton.clicked.connect(self.remove_from_team)
        self.optimizeButton.clicked.connect(self.optimize_team)

        # Connect double-click signal to add_to_team method
        self.availableCharactersList.itemDoubleClicked.connect(self.add_to_team)

    def load_characters(self):
        """
        Load characters from a JSON file into the available characters list with icons.
        Handles missing icons gracefully by using a default icon.
        """
        try:
            # Get the absolute path to the 'characters.json' file
            script_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.abspath(os.path.join(script_dir, '..', '..'))
            json_path = os.path.join(project_root, 'resources', 'characters.json')

            with open(json_path, 'r', encoding='utf-8') as file:
                characters = json.load(file)

            self.characters = characters  # Store for later use

            self.availableCharactersList.clear()

            for char in characters:
                # Check for required fields
                if not all(k in char for k in ("name", "role", "element")):
                    logging.warning(f"Character entry missing required fields: {char}")
                    continue

                # Ensure 'icon' field exists; if not, use 'icons/default.png'
                icon_filename = char.get('icon', 'icons/default.png')

                # Construct the full path to the icon
                icon_path = os.path.join(project_root, 'resources', icon_filename)

                # If the specified icon doesn't exist, fall back to the default icon
                if not os.path.exists(icon_path):
                    logging.warning(f"Icon not found for {char['name']}. Using default icon.")
                    icon_path = os.path.join(project_root, 'resources', 'icons', 'default.png')

                # Create the list item with text
                item_text = f"{char['name']} - {char['role']} - {char['element']}"
                item = QListWidgetItem(item_text)

                # Set the icon if the default icon exists
                if os.path.exists(icon_path):
                    item.setIcon(QIcon(icon_path))
                else:
                    logging.error("Default icon 'default.png' is missing in 'resources/icons/'.")
                    # Optionally, set a placeholder icon or leave it without an icon
                    item.setIcon(QIcon())  # Empty icon

                self.availableCharactersList.addItem(item)

            # Sort items alphabetically by name
            self.availableCharactersList.sortItems(QtCore.Qt.AscendingOrder)

            logging.info("Characters loaded successfully.")
        except FileNotFoundError:
            QMessageBox.critical(
                self,
                "Error",
                f"'characters.json' not found at {json_path}. Please ensure the file exists."
            )
            logging.critical(f"'characters.json' not found at {json_path}.")
        except json.JSONDecodeError as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Failed to parse 'characters.json': {e}"
            )
            logging.critical(f"JSON decode error in 'characters.json': {e}")
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"An unexpected error occurred while loading characters: {e}"
            )
            logging.critical(f"Unexpected error in load_characters: {e}")

    def load_reactions(self):
        """
        Load reactions from a 'reactions.json' file.
        """
        try:
            # Get the absolute path to the 'reactions.json' file
            script_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.abspath(os.path.join(script_dir, '..', '..'))
            json_path = os.path.join(project_root, 'resources', 'reactions.json')

            with open(json_path, 'r', encoding='utf-8') as file:
                reactions = json.load(file)

            # Validate reaction entries
            valid_reactions = []
            for reaction in reactions:
                if not all(k in reaction for k in ("name", "elements", "type_order", "damage_multiplier")):
                    logging.warning(f"Reaction entry missing required fields: {reaction}")
                    continue
                valid_reactions.append(reaction)

            self.reactions = valid_reactions  # Store for later use
            logging.info(f"Loaded {len(self.reactions)} reactions.")
        except FileNotFoundError:
            QMessageBox.critical(
                self,
                "Error",
                f"'reactions.json' not found at {json_path}. Please ensure the file exists."
            )
            logging.critical(f"'reactions.json' not found at {json_path}.")
            self.reactions = []
        except json.JSONDecodeError as e:
            QMessageBox.critical(
                self,
                "Error",
                f"Failed to parse 'reactions.json': {e}"
            )
            logging.critical(f"JSON decode error in 'reactions.json': {e}")
            self.reactions = []
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"An unexpected error occurred while loading reactions: {e}"
            )
            logging.critical(f"Unexpected error in load_reactions: {e}")
            self.reactions = []

    def setup_filters(self):
        """
        Set up filters for characters based on elements and roles.
        """
        try:
            # Populate Element Filter ComboBox (already added "All Elements" in UI)
            self.elementFilterComboBox.blockSignals(True)  # Prevent triggering filter during setup
            # Clear existing items except the first one ("All Elements")
            current_element = self.elementFilterComboBox.currentText()
            self.elementFilterComboBox.clear()
            self.elementFilterComboBox.addItem("All Elements")
            # Populate with unique elements from characters
            elements = sorted(set(
                char['element'] for char in self.characters
                if 'element' in char and char['element'] != "Unknown"
            ))
            self.elementFilterComboBox.addItems(elements)
            self.elementFilterComboBox.blockSignals(False)

            # Populate Role Filter ComboBox (already added "All Roles" in UI)
            self.roleFilterComboBox.blockSignals(True)
            self.roleFilterComboBox.clear()
            self.roleFilterComboBox.addItem("All Roles")
            # Populate with unique roles from characters
            roles = sorted(set(
                char['role'] for char in self.characters
                if 'role' in char and char['role'] != "Unknown"
            ))
            self.roleFilterComboBox.addItems(roles)
            self.roleFilterComboBox.blockSignals(False)

            # Connect filter ComboBoxes and LineEdit to apply_filters
            self.elementFilterComboBox.currentIndexChanged.connect(self.apply_filters)
            self.roleFilterComboBox.currentIndexChanged.connect(self.apply_filters)
            self.nameFilterLineEdit.textChanged.connect(self.apply_filters)

            logging.info("Filters configured successfully.")
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"An unexpected error occurred while setting up filters: {e}"
            )
            logging.critical(f"Unexpected error in setup_filters: {e}")

    def add_to_team(self, item=None):
        """
        Add selected characters from available list to the team list.
        Supports both button click and double-click.
        """
        try:
            # Determine if called by double-click (item is provided) or button click
            if item:
                items_to_add = [item]
            else:
                selected_items = self.availableCharactersList.selectedItems()
                if not selected_items:
                    QMessageBox.warning(
                        self,
                        "No Selection",
                        "Please select at least one character to add."
                    )
                    return
                items_to_add = selected_items

            for item in items_to_add:
                if self.selectedTeamList.count() >= 4:
                    QMessageBox.warning(
                        self,
                        "Team Full",
                        "The team can have a maximum of 4 characters."
                    )
                    break
                # Check if the character is already in the team
                existing_items = [
                    self.selectedTeamList.item(i).text()
                    for i in range(self.selectedTeamList.count())
                ]
                if item.text() not in existing_items:
                    self.selectedTeamList.addItem(item.text())
                    logging.info(f"Added '{item.text()}' to the team.")
                else:
                    logging.info(f"Character '{item.text()}' is already in the team.")
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"An unexpected error occurred while adding to the team: {e}"
            )
            logging.critical(f"Unexpected error in add_to_team: {e}")

    def remove_from_team(self):
        """
        Remove selected characters from the team list.
        """
        try:
            selected_items = self.selectedTeamList.selectedItems()
            if not selected_items:
                QMessageBox.warning(
                    self,
                    "No Selection",
                    "Please select at least one character to remove."
                )
                return

            for item in selected_items:
                self.selectedTeamList.takeItem(self.selectedTeamList.row(item))
                logging.info(f"Removed '{item.text()}' from the team.")
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"An unexpected error occurred while removing from the team: {e}"
            )
            logging.critical(f"Unexpected error in remove_from_team: {e}")

    def optimize_team(self):
        """
        Optimize the team based on selected characters.
        This implementation checks for elemental synergies and calculates potential damage.
        """
        try:
            team = [
                self.selectedTeamList.item(i).text()
                for i in range(self.selectedTeamList.count())
            ]
            if not team:
                QMessageBox.warning(
                    self,
                    "Empty Team",
                    "Please select at least one character to optimize."
                )
                return

            team_characters = [
                self.get_character(char_text) for char_text in team
            ]

            # Remove any None values if characters not found
            team_characters = [char for char in team_characters if char is not None]

            if not team_characters:
                QMessageBox.warning(
                    self,
                    "Invalid Team",
                    "Selected characters could not be found."
                )
                return

            elements = [char['element'] for char in team_characters]
            element_set = set(elements)

            # Check for at least two different elements for reactions
            if len(element_set) < 2:
                QMessageBox.warning(
                    self,
                    "Weak Synergy",
                    "It's better to have at least two different elements for optimal reactions."
                )
                return

            # Find possible reactions in the team
            possible_reactions = self.find_possible_reactions(team_characters)

            if not possible_reactions:
                QMessageBox.information(
                    self,
                    "No Reactions",
                    "No elemental reactions found in the team."
                )
                return

            # Calculate total damage with reactions
            total_damage = self.calculate_total_damage(team_characters, possible_reactions)

            # Display results
            reactions_info = "\n".join([
                f"{reaction['name']} (x{reaction['count']}): Damage x{reaction['damage_multiplier']}"
                for reaction in possible_reactions
            ])
            QMessageBox.information(
                self,
                "Analyzed",
                f"Elemental Reactions:\n{reactions_info}\n\nEstimated Total Damage Multiplier: x{total_damage}"
            )

            logging.info(f"Analyzed team calculated with total multiplier: x{total_damage}")
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"An unexpected error occurred while optimizing the team: {e}"
            )
            logging.critical(f"Unexpected error in optimize_team: {e}")

    def get_character(self, character_text):
        """
        Retrieve the character dictionary based on the selected list item text.
        """
        try:
            # Assuming the format "Name - Role - Element"
            name = character_text.split(" - ")[0]
            for char in self.characters:
                if char['name'] == name:
                    return char
            logging.warning(f"Character '{name}' not found in characters list.")
            return None
        except Exception as e:
            logging.error(f"Error in get_character: {e}")
            return None

    def find_possible_reactions(self, team_characters):
        """
        Find all possible elemental reactions in the team to analyze potential damage.
        """
        reactions_found = []

        # Create a dictionary counting elements in the team
        element_counts = {}
        for char in team_characters:
            element = char['element']
            element_counts[element] = element_counts.get(element, 0) + 1

        for reaction in self.reactions:
            required_elements = reaction['elements']

            # Handle reactions that require more than two elements
            if len(required_elements) == 2:
                # Simple binary reactions
                if all(elem in element_counts and element_counts[elem] > 0 for elem in required_elements):
                    # Calculate how many times this reaction can occur
                    reaction_count = min([element_counts[elem] for elem in required_elements])
                    if reaction_count > 0:
                        reactions_found.append({
                            "name": reaction['name'],
                            "type_order": reaction.get('type_order', 3),  # Default to lowest priority if missing
                            "damage_multiplier": reaction.get('damage_multiplier', 1.0),  # Default multiplier
                            "count": reaction_count,
                            "elements": required_elements
                        })
            else:
                # Reactions requiring multiple elements (e.g., Vegetation)
                if all(elem in element_counts and element_counts[elem] > 0 for elem in required_elements):
                    reaction_count = min([element_counts[elem] for elem in required_elements])
                    if reaction_count > 0:
                        reactions_found.append({
                            "name": reaction['name'],
                            "type_order": reaction.get('type_order', 3),
                            "damage_multiplier": reaction.get('damage_multiplier', 1.0),
                            "count": reaction_count,
                            "elements": required_elements
                        })

        # Sort reactions by priority (type_order)
        reactions_found.sort(key=lambda x: x['type_order'])
        logging.info(f"Found {len(reactions_found)} possible reactions.")
        return reactions_found

    def calculate_total_damage(self, team_characters, reactions):
        """
        Calculate the total damage considering reactions and physical damage.
        """
        total_multiplier = 1.0

        # Apply damage multipliers from reactions
        for reaction in reactions:
            # Assume each reaction contributes its damage multiplier
            total_multiplier += reaction['damage_multiplier'] * reaction['count']

        # Add base physical damage (e.g., from one physical DPS character)
        # This can be adjusted based on actual team composition and stats
        base_physical_damage = 1.0  # 100%

        # Calculate total damage
        total_damage = base_physical_damage * total_multiplier

        logging.info(f"Total damage multiplier calculated: {total_damage}")
        return round(total_damage, 2)

    def apply_filters(self):
        """
        Apply the selected filters to the list of available characters.
        """
        try:
            selected_element = self.elementFilterComboBox.currentText()
            selected_role = self.roleFilterComboBox.currentText()
            name_filter = self.nameFilterLineEdit.text().strip().lower()

            self.availableCharactersList.clear()

            for char in self.characters:
                # Skip characters missing required fields
                if 'element' not in char or 'role' not in char or 'name' not in char:
                    logging.warning(f"Skipping character with incomplete data: {char}")
                    continue

                # Apply element and role filters
                if (selected_element == "All Elements" or char['element'] == selected_element) and \
                        (selected_role == "All Roles" or char['role'] == selected_role):

                    # Apply name filter (case-insensitive)
                    if name_filter and name_filter not in char['name'].lower():
                        continue

                    item_text = f"{char['name']} - {char['role']} - {char['element']}"
                    item = QListWidgetItem(item_text)

                    # Set icon
                    icon_filename = char.get('icon', 'icons/default.png')
                    script_dir = os.path.dirname(os.path.abspath(__file__))
                    project_root = os.path.abspath(os.path.join(script_dir, '..', '..'))
                    icon_path = os.path.join(project_root, 'resources', icon_filename)

                    # If the specified icon doesn't exist, use the default icon
                    if not os.path.exists(icon_path):
                        logging.warning(f"Icon not found for {char['name']}. Using default icon.")
                        icon_path = os.path.join(project_root, 'resources', 'icons', 'default.png')

                    if os.path.exists(icon_path):
                        item.setIcon(QIcon(icon_path))
                    else:
                        logging.error("Default icon 'default.png' is missing in 'resources/icons/'.")
                        # Optionally, set a placeholder icon or leave it without an icon
                        item.setIcon(QIcon())  # Empty icon

                    self.availableCharactersList.addItem(item)

            # Sort items alphabetically by name after filtering
            self.availableCharactersList.sortItems(QtCore.Qt.AscendingOrder)

            logging.info("Filters applied successfully.")
        except Exception as e:
            QMessageBox.critical(
                self,
                "Error",
                f"An unexpected error occurred while applying filters: {e}"
            )
            logging.critical(f"Unexpected error in apply_filters: {e}")
