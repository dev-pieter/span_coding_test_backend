from lib.classes import _league_class
from lib.opperations import _league_loop

def print_divider():
    print("===============================")

def main():
    League = _league_class.League

    _league = League()

    print_divider()
    print("Process file: Enter txt file name (append the '.txt')")
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

    for idx, league_team in enumerate(_league.sort()) :
        formatted_output = "{0}. {1}, {2} pts".format(idx + 1, league_team[0], league_team[1].league_score)
        print(formatted_output)
                
