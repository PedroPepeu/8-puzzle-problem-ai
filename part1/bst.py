from node import Node

class BST:
    def __init__(self, first_sample, goal) -> None:
        self.root = Node(first_sample)  # Create a root Node
        counter = 0
        while not self.__dfs(self.root, goal):  # Pass the root node, not 'self'
            self.generate_samples(5)
            counter += 1
            if counter == 10:
                print("Not found")
                return

        print("Found solution")

    def generate_samples(self, depth):
        self.setRoot(self.__generate_samples(self.getRoot(), depth, 0, 'none'))

    def __generate_samples(self, node, depth, curDepth, mov):
        if depth == curDepth:
            return node
        
        movements = {
            'none': None,
            'up': self.move_up,
            'down': self.move_down,
            'left': self.move_left,
            'right': self.move_right
        }

        if node == None:
            node.setValue(movements.get(mov, lambda s: s)(node.getValue()))            

        node.setLeftLeftNode(self.__generate_samples(node.getLeftLeftNode(), depth, curDepth+1, 'left'))
        node.setLeftRightNode(self.__generate_samples(node.getLeftRightNode(), depth, curDepth+1, 'right'))
        node.setRightUpNode(self.__generate_samples(node.getRightUpNode(), depth, curDepth+1, 'up'))
        node.setRightDownNode(self.__generate_samples(node.getRightDownNode(), depth, curDepth+1, 'down'))

        return node
    
    def find_zero(sample):
        for i in range(len(sample)):
            for j in range(len(sample)):
                if i == 0 and j == 0:
                    return i, j

    def move_up(self, sample):
        x, y = self.find_zero(sample)
        try:
            temp = sample[x][y]
            sample[x][y] = sample[x][y-1]
            sample[x][y-1] = temp
            return sample
        except Exception as e:
            return []

    def move_down(self, sample):
        x, y = self.find_zero(sample)
        try:
            temp = sample[x][y]
            sample[x][y] = sample[x][y+1]
            sample[x][y+1] = temp
            return sample
        except Exception as e:
            return []

    def move_left(self, sample):
        x, y = self.find_zero(sample)
        try:
            temp = sample[x][y]
            sample[x][y] = sample[x-1][y]
            sample[x-1][y] = temp
            return sample
        except Exception as e:
            return []

    def move_right(self, sample):
        x, y = self.find_zero(sample)
        try:
            temp = sample[x][y]
            sample[x][y] = sample[x+1][y]
            sample[x+1][y] = temp
            return sample
        except Exception as e:
            return []

    def __dfs(self, node, goal):
        stack = []
        stack.append(node)

        while stack:
            cur = stack.pop()

            if cur.getValue() == goal:  # Use 'getValue()' instead of accessing 'cur.value' directly
                return True

            leftLeftSubTree = cur.getLeftLeftNode()
            leftRightSubTree = cur.getLeftRightNode()
            rightUpSubTree = cur.getRightUpNode()
            rightDownSubTree = cur.getRightDownNode()

            if leftLeftSubTree is not None:
                stack.append(leftLeftSubTree)
            if leftRightSubTree is not None:
                stack.append(leftRightSubTree)
            if rightUpSubTree is not None:
                stack.append(rightUpSubTree)
            if rightDownSubTree is not None:
                stack.append(rightDownSubTree)

        return False
    
    def bfs(goal):
        setRoot(__bfs(getRoot(), goal))

    def __bfs(node, goal): # fix
        queue = []
        queue.append(node)

        while not queue.empty():
            cur = queue.pop()

            if(cur.getValue() == goal):
                return True

            leftLeftSubTree = cur.getLeftLeftNode()
            leftRightSubTree = cur.getLeftRightNode()
            rightUpSubTree = cur.getRightUpNode()
            rightDownSubTree = cur.getRightDownNode()

            if leftLeftSubTree != None:
                stack.append(leftLeftSubTree)
            if leftRightSubTree != None:
                stack.append(leftRightSubTree)
            if rightUpSubTree != None:
                stack.append(rightUpSubTree)
            if rightDownSubTree != None:
                stack.append(rightDownSubTree)

        return False

    def getRoot(self):
        return self.root
    
    def setRoot(self, node):
        self.root = node

mtx = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

goal = [
    [3, 2, 1],
    [4, 5, 7],
    [0, 8, 7]
]

tree = BST(mtx, goal)

print(tree)