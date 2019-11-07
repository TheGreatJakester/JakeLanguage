class Node:
    def __init__(self):
        self.name = ""
        self.value = None
        self.children = []
    
    def addChild(self,child):
        self.children.append(child)


class ParseTree:
    def __init__(self):
        self.root = Node()
        self.root.name = "Root"

        self.lastStatment = None
        self.lastKeyword = None
        self.lastTerm = None
        self.lastFactor = None

    def addStatment(self,node):
        self.lastStatment = node
        self.root.addChild(statmentNode)

        self.lastKeyword = None
        self.lastTerm = None
        self.lastFactor = None

    def addKeyword(self,node):
        self.lastKeyword = node
        self.lastStatment.addChild(node)

    def addIdentifier(self,node):
        if(self.lastFactor):
            self.lastFactor.addChild(node)
        elif(self.lastTerm):
            self.lastTerm.addChild(node)
        elif(self.lastKeyword)
            self.lastKeyword.addChild(node)
        else:
            pass

        
    def addTerm(self,node):
        self.lastTerm = node
        self.lastStatment.addChild(node)
    
    def addFactor(self,node):
        if(self.lastFactor):
            self.lastFactor.addChild(node)
        else:
            self.lastTerm.addChild(node)
            self.lastTerm = node
