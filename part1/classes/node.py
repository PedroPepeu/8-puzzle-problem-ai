class Node:
    def __init__(self, value, parent=None):
        self._value = value
        self._parent = parent
        self._sons = [None] * 4
    
    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    def get_parent(self):
        return self._parent

    def set_parent(self, parent):
        self._parent = parent

    def get_sons(self):
        return self._sons

    def set_son(self, index, son):
        if 0 <= index < 4:
            self._sons[index] = son
        else:
            raise IndexError("Index out of bounds. Must be between 0 and 3.")