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
    return doesWordMeetPatter(word,r'^(make|if|else|return|class|method)$')

def parseOperators(word):
    return doesWordMeetPatter(word,r'^(\+|-|\*|=|\+=|-=|>|<|!=|>=|<=)$')

def parseIdentifiers(word):
    return doesWordMeetPatter(word,r'^([A-Za-z][A-Za-z0-9_]*)$') and not parseKeywords(word)

def parseDigits(words):
    return True

def parseStrings(word):
    return doesWordMeetPatter(word,r'^(\".*\")$')

def doesWordMeetPatter(word,pattern):
    find = re.search(pattern,word)
    return True if find else False