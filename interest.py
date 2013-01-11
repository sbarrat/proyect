import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    
    def __init__(self, parent = None):
        #Se llama a la clase superior y se inicia
        super(Form, self).__init__(parent)
        #creamos la layout
        layout = QGridLayout()
        #creamos las label
        principalLabel = QLabel("Principal:")
        rateLabel = QLabel("Rate:")
        yearsLabel = QLabel("Years:")
        amountLabel = QLabel("Amount")
        self.resultLabel = QLabel()
        #Creamos los campos
        self.principalSpinBox = QDoubleSpinBox()
        self.principalSpinBox.setPrefix("$ ")
        self.principalSpinBox.setRange(1, 1000000000)
        self.principalSpinBox.setValue(1000)
        
        self.rateSpinBox = QDoubleSpinBox()
        self.rateSpinBox.setSuffix(" %")
        self.rateSpinBox.setRange(1, 100)
        self.rateSpinBox.setValue(5)
        self.yearComboBox = QComboBox()
        self.yearComboBox.addItem("1 year")
        self.yearComboBox.addItems(["%d years" % x
                                     for x in range(2, 26)])
        
        
        layout.addWidget(principalLabel, 0, 0)
        layout.addWidget(rateLabel, 1, 0)
        layout.addWidget(yearsLabel, 2, 0)
        layout.addWidget(amountLabel, 3, 0)
        
        layout.addWidget(self.principalSpinBox, 0, 1)
        layout.addWidget(self.rateSpinBox, 1, 1)
        layout.addWidget(self.yearComboBox, 2, 1)
        layout.addWidget(self.resultLabel, 3, 1)
        
        self.setLayout(layout)
        
        self.connect(self.principalSpinBox, SIGNAL("valueChanged(double)"), self.updateUi)
        self.connect(self.rateSpinBox, SIGNAL("valueChanged(double)"), self.updateUi)
        self.connect(self.yearComboBox, SIGNAL("currentIndexChanged(int)"), self.updateUi)
        
        self.setWindowTitle("Interest")
        
        self.updateUi()
        
    def updateUi(self):
        """Calcula el interes compuesto """
        principal = self.principalSpinBox.value()
        rate = self.rateSpinBox.value()
        years = self.yearComboBox.currentIndex() + 1
        amount = principal * ((1 + (rate / 100.0)) ** years)
        self.resultLabel.setText("$ %.2f" % amount)
        
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()