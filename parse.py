import re
def parseComments(text):
    expression = r"\/\/.*$"
    found = re.findall(expression,text,re.MULTILINE)
    return found

def cleanComments(text):
    return ""

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

