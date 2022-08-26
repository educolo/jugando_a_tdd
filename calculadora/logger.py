from abc import ABC, abstractmethod


class Logger(ABC):

    def __init__(self, filename='logger.txt'):
        self.__filename = filename

    @property
    def filename(self):
        return self.__filename

    def log(self, message):
        with open(self.filename, 'a') as file:
            coded_message = self.encode_message(message)
            file.write(f'{coded_message}\n')

    @abstractmethod
    def encode_message(self):
        pass


class LoggerJSON(ABC):

