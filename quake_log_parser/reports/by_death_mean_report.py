# Import used to run pytest, without complete path, test doesn't work
# Please comment the last import

# from quake_log_parser.reports.report import Report

# Import used to run the program (main.py), with complete path, program
# doesn't work
# Please comment the first import

from reports.report import Report


class ByDeathMeanReport(Report):
    def generate(ranking_by_death_dict):
        for index, match in enumerate(ranking_by_death_dict.values()):
            match_num = index + 1
            deaths = match["kills_by_means"]
            print("--------------------------------------")
            print(f" Match: {match_num}")
            print(" Deaths By Mean:")
            for mean, death_quantity in deaths.items():
                print(f"    {mean}: {death_quantity}")
