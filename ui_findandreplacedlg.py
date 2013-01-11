# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'findandreplacedlg.ui'
#
# Created: Thu Jan 10 18:16:40 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(404, 210)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 10, 365, 185))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.findLineEdit = QtGui.QLineEdit(self.widget)
        self.findLineEdit.setObjectName(_fromUtf8("findLineEdit"))
        self.horizontalLayout.addWidget(self.findLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line = QtGui.QFrame(self.widget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.replaceLineEdit = QtGui.QLineEdit(self.widget)
        self.replaceLineEdit.setObjectName(_fromUtf8("replaceLineEdit"))
        self.horizontalLayout_2.addWidget(self.replaceLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.caseCheckBox = QtGui.QCheckBox(self.widget)
        self.caseCheckBox.setObjectName(_fromUtf8("caseCheckBox"))
        self.horizontalLayout_3.addWidget(self.caseCheckBox)
        self.wholeCheckBox = QtGui.QCheckBox(self.widget)
        self.wholeCheckBox.setObjectName(_fromUtf8("wholeCheckBox"))
        self.horizontalLayout_3.addWidget(self.wholeCheckBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.syntaxComboBox = QtGui.QComboBox(self.widget)
        self.syntaxComboBox.setObjectName(_fromUtf8("syntaxComboBox"))
        self.syntaxComboBox.addItem(_fromUtf8(""))
        self.syntaxComboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_4.addWidget(self.syntaxComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.line_2 = QtGui.QFrame(self.widget)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.horizontalLayout_5.addWidget(self.line_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.findButton = QtGui.QPushButton(self.widget)
        self.findButton.setObjectName(_fromUtf8("findButton"))
        self.verticalLayout.addWidget(self.findButton)
        self.replaceButton = QtGui.QPushButton(self.widget)
        self.replaceButton.setObjectName(_fromUtf8("replaceButton"))
        self.verticalLayout.addWidget(self.replaceButton)
        self.replaceAllButton = QtGui.QPushButton(self.widget)
        self.replaceAllButton.setObjectName(_fromUtf8("replaceAllButton"))
        self.verticalLayout.addWidget(self.replaceAllButton)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.closeButton = QtGui.QPushButton(self.widget)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.verticalLayout.addWidget(self.closeButton)
        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Find &what:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Replace w&ith:", None, QtGui.QApplication.UnicodeUTF8))
        self.caseCheckBox.setText(QtGui.QApplication.translate("Dialog", "&Case sensitive", None, QtGui.QApplication.UnicodeUTF8))
        self.wholeCheckBox.setText(QtGui.QApplication.translate("Dialog", "Wh&ole words", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "&Syntax:", None, QtGui.QApplication.UnicodeUTF8))
        self.syntaxComboBox.setItemText(0, QtGui.QApplication.translate("Dialog", "Literal text", None, QtGui.QApplication.UnicodeUTF8))
        self.syntaxComboBox.setItemText(1, QtGui.QApplication.translate("Dialog", "Regular expression", None, QtGui.QApplication.UnicodeUTF8))
        self.findButton.setText(QtGui.QApplication.translate("Dialog", "&Find", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceButton.setText(QtGui.QApplication.translate("Dialog", "&Replace", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceAllButton.setText(QtGui.QApplication.translate("Dialog", "Replace &All", None, QtGui.QApplication.UnicodeUTF8))
        self.closeButton.setText(QtGui.QApplication.translate("Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

