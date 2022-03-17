from reports.report import Report


class CompleteReport(Report):
    def generate(ranking_dict, ranking_by_death_dict):
        by_death_mean_message_list = list()
        for index, match in enumerate(ranking_by_death_dict.values()):
            match_num = index + 1
            deaths = match["kills_by_means"]
            by_death_mean_message = " Deaths By Mean:"
            for mean, death_quantity in deaths.items():
                by_death_mean_message += f"\n    {mean}: {death_quantity}"
            by_death_mean_message_list.append(by_death_mean_message)
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
            print(by_death_mean_message_list[index])
