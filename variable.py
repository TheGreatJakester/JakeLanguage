
STRING = 0
NUMBER = 1
BOOLEAN = 2


class Variable:
    def __init__(self,name,value,var_type):
        self.name = name
        self.value = value
        self.var_type = var_type