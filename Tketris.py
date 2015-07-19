from tkinter import Tk, Canvas

class Tetris():
    WIDTH = 500
    HEIGHT = 900
    
    def init(self):
        self.root = Tk()
        self.root.title("Tetris! By the Pritz Brothers")
        
        self.canvas = Canvas(
                self.root, 
                width=Tetris.WIDTH, 
                height=Tetris.HEIGHT)
        self.canvas.pack()

        self.current_piece = Piece(self.canvas)

        self.time_interval = 500
        self.timer()
        
        self.root.mainloop()

    def timer(self):
        self.root.after(self.time_interval, self.timer)
        self.current_piece.fall()

class Piece():
    BOX_SIZE = 50
    
    def __init__(self, canvas):
        self.canvas = canvas
        self.box = self.canvas.create_rectangle(100, 0, Piece.BOX_SIZE, Piece.BOX_SIZE, fill="blue")

    def fall(self):
        self.canvas.move(self.box, 0, Piece.BOX_SIZE)

if __name__ == "__main__":
    game = Tetris()
    game.init()
