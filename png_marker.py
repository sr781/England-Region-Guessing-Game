from turtle import Turtle


class Marker(Turtle):
    def __init__(self):
        super().__init__()

    # This function is responsible for marking the regions on the "england.gif" map
    def mark(self, x, y, answer):  # The function takes an x and y coordinates and the name of the region to plot
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x, y)
        self.write(f"{answer}", align="left", font=("Arial", 12, "normal"))
