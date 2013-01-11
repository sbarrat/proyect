import sys
import urllib2
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    
    def __init__(self,  parent = None):
        super(Form,  self).__init__(parent)
        
        date = self.getdata()
        rates = sorted(self.rates.keys())
        #Creamos la datelabel
        dateLabel = QLabel(date)
        #Creamos un ComboBox
        self.fromComboBox = QComboBox()
        self.fromComboBox.addItems(rates)
        #Creamos el spinBox
        self.fromSpinBox = QDoubleSpinBox()
        self.fromSpinBox.setRange(0.01,  10000000.00)
        self.fromSpinBox.setValue(1.00)
        #Creamos otro ComboBox
        self.toComboBox = QComboBox()
        self.toComboBox.addItems(rates)
        #Creamos otra Label
        self.toLabel = QLabel("1.00")
        #Creamos la Grid
        grid = QGridLayout()
        #Agregamos el datelabel a la grid
        grid.addWidget(dateLabel,  0,  0)
        #Agregamos el combobox
        grid.addWidget(self.fromComboBox, 1, 0)
        #Agregamos el spinBox
        grid.addWidget(self.fromSpinBox, 1, 1)
        #Agregamos el otro combobox
        grid.addWidget(self.toComboBox, 2, 0)
        #Agregamos la label
        grid.addWidget(self.toLabel, 2, 1)
        #Establecemos la capa con la grid
        self.setLayout(grid)
        #Conectamos los objetos con las signals
        self.connect(self.fromComboBox, SIGNAL("currentIndexChanged(int)"), self.updateUi)
        self.connect(self.toComboBox, SIGNAL("currentIndexChanged(int)"), self.updateUi)
        self.connect(self.fromSpinBox, SIGNAL("valueChanged(double)"), self.updateUi)
        #Establecemos el titulo de la ventana
        self.setWindowTitle("Currency")
        
    def updateUi(self):
        to = unicode(self.toComboBox.currentText())
        from_ = unicode(self.fromComboBox.currentText())
        amount = (self.rates[from_] / self.rates[to] * self.fromSpinBox.value())
        self.toLabel.setText("%0.2f" % amount)
        
    def getdata(self): #Ida cogida del libro Python Cookbook
        self.rates = {}
        try:
            date = "Unknown"
            fh = urllib2.urlopen("http://www.bankofcanada.ca/en/markets/csv/exchange_eng.csv")
            for line in fh:
                if not line or line.startswith(("#", "Closing ")):
                    continue
                fields = line.split(",")
                if line.startswith("Date "):
                    date = fields[-1]
                else:
                    try:
                        value = float(fields[-1])
                        self.rates[unicode(fields[0])] = value
                    except ValueError:
                        pass
            return "Exchange Rates Date: " + date
        except Exception, e:
            return "Failed to download:\n%s" % e
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()
