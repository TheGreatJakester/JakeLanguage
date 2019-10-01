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
    wordPatter = r'\w+|".*"'
    words = re.findall(wordPatter,text,re.MULTILINE)
    return words

def parseKeywords(word):
    keywordsPattern = r'^(make|if|else|return|class|method)$'
    find = re.search(keywordsPattern,word)
    return True if find else False

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

