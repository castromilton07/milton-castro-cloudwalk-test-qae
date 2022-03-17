# Import used to run pytest, without complete path, test doesn't work
# Please comment the last import

# from quake_log_parser.reports.report import Report

# Import used to run the program (main.py), with complete path, program
# doesn't work
# Please comment the first import

from reports.report import Report


class DefaultReport(Report):
    def generate(ranking_dict):
        report_message = ""
        for index, match in enumerate(ranking_dict.values()):
            match_num = index + 1
            total_kills = match["total_kills"]
            players = match["players"]
            scores = match["kills"]
            report_message += "\n--------------------------------------"
            report_message += f"\n Match: {match_num}"
            report_message += f"\n Total Kills in Match: {total_kills}"
            report_message += "\n Players: "
            for player_index, player in enumerate(players):
                if player_index == len(players) - 1:
                    report_message += f"{player}"
                else:
                    report_message += f"{player}, "
            report_message += "\n Ranking:"
            for player, score in scores.items():
                report_message += f"\n    {player}: {score}"
        return report_message
