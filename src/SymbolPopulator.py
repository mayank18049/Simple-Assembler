# Populates symbols
from utils.colors import bcolors

class SymbolPopulator:

    symbolTable = None
    populatedCode = None

    def __init__(self, theSymbolTable, theGeneratedCode):
        self.symbolTable = theSymbolTable
        self.populatedCode = theGeneratedCode

    def resolveSymbols(self):
        pass