# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DynamicUser.ui'
#
# Created: Wed Jan  9 17:24:57 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dynamic_User(object):
    def setupUi(self, Dynamic_User):
        Dynamic_User.setObjectName(_fromUtf8("Dynamic_User"))
        Dynamic_User.resize(621, 301)
        self.centralwidget = QtGui.QWidget(Dynamic_User)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.File = QtGui.QGroupBox(self.centralwidget)
        self.File.setGeometry(QtCore.QRect(10, 50, 581, 81))
        self.File.setObjectName(_fromUtf8("File"))
        self.label = QtGui.QLabel(self.File)
        self.label.setGeometry(QtCore.QRect(10, 10, 191, 41))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.File)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 61, 41))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.File)
        self.label_3.setGeometry(QtCore.QRect(200, 40, 141, 41))
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.browseButtom = QtGui.QPushButton(self.File)
        self.browseButtom.setGeometry(QtCore.QRect(490, 20, 75, 23))
        self.browseButtom.setObjectName(_fromUtf8("browseButtom"))
        self.comboBox = QtGui.QComboBox(self.File)
        self.comboBox.setGeometry(QtCore.QRect(140, 50, 41, 21))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(self.File)
        self.comboBox_2.setGeometry(QtCore.QRect(380, 50, 41, 21))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.timestep = QtGui.QSpinBox(self.File)
        self.timestep.setGeometry(QtCore.QRect(80, 50, 51, 21))
        self.timestep.setObjectName(_fromUtf8("timestep"))
        self.timesimulation = QtGui.QSpinBox(self.File)
        self.timesimulation.setGeometry(QtCore.QRect(320, 50, 51, 21))
        self.timesimulation.setObjectName(_fromUtf8("timesimulation"))
        self.ProbFile = QtGui.QLineEdit(self.File)
        self.ProbFile.setGeometry(QtCore.QRect(220, 20, 261, 21))
        self.ProbFile.setText(_fromUtf8(""))
        self.ProbFile.setObjectName(_fromUtf8("ProbFile"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 140, 591, 131))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.Mobility = QtGui.QLabel(self.groupBox)
        self.Mobility.setGeometry(QtCore.QRect(20, 10, 61, 41))
        self.Mobility.setTextFormat(QtCore.Qt.AutoText)
        self.Mobility.setObjectName(_fromUtf8("Mobility"))
        self.LowMediumHigh = QtGui.QComboBox(self.groupBox)
        self.LowMediumHigh.setGeometry(QtCore.QRect(70, 20, 69, 22))
        self.LowMediumHigh.setObjectName(_fromUtf8("LowMediumHigh"))
        self.LowMediumHigh.addItem(_fromUtf8(""))
        self.LowMediumHigh.addItem(_fromUtf8(""))
        self.LowMediumHigh.addItem(_fromUtf8(""))
        self.NumberAbsences = QtGui.QLabel(self.groupBox)
        self.NumberAbsences.setGeometry(QtCore.QRect(20, 40, 131, 41))
        self.NumberAbsences.setTextFormat(QtCore.Qt.AutoText)
        self.NumberAbsences.setObjectName(_fromUtf8("NumberAbsences"))
        self.number = QtGui.QSpinBox(self.groupBox)
        self.number.setGeometry(QtCore.QRect(150, 50, 42, 22))
        self.number.setObjectName(_fromUtf8("number"))
        self.DistribAbsences = QtGui.QLabel(self.groupBox)
        self.DistribAbsences.setGeometry(QtCore.QRect(20, 60, 211, 61))
        self.DistribAbsences.setTextFormat(QtCore.Qt.AutoText)
        self.DistribAbsences.setObjectName(_fromUtf8("DistribAbsences"))
        self.LongAbsencesFile = QtGui.QLineEdit(self.groupBox)
        self.LongAbsencesFile.setGeometry(QtCore.QRect(220, 80, 261, 21))
        self.LongAbsencesFile.setObjectName(_fromUtf8("LongAbsencesFile"))
        self.browseButtom_2 = QtGui.QPushButton(self.groupBox)
        self.browseButtom_2.setGeometry(QtCore.QRect(500, 80, 75, 23))
        self.browseButtom_2.setObjectName(_fromUtf8("browseButtom_2"))
        self.nameLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.nameLineEdit.setGeometry(QtCore.QRect(50, 20, 113, 23))
        self.nameLineEdit.setObjectName(_fromUtf8("nameLineEdit"))
        self.nameLabel = QtGui.QLabel(self.centralwidget)
        self.nameLabel.setGeometry(QtCore.QRect(10, 20, 31, 23))
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.saveButton = QtGui.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(170, 20, 101, 23))
        self.saveButton.setObjectName(_fromUtf8("saveButton"))
        self.cancelButton = QtGui.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(280, 20, 101, 23))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        Dynamic_User.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Dynamic_User)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Dynamic_User.setStatusBar(self.statusbar)
        self.label_2.setBuddy(self.timestep)
        self.label_3.setBuddy(self.timesimulation)

        self.retranslateUi(Dynamic_User)
        QtCore.QMetaObject.connectSlotsByName(Dynamic_User)

    def retranslateUi(self, Dynamic_User):
        Dynamic_User.setWindowTitle(QtGui.QApplication.translate("Dynamic_User", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.File.setTitle(QtGui.QApplication.translate("Dynamic_User", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dynamic_User", "Choose file of probability of presence", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dynamic_User", "Time step ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dynamic_User", "Total time of simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.browseButtom.setText(QtGui.QApplication.translate("Dynamic_User", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Dynamic_User", "seg", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Dynamic_User", "min", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Dynamic_User", "hour", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("Dynamic_User", "day", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(0, QtGui.QApplication.translate("Dynamic_User", "seg", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(1, QtGui.QApplication.translate("Dynamic_User", "min", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(2, QtGui.QApplication.translate("Dynamic_User", "hour", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(3, QtGui.QApplication.translate("Dynamic_User", "day", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dynamic_User", "Data ", None, QtGui.QApplication.UnicodeUTF8))
        self.Mobility.setText(QtGui.QApplication.translate("Dynamic_User", "Mobility", None, QtGui.QApplication.UnicodeUTF8))
        self.LowMediumHigh.setItemText(0, QtGui.QApplication.translate("Dynamic_User", "Low", None, QtGui.QApplication.UnicodeUTF8))
        self.LowMediumHigh.setItemText(1, QtGui.QApplication.translate("Dynamic_User", "Medium", None, QtGui.QApplication.UnicodeUTF8))
        self.LowMediumHigh.setItemText(2, QtGui.QApplication.translate("Dynamic_User", "High", None, QtGui.QApplication.UnicodeUTF8))
        self.NumberAbsences.setText(QtGui.QApplication.translate("Dynamic_User", "Number of long absences ", None, QtGui.QApplication.UnicodeUTF8))
        self.DistribAbsences.setText(QtGui.QApplication.translate("Dynamic_User", "Distribution of duration of long absences", None, QtGui.QApplication.UnicodeUTF8))
        self.browseButtom_2.setText(QtGui.QApplication.translate("Dynamic_User", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLabel.setText(QtGui.QApplication.translate("Dynamic_User", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.saveButton.setText(QtGui.QApplication.translate("Dynamic_User", "Save / Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelButton.setText(QtGui.QApplication.translate("Dynamic_User", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

