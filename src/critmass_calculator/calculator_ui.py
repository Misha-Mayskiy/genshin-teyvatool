# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalculatorWindow(object):
    def setupUi(self, CalculatorWindow):
        CalculatorWindow.setObjectName("CalculatorWindow")
        CalculatorWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(CalculatorWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Крит. Урон
        self.critDamageLabel = QtWidgets.QLabel(self.centralwidget)
        self.critDamageLabel.setGeometry(QtCore.QRect(50, 50, 100, 30))
        self.critDamageLabel.setObjectName("critDamageLabel")

        self.critDamageInput = QtWidgets.QLineEdit(self.centralwidget)
        self.critDamageInput.setGeometry(QtCore.QRect(200, 50, 150, 30))
        self.critDamageInput.setObjectName("critDamageInput")

        # Крит. Шанс
        self.critChanceLabel = QtWidgets.QLabel(self.centralwidget)
        self.critChanceLabel.setGeometry(QtCore.QRect(50, 100, 100, 30))
        self.critChanceLabel.setObjectName("critChanceLabel")

        self.critChanceInput = QtWidgets.QLineEdit(self.centralwidget)
        self.critChanceInput.setGeometry(QtCore.QRect(200, 100, 150, 30))
        self.critChanceInput.setObjectName("critChanceInput")

        # Кнопка расчета
        self.calculateButton = QtWidgets.QPushButton(self.centralwidget)
        self.calculateButton.setGeometry(QtCore.QRect(150, 150, 100, 40))
        self.calculateButton.setObjectName("calculateButton")

        # Результат
        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel.setGeometry(QtCore.QRect(50, 210, 300, 30))
        self.resultLabel.setObjectName("resultLabel")

        # Оценка
        self.evaluationLabel = QtWidgets.QLabel(self.centralwidget)
        self.evaluationLabel.setGeometry(QtCore.QRect(50, 250, 300, 30))
        self.evaluationLabel.setObjectName("evaluationLabel")

        CalculatorWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CalculatorWindow)
        QtCore.QMetaObject.connectSlotsByName(CalculatorWindow)

    def retranslateUi(self, CalculatorWindow):
        _translate = QtCore.QCoreApplication.translate
        CalculatorWindow.setWindowTitle(_translate("CalculatorWindow", "Калькулятор Крит Массы"))
        self.critDamageLabel.setText(_translate("CalculatorWindow", "Крит. Урон:"))
        self.critChanceLabel.setText(_translate("CalculatorWindow", "Крит. Шанс:"))
        self.calculateButton.setText(_translate("CalculatorWindow", "Рассчитать"))
        self.resultLabel.setText(_translate("CalculatorWindow", "Крит масса:"))
        self.evaluationLabel.setText(_translate("CalculatorWindow", "Оценка:"))
