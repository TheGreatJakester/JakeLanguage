import re
import parse
import Token

keyword_dict = {
    "make": "declares a variable",
    "if": "if control flow",
    "else": "else control flow",
    "return": "returns out of a method",
    "class": "declares a class",
    "method": "declares a method",
}

def classifyToken(word):
    if(parse.parseKeywords(word)):
        return Token.Token(word + ": is a keyword of type ~:~ " + keyword_dict[word])
    elif(parse.parseStrings(word)):
        return Token.Token(word + ": is a string")
    elif(parse.parseOperators(word)):
        return Token.Token(word + ": is an operator")
    elif(parse.parseDigits(word)):
        return Token.Token(word + ": is a number")
    elif(parse.parseIdentifiers(word)):
        return Token.Token(word + ": is an identefier")
    else:
        return Token.Token(word)

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
    print
    print

contents = parse.cleanComments(contents)
words = parse.parseOutWords(contents)
tokens = [classifyToken(word) for word in words]
for token in tokens:
    print(token.description)