from quake_log_parser.importer.importer import Importer


class TxtImporter(Importer):
    def import_data(path):
        if path[-3:] == 'log':
            with open(path) as file:
                return file
        else:
            raise ValueError('Invalid file')
