from node import Node

class first_implementation:
    def __init__(self, root_value, goal_sample):
        self.root = Node(value=root_value)
        self.goal_sample = Node(value=goal_sample)
        
    def depth_first_search(self, node, target_value):
        if node is None:
            return None
        
        if node.get_value() == target_value:
            return node
        
        for son in node.get_sons():
            result = self.depth_first_search(son, target_value)
            if result is not None:
                return result
        
        return None
    
    def put(self, node, value):
        if node is None:
            return None
        
        for i in range(4):
            if node.get_sons()[i] is None:
                new_node = Node(value=value, parent=node)
                node.set_son(i, new_node)
                return new_node

        for son in node.get_sons():
            result = self.put(son, value)
            if result is not None:
                return result
        
        return None
    
    def generate_samples(self, node, depth, cur_depth, mov):

        movements = {
            0: None,
            1: self.move_up,
            2: self.move_down,
            3: self.move_left,
            4: self.move_right
        }

        if mov is not 0:
            node.set_value(movements.get(mov, lambda s: s)(node.get_value()))

        if node.get_value() == self.goal_sample.get_value():
            print("Solution found")
        
        if depth == cur_depth:
            return node

        children = node.get_sons()
        for i in range(len(children)):
            if children[i] is None:
                children[i] = Node(value=node.get_value(), parent=node)
                children[i] = self.generate_samples(children[i], depth, cur_depth+1, i+1)
            else:
                children[i] = self.generate_samples(children[i], depth, cur_depth+1, 0)
        
        return node

    def _generate_samples(self, node, depth, cur_depth, mov, goal_sample):
        
        if cur_depth == depth:
            return node

        if node.get_value() == goal_sample:
            return node

        movements = {
            'none': None,
            'up': self.mtxop.move_up,
            'down': self.mtxop.move_down,
            'left': self.mtxop.move_left,
            'right': self.mtxop.move_right
        }

        if node is None:
            node = Node(value=node.get_parent().get_value()) 
            node.setValue(movements.get(mov, lambda s: s)(node.getValue()))

        directions = [
            ('left', node.setLeftLeftNode),
            ('right', node.setLeftRightNode),
            ('up', node.setRightUpNode),
            ('down', node.setRightDownNode)
        ]

        for direction, setter in directions:
            setter(self._generate_samples(getattr(node, f'get{direction.capitalize()}Node')(), depth, cur_depth + 1, direction))

        return node
    
    def find_zero(self, sample):
        for i in range(len(sample)):
            for j in range(len(sample[i])):
                if sample[i][j] == 0:
                    return i, j

    def move_up(self, sample):
        x, y = self.find_zero(sample)
        
        if x - 1 >= 0:
            sample[x][y], sample[x - 1][y] = sample[x - 1][y], sample[x][y]
            return sample
        else:
            return []

    def move_down(self, sample):
        x, y = self.find_zero(sample)
        
        if x + 1 < len(sample):
            sample[x][y], sample[x + 1][y] = sample[x + 1][y], sample[x][y]
            return sample
        else:
            return []

    def move_left(self, sample):
        x, y = self.find_zero(sample)
        
        if y - 1 >= 0:
            sample[x][y], sample[x][y - 1] = sample[x][y - 1], sample[x][y]
            return sample
        else:
            return []


    def move_right(self, sample):
        x, y = self.find_zero(sample)
    
        if y + 1 < len(sample[0]):
            sample[x][y], sample[x][y + 1] = sample[x][y + 1], sample[x][y]
            return sample
        else:
            return []

root = [
    [8, 0, 6],
    [3, 2, 7],
    [4, 5, 1]
]

goal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

t = first_implementation(root_value=root, goal_sample=goal)
root = Node(value=root)
t.generate_samples(root, 10, 0, 0)



