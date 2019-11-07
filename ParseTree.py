class Node:
    def __init__(self,name):
        self.name = name
        self.value = None
        self.children = []
    
    def addChild(self,child):
        self.children.append(child)


class ParseTree:
    def __init__(self):
        self.root = Node()
        self.root.name = "Root"

        self.lastStatment = Node("")
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
        if(self.lastStatment):
            self.lastStatment.addChild(node)

    def addAssignOperaotr(self,node):
        if(self.lastStatment):
            self.lastStatment.addChild(node)

    def addTermOperator(self,node):
        self.lastFactor = Node
        if(self.lastStatment):
            self.lastStatment.addChild(node)

    def addFactorOperator(self,node):
        self.lastFactor = node
        if(self.lastTerm):
            self.lastTerm.addChild(node)


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
        if(self.lastStatment):
            self.lastStatment.addChild(node)
    
    def addFactor(self,node):
        if(self.lastFactor):
            self.lastFactor.addChild(node)
        else:
            self.lastTerm.addChild(node)
            self.lastTerm = node
