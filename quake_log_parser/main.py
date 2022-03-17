from reports.by_death_mean_report import ByDeathMeanReport
from reports.complete_report import CompleteReport
from reports.default_report import DefaultReport
from importer.txt_importer import TxtImporter
import sys


menu = """
Select one of the options below:
 0 - Default report (total kills, players, kills ranking);
 1 - Report by death mean (kills by means);
 2 - Complete report;
 3 - Dictionary/JSON of Default Report;
 4 - Dictionary/JSON of By Death Mean Report;
 5 - Exit.\n
 -> """

import_instance = TxtImporter

file_log = import_instance.import_data("./quake_log_parser/data/qgames.log")
joined_info_to_divide = import_instance.prepare_to_divide_by_match(file_log)
init_lines = joined_info_to_divide[0]
total_matches = joined_info_to_divide[1]
log_by_match = import_instance.divide_log_by_match(file_log, init_lines, total_matches)
ranking = import_instance.create_ranking_dict(log_by_match, total_matches)
import_instance.add_score_to_ranking(ranking, log_by_match, total_matches)
ranking_by_death = import_instance.create_ranking_by_death_dict(log_by_match, total_matches)


def option_0():
    report_instance = DefaultReport
    report_instance.generate(ranking)


def option_1():
    report_instance = ByDeathMeanReport
    report_instance.generate(ranking_by_death)


def option_2():
    report_instance = CompleteReport
    report_instance.generate(ranking, ranking_by_death)


def option_3():
    return(print(f"\n{ranking}\n"))


def option_4():
    return(print(f"\n{ranking_by_death}\n"))


def option_5():
    return print("\nTerminating script!\n")


options = {
    "0": option_0,
    "1": option_1,
    "2": option_2,
    "3": option_3,
    "4": option_4,
    "5": option_5,
}


if __name__ == "__main__":
    sys.stdout.write(menu)
    option = input()
    if option in options.keys():
        options[option]()
    else:
        sys.stderr.write("Invalid option\n")
