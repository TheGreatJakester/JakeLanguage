

class SymbolTable:
    table = []

    def addSymbol(variable):
        if not this.hasSymbol(variable):
            table.append(variable)
        else:
            pass

    def hasSymbol(variable):
        return False

    def findVariableByName(name):
        for var in table:
            if var.name == name:
                return var