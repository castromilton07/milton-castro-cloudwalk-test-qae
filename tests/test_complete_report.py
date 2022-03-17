from quake_log_parser.reports.complete_report import CompleteReport
import json
import pytest

with open("tests/mocks/default_ranking_dict.json", mode="r") as file:
    default_dict = json.loads(file.read())

with open("tests/mocks/by_death_ranking_dict.json", mode="r") as file:
    by_death_dict = json.loads(file.read())


@pytest.fixture
def default_dict_fixture():
    return default_dict


@pytest.fixture
def by_death_dict_fixture():
    return by_death_dict


def test_validate_complete_report_return_match_number_correctly(default_dict_fixture, by_death_dict_fixture):
    report = CompleteReport.generate(default_dict_fixture, by_death_dict_fixture)
    expected = " Match: 21"
    assert expected in report


def test_validate_complete_report_return_total_kills_correctly(default_dict_fixture, by_death_dict_fixture):
    report = CompleteReport.generate(default_dict_fixture, by_death_dict_fixture)
    expected = " Total Kills in Match: 131"
    assert expected in report


def test_validate_complete_report_return_players_correctly(default_dict_fixture, by_death_dict_fixture):
    report = CompleteReport.generate(default_dict_fixture, by_death_dict_fixture)
    expected = " Players: Assasinu Credi, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh"
    assert expected in report


def test_validate_complete_report_return_ranking_correctly(default_dict_fixture, by_death_dict_fixture):
    report = CompleteReport.generate(default_dict_fixture, by_death_dict_fixture)
    expected = "Ranking:\n    Mal: 6\n    Dono da Bola: 12\n    Assasinu Credi: 16\n    Isgalamido: 17\n    Zeh: 19\n    Oootsimo: 21"
    assert expected in report


def test_validate_complete_report_return_death_by_mean_correctly(default_dict_fixture, by_death_dict_fixture):
    report = CompleteReport.generate(default_dict_fixture, by_death_dict_fixture)
    expected = " Deaths By Mean:\n    MOD_ROCKET_SPLASH: 60\n    MOD_ROCKET: 37\n    MOD_TRIGGER_HURT: 14\n    MOD_RAILGUN: 9\n    MOD_SHOTGUN: 4\n    MOD_MACHINEGUN: 4\n    MOD_FALLING: 3"
    assert expected in report


def test_validate_complete_report_return_correct_format(default_dict_fixture, by_death_dict_fixture):
    report = CompleteReport.generate(default_dict_fixture, by_death_dict_fixture)
    expected = """
--------------------------------------
 Match: 1
 Total Kills in Match: 0
 Players: Isgalamido
 Ranking:
    Isgalamido: 0
 Deaths By Mean:
--------------------------------------
 Match: 2
 Total Kills in Match: 11
 Players: Dono da Bola, Isgalamido, Mocinha
 Ranking:
    Isgalamido: -7
    Dono da Bola: 0
    Mocinha: 0
 Deaths By Mean:
    MOD_TRIGGER_HURT: 7
    MOD_ROCKET_SPLASH: 3
    MOD_FALLING: 1
--------------------------------------
 Match: 3
 Total Kills in Match: 4
 Players: Dono da Bola, Isgalamido, Mocinha, Zeh
 Ranking:
    Zeh: -2
    Dono da Bola: -1
    Mocinha: 0
    Isgalamido: 1
 Deaths By Mean:
    MOD_TRIGGER_HURT: 2
    MOD_FALLING: 1
    MOD_ROCKET: 1
--------------------------------------
 Match: 4
 Total Kills in Match: 105
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Zeh
 Ranking:
    Dono da Bola: 9
    Assasinu Credi: 12
    Isgalamido: 19
    Zeh: 20
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 51
    MOD_ROCKET: 20
    MOD_FALLING: 11
    MOD_TRIGGER_HURT: 9
    MOD_RAILGUN: 8
    MOD_MACHINEGUN: 4
    MOD_SHOTGUN: 2
--------------------------------------
 Match: 5
 Total Kills in Match: 14
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Zeh
 Ranking:
    Assasinu Credi: -1
    Dono da Bola: 0
    Zeh: 1
    Isgalamido: 2
 Deaths By Mean:
    MOD_TRIGGER_HURT: 5
    MOD_ROCKET_SPLASH: 4
    MOD_ROCKET: 4
    MOD_RAILGUN: 1
--------------------------------------
 Match: 6
 Total Kills in Match: 29
 Players: Assasinu Credi, Dono da Bola, Fasano Again, Isgalamido, Mal, Maluquinho, Oootsimo, UnnamedPlayer, Zeh
 Ranking:
    Fasano Again: 0
    Mal: 0
    Maluquinho: 0
    UnnamedPlayer: 0
    Assasinu Credi: 1
    Dono da Bola: 2
    Isgalamido: 3
    Zeh: 7
    Oootsimo: 8
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 13
    MOD_ROCKET: 5
    MOD_SHOTGUN: 4
    MOD_TRIGGER_HURT: 3
    MOD_RAILGUN: 2
    MOD_MACHINEGUN: 1
    MOD_FALLING: 1
--------------------------------------
 Match: 7
 Total Kills in Match: 130
 Players: Assasinu Credi, Chessus, Chessus!, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Mal: -3
    Chessus: 0
    Chessus!: 0
    Zeh: 8
    Dono da Bola: 10
    Isgalamido: 14
    Assasinu Credi: 19
    Oootsimo: 20
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 49
    MOD_ROCKET: 29
    MOD_TRIGGER_HURT: 20
    MOD_MACHINEGUN: 9
    MOD_RAILGUN: 9
    MOD_SHOTGUN: 7
    MOD_FALLING: 7
--------------------------------------
 Match: 8
 Total Kills in Match: 89
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Mal: -3
    Dono da Bola: 1
    Assasinu Credi: 9
    Zeh: 12
    Oootsimo: 15
    Isgalamido: 20
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 39
    MOD_ROCKET: 18
    MOD_RAILGUN: 12
    MOD_TRIGGER_HURT: 9
    MOD_FALLING: 6
    MOD_MACHINEGUN: 4
    MOD_SHOTGUN: 1
--------------------------------------
 Match: 9
 Total Kills in Match: 67
 Players: Assasinu Credi, Chessus, Chessus!, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Chessus!: 0
    Dono da Bola: 1
    Isgalamido: 1
    Mal: 2
    Assasinu Credi: 7
    Chessus: 8
    Oootsimo: 8
    Zeh: 12
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 25
    MOD_ROCKET: 17
    MOD_RAILGUN: 10
    MOD_TRIGGER_HURT: 8
    MOD_FALLING: 3
    MOD_MACHINEGUN: 3
    MOD_SHOTGUN: 1
--------------------------------------
 Match: 10
 Total Kills in Match: 60
 Players: Assasinu Credi, Chessus, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Oootsimo: -1
    Mal: 1
    Assasinu Credi: 3
    Dono da Bola: 3
    Chessus: 5
    Isgalamido: 5
    Zeh: 7
 Deaths By Mean:
    MOD_TELEFRAG: 25
    MOD_TRIGGER_HURT: 17
    MOD_RAILGUN: 7
    MOD_ROCKET: 4
    MOD_BFG: 2
    MOD_BFG_SPLASH: 2
    MOD_CRUSH: 1
    MOD_MACHINEGUN: 1
    MOD_ROCKET_SPLASH: 1
--------------------------------------
 Match: 11
 Total Kills in Match: 20
 Players: Assasinu Credi, Chessus, Dono da Bola, Isgalamido, Mal, Oootsimo, UnnamedPlayer, Zeh
 Ranking:
    Assasinu Credi: -3
    Dono da Bola: -2
    Chessus: 0
    Mal: 0
    UnnamedPlayer: 0
    Zeh: 0
    Isgalamido: 4
    Oootsimo: 4
 Deaths By Mean:
    MOD_TRIGGER_HURT: 7
    MOD_RAILGUN: 4
    MOD_ROCKET_SPLASH: 4
    MOD_BFG_SPLASH: 3
    MOD_MACHINEGUN: 1
    MOD_CRUSH: 1
--------------------------------------
 Match: 12
 Total Kills in Match: 160
 Players: Assasinu Credi, Chessus, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Mal: -7
    Dono da Bola: 3
    Zeh: 11
    Chessus: 12
    Oootsimo: 12
    Assasinu Credi: 18
    Isgalamido: 24
 Deaths By Mean:
    MOD_RAILGUN: 38
    MOD_TRIGGER_HURT: 37
    MOD_ROCKET_SPLASH: 35
    MOD_ROCKET: 25
    MOD_BFG: 8
    MOD_BFG_SPLASH: 8
    MOD_MACHINEGUN: 7
    MOD_FALLING: 2
--------------------------------------
 Match: 13
 Total Kills in Match: 6
 Players: Assasinu Credi, Chessus, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Dono da Bola: -1
    Isgalamido: -1
    Assasinu Credi: 0
    Chessus: 0
    Mal: 0
    Oootsimo: 1
    Zeh: 2
 Deaths By Mean:
    MOD_TRIGGER_HURT: 2
    MOD_BFG: 1
    MOD_BFG_SPLASH: 1
    MOD_ROCKET_SPLASH: 1
    MOD_ROCKET: 1
--------------------------------------
 Match: 14
 Total Kills in Match: 122
 Players: Assasinu Credi, Chessus, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Mal: -5
    Dono da Bola: 1
    Assasinu Credi: 3
    Zeh: 4
    Chessus: 7
    Oootsimo: 9
    Isgalamido: 22
 Deaths By Mean:
    MOD_TRIGGER_HURT: 31
    MOD_ROCKET_SPLASH: 24
    MOD_ROCKET: 23
    MOD_RAILGUN: 20
    MOD_BFG_SPLASH: 10
    MOD_BFG: 5
    MOD_FALLING: 5
    MOD_MACHINEGUN: 4
--------------------------------------
 Match: 15
 Total Kills in Match: 3
 Players: Assasinu Credi, Dono da Bola, Fasano Again, Isgalamido, Oootsimo, Zeh
 Ranking:
    Zeh: -3
    Assasinu Credi: 0
    Dono da Bola: 0
    Fasano Again: 0
    Isgalamido: 0
    Oootsimo: 0
 Deaths By Mean:
    MOD_TRIGGER_HURT: 3
--------------------------------------
 Match: 16
 Total Kills in Match: 0
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Oootsimo, Zeh
 Ranking:
    Assasinu Credi: 0
    Dono da Bola: 0
    Isgalamido: 0
    Oootsimo: 0
    Zeh: 0
 Deaths By Mean:
--------------------------------------
 Match: 17
 Total Kills in Match: 13
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Mal, Oootsimo, UnnamedPlayer, Zeh
 Ranking:
    Assasinu Credi: -3
    Dono da Bola: -2
    Mal: -1
    Isgalamido: 0
    Oootsimo: 0
    UnnamedPlayer: 0
    Zeh: 0
 Deaths By Mean:
    MOD_TRIGGER_HURT: 6
    MOD_FALLING: 3
    MOD_ROCKET_SPLASH: 2
    MOD_RAILGUN: 2
--------------------------------------
 Match: 18
 Total Kills in Match: 7
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Dono da Bola: -1
    Mal: -1
    Oootsimo: 0
    Isgalamido: 1
    Assasinu Credi: 2
    Zeh: 2
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 4
    MOD_TRIGGER_HURT: 1
    MOD_FALLING: 1
    MOD_ROCKET: 1
--------------------------------------
 Match: 19
 Total Kills in Match: 95
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Mal: 2
    Assasinu Credi: 8
    Oootsimo: 10
    Dono da Bola: 12
    Isgalamido: 13
    Zeh: 20
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 32
    MOD_ROCKET: 27
    MOD_TRIGGER_HURT: 12
    MOD_RAILGUN: 10
    MOD_MACHINEGUN: 7
    MOD_SHOTGUN: 6
    MOD_FALLING: 1
--------------------------------------
 Match: 20
 Total Kills in Match: 3
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Assasinu Credi: 0
    Isgalamido: 0
    Mal: 0
    Zeh: 0
    Dono da Bola: 1
    Oootsimo: 1
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 2
    MOD_ROCKET: 1
--------------------------------------
 Match: 21
 Total Kills in Match: 131
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Mal, Oootsimo, Zeh
 Ranking:
    Mal: 6
    Dono da Bola: 12
    Assasinu Credi: 16
    Isgalamido: 17
    Zeh: 19
    Oootsimo: 21
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 60
    MOD_ROCKET: 37
    MOD_TRIGGER_HURT: 14
    MOD_RAILGUN: 9
    MOD_SHOTGUN: 4
    MOD_MACHINEGUN: 4
    MOD_FALLING: 3"""
    assert expected == report
