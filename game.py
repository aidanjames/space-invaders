from scoreboard import Scoreboard


class Game:

    def __init__(self):
        self.scoreboard = Scoreboard()
        self.enemies = []
        self.create_enemies()

    def lose_life(self):
        self.scoreboard.lose_life()

    def create_enemies(self):
        self.enemies = []

    def kill_enemy(self, enemy):
        self.enemies.remove(enemy)
