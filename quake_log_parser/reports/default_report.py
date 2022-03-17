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
