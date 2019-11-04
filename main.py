import re
import Tokenize
import Token
import interpreture

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
runner = interpreture.Interpreture()
for word in words:
    runner.classifyToken(word)
    