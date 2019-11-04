STRING = 0
NUMBER = 1
BOOLEAN = 2


class Operand:
    def __init__(self,value,var_type):
        self.value = value
        self.var_type = var_type