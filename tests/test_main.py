from unittest.mock import patch
from quake_log_parser.main import show_menu


def test_show_menu_options(capsys):
    # validate output in console when show/print menu informations
    def fake_input(prompt=""):
        print(prompt, end=" ")
        return ""
    with patch("builtins.input", fake_input):
        show_menu()
    out, err = capsys.readouterr()
    assert (
        "Select one of the options below:\n 0 - Default report (total kills, players, kills ranking);\n 1 - Report by death mean (kills by means);\n 2 - Complete report;\n 3 - Dictionary/JSON of Default Report;\n 4 - Dictionary/JSON of By Death Mean Report;\n 5 - Exit.\n\n -> "
        in out
    )


def test_show_menu_functions(capsys):
    # execute default report (0) option
    with patch("builtins.input") as mocked_input:
        mocked_input.side_effect = ["0", ""]
        show_menu()
    out, err = capsys.readouterr()
    expected = """
--------------------------------------
 Match: 1
 Total Kills in Match: 0
 Players: Isgalamido
 Ranking:
    Isgalamido: 0
--------------------------------------
 Match: 2
 Total Kills in Match: 11
 Players: Dono da Bola, Isgalamido, Mocinha
 Ranking:
    Isgalamido: -7
    Dono da Bola: 0
    Mocinha: 0
--------------------------------------
 Match: 3
 Total Kills in Match: 4
 Players: Dono da Bola, Isgalamido, Mocinha, Zeh
 Ranking:
    Zeh: -2
    Dono da Bola: -1
    Mocinha: 0
    Isgalamido: 1
--------------------------------------
 Match: 4
 Total Kills in Match: 105
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Zeh
 Ranking:
    Dono da Bola: 9
    Assasinu Credi: 12
    Isgalamido: 19
    Zeh: 20
--------------------------------------
 Match: 5
 Total Kills in Match: 14
 Players: Assasinu Credi, Dono da Bola, Isgalamido, Zeh
 Ranking:
    Assasinu Credi: -1
    Dono da Bola: 0
    Zeh: 1
    Isgalamido: 2
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
    Oootsimo: 21"""
    assert expected in out

    # execute by death mean report (1) option
    with patch("builtins.input") as mocked_input:
        mocked_input.side_effect = ["1", ""]
        show_menu()
    out, err = capsys.readouterr()
    expected = """
--------------------------------------
 Match: 1
 Deaths By Mean:
--------------------------------------
 Match: 2
 Deaths By Mean:
    MOD_TRIGGER_HURT: 7
    MOD_ROCKET_SPLASH: 3
    MOD_FALLING: 1
--------------------------------------
 Match: 3
 Deaths By Mean:
    MOD_TRIGGER_HURT: 2
    MOD_FALLING: 1
    MOD_ROCKET: 1
--------------------------------------
 Match: 4
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
 Deaths By Mean:
    MOD_TRIGGER_HURT: 5
    MOD_ROCKET_SPLASH: 4
    MOD_ROCKET: 4
    MOD_RAILGUN: 1
--------------------------------------
 Match: 6
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
 Deaths By Mean:
    MOD_TRIGGER_HURT: 7
    MOD_RAILGUN: 4
    MOD_ROCKET_SPLASH: 4
    MOD_BFG_SPLASH: 3
    MOD_MACHINEGUN: 1
    MOD_CRUSH: 1
--------------------------------------
 Match: 12
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
 Deaths By Mean:
    MOD_TRIGGER_HURT: 2
    MOD_BFG: 1
    MOD_BFG_SPLASH: 1
    MOD_ROCKET_SPLASH: 1
    MOD_ROCKET: 1
--------------------------------------
 Match: 14
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
 Deaths By Mean:
    MOD_TRIGGER_HURT: 3
--------------------------------------
 Match: 16
 Deaths By Mean:
--------------------------------------
 Match: 17
 Deaths By Mean:
    MOD_TRIGGER_HURT: 6
    MOD_FALLING: 3
    MOD_ROCKET_SPLASH: 2
    MOD_RAILGUN: 2
--------------------------------------
 Match: 18
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 4
    MOD_TRIGGER_HURT: 1
    MOD_FALLING: 1
    MOD_ROCKET: 1
--------------------------------------
 Match: 19
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
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 2
    MOD_ROCKET: 1
--------------------------------------
 Match: 21
 Deaths By Mean:
    MOD_ROCKET_SPLASH: 60
    MOD_ROCKET: 37
    MOD_TRIGGER_HURT: 14
    MOD_RAILGUN: 9
    MOD_SHOTGUN: 4
    MOD_MACHINEGUN: 4
    MOD_FALLING: 3"""
    assert expected in out

    # execute complete report (2) option
    with patch("builtins.input") as mocked_input:
        mocked_input.side_effect = ["2", ""]
        show_menu()
    out, err = capsys.readouterr()
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
    assert expected in out

    # execute dict/json default report (3) option
    with patch("builtins.input") as mocked_input:
        mocked_input.side_effect = ["3", ""]
        show_menu()
    out, err = capsys.readouterr()
    expected = "{'game_1': {'total_kills': 0, 'players': ['Isgalamido'], 'kills': {'Isgalamido': 0}}, 'game_2': {'total_kills': 11, 'players': ['Dono da Bola', 'Isgalamido', 'Mocinha'], 'kills': {'Isgalamido': -7, 'Dono da Bola': 0, 'Mocinha': 0}}, 'game_3': {'total_kills': 4, 'players': ['Dono da Bola', 'Isgalamido', 'Mocinha', 'Zeh'], 'kills': {'Zeh': -2, 'Dono da Bola': -1, 'Mocinha': 0, 'Isgalamido': 1}}, 'game_4': {'total_kills': 105, 'players': ['Assasinu Credi', 'Dono da Bola', 'Isgalamido', 'Zeh'], 'kills': {'Dono da Bola': 9, 'Assasinu Credi': 12, 'Isgalamido': 19, 'Zeh': 20}}, 'game_5': {'total_kills': 14, 'players': ['Assasinu Credi', 'Dono da Bola', 'Isgalamido', 'Zeh'], 'kills': {'Assasinu Credi': -1, 'Dono da Bola': 0, 'Zeh': 1, 'Isgalamido': 2}}, 'game_6': {'total_kills': 29, 'players': ['Assasinu Credi', 'Dono da Bola', 'Fasano Again', 'Isgalamido', 'Mal', 'Maluquinho', 'Oootsimo', 'UnnamedPlayer', 'Zeh'], 'kills': {'Fasano Again': 0, 'Mal': 0, 'Maluquinho': 0, 'UnnamedPlayer': 0, 'Assasinu Credi': 1, 'Dono da Bola': 2, 'Isgalamido': 3, 'Zeh': 7, 'Oootsimo': 8}}, 'game_7': {'total_kills': 130, 'players': ['Assasinu Credi', 'Chessus', 'Chessus!', 'Dono da Bola', 'Isgalamido', 'Mal', 'Oootsimo', 'Zeh'], 'kills': {'Mal': -3, 'Chessus': 0, 'Chessus!': 0, 'Zeh': 8, 'Dono da Bola': 10, 'Isgalamido': 14, 'Assasinu Credi': 19, 'Oootsimo': 20}}, 'game_8': {'total_kills': 89, 'players': ['Assasinu Credi', 'Dono da Bola', 'Isgalamido', 'Mal', 'Oootsimo', 'Zeh'], 'kills': {'Mal': -3, 'Dono da Bola': 1, 'Assasinu Credi': 9, 'Zeh': 12, 'Oootsimo': 15, 'Isgalamido': 20}}, 'game_9': {'total_kills': 67, 'players': ['Assasinu Credi', 'Chessus', 'Chessus!', 'Dono da Bola', 'Isgalamido', 'Mal', 'Oootsimo', 'Zeh'], 'kills': {'Chessus!': 0, 'Dono da Bola': 1, 'Isgalamido': 1, 'Mal': 2, 'Assasinu Credi': 7, 'Chessus': 8, 'Oootsimo': 8, 'Zeh': 12}}, 'game_10': {'total_kills': 60, 'players': ['Assasinu Credi', 'Chessus', 'Dono da Bola', 'Isgalamido', 'Mal', 'Oootsimo', 'Zeh'], 'kills': {'Oootsimo': -1, 'Mal': 1, 'Assasinu Credi': 3, 'Dono da Bola': 3, 'Chessus': 5, 'Isgalamido': 5, 'Zeh': 7}}, 'game_11': {'total_kills': 20, 'players': ['Assasinu Credi', 'Chessus', 'Dono da Bola', 'Isgalamido', 'Mal', 'Oootsimo', 'UnnamedPlayer', 'Zeh'], 'kills': {'Assasinu Credi': -3, 'Dono da Bola': -2, 'Chessus': 0, 'Mal': 0, 'UnnamedPlayer': 0, 'Zeh': 0, 'Isgalamido': 4, 'Oootsimo': 4}}, 'game_12': {'total_kills': 160, 'players': ['Assasinu Credi', 'Chessus', 'Dono da Bola', 'Isgalamido', 'Mal', 'Oootsimo', 'Zeh'], 'kills': {'Mal': -7, 'Dono da Bola': 3, 'Zeh': 11, 'Chessus': 12, 'Oootsimo': 12, 'Assasinu Credi': 18, 'Isgalamido': 24}}, 'game_13': {'total_kills': 6, 'players': ['Assasinu Credi', 'Chessus', 'Dono da Bola', 'Isgalamido', 'Mal', 'Oootsimo', 'Zeh'], 'kills': {'Dono da Bola': -1, 'Isgalamido': -1, 'Assasinu Credi': 0, 'Chessus': 0, 'Mal': 0, 'Oootsimo': 1, 'Zeh': 2}}, 'game_14': {'total_kills': 122, 'players': ['Assasinu Credi', 'Chessus', 'Dono da Bola', 'Isgalamido', 'Mal', 'Oootsimo', 'Zeh'], 'kills': {'Mal': -5, 'Dono da Bola': 1, 'Assasinu Credi': 3, 'Zeh': 4, 'Chessus': 7, 'Oootsimo': 9, 'Isgalamido': 22}}, 'game_15': {'total_kills': 3, 'players': ['Assasinu Credi', 'Dono da Bola', 'Fasano Again', 'Isgalamido', 'Oootsimo', 'Zeh'], 'kills': {'Zeh': -3, 'Assasinu Credi': 0, 'Dono da Bola': 0, 'Fasano Again': 0, 'Isgalamido': 0, 'Oootsimo': 0}}, 'game_16': {'total_kills': 0, 'players': ['Assasinu Credi', 'Dono da Bola', 'Isgalamido', 'Oootsimo', 'Zeh'], 'kills': {'Assasinu Credi': 0, 'Dono da Bola': 0, 'Isgalamido': 0, 'Oootsimo': 0, 'Zeh': 0}}, 'game_17': {'total_kills': 13, 'players': ['Assasinu Credi', 'Dono da Bola', 'Isgalamido', 'Mal', 'Oootsimo', 'UnnamedPlayer', 'Zeh'], 'kills': {'Assasinu Credi': -3, 'Dono da Bola': -2, 'Mal': -1, 'Isgalamido': 0, 'Oootsimo': 0, 'UnnamedPlayer': 0, 'Zeh': 0}}, 'game_18': {'total_kills': 7, 'players': ['Assasinu Credi', 'Dono da Bola', 'Isgalamido', 'Mal', 'Oootsimo', 'Zeh'], 'kills': {'Dono da Bola': -1, 'Mal': -1, 'Oootsimo': 0, 'Isgalamido': 1, 'Assasinu Credi': 2, 'Zeh': 2}}, 'game_19': {'total_kills': 95, 'players': ['Assasinu Credi', 'Dono da Bola', 'Isgalamido', 'Mal', 'Oootsimo', 'Zeh'], 'kills': {'Mal': 2, 'Assasinu Credi': 8, 'Oootsimo': 10, 'Dono da Bola': 12, 'Isgalamido': 13, 'Zeh': 20}}, 'game_20': {'total_kills': 3, 'players': ['Assasinu Credi', 'Dono da Bola', 'Isgalamido', 'Mal', 'Oootsimo', 'Zeh'], 'kills': {'Assasinu Credi': 0, 'Isgalamido': 0, 'Mal': 0, 'Zeh': 0, 'Dono da Bola': 1, 'Oootsimo': 1}}, 'game_21': {'total_kills': 131, 'players': ['Assasinu Credi', 'Dono da Bola', 'Isgalamido', 'Mal', 'Oootsimo', 'Zeh'], 'kills': {'Mal': 6, 'Dono da Bola': 12, 'Assasinu Credi': 16, 'Isgalamido': 17, 'Zeh': 19, 'Oootsimo': 21}}}"
    assert expected in out

    # execute dict/json by death mean repor (4) option
    with patch("builtins.input") as mocked_input:
        mocked_input.side_effect = ["4", ""]
        show_menu()
    out, err = capsys.readouterr()
    expected = "{'game-1': {'kills_by_means': {}}, 'game-2': {'kills_by_means': {'MOD_TRIGGER_HURT': 7, 'MOD_ROCKET_SPLASH': 3, 'MOD_FALLING': 1}}, 'game-3': {'kills_by_means': {'MOD_TRIGGER_HURT': 2, 'MOD_FALLING': 1, 'MOD_ROCKET': 1}}, 'game-4': {'kills_by_means': {'MOD_ROCKET_SPLASH': 51, 'MOD_ROCKET': 20, 'MOD_FALLING': 11, 'MOD_TRIGGER_HURT': 9, 'MOD_RAILGUN': 8, 'MOD_MACHINEGUN': 4, 'MOD_SHOTGUN': 2}}, 'game-5': {'kills_by_means': {'MOD_TRIGGER_HURT': 5, 'MOD_ROCKET_SPLASH': 4, 'MOD_ROCKET': 4, 'MOD_RAILGUN': 1}}, 'game-6': {'kills_by_means': {'MOD_ROCKET_SPLASH': 13, 'MOD_ROCKET': 5, 'MOD_SHOTGUN': 4, 'MOD_TRIGGER_HURT': 3, 'MOD_RAILGUN': 2, 'MOD_MACHINEGUN': 1, 'MOD_FALLING': 1}}, 'game-7': {'kills_by_means': {'MOD_ROCKET_SPLASH': 49, 'MOD_ROCKET': 29, 'MOD_TRIGGER_HURT': 20, 'MOD_MACHINEGUN': 9, 'MOD_RAILGUN': 9, 'MOD_SHOTGUN': 7, 'MOD_FALLING': 7}}, 'game-8': {'kills_by_means': {'MOD_ROCKET_SPLASH': 39, 'MOD_ROCKET': 18, 'MOD_RAILGUN': 12, 'MOD_TRIGGER_HURT': 9, 'MOD_FALLING': 6, 'MOD_MACHINEGUN': 4, 'MOD_SHOTGUN': 1}}, 'game-9': {'kills_by_means': {'MOD_ROCKET_SPLASH': 25, 'MOD_ROCKET': 17, 'MOD_RAILGUN': 10, 'MOD_TRIGGER_HURT': 8, 'MOD_FALLING': 3, 'MOD_MACHINEGUN': 3, 'MOD_SHOTGUN': 1}}, 'game-10': {'kills_by_means': {'MOD_TELEFRAG': 25, 'MOD_TRIGGER_HURT': 17, 'MOD_RAILGUN': 7, 'MOD_ROCKET': 4, 'MOD_BFG': 2, 'MOD_BFG_SPLASH': 2, 'MOD_CRUSH': 1, 'MOD_MACHINEGUN': 1, 'MOD_ROCKET_SPLASH': 1}}, 'game-11': {'kills_by_means': {'MOD_TRIGGER_HURT': 7, 'MOD_RAILGUN': 4, 'MOD_ROCKET_SPLASH': 4, 'MOD_BFG_SPLASH': 3, 'MOD_MACHINEGUN': 1, 'MOD_CRUSH': 1}}, 'game-12': {'kills_by_means': {'MOD_RAILGUN': 38, 'MOD_TRIGGER_HURT': 37, 'MOD_ROCKET_SPLASH': 35, 'MOD_ROCKET': 25, 'MOD_BFG': 8, 'MOD_BFG_SPLASH': 8, 'MOD_MACHINEGUN': 7, 'MOD_FALLING': 2}}, 'game-13': {'kills_by_means': {'MOD_TRIGGER_HURT': 2, 'MOD_BFG': 1, 'MOD_BFG_SPLASH': 1, 'MOD_ROCKET_SPLASH': 1, 'MOD_ROCKET': 1}}, 'game-14': {'kills_by_means': {'MOD_TRIGGER_HURT': 31, 'MOD_ROCKET_SPLASH': 24, 'MOD_ROCKET': 23, 'MOD_RAILGUN': 20, 'MOD_BFG_SPLASH': 10, 'MOD_BFG': 5, 'MOD_FALLING': 5, 'MOD_MACHINEGUN': 4}}, 'game-15': {'kills_by_means': {'MOD_TRIGGER_HURT': 3}}, 'game-16': {'kills_by_means': {}}, 'game-17': {'kills_by_means': {'MOD_TRIGGER_HURT': 6, 'MOD_FALLING': 3, 'MOD_ROCKET_SPLASH': 2, 'MOD_RAILGUN': 2}}, 'game-18': {'kills_by_means': {'MOD_ROCKET_SPLASH': 4, 'MOD_TRIGGER_HURT': 1, 'MOD_FALLING': 1, 'MOD_ROCKET': 1}}, 'game-19': {'kills_by_means': {'MOD_ROCKET_SPLASH': 32, 'MOD_ROCKET': 27, 'MOD_TRIGGER_HURT': 12, 'MOD_RAILGUN': 10, 'MOD_MACHINEGUN': 7, 'MOD_SHOTGUN': 6, 'MOD_FALLING': 1}}, 'game-20': {'kills_by_means': {'MOD_ROCKET_SPLASH': 2, 'MOD_ROCKET': 1}}, 'game-21': {'kills_by_means': {'MOD_ROCKET_SPLASH': 60, 'MOD_ROCKET': 37, 'MOD_TRIGGER_HURT': 14, 'MOD_RAILGUN': 9, 'MOD_SHOTGUN': 4, 'MOD_MACHINEGUN': 4, 'MOD_FALLING': 3}}}"
    assert expected in out

    # execute exit/close (5) option
    with patch("builtins.input") as mocked_input:
        mocked_input.side_effect = ["5", ""]
        show_menu()
    out, err = capsys.readouterr()
    assert "\nTerminating script!\n" in out

    # execute invalid option (range out of 0..5) ex.: 6
    with patch("builtins.input") as mocked_input:
        mocked_input.side_effect = ["6", ""]
        show_menu()
    out, err = capsys.readouterr()
    assert err == "Invalid option\n"
