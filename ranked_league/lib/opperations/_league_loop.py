
def loop(file, _league):
    for line in file:
        teams = line.split(",")

        teams[0]= teams[0].lstrip().rsplit(" ", 1)
        teams[1]= teams[1].lstrip().rsplit(" ", 1)

        score_1 = int(teams[0][1])
        score_2 = int(teams[1][1])

        if score_1 > score_2:
            _league.trigger_win(teams[0][0])
            _league.trigger_lose(teams[1][0])
        
        elif score_1 == score_2:
            _league.trigger_draw([teams[0][0], teams[1][0]])

        else:
            _league.trigger_win(teams[1][0])
            _league.trigger_lose(teams[0][0])
