from lib.classes import _league_class, _team_class
from lib.opperations import _league_loop

def test_league_sort():
    _league = _league_class.League()

    with open("test_input.txt") as file:
            #Loop text file and populate League
            _league_loop.loop(file, _league)

    test_sort = _league.sort()

    #SORT EXPECTED:
    # 1. Manchester, 6 pts
    # 2. Tarantulas, 6 pts
    # 3. Lions, 5 pts
    # 4. FC Awesome, 1 pts
    # 5. Snakes, 1 pts
    # 6. Grouches, 0 pts
    
    assert [test_sort[0][0], test_sort[0][1].league_score] == ["Manchester", 6]
    assert [test_sort[1][0], test_sort[1][1].league_score] == ["Tarantulas", 6]
    assert [test_sort[2][0], test_sort[2][1].league_score] == ["Lions", 5]
    assert [test_sort[3][0], test_sort[3][1].league_score] == ["FC Awesome", 1]
    assert [test_sort[4][0], test_sort[4][1].league_score] == ["Snakes", 1]
    assert [test_sort[5][0], test_sort[5][1].league_score] == ["Grouches", 0]


def test_match_win():
    _league = _league_class.League()

    _league.trigger_win("TEST")

    assert _league.teams["TEST"].league_score == 3
    assert _league.teams["TEST"].wins == 1

def test_match_lose():
    _league = _league_class.League()

    _league.trigger_lose("TEST")

    assert _league.teams["TEST"].league_score == 0
    assert _league.teams["TEST"].losses == 1

def test_match_draw():
    _league = _league_class.League()

    _league.trigger_draw(["TEST_1", "TEST_2"])

    assert _league.teams["TEST_1"].league_score == 1
    assert _league.teams["TEST_1"].losses == 0
    assert _league.teams["TEST_1"].wins == 0

    assert _league.teams["TEST_2"].league_score == 1
    assert _league.teams["TEST_2"].losses == 0
    assert _league.teams["TEST_2"].wins == 0