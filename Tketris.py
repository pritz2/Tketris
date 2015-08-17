from tkinter import Tk, Canvas

class Tetris():
    def init(self):
        self.root = Tk()
        self.root.title("Tetris! By the Pritz Brothers")

        self.board = Board(self.root)
        self.current_piece = Piece(self.board)

        self.time_interval = 500
        self.timer()
        
        self.root.mainloop()

    def timer(self):
        self.root.after(self.time_interval, self.timer)
        self.current_piece.fall()

class Board():
    BOX_SIZE = 50
    WIDTH = 500
    HEIGHT = 900

    def __init__(self, root):
        self.canvas = Canvas(
            root,
            width=Board.WIDTH,
            height=Board.HEIGHT)
        self.canvas.pack()

    def create_rectangle(self):
        return self.canvas.create_rectangle(100, 0, Board.BOX_SIZE, Board.BOX_SIZE, fill="blue")

    def fall(self, box):
        if self.can_move(box):
            self.canvas.move(box, 0, Board.BOX_SIZE)
            #print(self.canvas.coords(piece))

    def can_move(self, box):
        coords = self.canvas.coords(box)
        print(coords)
        if coords[0] == 0 or coords[2] == Board.WIDTH or coords[3] == Board.HEIGHT:
            return False
        return True


class Piece():
    def __init__(self, board):
        self.board = board
        self.box = self.board.create_rectangle()

    def fall(self):
        self.board.fall(self.box)


if __name__ == "__main__":
    game = Tetris()
    game.init()
