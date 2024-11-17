# calculator_ui.py

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalculatorWindow(object):
    def setupUi(self, CalculatorWindow):
        CalculatorWindow.setObjectName("CalculatorWindow")
        CalculatorWindow.resize(400, 350)
        CalculatorWindow.setFixedSize(400, 350)  # Fixed window size
        CalculatorWindow.setWindowIcon(QtGui.QIcon("resources/icons/calculator_icon.png"))

        # Central Widget
        self.centralwidget = QtWidgets.QWidget(CalculatorWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Title Label
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(50, 20, 300, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")

        # Critical Damage Label
        self.critDamageLabel = QtWidgets.QLabel(self.centralwidget)
        self.critDamageLabel.setGeometry(QtCore.QRect(50, 80, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.critDamageLabel.setFont(font)
        self.critDamageLabel.setObjectName("critDamageLabel")

        # Critical Damage Input
        self.critDamageInput = QtWidgets.QLineEdit(self.centralwidget)
        self.critDamageInput.setGeometry(QtCore.QRect(200, 80, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.critDamageInput.setFont(font)
        self.critDamageInput.setAlignment(QtCore.Qt.AlignCenter)
        self.critDamageInput.setObjectName("critDamageInput")

        # Critical Chance Label
        self.critChanceLabel = QtWidgets.QLabel(self.centralwidget)
        self.critChanceLabel.setGeometry(QtCore.QRect(50, 130, 120, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.critChanceLabel.setFont(font)
        self.critChanceLabel.setObjectName("critChanceLabel")

        # Critical Chance Input
        self.critChanceInput = QtWidgets.QLineEdit(self.centralwidget)
        self.critChanceInput.setGeometry(QtCore.QRect(200, 130, 150, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.critChanceInput.setFont(font)
        self.critChanceInput.setAlignment(QtCore.Qt.AlignCenter)
        self.critChanceInput.setObjectName("critChanceInput")

        # Calculate Button
        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setGeometry(QtCore.QRect(150, 180, 100, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(10)
        self.calculateButton.setFont(font)
        self.calculateButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.calculateButton.setObjectName("calculateButton")

        # Result Label
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel.setGeometry(QtCore.QRect(50, 240, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.resultLabel.setFont(font)
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultLabel.setObjectName("resultLabel")

        # Evaluation Label
        self.evaluationLabel = QtWidgets.QLabel(self.centralwidget)
        self.evaluationLabel.setGeometry(QtCore.QRect(50, 280, 300, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.evaluationLabel.setFont(font)
        self.evaluationLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.evaluationLabel.setObjectName("evaluationLabel")

        CalculatorWindow.setCentralWidget(self.centralwidget)

        # Apply Stylesheet
        self.applyStyles()

        self.retranslateUi(CalculatorWindow)
        QtCore.QMetaObject.connectSlotsByName(CalculatorWindow)

    def retranslateUi(self, CalculatorWindow):
        _translate = QtCore.QCoreApplication.translate
        CalculatorWindow.setWindowTitle(_translate("CalculatorWindow", "ArteFactor - Crit Mass Calculator"))
        self.titleLabel.setText(_translate("CalculatorWindow", "Critical Mass Calculator"))
        self.critDamageLabel.setText(_translate("CalculatorWindow", "Critical Damage:"))
        self.critChanceLabel.setText(_translate("CalculatorWindow", "Critical Chance:"))
        self.calculateButton.setText(_translate("CalculatorWindow", "Calculate"))
        self.resultLabel.setText(_translate("CalculatorWindow", "Critical Mass: -"))
        self.evaluationLabel.setText(_translate("CalculatorWindow", "Evaluation: -"))

    def applyStyles(self):
        style = """
        QWidget {
            background-color: #2E3440;
            color: #D8DEE9;
        }
        QLabel {
            color: #D8DEE9;
        }
        QLineEdit {
            background-color: #3B4252;
            border: 2px solid #4C566A;
            border-radius: 5px;
            padding: 5px;
        }
        QLineEdit:focus {
            border: 2px solid #88C0D0;
        }
        QPushButton {
            background-color: #88C0D0;
            border: none;
            border-radius: 5px;
            color: #2E3440;
        }
        QPushButton:hover {
            background-color: #81A1C1;
        }
        """
        self.centralwidget.setStyleSheet(style)
