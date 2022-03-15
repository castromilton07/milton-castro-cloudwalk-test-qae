from quake_log_parser.reports.by_death_cause_report import ByDeathCauseReport
from quake_log_parser.reports.complete_report import CompleteReport
from quake_log_parser.reports.default_report import DefaultReport
from quake_log_parser.importer.txt_importer import TxtImporter
import sys


menu = """Select one of the options below:
 0 - Default report (total kills, players, kills ranking);
 1 - Report by death cause (kills by means);
 2 - Complete report;
 3 - Exit."""

import_instance = TxtImporter("./quake_log_parser/data/qgames.log")


def option_0():
    report_instance = DefaultReport
    return print(report_instance.generate(import_instance))


def option_1():
    report_instance = ByDeathCauseReport
    return print(report_instance.generate(import_instance))


def option_2():
    report_instance = CompleteReport
    return print(report_instance.generate(import_instance))


def option_3():
    return print("Terminating script\n")


options = {
    "0": option_0,
    "1": option_1,
    "2": option_2,
    "3": option_3,
}


def main():
    sys.stdout.write(menu)
    option = input()
    if option in options.keys():
        return options[option]()
    else:
        sys.stderr.write("Invalid option\n")
