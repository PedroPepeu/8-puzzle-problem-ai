import node

class BST:
    def __init__(self, first_sample) -> None:

        self.root = node.Node(first_sample)

    def generate_samples(depth):
        setRoot(getRoot(), depth, 0, 'none')

    def __generate_samples(node, depth, curDepth, mov):
        if depth == curDepth:
            return node
        
        movements = {
            'none': None,
            'up': move_up,
            'down': move_down,
            'left': move_left,
            'right': move_right
        }

        if node == None:
            node.setValue(movements.get(mov, lambda s: s)(node.getValue()))            

        node.setLeftLeftNode(__generate_samples(node.getLeftLeftNode(), depth, curDepth+1, 'left'))
        node.setLeftRightNode(__generate_samples(node.getLeftRightNode(), depth, curDepth+1, 'right'))
        node.setRightUpNode(__generate_samples(node.getRightUpNode(), depth, curDepth+1, 'up'))
        node.setRightDownNode(__generate_samples(node.getRightDownNode(), depth, curDepth+1, 'down'))

        return node
    
    def find_zero(sample):
        for i in range(len(sample)):
            for j in range(len(sample)):
                if i == 0 and j == 0:
                    return i, j

    def move_up(sample):
        x, y = find_zero(sample)
        try:
            temp = sample[x][y]
            sample[x][y] = sample[x][y-1]
            sample[x][y-1] = temp
            return sample
        except Exception as e:
            return []

    def move_down(sample):
        x, y = find_zero(sample)
        try:
            temp = sample[x][y]
            sample[x][y] = sample[x][y+1]
            sample[x][y+1] = temp
            return sample
        except Exception as e:
            return []

    def move_left(sample):
        x, y = find_zero(sample)
        try:
            temp = sample[x][y]
            sample[x][y] = sample[x-1][y]
            sample[x-1][y] = temp
            return sample
        except Exception as e:
            return []

    def move_right(sample):
        x, y = find_zero(sample)
        try:
            temp = sample[x][y]
            sample[x][y] = sample[x+1][y]
            sample[x+1][y] = temp
            return sample
        except Exception as e:
            return []

    def dfs(goal):
        setRoot(__dfs(getRoot(), goal))

    def __dfs(node, goal):
        stack = []
        stack.append(node)

        while not stack.empty():
            cur = stack.pop()

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
    [1, 2, 3],
    [1, 2, 3]
]

tree = BST(mtx)