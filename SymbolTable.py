

class SymbolTable:
    def __init__(self):
        self.table = []

    def addSymbol(self,variable):
        if not self.hasSymbol(variable):
            self.table.append(variable)
        else:
            print "already defined that variable"
            raise SyntaxError

    def hasSymbol(self,variable):
        for var in self.table:
            if var.name == variable.name:
                return True
        return False

    def findVariableByName(self,name):
        for var in self.table:
            if var.name == name:
                return var
        return None