class HumanPlayer:
    def __init__(self, piece):
        self.piece = piece

    def get_cell(self):
        row = int(input("Make your row selection (1-9): ")) - 1
        col = int(input("Make your column selection (1-9): ")) - 1
        return row, col


class AiPlayer:
    def __init__(self, piece):
        self.piece = piece
