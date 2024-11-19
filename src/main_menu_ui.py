from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainMenuWindow(object):
    def setupUi(self, MainMenuWindow):
        MainMenuWindow.setObjectName("MainMenuWindow")
        MainMenuWindow.resize(500, 400)
        MainMenuWindow.setFixedSize(500, 400)
        MainMenuWindow.setWindowIcon(QtGui.QIcon("resources/icons/main_icon.png"))

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

        # Critical Mass Button and Info Button
        self.calculatorButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculatorButton.setGeometry(QtCore.QRect(100, 100, 250, 60))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.calculatorButton.setFont(font)
        self.calculatorButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculatorButton.setObjectName("calculatorButton")

        self.calculatorInfoButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculatorInfoButton.setGeometry(QtCore.QRect(360, 100, 40, 60))
        self.calculatorInfoButton.setIcon(QtGui.QIcon("resources/icons/info_icon.png"))
        self.calculatorInfoButton.setIconSize(QtCore.QSize(32, 32))
        self.calculatorInfoButton.setFlat(True)
        self.calculatorInfoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculatorInfoButton.setObjectName("calculatorInfoButton")

        # Team Builder Button and Info Button
        self.teamBuilderButton = QtWidgets.QPushButton(self.centralwidget)
        self.teamBuilderButton.setGeometry(QtCore.QRect(100, 180, 250, 60))
        self.teamBuilderButton.setFont(font)
        self.teamBuilderButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.teamBuilderButton.setObjectName("teamBuilderButton")

        self.teamBuilderInfoButton = QtWidgets.QPushButton(self.centralwidget)
        self.teamBuilderInfoButton.setGeometry(QtCore.QRect(360, 180, 40, 60))
        self.teamBuilderInfoButton.setIcon(QtGui.QIcon("resources/icons/info_icon.png"))
        self.teamBuilderInfoButton.setIconSize(QtCore.QSize(32, 32))
        self.teamBuilderInfoButton.setFlat(True)
        self.teamBuilderInfoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.teamBuilderInfoButton.setObjectName("teamBuilderInfoButton")

        # Artifact Drop Calculator Button and Info Button
        self.dropCalculatorButton = QtWidgets.QPushButton(self.centralwidget)
        self.dropCalculatorButton.setGeometry(QtCore.QRect(100, 260, 250, 60))
        self.dropCalculatorButton.setFont(font)
        self.dropCalculatorButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dropCalculatorButton.setObjectName("dropCalculatorButton")

        self.dropCalculatorInfoButton = QtWidgets.QPushButton(self.centralwidget)
        self.dropCalculatorInfoButton.setGeometry(QtCore.QRect(360, 260, 40, 60))
        self.dropCalculatorInfoButton.setIcon(QtGui.QIcon("resources/icons/info_icon.png"))
        self.dropCalculatorInfoButton.setIconSize(QtCore.QSize(32, 32))
        self.dropCalculatorInfoButton.setFlat(True)
        self.dropCalculatorInfoButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dropCalculatorInfoButton.setObjectName("dropCalculatorInfoButton")

        # Icons
        self.calculatorButton.setIcon(QtGui.QIcon("resources/icons/calculator_icon.png"))
        self.calculatorButton.setIconSize(QtCore.QSize(32, 32))
        self.teamBuilderButton.setIcon(QtGui.QIcon("resources/icons/team_builder_icon.png"))
        self.teamBuilderButton.setIconSize(QtCore.QSize(32, 32))
        self.dropCalculatorButton.setIcon(QtGui.QIcon("resources/icons/drop_calculator_icon.png"))
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
        self.dropCalculatorButton.setText(_translate("MainMenuWindow", "Artifact Analyzer"))
        self.calculatorInfoButton.setText(_translate("MainMenuWindow", "INFO"))
        self.dropCalculatorInfoButton.setText(_translate("MainMenuWindow", "INFO"))
        self.teamBuilderInfoButton.setText(_translate("MainMenuWindow", "INFO"))

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
