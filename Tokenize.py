import re
import Keyword
import Operand
import Operator
import endOfStatment
import variable
import Identifier
import Token

def tokenizeComments(text):
    expression = r"\/\/.*$"
    found = re.findall(expression,text,re.MULTILINE)
    return found

def cleanComments(text):
    expression = r"\/\/.*$"
    noComment = re.sub(expression,"",text,0,re.MULTILINE)
    return noComment

def tokenizeOutWords(text):
    wordPatter = r'".*"|[^\s]+'
    words = re.findall(wordPatter,text,re.MULTILINE)
    return words

def tokenizeKeywords(word):
    return doesWordMeetPattern(word,r'^(make|if|else|return|class|method)$')

def tokenizeOperators(word):
    return doesWordMeetPattern(word,r'^(\+|-|\*|=|\+=|-=|>|<|!=|>=|<=)$')

def tokenizeIdentifiers(word):
    return doesWordMeetPattern(word,r'^([A-Za-z][A-Za-z0-9_]*)$') and not tokenizeKeywords(word)

def tokenizeDigits(word):
    return doesWordMeetPattern(word,r'^((-?)\d*(\.\d*)?)$')

def tokenizeStrings(word):
    return doesWordMeetPattern(word,r'^(\".*\")$')

def tokenizeEndOfStatment(word):
    return doesWordMeetPattern(word,r'^[;]$')

def doesWordMeetPattern(word,pattern):
    find = re.search(pattern,word)
    return True if find else False


def classifyToken(word):
    if(tokenizeKeywords(word)):
        if(word == "make"):
            return Token.Token(Keyword.Keyword())
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

    elif(tokenizeEndOfStatment(word)):
        
        return Token.Token(endOfStatment.EndOfStatment)

    elif(tokenizeDigits(word)):
        return Token.Token(Operand.Operand(word,Operand.NUMBER))

    elif(tokenizeIdentifiers(word)):
        return Token.Token(Identifier.Identifier(word))
    else:
        raise "didn't find that word"
