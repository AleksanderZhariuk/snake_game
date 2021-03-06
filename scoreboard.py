from turtle import Turtle

FONT_SETTINGS = ('Comic Sans MS', 16, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.user_score = 0
        self.start_score_position()

    def start_score_position(self):
        self.goto(0, 270)
        self.pendown()
        self.color('white')
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f'SCORE: {self.user_score}', align='center', font=FONT_SETTINGS)

    def game_over(self):
        self.clear()
        self.goto(0, 20)
        self.write(f'GAME OVER!', align='center', font=FONT_SETTINGS)
        self.goto(0, -20)
        self.write(f'YOUR SCORE: {self.user_score}', align='center', font=FONT_SETTINGS)

    def increase_score(self):
        self.clear()
        self.user_score += 1
        self.update_scoreboard()
