from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ArtifactAnalyzerWindow(object):
    def setupUi(self, ArtifactAnalyzerWindow):
        ArtifactAnalyzerWindow.setObjectName("ArtifactAnalyzerWindow")
        ArtifactAnalyzerWindow.resize(600, 500)
        ArtifactAnalyzerWindow.setFixedSize(600, 500)
        ArtifactAnalyzerWindow.setWindowIcon(QtGui.QIcon("resources/icons/drop_calculator_icon.png"))

        # Central Widget
        self.centralWidget = QtWidgets.QWidget(ArtifactAnalyzerWindow)
        self.centralWidget.setObjectName("centralWidget")
        ArtifactAnalyzerWindow.setCentralWidget(self.centralWidget)

        # Main Layout
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralWidget)

        # Title Label
        self.titleLabel = QtWidgets.QLabel("Artifact Probability Calculator")
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLayout.addWidget(self.titleLabel)

        # Rarity Selection
        rarityLayout = QtWidgets.QHBoxLayout()
        rarityLabel = QtWidgets.QLabel("Artifact Rarity:")
        self.rarityComboBox = QtWidgets.QComboBox()
        self.rarityComboBox.addItems(["4-Star", "5-Star"])
        rarityLayout.addWidget(rarityLabel)
        rarityLayout.addWidget(self.rarityComboBox)
        self.mainLayout.addLayout(rarityLayout)

        # Artifact Type Selection
        typeLayout = QtWidgets.QHBoxLayout()
        typeLabel = QtWidgets.QLabel("Artifact Type:")
        self.typeComboBox = QtWidgets.QComboBox()
        self.typeComboBox.addItems(["Flower", "Plume", "Sands", "Goblet", "Circlet"])
        typeLayout.addWidget(typeLabel)
        typeLayout.addWidget(self.typeComboBox)
        self.mainLayout.addLayout(typeLayout)

        # Preferred Substats Selection
        substatGroupLabel = QtWidgets.QLabel("Select Preferred Substats (Up to 4):")
        self.mainLayout.addWidget(substatGroupLabel)

        self.substatCheckboxes = []
        substatOptions = ["HP%", "ATK%", "DEF%", "Energy Recharge%", "Elemental Mastery",
                          "Crit Rate%", "Crit Damage%", "Flat HP", "Flat ATK", "Flat DEF"]
        substatGridLayout = QtWidgets.QGridLayout()
        for i, substat in enumerate(substatOptions):
            checkbox = QtWidgets.QCheckBox(substat)
            self.substatCheckboxes.append(checkbox)
            substatGridLayout.addWidget(checkbox, i // 2, i % 2)
        self.mainLayout.addLayout(substatGridLayout)

        # Calculate Button
        self.calculateButton = QtWidgets.QPushButton("Calculate Probability")
        self.mainLayout.addWidget(self.calculateButton)

        # Result Label
        self.resultLabel = QtWidgets.QLabel("")
        self.resultLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultLabel.setWordWrap(True)
        self.mainLayout.addWidget(self.resultLabel)

        # Apply Stylesheet
        self.applyStyles()

        # Retranslate UI (if needed)
        self.retranslateUi(ArtifactAnalyzerWindow)
        QtCore.QMetaObject.connectSlotsByName(ArtifactAnalyzerWindow)

    def retranslateUi(self, ArtifactAnalyzerWindow):
        _translate = QtCore.QCoreApplication.translate
        ArtifactAnalyzerWindow.setWindowTitle(_translate("ArtifactAnalyzerWindow", "Artifact Analyzer"))

    def applyStyles(self):
        style = """
        QWidget {
            background-color: #3B4252;
            color: #ECEFF4;
            font-size: 14px;
        }
        QLabel {
            color: #ECEFF4;
        }
        QPushButton {
            background-color: #5E81AC;
            border: none;
            border-radius: 10px;
            color: #ECEFF4;
            height: 40px;
        }
        QPushButton:hover {
            background-color: #81A1C1;
        }
        QComboBox, QCheckBox {
            background-color: #434C5E;
            color: #ECEFF4;
            border: none;
            selection-background-color: #5E81AC;
        }
        """
        self.centralWidget.setStyleSheet(style)
