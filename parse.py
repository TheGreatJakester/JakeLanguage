import re
def parseComments(text):
    expression = r"\/\/.*$"
    found = re.findall(expression,text,re.MULTILINE)
    return found

def cleanComments(text):
    expression = r"\/\/.*$"
    noComment = re.sub(expression,"",text,0,re.MULTILINE)
    return noComment

def parseOutWords(text):
    return True

def parseKeywords(words):
    return True

def parseOperators(words):
    return True

def parseIdentifiers(words):
    return True

def parseDigits(words):
    return True

def parseStrings(text):
    return []

def cleanStrings(text):
    return ""

