from tkinter import Tk, Canvas

class Tetris():
    WIDTH = 500
    HEIGHT = 650
    
    def init(self):
        self.root = Tk()
        self.root.title("Tetris! By the Pritz Brothers")
        
        self.canvas = Canvas(
                self.root, 
                width=Tetris.WIDTH, 
                height=Tetris.HEIGHT)
        self.canvas.pack()
        
        self.root.mainloop()

if __name__ == "__main__":
    game = Tetris()
    game.init()