from turtle import Turtle

class Boundary(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=0.1, stretch_wid=40)
        