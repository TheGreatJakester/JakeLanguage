import unittest
import parse
import random

class Test_TestParsing(unittest.TestCase):
    def test_parseComments(self):
        expectedOutput = "//TEST"
        input = expectedOutput + '\n the rest of the file'
        commentArray = parse.parseComments(input)
        output = commentArray[0]
        self.assertEquals(output,expectedOutput,"first element was not the comment")

    def test_cleanCommentsOut(self):
        notAComment = '\nNot a comment'
        input = "//here is a comment"+notAComment+"//asdfasdf"
        output = parse.cleanComments(input)
        self.assertTrue("//" not in output)
        self.assertEqual(output,notAComment)
        
    
    def test_parseWords(self):
        testArray = ["these","are","all","words",'"or a string"']
        text = " ".join(testArray)
        output = parse.parseOutWords(text)
        self.assertItemsEqual(output,testArray)

    def test_parseKeyWords(self):
        wrong = ["some","of","these","words","are","not","keywords"]
        keywords = ["make","if","else","return","class","method"]
        input = wrong + keywords
        random.shuffle(input)
        output = [ word for word in input if parse.parseKeywords(word)]
        self.assertItemsEqual(output,keywords,"find the keywords")
    
    def test_parseOperators(self):
        wrong = ["these","are","not","operators","#","$","_"]
        opperators = ["+","-","*","=","+=","-=",">","<","!=",">=","<="]
        input = random.shuffle(wrong + opperators)
        output = [word for word in input if parse.parseOperators(word)]
        self.assertItemsEqual(output,opperators,"find the operators")

    def test_parseIdentifiers(self):
        opperators = ["+","-","*","=","+=","-=",">","<","!=",">=","<="]
        keywords = ["make","if","else","return","class","method"]
        invalids = ["2er4",",sdf","@sd"]
        identifiers = ["x","y","count","total","r3","R2","totalMoney","i"]

        input = random.shuffle(opperators + keywords + invalids + identifiers)
        output = [ word for word in input if parse.parseIdentifiers(word)]
        self.assertSequenceEqual(output,identifiers,"find the indentifiers")

    def test_Digits(self):
        wrong = ["these","are","not","digits","0.0.0"]
        digits = ["0","-1","3","9.0",".9","100000000"]
        input = random.shuffle(wrong + digits)
        output = [ word for word in input if parse.parseDigits(word) ]
        self.assertItemsEqual(output,digits,"find digits")

    def test_parseStrings(self):
        strings = ["\"string with spaces\"","\"stringWithNoSpaces\""]
        opperators = ["+","-","*","=","+=","-=",">","<","!=",">=","<="]
        keywords = ["make","if","else","return","class","method"]
        invalids = ["2er4",",sdf","@sd"]
        input = random.shuffle(strings + opperators + keywords + invalids)
        input = str.join(input," ")
        output = parse.parseStrings(input)
        self.assertItemsEqual(output,strings,"find strings")

    def test_cleanStrings(self):
        strings = ["\"string with spaces\"","\"stringWithNoSpaces\""]
        opperators = ["+","-","*","=","+=","-=",">","<","!=",">=","<="]
        keywords = ["make","if","else","return","class","method"]
        invalids = ["2er4",",sdf","@sd"]

        input = random.shuffle(strings + opperators + keywords + invalids)
        input = str.join(input," ")
        output = parse.cleanStrings(input)
        self.assertTrue("\"" not in input)
    


        
