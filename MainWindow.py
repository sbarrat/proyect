import DynamicUser
from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MainWindow(QDialog):
    def __init__(self,  parent = None):
        super(MainWindow,  self).__init__(parent)
        #Main App
        mainLayout = QBoxLayout(QBoxLayout.LeftToRight)
        mainLayout.addWidget(self.leftSection())
        mainLayout.addWidget(self.rightSection())
        #mainLayout.addWidget(self.dataSection())
        self.setLayout(mainLayout)
        self.setWindowTitle("Generate Graphic")
     
    #Left section of main window
    def leftSection(self):
        #Graphics View
        self.graphicView = QGraphicsView()
        self.graphicScene = QGraphicsScene()
        #self.graphicScene.setForegroundBrush(QBrush(Qt.lightGray, Qt.HorPattern))
        self.graphicScene.setSceneRect(0, 0, 400, 400)
        self.item = QGraphicsRectItem()
        self.item.setRect(1, 1, 50, 50)
        self.item.setPen(QPen(Qt.blue, 4, Qt.SolidLine))
        self.item.setBrush(QBrush(Qt.green, Qt.SolidPattern))
        self.graphicScene.addItem(self.item)
        self.graphicView.setScene(self.graphicScene)
        self.graphicView.setRenderHints(QPainter.Antialiasing)
        self.graphicView.show()
        
        leftGroup = QGroupBox()
        leftLayout = QBoxLayout(QBoxLayout.LeftToRight)
        leftLayout.addWidget(self.graphicView)
        leftGroup.setLayout(leftLayout)
        return leftGroup
    
    def rightSection(self):
        #labels
        experimentLabel = QLabel("Experiment:")
        propertiesLabel = QLabel("Properties:")
        self.propertiesResult = QLabel()
        self.propertiesResult.setGeometry(20,20, 200, 200)
        #Comboboxes
        self.experimentComboBox = QComboBox() #Load values from file
        self.experimentComboBox.addItems(self.loadExpemeriment())
        #Buttons
        loadButton = QPushButton("Load Experiment")
        newButton = QPushButton("New Experiment")
        
        #Conect
        self.connect(newButton, SIGNAL("clicked()"), self.loadProyect)
        #Group Layout
        rightGroup = QGroupBox()
        rightLayout = QBoxLayout(QBoxLayout.TopToBottom)
        rightLayout.addWidget(experimentLabel)
        rightLayout.addWidget(self.experimentComboBox)
        rightLayout.addWidget(propertiesLabel)
        rightLayout.addWidget(self.propertiesResult)
        rightLayout.addWidget(loadButton)
        rightLayout.addWidget(newButton)
        
        rightGroup.setLayout(rightLayout)
        return rightGroup
        
    def loadProyect(self):
        form = DynamicUser.DynamicUser()
        form.show()
        form.exec_()
        
    #Load experiment names from file
    def loadExpemeriment(self):
        experiments = ["Uno", "Dos", "Tres"]
        return experiments
