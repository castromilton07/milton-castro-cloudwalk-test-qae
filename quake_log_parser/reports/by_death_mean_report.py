# Import used to run pytest, without complete path, test doesn't work
# Please comment the last import

# from quake_log_parser.reports.repsort import Report

# Import used to run the program (main.py), with complete path, program
# doesn't work
# Please comment the first import

from reports.report import Report


class ByDeathMeanReport(Report):
    def generate(ranking_by_death_dict):
        report_message = ""
        for index, match in enumerate(ranking_by_death_dict.values()):
            match_num = index + 1
            deaths = match["kills_by_means"]
            report_message += "\n--------------------------------------"
            report_message += f"\n Match: {match_num}"
            report_message += "\n Deaths By Mean:"
            for mean, death_quantity in deaths.items():
                report_message += f"\n    {mean}: {death_quantity}"
        return report_message
