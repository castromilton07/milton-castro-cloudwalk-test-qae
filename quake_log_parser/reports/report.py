from abc import ABC, abstractmethod


class Report(ABC):
    def __init__(self, imported_log):
        self.log = imported_log

    @abstractmethod
    def generate(imported_log):
        raise NotImplementedError
