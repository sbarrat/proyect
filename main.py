'''
Created on 12/01/2013

@author: Ruben Lacasa http://rubenlacasa.es
'''
import sys, MainWindow
from PyQt4.QtCore import *
from PyQt4.QtGui import *
#Launch the App
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainWindow.MainWindow()
    form.show()
    app.exec_()