from Tokenize import *
import Token
import SymbolTable
import variable


class Interpreture:
    def __init__(self):
        self.table = SymbolTable.SymbolTable()

        self.printState = False
        self.makeState = False
        self.assignState = False

        self.assignVar = None

        self.expectingIdentifier = False
        self.expectingOperand = False
        self.lastOperand = None

        self.expectingOperator = False
        self.expectingAssignmentOperator = False

        self.expectEndState = False


    def classifyToken(self,word):
        if(tokenizeKeywords(word)):
            if(word == "make"):
                self.makeState = True
                self.expectingIdentifier = True
            if(word == "print"):
                self.printState = True
                self.expectingIdentifier = True
            else:
                print "error: no support for that keyword"
                raise

        elif(tokenizeStrings(word)):
            if self.expectingOperand:
                self.lastOperand = Operand.Operand(word,Operand.STRING)
                self.expectingOperand = False
                self.expectingOperator = True
                self.expectEndState = True

            else:
                print "not expecint operand {word}"
                raise


        elif(tokenizeOperators(word)):
            if word == "=":
                if self.expectingAssignmentOperator:
                    self.assignState = True
                    return
                else:
                    print "Not expeccting assignment operator"
                    raise

            if not self.expectingOperator:
                print "Not expecting operator {word}"
                raise

            operator = None
            if word == "+":
                operator = Operator.PlusOperator()
            elif word == "-":
                operator = Operator.MinusOperator()
            elif word == "*":
                operator = Operator.TimesOperator()
            elif word == "/":
                operator = Operator.DividesOperator()

            if operator:
                if not operator.doesCompute(self.lastOperand, self.assignVar):
                    print "{operator.name} doesn't work on {self.lastOperand.var_type} and {self.assignVar.var_type}"
                    raise
            else:
                print "no support for that operator"
                raise

            self.expectEndState = False
            self.expectingOperand = True
            self.expectingOperator = False


        elif(tokenizeEndOfStatment(word)):
            if self.expectEndState:
                self.printState = False
                self.makeState = False
                self.assignState = False

                self.assignVar = None

                self.expectingIdentifier = False
                self.expectingOperand = False
                self.lastOperand = None

                self.expectingOperator = False
                self.expectingAssignmentOperator = False

                self.expectEndState = False
            else: 
                print "not expecting end of statment"
                raise

        elif(tokenizeDigits(word)):
            if not self.expectingOperand:
                print "not expecting operand {word}"
                raise
            self.lastOperand = Operand.Operand(word,Operand.NUMBER)
            self.expectingOperand = False
            self.expectingOperator = True
            self.expectEndState = True

        elif(tokenizeIdentifiers(word)):
            variable = self.table.findVariableByName(word)
            if not variable:
                # no variable found; make sure we are in a make state
                if self.makeState:
                    self.assignVar = variable.Variable(word,None,None)
                    self.expectingAssignmentOperator = True
                else:
                    print "identifier not declared"
                    raise
            else:
                #we found a declared variable... check states
                if self.makeState:
                    print "identifier allready declared"
                    raise
                elif self.printState:
                    print(variable.variable.value)
                    self.expectEndState = True
                elif self.assignState:
                    if not self.assignVar.var_type:
                        self.assignVar.var_type = variable.var_type
                    if not variable.var_type == self.assignVar.var_type:
                        print "type of {variable.name} doesn't match {self.assignVar.name}"
                        raise
                elif not self.assignVar:
                    #we must be statless and able to start assigning this variable
                    self.assignVar = variable
                    self.expectingAssignmentOperator = True
            

        else:
            print "didn't find that word {word}"
            raise
