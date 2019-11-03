import re
import Tokenize
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
    if(Tokenize.TokenizeKeywords(word)):
        return Token.Token(word + ": is a keyword of type ~:~ " + keyword_dict[word])
    elif(Tokenize.TokenizeStrings(word)):
        return Token.Token(word + ": is a string")
    elif(Tokenize.TokenizeOperators(word)):
        return Token.Token(word + ": is an operator")
    elif(Tokenize.TokenizeEndOfStatment(word)):
        return Token.Token("; : is an end of statment")
    elif(Tokenize.TokenizeDigits(word)):
        return Token.Token(word + ": is a number")
    elif(Tokenize.TokenizeIdentifiers(word)):
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

comments = Tokenize.TokenizeComments(contents)
for word in comments:
    print(word)
    print("is a comment and is now removed")
    
print
print

contents = Tokenize.cleanComments(contents)
words = Tokenize.TokenizeOutWords(contents)
tokens = [classifyToken(word) for word in words]
for token in tokens:
    print(token.description)