# Import used to run pytest, without complete path, test doesn't work
# Please comment the last import

# from quake_log_parser.reports.report import Report

# Import used to run the program (main.py), with complete path, program
# doesn't work
# Please comment the first import

from reports.report import Report


class DefaultReport(Report):
    def generate(ranking_dict):
        for index, match in enumerate(ranking_dict.values()):
            match_num = index + 1
            total_kills = match["total_kills"]
            players = match["players"]
            scores = match["kills"]
            print("--------------------------------------")
            print(f" Match: {match_num}")
            print(f" Total Kills in Match: {total_kills}")
            print(" Players: ", end="")
            print(*players, sep=", ")
            print(" Ranking:")
            for player, score in scores.items():
                print(f"    {player}: {score}")
