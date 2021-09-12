from lib import _league_class

def main():
    League = _league_class.League

    _league = League()

    inputs = input("Enter name of input file: ")

    with open(inputs) as file:
        for line in file:

            teams = line.split(",")

            teams[0]= teams[0].lstrip().split(" ")
            teams[1]= teams[1].lstrip().split(" ")

            if teams[0][1] > teams[1][1]:
                _league.trigger_win(teams[0][0])
                _league.trigger_lose(teams[1][0])
            
            elif teams[0][1] == teams[1][1]:
                _league.trigger_draw([teams[0][0], teams[1][0]])

            else:
                _league.trigger_win(teams[1][0])
                _league.trigger_lose(teams[0][0])

    # print(_league.teams)

    for league_team in _league.teams :
        print("Team: ", _league.teams[league_team].name, "|| League score: ", _league.teams[league_team].league_score)
                



if __name__ == "__main__":
    main()