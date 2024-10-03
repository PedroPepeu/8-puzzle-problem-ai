class node:
    def __init__(self, val) -> None:
        self.val = val
        
        self.Up = None
        self.Down = None
        self.Right = None
        self.Left = None

    def getVal():
        return self.val

    def getUp():
        return self.Up

    def getDown():
        return self.Down

    def getRight():
        return self.Right

    def getLeft():
        return self.Left
        
    def setVal(val):
        self.val = val
    
    def setUp(node):
        self.Up = node

    def setDown(node):
        self.Down = node

    def setRight(node):
        self.Right = node

    def setLeft(node):
        self.Left = node

class tree:
    def __init__(self, mtxlist) -> None:
        self.root = node(-1)
        self.root = matrix_to_graph(mtxlist, visitlist(mtxlist), self.root, 0, 0)

    def visitlist(mtx):
        vis = mtx

        for i in range(len(mtx)):
            for j in range(len(mtx[i])):
                vis[i][j] = 0

        return vis

    def matrix_to_graph(mtx, vis, node, i, j):
        if vis[i][j] == 1:
            return None
        
        node.setVal(mtx[i][j])
        vis[i][j] = 1

        if i+1 <= len(mtx):
            node.setRight(matrix_to_grapth(mtx, vis, node, i+1, j))
        
        if j+i <= len(mtx[i]):
            node.setDown(matrix_to_grapth(mtx, vis, node, i, j+1))

        return node

    def generate_sample():
        pass

    
