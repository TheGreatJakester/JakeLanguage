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
        self.assignSetupState = False
        self.assignVar = None

        self.printState = False

        self.expectingIdentifier = False
        self.expectingOperand = False
        self.expectingOperator = False



        self.expectingAssignmentOperator = False



    def classifyToken(self,word):
        if(tokenizeKeywords(word)):
            if(word == "make"):
                self.makeState = True
                self.expectingIdentifier = True
            if(word == "print"):
                self.printState = True
                self.expectingIdentifier = True
            else:
                raise "error: no support for that keyword"

        elif(tokenizeStrings(word)):
            return Token.Token(Operand.Operand(word,Operand.STRING))

        elif(tokenizeOperators(word)):
            if word == "+":
                return Token.Token(Operator.PlusOperator())
            if word == "-":
                return Token.Token(Operator.MinusOperator())
            if word == "*":
                return Token.Token(Operator.TimesOperator())
            if word == "/":
                return Token.Token(Operator.DividesOperator())
            if word == "=":
                return Token.Token(assignment.AssignmentOperator())

        elif(tokenizeEndOfStatment(word)):
            
            return Token.Token(endOfStatment.EndOfStatment())

        elif(tokenizeDigits(word)):
            return Token.Token(Operand.Operand(word,Operand.NUMBER))

        elif(tokenizeIdentifiers(word)):
            variable = self.table.findVariableByName(word)
            if not variable:
                # no variable found; make sure we are in a make state
                if self.makeState:
                    self.assignVar = variable.Variable(word,None,None)
                else:
                    raise "identifier not declared"
            else:
                #we found a declared variable... check states
                    
            if not self.expectingIdentifier:
                raise "not expecting Identifier: " + word
            

        else:
            raise "didn't find that word"
