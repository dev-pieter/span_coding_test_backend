class Team:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.losses = 0
        self.league_score = 0

    def win(self):
        self.league_score += 3
        self.wins += 1

    def lose(self):
        self.losses += 1

    def draw(self):
        self.league_score += 1