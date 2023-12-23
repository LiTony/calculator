from PyQt6.QtCore import QDateTime, Qt, QTimer
from PyQt6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget, QToolBox, QToolButton)

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
    
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()
        
        inputLabel = QLabel("&Input:")
        inputTextArea = QTextEdit()
        inputTextArea.setObjectName("inputText")
        inputTextArea.setReadOnly(True)
        inputLabel.setBuddy(inputTextArea)

        outputLabel = QLabel("&Output:")
        outputTextArea = QTextEdit()
        outputTextArea.setObjectName("outputText")
        outputTextArea.setReadOnly(True)
        outputLabel.setBuddy(outputTextArea)

        topLayout = QHBoxLayout()
        topLayout.addWidget(inputLabel)
        topLayout.addWidget(inputTextArea)
        topLayout.addWidget(outputLabel)
        topLayout.addWidget(outputTextArea)

        self.createLeftNumbers()
        self.createCenterNumbers()
        self.createRightNumbers()
        self.createOperationsColumn()
        self.createZeroBar()
        self.createClearButton()

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 4)
    
        mainLayout.addWidget(self.leftNumbers, 1, 0)
        mainLayout.addWidget(self.centerNumbers, 1, 1)
        mainLayout.addWidget(self.rightNumbers, 1, 2)
        mainLayout.addWidget(self.operationsColumn, 1, 3)
        mainLayout.addWidget(self.zeroBar, 2, 0, 1, 3)
        mainLayout.addWidget(self.clearButton, 2, 3)
        mainLayout.setRowStretch(1, 1)
        mainLayout.setRowStretch(2, 1)
        mainLayout.setColumnStretch(0, 1)
        mainLayout.setColumnStretch(1, 1)
        mainLayout.setColumnStretch(2, 1)
        mainLayout.setColumnStretch(3, 1)

        for num in [1,4,7]:
            name = "Button%d" % num
            self.leftNumbers.findChild(QPushButton, name) \
                .clicked.connect(self.numberPress)
        for num in [2,5,8]:
            name = "Button%d" % num
            self.centerNumbers.findChild(QPushButton, name) \
                .clicked.connect(self.numberPress)
        for num in [3,6,9]:
            name = "Button%d" % num
            self.rightNumbers.findChild(QPushButton, name) \
                .clicked.connect(self.numberPress)
        for ops in "+-=":
            name = "Button%s" % ops
            self.operationsColumn.findChild(QPushButton, name) \
                .clicked.connect(self.operationPress)
            
        name = "Button0"
        self.zeroBar.findChild(QPushButton) \
            .clicked.connect(self.numberPress)
        name = "ButtonC"
        self.clearButton.findChild(QPushButton) \
            .clicked.connect(self.clearPress)
        self.setLayout(mainLayout)

        self.setWindowTitle("Calculator App by LiTony")

    def clearPress(self):
        self.findChild(QTextEdit, "inputText").setText("")
        print("input field cleared")

    def numberPress(self):
        sending_button = self.sender()
        buttonName = str(sending_button.objectName())
        print("hello number: %s Clicked!" % buttonName)
        self.findChild(QTextEdit, "inputText").insertHtml(buttonName[-1].strip())

    def operationPress(self):
        sending_button = self.sender()
        buttonName = str(sending_button.objectName())
        operation = buttonName[-1]
        lastPress = self.findChild(QTextEdit).toPlainText()[-1]
        print("Last press = (%s)" % lastPress)
        print("hello operation: %s Clicked!" % str(sending_button.objectName()))
        if (lastPress not in "+-"):
            if (operation == '='):
                inputText = self.findChild(QTextEdit, "inputText")
                outputText = self.findChild(QTextEdit, "outputText")
                outputText.setText("")
                expression = inputText.toPlainText()
                print("Evaluating: %s" % expression)
                self.findChild(QTextEdit, "outputText") \
                    .insertHtml(str(eval(expression)))
            else:
                self.findChild(QTextEdit, "inputText").insertHtml(buttonName[-1].strip())
        else:
            print("error last press was already an operation!")
    def createLeftNumbers(self):
        self.leftNumbers = QGroupBox("Left Numbers")
        layout = QVBoxLayout()

        for button_number in [7,4,1]:
            button = QPushButton('%d' % button_number)
            button.setDefault(True)
            button.setObjectName('Button%d' % button_number)
            layout.addWidget(button)

        layout.addStretch(1)
        self.leftNumbers.setLayout(layout)
    def createZeroBar(self):
        self.zeroBar = QGroupBox("Zero")

        layout = QVBoxLayout()

        for button_number in [0]:
            button = QPushButton('%d' % button_number)
            button.setDefault(True)
            button.setObjectName('Button%d' % button_number)
            layout.addWidget(button)
        
        self.zeroBar.setLayout(layout)


    def createClearButton(self):
        self.clearButton = QGroupBox("Clear Input")

        layout = QVBoxLayout()

        for button_number in ["C"]:
            button = QPushButton('%s' % button_number)
            button.setDefault(True)
            button.setObjectName('Button%s' % button_number)
            layout.addWidget(button)
        
        self.clearButton.setLayout(layout)

    def createCenterNumbers(self):
        self.centerNumbers = QGroupBox("Center Numbers")

        layout = QVBoxLayout()

        for button_number in [8,5,2]:
            button = QPushButton('%d' % button_number)
            button.setDefault(True)
            button.setObjectName('Button%d' % button_number)
            layout.addWidget(button)
            
        layout.addStretch(1)
        self.centerNumbers.setLayout(layout)

    def createRightNumbers(self):
        self.rightNumbers = QGroupBox("Right Numbers")
        layout = QVBoxLayout()

        for button_number in [9,6,3]:
            button = QPushButton('%d' % button_number)
            button.setDefault(True)
            button.setObjectName('Button%d' % button_number)
            layout.addWidget(button)
            
        layout.addStretch(1)
        self.rightNumbers.setLayout(layout)

    def createOperationsColumn(self):
        self.operationsColumn = QGroupBox("Operations")
        layout = QVBoxLayout()

        for button_number in ['+','-','=']:
            button = QPushButton('%s' % button_number)
            button.setDefault(True)
            button.setObjectName('Button%s' % button_number)
            layout.addWidget(button)
            
        layout.addStretch(1)
        self.operationsColumn.setLayout(layout)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec())
