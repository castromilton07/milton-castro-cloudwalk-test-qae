from abc import ABC, abstractmethod


class Importer(ABC):
    def __init__(self, path):
        self.path = path

    @abstractmethod
    def import_data(path):
        raise NotImplementedError
