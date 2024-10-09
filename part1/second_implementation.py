import copy
import sys
from node import Node
import time

class second_implementation:
    def __init__(self, root_value, goal_sample, depth):
        self.root = Node(value=root_value)
        self.goal_sample = Node(value=goal_sample)
        sys.setrecursionlimit(depth+100)
        self.check = 0
        self.start_time = time.time()
        self.end_time = time.time()
    
    def generate_samples(self, node, depth, cur_depth, mov):

        movements = {
            0: None,
            1: self.move_up,
            2: self.move_down,
            3: self.move_left,
            4: self.move_right
        }

        if mov != 0:
            node.set_value(movements.get(mov, lambda s: s)(copy.deepcopy(node.get_parent().get_value())))
            if node.get_value() == []:
                return None
            elif cur_depth >= 2 and node.get_parent().get_parent().get_value() == node.get_value():
                return None

        if node.get_value() == self.goal_sample.get_value():
            self.check = 1
            self.end_time = time.time()

        print(node.get_value())
        if self.check == 1:
            print(f"solution found in {self.end_time-self.start_time} seconds.")
        
        if depth == cur_depth:
            return node

        children = node.get_sons()
        for i in range(len(children)):
            if children[i] is None:
                children[i] = Node(value=None, parent=node)
                children[i] = self.generate_samples(children[i], depth, cur_depth+1, i+1)
            else:
                children[i] = self.generate_samples(children[i], depth, cur_depth+1, 0)
        
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
depth=100

t = second_implementation(root_value=root, goal_sample=goal, depth=depth)
root = Node(value=root)
t.generate_samples(root, depth, 0, 0)




