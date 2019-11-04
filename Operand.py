STRING = 111
NUMBER = 222
BOOLEAN = 333


class Operand:
    def __init__(self,value,var_type):
        self.value = value
        self.var_type = var_type