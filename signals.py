import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class Form(QDialog):
    
    def __init__(self, parent = None):
        #Se llama a la clase superior y se inicia
        super(Form, self).__init__(parent)
        
        #Creamos el dial
        dial = QDial()
        dial.setNotchesVisible(True)
        #Creamo el spinbox
        spinbox = QSpinBox()
        #Creamo la capa
        layout = QHBoxLayout()
        layout.addWidget(dial)
        layout.addWidget(spinbox)
        self.setLayout(layout)
        
        #Conectamos las signals
        self.connect(dial, SIGNAL("valueChanged(int)"), spinbox.setValue)
        self.connect(spinbox, SIGNAL("valueChanged(int)"), dial.setValue)
        
        self.setWindowTitle("Signals and Slots")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = Form()
    form.show()
    app.exec_()