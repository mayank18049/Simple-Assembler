# Generates code and symbol table
from utils.colors import bcolors

class SymbolTable:

    varDecls = {}
    labelDecls = {}
    varUsage = []
    labelUsage = []

    def addVarDecl(self, varName):
        pass

    def resolveVarAddr(self, codeSize):
        pass

    def addLabelDecl(self, labelName, addr):
        pass

    def addVarUsage(self, varName, instNum):
        pass

    def addLabelUsage(self, labelName, instNum):
        pass

class CodeGen:

    symbolTable = None
    generatedCode = None
    halted = False
    instNum = 0

    def __init__(self):
        pass

    def instNumToAddr(self, instNum):
        pass

    def generate(self, frontendPass, tokens):
        pass

