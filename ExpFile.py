'''
Created on 12/01/2013

@author: ruben
'''
from PyQt4.QtCore import *
import os.path, fileinput
class ExpFile():
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._filename = "experiments.txt"
        if not os.path.isfile(self._filename):
            fh = open(self._filename, "w")
            fh.close()
            
    def readFile(self):
        fh = open(self._filename, "r")
        fileContens = fileinput.filename(fh)
        pass
    
    def writeFile(self):
        fh = open(self._filename, "a")
        pass
        
        