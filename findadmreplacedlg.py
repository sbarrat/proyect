import re
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_findandreplacedlg

class FindAndReplaceDlg(QDialog, ui_findandreplacedlg.Ui_Dialog):
    
    def __init__(self, text, parent = None):
        super(FindAndReplaceDlg, self).__init__(parent)
        self.__text = unicode(text)
        self.__index = 0
        self.setupUi(self)
        self.updateUi()
