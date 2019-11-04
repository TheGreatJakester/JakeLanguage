from Tokenize import *
import Token


class Interpreture:
    def classifyToken(word):
        if(tokenizeKeywords(word)):
            if(word == "make"):
                return Token.Token(Keyword.Keyword())
            if(word == "print"):
                return Token.Token(printOperator.PrintOperator())
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
            return Token.Token(Identifier.Identifier(word))
        else:
            raise "didn't find that word"
