import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import QtCore
from .calculator_ui import Ui_CalculatorWindow  # Импортируем сгенерированный класс


class CalculatorWindow(QMainWindow, Ui_CalculatorWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.calculateButton.clicked.connect(self.calculate_crit_mass)

    def calculate_crit_mass(self):
        try:
            crit_damage = float(self.critDamageInput.text().replace(',', '.'))
            crit_chance = float(self.critChanceInput.text().replace(',', '.'))
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите корректные числовые значения.")
            return

        # Вычисление крит.массы по формуле крит.масса = крит.шанс * 2 + крит.урон
        crit_mass = crit_chance * 2 + crit_damage
        crit_mass = round(crit_mass, 1)
        self.resultLabel.setText(f"Крит масса: {crit_mass}")

        # Оценка количества крит.массы
        if crit_mass < 50.0:
            evaluation = "Вам следует сменить или улучшить артефакты"
        elif 50.0 <= crit_mass < 90.0:
            evaluation = "Хорошая крит.масса для саппортов"
        elif 90.0 <= crit_mass < 130.0:
            evaluation = "Отличная крит.масса для саб-дд"
        elif 130.0 <= crit_mass < 500.0:
            evaluation = "У вас идеальные артефакты!"
        else:
            evaluation = "Вы уверены что не ошиблись в значениях?)"

        self.evaluationLabel.setText(f"Оценка: {evaluation}")

        # Дополнительные проверки с советами по улучшению
        if crit_chance > 100:
            QMessageBox.information(self, "Информация", "Крит.шанс больше 100%, увеличьте перевес в сторону крит.урона.")

        # Проверка соотношения крит.шанса и крит.урона 1 к 2 для баланса
        if abs(crit_chance - (crit_damage / 2)) > 20:  # Допустимое отклонение
            QMessageBox.information(self, "Информация", "Оптимальное соотношение крит.шанса и крит.урона: 1 к 2.")
