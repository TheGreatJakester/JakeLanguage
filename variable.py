import Operand

class Variable(Operand):
    def __init__(self,name,value,var_type):
        super(self,value,var_type)
        self.name = name