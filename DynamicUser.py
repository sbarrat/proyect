from PyQt4.QtCore import *
from PyQt4.QtGui import *
import MarkovChain

class DynamicUser(QDialog):
    def __init__(self,  parent = None):
        super(DynamicUser,  self).__init__(parent)
        
        #Main App
        mainLayout = QBoxLayout(QBoxLayout.TopToBottom)
        mainLayout.addWidget(self.topSection())
        mainLayout.addWidget(self.fileSection())
        mainLayout.addWidget(self.dataSection())
        self.setLayout(mainLayout)
        self.setWindowTitle("DynamicUser")
        
    #Top Section
    def topSection(self):
        #Label
        nameLabel = QLabel("Name:")
        
        #LineEdit
        self.nameText = QLineEdit()
        
        #Buttons
        self.saveAddButton = QPushButton()
        self.saveAddButton.setText("Save / Add")
        self.cancelButton = QPushButton()
        self.cancelButton.setText("Cancel")
        
        #Connect objects with signals
        self.connect(self.saveAddButton, SIGNAL("clicked()"), self.addExperiment)
        
        #Group
        mainGroup = QGroupBox()
        #Layout
        mainLayout = QHBoxLayout()
        mainLayout.addWidget(nameLabel)
        mainLayout.addWidget(self.nameText)
        mainLayout.addWidget(self.saveAddButton)
        mainLayout.addWidget(self.cancelButton)
        mainGroup.setLayout(mainLayout)
        return mainGroup
        
    #File Section
    def fileSection(self):
        #Labels
        fileChooseLabel = QLabel("Choose file of probability of presence:")
        timeStepLabel = QLabel("Time step:")
        totalTimeLabel = QLabel("Total time of simulation:")
        #LineEdit
        self.fileChooseText = QLineEdit()
        #Buttons
        self.fileBrowseButton = QPushButton()
        self.fileBrowseButton.setText("Browse")
        #SpinBoxes
        self.timeStepSpinBox = QSpinBox()
        self.timeStepSpinBox.setRange(0, 10000)
        self.totalTimeSpinBox = QSpinBox()
        self.totalTimeSpinBox.setRange(0, 60)
        #ComboBoxes
        self.timeStepComboBox = QComboBox()
        self.timeStepComboBox.addItems(["seg", "min", "hour", "day"]) 
        self.totalTimeComboBox = QComboBox()
        self.totalTimeComboBox.addItems(["seg", "min", "hour", "day"])
        
        #Connect objects with signals
        self.connect(self.fileBrowseButton, SIGNAL("clicked()"), self.setProfileFile)
        
        #Main Group
        fileGroup = QGroupBox()
        fileGroup.setTitle("File")
        
        #Layout
        fileLayout = QBoxLayout(QBoxLayout.TopToBottom)
        topFileLayout = QHBoxLayout()
        bottomFileLayout = QHBoxLayout()
        
        #Top Layout
        topFileLayout.addWidget(fileChooseLabel)
        topFileLayout.addWidget(self.fileChooseText)
        topFileLayout.addWidget(self.fileBrowseButton)
        #Bottom Layout
        bottomFileLayout.addWidget(timeStepLabel)
        bottomFileLayout.addWidget(self.timeStepSpinBox)
        bottomFileLayout.addWidget(self.timeStepComboBox)
        
        bottomFileLayout.addWidget(totalTimeLabel)
        bottomFileLayout.addWidget(self.totalTimeSpinBox)
        bottomFileLayout.addWidget(self.totalTimeComboBox)
        #Adds layouts to main layout
        fileLayout.addLayout(topFileLayout)
        fileLayout.addLayout(bottomFileLayout)
        fileGroup.setLayout(fileLayout)
        
        return fileGroup
    
    #Data Section
    def dataSection(self):
        #Labels
        mobilityLabel = QLabel("Mobility:")
        numberLabel = QLabel("Number of long absences:")
        distributionLabel = QLabel("Distribution of duration of long:")
        #ComboBoxes
        self.mobilityComboBox = QComboBox()
        self.mobilityComboBox.addItems(["Low", "Medium", "High"])
        #SpinBoxes
        self.numberSpinBox = QSpinBox()
        self.numberSpinBox.setRange(0, 1000)
        #LineEdit
        self.distributionLineEdit = QLineEdit()
        #Button
        self.distributionButton = QPushButton()
        self.distributionButton.setText("Browse")
        
        #Group
        dataGroup = QGroupBox()
        dataGroup.setTitle("Data")
        dataLayout = QBoxLayout(QBoxLayout.TopToBottom)
        
        topLayout = QBoxLayout(QBoxLayout.LeftToRight)
        middleLayout = QBoxLayout(QBoxLayout.LeftToRight)
        bottomLayout = QBoxLayout(QBoxLayout.LeftToRight)
        #Top layout
        topLayout.addWidget(mobilityLabel)
        topLayout.addWidget(self.mobilityComboBox)
        #Middle Layout
        middleLayout.addWidget(numberLabel)
        middleLayout.addWidget(self.numberSpinBox)
        #Bottom Layout
        bottomLayout.addWidget(distributionLabel)
        bottomLayout.addWidget(self.distributionLineEdit)
        bottomLayout.addWidget(self.distributionButton)
        
        #Add Layouts to data Layout
        dataLayout.addLayout(topLayout)
        dataLayout.addLayout(middleLayout)
        dataLayout.addLayout(bottomLayout)
        dataGroup.setLayout(dataLayout)
        
        return dataGroup
    
    #Catch Browse file signal
    def setProfileFile(self):
        fileName = QFileDialog.getOpenFileName(self, "Select Profile File")
        if fileName == '':
            self.alertDialog("Error", "You must select a file")
        else:
            markov = MarkovChain.MarkovChain()
            self.pares = markov.Create_List_Pairs(fileName)
            self.fileChooseText.setText(fileName)
    
    #Add a new experiment
    def addExperiment(self):
        if self.nameText.text() == "":
            self.alertDialog("Error", "You must enter a experiment name");
        else:
            if self.fileChooseText.text() != "":
                timeStep = self.timeStepSpinBox.value()
                timeStepUnits = self.timeStepComboBox.currentText()
                totalTime = self.totalTimeSpinBox.value()
                totalTimeUnits = self.totalTimeComboBox.currentText()
                fileName = self.fileChooseText.text();
                experimentName = self.nameText.text();
                resultLine = "File: %s\nExp Name: %s\n TimeStep: %i %s \n TotalTime: %i %s \n %s" \
                % (fileName, experimentName, timeStep, timeStepUnits, totalTime, totalTimeUnits, self.pares)
                self.alertDialog("Result", resultLine)
            else:
                self.setProfileFile()
             
    #Open a new dialog box, for testing purposes
    def alertDialog(self, title, text):
        dialog = QDialog()
        dialog.setWindowTitle(title)
        result = QLabel()
        result.setText(text)
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        layout.addWidget(result)
        dialog.setLayout(layout)
        dialog.show()
        dialog.exec_()

#Launch the App        
#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    form = DynamicUser()
#    form.show()
#    app.exec_()
        
        