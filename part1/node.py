class Node:
    def __init__(self, matrix) -> None:
        self.value = matrix  # Let's standardize to 'value'
        self.parent = None
        self.rightDownNode = None
        self.rightUpNode = None
        self.leftLeftNode = None
        self.leftRightNode = None
        
    def getValue(self):
        return self.value  # Consistently use 'value' here
    
    def setValue(self, matrix):
        self.value = matrix  # Use 'value' instead of 'matrix'

    def getRightDownNode(self):
        return self.rightDownNode
    
    def setRightDownNode(self, node):
        self.rightDownNode = node

    def getRightUpNode(self):
        return self.rightUpNode
    
    def setRightUpNode(self, node):
        self.rightUpNode = node

    def getLeftLeftNode(self):
        return self.leftLeftNode
    
    def setLeftLeftNode(self, node):
        self.leftLeftNode = node

    def getLeftRightNode(self):
        return self.leftRightNode
    
    def setLeftRightNode(self, node):
        self.leftRightNode = node

    def getParent(self):
        return self.parent
    
    def setParent(self, node):
        self.parent = node
