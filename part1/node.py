class Node:
    def __init__(self, matrix) -> None:
        self.matrix = matrix

        self.parent = None

        self.rightDownNode = None
        self.rightUpNode = None
        self.leftLeftNode = None
        self.leftRightNode = None
        
    def getValue(self):
        return self.matrix
    
    def setValue(self, matrix):
        self.matrix = matrix

    def getRightDownNode(self):
        return self.rightNode
    
    def setRightDownNode(self, node):
        self.rightNode = node

    def getRightUpNode(self):
        return self.rightNode
    
    def setRightUpNode(self, node):
        self.rightNode = node

    def getLeftLeftNode(self):
        return self.leftNode
    
    def setLeftLeftNode(self, node):
        self.leftNode = node

    def getLeftRightNode(self):
        return self.leftNode
    
    def setLeftRightNode(self, node):
        self.leftNode = node

    def getParent(self):
        return self.parent
    
    def setParent(self, node):
        self.parent = node
