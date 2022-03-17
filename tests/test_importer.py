from quake_log_parser.importer.importer import Importer
from quake_log_parser.importer.txt_importer import TxtImporter
import pytest
import json

with open("tests/mocks/default_ranking_dict.json", mode="r") as file:
    default_dict = json.loads(file.read())

with open("tests/mocks/by_death_ranking_dict.json", mode="r") as file:
    by_death_ranking_dict = json.loads(file.read())


def test_validate_class_txtimporter_is_inheriting_importer():
    assert issubclass(TxtImporter, Importer)


def test_validate_extension_invalid_in_txtimporter():
    with pytest.raises(ValueError, match="Invalid file"):
        assert TxtImporter.import_data('quake_log_parser/data/qgames.csv')


def test_validate_class_txtimporter_create_default_dict_correctly():
    file_log = TxtImporter.import_data("quake_log_parser/data/qgames.log")
    joined_info_to_divide = TxtImporter.prepare_to_divide_by_match(file_log)
    init_lines = joined_info_to_divide[0]
    total_matches = joined_info_to_divide[1]
    log_by_match = TxtImporter.divide_log_by_match(file_log, init_lines, total_matches)
    report = TxtImporter.create_ranking_dict(log_by_match, total_matches)
    TxtImporter.add_score_to_ranking(report, log_by_match, total_matches)
    assert default_dict == report


def test_validate_class_txtimporter_create_by_death_dict_correctly():
    file_log = TxtImporter.import_data("quake_log_parser/data/qgames.log")
    joined_info_to_divide = TxtImporter.prepare_to_divide_by_match(file_log)
    init_lines = joined_info_to_divide[0]
    total_matches = joined_info_to_divide[1]
    log_by_match = TxtImporter.divide_log_by_match(file_log, init_lines, total_matches)
    report = TxtImporter.create_ranking_by_death_dict(log_by_match, total_matches)
    assert by_death_ranking_dict == report
