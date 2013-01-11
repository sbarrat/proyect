# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created: Wed Jan  9 20:51:57 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_fileName(object):
    def setupUi(self, fileName):
        fileName.setObjectName(_fromUtf8("fileName"))
        fileName.resize(458, 162)
        self.profileComboBox = QtGui.QComboBox(fileName)
        self.profileComboBox.setGeometry(QtCore.QRect(320, 20, 78, 27))
        self.profileComboBox.setObjectName(_fromUtf8("profileComboBox"))
        self.profileComboBox.addItem(_fromUtf8(""))
        self.profileComboBox.addItem(_fromUtf8(""))
        self.profileComboBox.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(fileName)
        self.label.setGeometry(QtCore.QRect(0, 30, 311, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(fileName)
        self.pushButton.setGeometry(QtCore.QRect(310, 70, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(fileName)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 271, 27))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        self.retranslateUi(fileName)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), fileName.open)
        QtCore.QMetaObject.connectSlotsByName(fileName)

    def retranslateUi(self, fileName):
        fileName.setWindowTitle(QtGui.QApplication.translate("fileName", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.profileComboBox.setItemText(0, QtGui.QApplication.translate("fileName", "High", None, QtGui.QApplication.UnicodeUTF8))
        self.profileComboBox.setItemText(1, QtGui.QApplication.translate("fileName", "Medium", None, QtGui.QApplication.UnicodeUTF8))
        self.profileComboBox.setItemText(2, QtGui.QApplication.translate("fileName", "Other", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("fileName", "Which kind of profile do you want to simulate?", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("fileName", "Select File", None, QtGui.QApplication.UnicodeUTF8))

