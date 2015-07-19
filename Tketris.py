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

        self.time_interval = 500
        self.timer()
        
        self.root.mainloop()

    def timer(self):
        print("Hello")
        self.root.after(self.time_interval, self.timer)

if __name__ == "__main__":
    game = Tetris()
    game.init()
