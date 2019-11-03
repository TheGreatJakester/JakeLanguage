import re
def TokenizeComments(text):
    expression = r"\/\/.*$"
    found = re.findall(expression,text,re.MULTILINE)
    return found

def cleanComments(text):
    expression = r"\/\/.*$"
    noComment = re.sub(expression,"",text,0,re.MULTILINE)
    return noComment

def TokenizeOutWords(text):
    wordPatter = r'".*"|[^\s]+'
    words = re.findall(wordPatter,text,re.MULTILINE)
    return words

def TokenizeKeywords(word):
    return doesWordMeetPattern(word,r'^(make|if|else|return|class|method)$')

def TokenizeOperators(word):
    return doesWordMeetPattern(word,r'^(\+|-|\*|=|\+=|-=|>|<|!=|>=|<=)$')

def TokenizeIdentifiers(word):
    return doesWordMeetPattern(word,r'^([A-Za-z][A-Za-z0-9_]*)$') and not TokenizeKeywords(word)

def TokenizeDigits(word):
    return doesWordMeetPattern(word,r'^((-?)\d*(\.\d*)?)$')

def TokenizeStrings(word):
    return doesWordMeetPattern(word,r'^(\".*\")$')

def TokenizeEndOfStatment(word):
    return doesWordMeetPattern(word,r'^[;]$')

def doesWordMeetPattern(word,pattern):
    find = re.search(pattern,word)
    return True if find else False

