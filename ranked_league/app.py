from lib.classes import _league_class
from lib.opperations import _league_loop

def print_divider():
    print("===============================")

def main():
    League = _league_class.League

    _league = League()

    print_divider()
    print("Process file: *Enter file name*")
    print("Exit: ' x '")
    print_divider()

    inputs = input("Command: ")

    if(inputs == "x"):
        exit()

    try:
        with open(inputs) as file:
            #Loop text file and populate League
            print_divider()
            _league_loop.loop(file, _league)
            
    except Exception as e:
        print("ERROR: couldnt find file.")
        print_divider()

    # print(_league.sort())

    for league_team in _league.sort() :
        print("Team: ", league_team[0], ", League score: ", league_team[1].league_score)
                

if __name__ == "__main__":
    while True:
        main()