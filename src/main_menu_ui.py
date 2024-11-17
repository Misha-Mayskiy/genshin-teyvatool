# main_menu_ui.py

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainMenuWindow(object):
    def setupUi(self, MainMenuWindow):
        MainMenuWindow.setObjectName("MainMenuWindow")
        MainMenuWindow.resize(500, 400)
        MainMenuWindow.setFixedSize(500, 400)  # Fixed window size
        MainMenuWindow.setWindowIcon(QtGui.QIcon("resources/main_icon.png"))

        # Central Widget
        self.centralwidget = QtWidgets.QWidget(MainMenuWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Title Label
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(100, 30, 300, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        # Critical Mass Button
        self.calculatorButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculatorButton.setGeometry(QtCore.QRect(150, 100, 200, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calculatorButton.setFont(font)
        self.calculatorButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculatorButton.setObjectName("calculatorButton")

        # Team Builder Button
        self.teamBuilderButton = QtWidgets.QPushButton(self.centralwidget)
        self.teamBuilderButton.setGeometry(QtCore.QRect(150, 180, 200, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.teamBuilderButton.setFont(font)
        self.teamBuilderButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.teamBuilderButton.setObjectName("teamBuilderButton")

        # Artifact Drop Calculator Button
        self.dropCalculatorButton = QtWidgets.QPushButton(self.centralwidget)
        self.dropCalculatorButton.setGeometry(QtCore.QRect(150, 260, 200, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dropCalculatorButton.setFont(font)
        self.dropCalculatorButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dropCalculatorButton.setObjectName("dropCalculatorButton")

        # Icons :D
        self.calculatorButton.setIcon(QtGui.QIcon("resources/calculator_icon.png"))
        self.calculatorButton.setIconSize(QtCore.QSize(32, 32))
        self.teamBuilderButton.setIcon(QtGui.QIcon("resources/team_builder_icon.png"))
        self.teamBuilderButton.setIconSize(QtCore.QSize(32, 32))
        self.dropCalculatorButton.setIcon(QtGui.QIcon("resources/drop_calculator_icon.png"))
        self.dropCalculatorButton.setIconSize(QtCore.QSize(32, 32))

        MainMenuWindow.setCentralWidget(self.centralwidget)

        # Apply Stylesheet
        self.applyStyles()

        self.retranslateUi(MainMenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MainMenuWindow)

    def retranslateUi(self, MainMenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MainMenuWindow.setWindowTitle(_translate("MainMenuWindow", "ArteFactor - Main Menu"))
        self.titleLabel.setText(_translate("MainMenuWindow", "ArteFactor Toolkit"))
        self.calculatorButton.setText(_translate("MainMenuWindow", "Critical Mass Calculator"))
        self.teamBuilderButton.setText(_translate("MainMenuWindow", "Team Builder"))
        self.dropCalculatorButton.setText(_translate("MainMenuWindow", "Artifact Drop Calculator"))

    def applyStyles(self):
        style = """
        QWidget {
            background-color: #3B4252;
            color: #ECEFF4;
        }
        QLabel {
            color: #ECEFF4;
        }
        QPushButton {
            background-color: #5E81AC;
            border: none;
            border-radius: 10px;
            color: #ECEFF4;
        }
        QPushButton:hover {
            background-color: #81A1C1;
        }
        """
        self.centralwidget.setStyleSheet(style)