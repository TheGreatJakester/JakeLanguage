import re
import parse

keyword_dict = {
    "make": "declares a variable",
    "if": "if control flow",
    "else": "else control flow",
    "return": "returns out of a method",
    "class": "declares a class",
    "method": "declares a method",
}

def classifyToken(word):
    print(word)
    if(parse.parseKeywords(word)):
        print("is a keyword of type:" + keyword_dict[word])
    elif(parse.parseStrings(word)):
        print("is a string")
    elif(parse.parseOperators(word)):
        print("is an operator")
    elif(parse.parseDigits(word)):
        print("is a number")
    elif(parse.parseIdentifiers(word)):
        print("is an identefier")
    else:
        print("unknown")

contents = ""
try:
    codeFile = open("myCode.txt","r")
    contents = codeFile.read()
    codeFile.close()
except:
    print("there was an issue reading the file")

comments = parse.parseComments(contents)
for word in comments:
    print(word)
    print("is a comment and is now removed")

contents = parse.cleanComments(contents)
words = parse.parseOutWords(contents)
for word in words:
    classifyToken(word)