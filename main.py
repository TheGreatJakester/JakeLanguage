import re
import parse

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
    print(word)