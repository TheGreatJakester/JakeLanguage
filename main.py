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


contents = ""
try:
    codeFile = open("myCode.txt","r")
    contents = codeFile.read()
    codeFile.close()
except:
    print("there was an issue reading the file")

comments = Tokenize.tokenizeComments(contents)
for word in comments:
    print(word)
    print("is a comment and is now removed")
    
print
print

contents = Tokenize.cleanComments(contents)
words = Tokenize.tokenizeOutWords(contents)
tokens = [Tokenize.classifyToken(word) for word in words]
for token in tokens:
    mes = token.value.name
    
    print(mes)