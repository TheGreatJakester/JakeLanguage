STRING = "STRING"
NUMBER = "NUMBER"
BOOLEAN = "BOOLEAN"


class Operand:
    def __init__(self,value,var_type):
        self.value = value
        self.var_type = var_type