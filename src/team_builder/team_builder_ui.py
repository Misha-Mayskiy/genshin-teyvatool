# team_builder_ui.py

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TeamBuilderWindow(object):
    def setupUi(self, TeamBuilderWindow):
        TeamBuilderWindow.setObjectName("TeamBuilderWindow")
        TeamBuilderWindow.resize(600, 500)
        TeamBuilderWindow.setFixedSize(600, 500)  # Fixed window size

        # Central Widget
        self.centralwidget = QtWidgets.QWidget(TeamBuilderWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Title Label
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(150, 20, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        # Available Characters List
        self.availableCharactersLabel = QtWidgets.QLabel(self.centralwidget)
        self.availableCharactersLabel.setGeometry(QtCore.QRect(50, 80, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.availableCharactersLabel.setFont(font)
        self.availableCharactersLabel.setObjectName("availableCharactersLabel")

        self.availableCharactersList = QtWidgets.QListWidget(self.centralwidget)
        self.availableCharactersList.setGeometry(QtCore.QRect(50, 120, 200, 300))
        self.availableCharactersList.setObjectName("availableCharactersList")
        self.availableCharactersList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

        # Selected Team List
        self.selectedTeamLabel = QtWidgets.QLabel(self.centralwidget)
        self.selectedTeamLabel.setGeometry(QtCore.QRect(350, 80, 200, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.selectedTeamLabel.setFont(font)
        self.selectedTeamLabel.setObjectName("selectedTeamLabel")

        self.selectedTeamList = QtWidgets.QListWidget(self.centralwidget)
        self.selectedTeamList.setGeometry(QtCore.QRect(350, 120, 200, 300))
        self.selectedTeamList.setObjectName("selectedTeamList")
        self.selectedTeamList.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)

        # Buttons
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(275, 180, 50, 30))
        self.addButton.setObjectName("addButton")
        self.addButton.setText(">>")

        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setGeometry(QtCore.QRect(275, 220, 50, 30))
        self.removeButton.setObjectName("removeButton")
        self.removeButton.setText("<<")

        self.optimizeButton = QtWidgets.QPushButton(self.centralwidget)
        self.optimizeButton.setGeometry(QtCore.QRect(250, 400, 100, 40))
        self.optimizeButton.setObjectName("optimizeButton")

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
        self.optimizeButton.setText(_translate("TeamBuilderWindow", "Optimize Team"))

    def applyStyles(self):
        style = """
        QWidget {
            background-color: #3B4252;
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
            padding: 5px;
        }
        QPushButton:hover {
            background-color: #81A1C1;
        }
        """
        self.centralwidget.setStyleSheet(style)
