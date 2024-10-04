class Node:
    def __init__(self, matrix) -> None:
        self.matrix = matrix

        self.rightDownNode = None
        self.rightNode = None
        self.leftNode = None
        self.leftNode = None
        

    # def __init__(self, matrix, left, right) -> None:
    #     pass

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
