from lib.classes import _team_class

class League:
    def __init__(self):
        self.teams = {}

    def trigger_win(self, name):
        try:
            self.teams.get(name).win()
        
        except:
            new_team = _team_class.Team(name)
            new_team.win()
            self.teams[name] = new_team

    def trigger_lose(self, name):
        try:
            self.teams.get(name).lose()
        
        except:
            new_team = _team_class.Team(name)
            new_team.lose()
            self.teams[name] = new_team

    def trigger_draw(self, draw_teams):
        for name in draw_teams:
            try:
                self.teams.get(name).draw()

            except:
                new_team = _team_class.Team(name)
                new_team.draw()
                self.teams[name] = new_team

    def sort(self):
        #sort teams by name (ASC)
        name_sort = sorted(self.teams.items(), key=lambda x: x[1].name, reverse=False)
        #return sorted teams by score (DESC)
        return sorted(name_sort ,key=lambda x: x[1].league_score, reverse=True)