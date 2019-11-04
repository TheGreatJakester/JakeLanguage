
import Operand
import Operator

def doubleCheck(operand1,operand2,data_type):
    return operand1.type == data_type and operand2.type == data_type
           

class Operator:
    def __init__(self):    
        self.name = ""
        self.data_types = []
    def doesCompute(self,op1,op2):
        for dt in self.data_types:
            if not doubleCheck(op1,op2,dt):
                return False
        return True

    def evaluate(operand1,operand):
        pass

    def execute(op1,op2):
        if self.doesCompute(op1,op2) :
            return self.evaluate(op1,op2)
        else:
            raise "Operator %s doesn't work on %s and %s" % name, op1.type, op2.type

class PlusOperator(Operator):
    def __init__(self): 
        self.name = "+"
        self.data_types = [Operand.STRING,Operand.NUMBER]
    def evaluate(operand1,operand):
        return operand1 + operand2

class MinusOperator(Operator):
    def __init__(self): 
        self.name = "-"
        self.data_types = [Operand.STRING,Operand.NUMBER]
    def evaluate(operand1,operand):
        return operand1 * operand2


class TimesOperator(Operator):
    def __init__(self): 
        self.name = "*"
        self.data_types = [Operand.NUMBER]
    def evaluate(operand1,operand):
        return operand1 * operand2
    
class DividesOperator(Operator):
    def __init__(self): 
        self.name = "/"
        self.data_types = [Operand.NUMBER]
    def evaluate(operand1,operand):
        return operand1 / operand2