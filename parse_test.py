import unittest
import parse

class Test_TestParsing(unittest.TestCase):
    def parseComments(self):
        output = "TEST"
        input = "//" + output + "\n the rest of the line"
        commentArray = parse.parseComments(input)
        self.assertEquals(output,commentArray[0],"first element was not the comment")
    def test_parseWords(self):
        testArray = ["these","are","all","words"]
        self.assertSequenceEqual(parse.parseOutWords(str.join(testArray," ")),testArray)

    def test_parseKeyWords(self):
        pass
    
    def test_parseOperators:
        pass

    def test_parseIdentifiers:
        pass

    def test_Digits:
        pass

    def test_parseStrings:
        pass
        


    
