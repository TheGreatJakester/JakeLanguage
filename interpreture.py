from Tokenize import *
import Token
import SymbolTable
from variable import *
from ParseTree import *


class Interpreture:
    def __init__(self):
        self.table = SymbolTable.SymbolTable()
        self.tree = ParseTree()

        self.printState = False
        self.makeState = False
        self.assignState = False

        self.assignVar = None

        self.expectingIdentifier = False
        self.expectingOperand = False

        self.lastOperand = None
        self.lastOperator = None

        self.cur_value = None

        self.expectingOperator = False
        self.expectingAssignmentOperator = False

    def handleOperand(self,op):
        self.tree.addFactor(Node(op))
        if self.printState:
            print(word)
        elif self.assignState:
            if self.lastOperator and self.lastOperand :
                if not self.lastOperator.doesCompute(self.lastOperand, op):
                    print "{} doesn't work on {} and {}".format(self.lastOperator.name,self.lastOperand.var_type,op.var_type)
                    raise SyntaxError
                else:
                    self.lastOperand = self.lastOperator.execute(op,self.lastOperand)
            else:
                self.lastOperand = op
            if not self.assignVar.var_type:
                self.assignVar.var_type = op.var_type
            if not self.assignVar.var_type == op.var_type:
                print "expected type of {} to be {}".format(op.value,self.assignVar.var_type)
            
            self.expectingOperand = False
            self.expectingOperator = True


    def classifyToken(self,word):
        if(tokenizeKeywords(word)):
            if self.makeState or self.printState or self.assignState:
                self.tree.addStatment(Node(""))
                print "Wasn't expecint keyword {}".format(word)
                raise SyntaxError

            if(word == "make"):
                self.makeState = True
                self.expectingIdentifier = True
                self.tree.addKeyword(Node("make"))
            elif(word == "print"):
                self.printState = True
                self.expectingOperand = True
                self.tree.addKeyword(Node("print"))
            else:
                print "error: no support for that keyword"
                raise SyntaxError

        elif(tokenizeStrings(word)):
            if self.expectingOperand:
                op = Operand.Operand(word,Operand.STRING)
                self.handleOperand(op)
                
            else:
                print "not expecint operand {}".format(word)
                raise SyntaxError


        elif(tokenizeOperators(word)):
            if word == "=":
                if self.expectingAssignmentOperator:
                    self.assignState = True
                    self.expectingOperand = True
                    self.tree.addAssignOperaotr(Node("="))
                    return
                else:
                    print "Not expeccting assignment operator"
                    raise SyntaxError

            if not self.expectingOperator:
                print "Not expecting operator {}".format(word)
                raise SyntaxError

            operator = None
            if word == "+":
                operator = Operator.PlusOperator()
                self.tree.addTermOperator(Node("+"))
            elif word == "-":
                operator = Operator.MinusOperator()
                self.tree.addTermOperator(Node("-"))
            elif word == "*":
                operator = Operator.TimesOperator()
                self.tree.addFactorOperator(Node("*"))
            elif word == "/":
                operator = Operator.DividesOperator()
                self.tree.addFactorOperator(Node("/"))

            if operator:
                self.lastOperator = operator
            else:
                print "no support for that operator"
                raise SyntaxError

            self.expectingOperand = True
            self.expectingOperator = False


        elif(tokenizeEndOfStatment(word)):
            if (self.assignState and self.expectingOperator) or self.printState:
                self.printState = False
                self.makeState = False
                if self.assignState and self.lastOperand:
                    self.assignVar.value = self.lastOperand.value
                self.assignState = False


                self.assignVar = None

                self.expectingIdentifier = False
                self.expectingOperand = False
                self.lastOperand = None

                self.expectingOperator = False
                self.expectingAssignmentOperator = False

                self.cur_value = None
                self.tree.addStatment(Node(""))

            else: 
                print "not expecting end of statment"
                raise SyntaxError

        elif(tokenizeDigits(word)):
            if self.expectingOperand:
                op = Operand.Operand(float(word),Operand.NUMBER)
                self.handleOperand(op)
                self.tree.addFactor(Node(word))
                
            else:
                print "not expecint operand {}".format(word)
                raise SyntaxError


        elif(tokenizeIdentifiers(word)):
            cur_variable = self.table.findVariableByName(word)
            if not cur_variable:
                # no variable found; make sure we are in a make state
                if self.makeState:
                    self.assignVar = Variable(word,None,None)
                    self.expectingAssignmentOperator = True
                    self.makeState = False
                    self.table.addSymbol(self.assignVar)
                    self.tree.addIdentifier(Node(word))
                else:
                    print "identifier {} not declared".format(word)
                    raise SyntaxError
            else:
                #we found a declared variable... check states
                if self.makeState:
                    print "identifier allready declared"
                    raise SyntaxError
                elif self.printState:
                    print(cur_variable.value)
                    self.expectingOperand = True
                    self.tree.addIdentifier(Node(word))
                elif self.assignState:
                    if self.expectingOperand:
                        self.handleOperand(cur_variable)
                        node = Node(word)
                        node.value = cur_variable.value
                        self.tree.addFactor(node)
                    else:
                        print "Not expecting identifier {}".format(word)

                elif not self.assignVar:
                    self.tree.addIdentifier(Node(word))
                    #we must be statless and able to start assigning this variable
                    self.assignVar = cur_variable
                    self.expectingAssignmentOperator = True
            

        else:
            print "didn't find that word {}".format(word)
            raise SyntaxError
