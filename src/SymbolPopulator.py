# Populates symbols
from utils.colors import bcolors

class SymbolPopulator:

    symbolTable = None
    populatedCode = None
    
    def checkHalted(self):
        pass

    def checkCodeSize(self):
        pass

    def __init__(self, theSymbolTable, theGeneratedCode):
        self.symbolTable = theSymbolTable
        self.populatedCode = theGeneratedCode
        self.checkHalted()
        self.checkCodeSize()

    def resolveSymbols(self):
        pass