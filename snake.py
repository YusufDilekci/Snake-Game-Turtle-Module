from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):

        for position in STARTING_POSITION:
            self.add_square(position)

    def add_square(self, position):
        new_square = Turtle('square')
        new_square.color('white')
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square)

    def extend(self):
        self.add_square(self.squares[-1].position())# sonuncu yılan bölmesi belirlediğimiz algoritmaya göre bir önceki
                                                    #bölmeye geleceğine göre ekledğimiz her yeni segment en sondakinin
                                                    # pozisyonuna geçer


    def reset(self):
        for suq in self.squares:
            suq.goto(1000, 1000)

        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]
    def move(self):

        for square in range(len(self.squares) - 1, 0, -1):
            new_x = self.squares[square - 1].xcor()
            new_y = self.squares[square - 1].ycor()
            self.squares[square].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)





