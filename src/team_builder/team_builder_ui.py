# team_builder_ui.py

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TeamBuilderWindow(object):
    def setupUi(self, TeamBuilderWindow):
        TeamBuilderWindow.setObjectName("TeamBuilderWindow")
        TeamBuilderWindow.resize(1000, 700)
        TeamBuilderWindow.setMinimumSize(QtCore.QSize(1000, 700))
        TeamBuilderWindow.setMaximumSize(QtCore.QSize(1000, 700))  # Fixed window size

        # Central Widget
        self.centralwidget = QtWidgets.QWidget(TeamBuilderWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Title Label
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(400, 20, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        # Filters Group Box
        self.filtersGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.filtersGroupBox.setGeometry(QtCore.QRect(50, 80, 900, 60))
        self.filtersGroupBox.setTitle("")
        self.filtersGroupBox.setObjectName("filtersGroupBox")

        # Element Filter Label
        self.elementFilterLabel = QtWidgets.QLabel(self.filtersGroupBox)
        self.elementFilterLabel.setGeometry(QtCore.QRect(10, 20, 130, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.elementFilterLabel.setFont(font)
        self.elementFilterLabel.setObjectName("elementFilterLabel")
        self.elementFilterLabel.setText("Filter by Element:")

        # Element Filter ComboBox
        self.elementFilterComboBox = QtWidgets.QComboBox(self.filtersGroupBox)
        self.elementFilterComboBox.setGeometry(QtCore.QRect(150, 18, 150, 30))
        self.elementFilterComboBox.setObjectName("elementFilterComboBox")
        self.elementFilterComboBox.addItem("All Elements")
        # Elements will be populated dynamically in team_builder_window.py

        # Role Filter Label
        self.roleFilterLabel = QtWidgets.QLabel(self.filtersGroupBox)
        self.roleFilterLabel.setGeometry(QtCore.QRect(320, 20, 100, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.roleFilterLabel.setFont(font)
        self.roleFilterLabel.setObjectName("roleFilterLabel")
        self.roleFilterLabel.setText("Filter by Role:")

        # Role Filter ComboBox
        self.roleFilterComboBox = QtWidgets.QComboBox(self.filtersGroupBox)
        self.roleFilterComboBox.setGeometry(QtCore.QRect(430, 18, 150, 30))
        self.roleFilterComboBox.setObjectName("roleFilterComboBox")
        self.roleFilterComboBox.addItem("All Roles")
        # Roles will be populated dynamically in team_builder_window.py

        # Name Filter Label
        self.nameFilterLabel = QtWidgets.QLabel(self.filtersGroupBox)
        self.nameFilterLabel.setGeometry(QtCore.QRect(600, 20, 120, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nameFilterLabel.setFont(font)
        self.nameFilterLabel.setObjectName("nameFilterLabel")
        self.nameFilterLabel.setText("Search by Name:")

        # Name Filter LineEdit
        self.nameFilterLineEdit = QtWidgets.QLineEdit(self.filtersGroupBox)
        self.nameFilterLineEdit.setGeometry(QtCore.QRect(730, 18, 160, 30))
        self.nameFilterLineEdit.setObjectName("nameFilterLineEdit")
        self.nameFilterLineEdit.setPlaceholderText("Enter character name")

        # Available Characters Label
        self.availableCharactersLabel = QtWidgets.QLabel(self.centralwidget)
        self.availableCharactersLabel.setGeometry(QtCore.QRect(50, 160, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.availableCharactersLabel.setFont(font)
        self.availableCharactersLabel.setObjectName("availableCharactersLabel")
        self.availableCharactersLabel.setText("Available Characters")

        # Available Characters List (Grid of Icons)
        self.availableCharactersList = QtWidgets.QListWidget(self.centralwidget)
        self.availableCharactersList.setGeometry(QtCore.QRect(50, 200, 400, 400))
        self.availableCharactersList.setObjectName("availableCharactersList")
        self.availableCharactersList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        # Selected Team Label
        self.selectedTeamLabel = QtWidgets.QLabel(self.centralwidget)
        self.selectedTeamLabel.setGeometry(QtCore.QRect(550, 160, 250, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.selectedTeamLabel.setFont(font)
        self.selectedTeamLabel.setObjectName("selectedTeamLabel")
        self.selectedTeamLabel.setText("Selected Team")

        # Selected Team List (Grid of Icons)
        self.selectedTeamList = QtWidgets.QListWidget(self.centralwidget)
        self.selectedTeamList.setGeometry(QtCore.QRect(550, 200, 400, 400))
        self.selectedTeamList.setObjectName("selectedTeamList")
        self.selectedTeamList.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        # Buttons
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(475, 210, 50, 30))
        self.addButton.setObjectName("addButton")
        self.addButton.setText(">>")

        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setGeometry(QtCore.QRect(475, 250, 50, 30))
        self.removeButton.setObjectName("removeButton")
        self.removeButton.setText("<<")

        # Optimize Button
        self.optimizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.optimizeButton.setGeometry(QtCore.QRect(400, 620, 200, 40))  # Positioned at the bottom center
        self.optimizeButton.setObjectName("optimizeButton")
        self.optimizeButton.setText("Analyze Team")

        TeamBuilderWindow.setCentralWidget(self.centralwidget)

        # Apply Stylesheet
        self.applyStyles()

        self.retranslateUi(TeamBuilderWindow)
        QtCore.QMetaObject.connectSlotsByName(TeamBuilderWindow)

    def retranslateUi(self, TeamBuilderWindow):
        _translate = QtCore.QCoreApplication.translate
        TeamBuilderWindow.setWindowTitle(_translate("TeamBuilderWindow", "ArteFactor - Team Builder"))
        self.titleLabel.setText(_translate("TeamBuilderWindow", "Team Builder"))
        self.availableCharactersLabel.setText(_translate("TeamBuilderWindow", "Available Characters"))
        self.selectedTeamLabel.setText(_translate("TeamBuilderWindow", "Selected Team"))
        self.optimizeButton.setText(_translate("TeamBuilderWindow", "Analyze Team"))

    def applyStyles(self):
        style = """
            QWidget {
                background-color: #2E3440;
                color: #ECEFF4;
                font-family: Arial, sans-serif;
            }
            QLabel {
                color: #ECEFF4;
            }
            QListWidget {
                background-color: #434C5E;
                border: 2px solid #4C566A;
                border-radius: 5px;
                padding: 5px;
                color: #ECEFF4;
            }
            QPushButton {
                background-color: #88C0D0;
                border: none;
                border-radius: 5px;
                color: #2E3440;
                padding: 10px;
                font-size: 14px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #81A1C1;
            }
            QGroupBox {
                border: none;
            }
            QLineEdit {
                background-color: #434C5E;
                border: 2px solid #4C566A;
                border-radius: 5px;
                padding: 5px;
                color: #ECEFF4;
            }
            """
        self.centralwidget.setStyleSheet(style)
