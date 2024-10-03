class n_puzzle_operation:
    def __init__(self, stateMtx) -> None:
        self.state = matrix_to_tree(stateMtx)

    def matrix_to_tree(stateMtx):
        return None
    
    def generate_new_state(state):
        return None
    
    def check_state(state):
        return None
    
    def find_blank_position(state):
        return None

    def change_position(state, mov):
        movements = {
            'up': move_up,
            'down': move_down,
            'left': move_left,
            'right': move_right
        }

        pos = find_blank_position(state)
        return movements.get(mov, lambda s: s)(state, pos)
    
    def move_up(state, pos):
        try:
            

        except Exception as e:
            return None

    def move_down(state, pos):
        try:
            return None

        except Exception as e:
            return None

    def move_left(state, pos):
        try:
            return None

        except Exception as e:
            return None

    def move_right(state, pos):
        try:
            return None

        except Exception as e:
            return None

