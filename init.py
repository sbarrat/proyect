import sys

#from PyQt4 import QtGui


#from DynamicUser import UI_Dynamic_User
from test import Ui_fileName
from MarkovChain import MarkovChain

#class MyFrom(QtGui.QMainWindow):
#    def __init__(self, parent=None):
#        QtGui.QWidget.__init__(self, parent)
#        self.ui = Ui_MainWindow()
#        self.ui.setupUi(self)
        
class MyForm(QtGui.QMainWindow):
    def __init__(self,  parent=None):
        QtGui.QWidget.__init__(self,  parent)
        self.ui = Ui_fileName()
        self.ui = setupUi(self)

form = MyForm()
experiment = MarkovChain()

mobility = input("Which kind of profile do you want to simulate? ") 
u = experiment.Parameter_Mobility (mobility)
document = input("Where is the profile of probability? ")
list_pairs = experiment.Create_List_Pairs (document)
#print list_pairs
intento = experiment.Markov(list_pairs, u)
#if __name__ == "__main__":
#    app = QtGui.QApplication(sys.argv)
#    myapp = MyFrom()
#    myapp.show()
#    sys.exit(app.exec_())
