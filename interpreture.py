from Tokenize import *
import Token
import SymbolTable
from variable import *


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
            elif(word == "print"):
                self.printState = True
                self.expectingIdentifier = True
            else:
                print "error: no support for that keyword"
                raise SyntaxError

        elif(tokenizeStrings(word)):
            if self.expectingOperand:
                self.lastOperand = Operand.Operand(word,Operand.STRING)
                if not self.assignVar.var_type:
                    self.assignVar.var_type = Operand.STRING
                self.expectingOperand = False
                self.expectingOperator = True
                self.expectEndState = True

            else:
                print "not expecint operand {word}"
                raise SyntaxError


        elif(tokenizeOperators(word)):
            if word == "=":
                if self.expectingAssignmentOperator:
                    self.assignState = True
                    self.expectingOperand = True
                    return
                else:
                    print "Not expeccting assignment operator"
                    raise SyntaxError

            if not self.expectingOperator:
                print "Not expecting operator {word}"
                raise SyntaxError

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
                    print "{} doesn't work on {} and {}".format(operator.name,self.lastOperand.var_type,self.assignVar.var_type)
                    raise SyntaxError
            else:
                print "no support for that operator"
                raise SyntaxError

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
                raise SyntaxError

        elif(tokenizeDigits(word)):
            if not self.expectingOperand:
                print "not expecting operand {word}"
                raise SyntaxError
            self.lastOperand = Operand.Operand(word,Operand.NUMBER)
            if not self.assignVar.var_type:
                self.assignVar.var_type = Operand.NUMBER
            self.expectingOperand = False
            self.expectingOperator = True
            self.expectEndState = True

        elif(tokenizeIdentifiers(word)):
            variable = self.table.findVariableByName(word)
            if not variable:
                # no variable found; make sure we are in a make state
                if self.makeState:
                    self.assignVar = Variable(word,None,None)
                    self.expectingAssignmentOperator = True
                    self.table.addSymbol(self.assignVar)
                else:
                    print "identifier not declared"
                    raise SyntaxError
            else:
                #we found a declared variable... check states
                if self.makeState:
                    print "identifier allready declared"
                    raise SyntaxError
                elif self.printState:
                    print(variable.value)
                    self.expectEndState = True
                elif self.assignState:
                    if not self.assignVar.var_type:
                        self.assignVar.var_type = variable.var_type
                    if not variable.var_type == self.assignVar.var_type:
                        print "type of {variable.name} doesn't match {self.assignVar.name}"
                        raise SyntaxError
                elif not self.assignVar:
                    #we must be statless and able to start assigning this variable
                    self.assignVar = variable
                    self.expectingAssignmentOperator = True
            

        else:
            print "didn't find that word {word}"
            raise SyntaxError
