"""
Das Skript ist über abstrakten Klassen in Python sowie über Interfaces
"""

from abc import ABCMeta, abstractmethod, ABC
import pandas as pd

# abc Modul definiert eine Basisabstraktklasse.
# ABCMeta Metaklasse wird jeweiliger abstrakter Klasse assigniert
# abstractmethod wird leeren Methoden / Access Modifieres einer abstrakten Klasse (haben nur PASS in sich) zugewiesen

"""
Vorteile von abstrakten Klassen:
- werden zur Verbeugung falscher / inkorrekter Implementierung von Klassen erstellt
- trennen Interfaces von Implementation => der Code wird besser wartbar
- helfen, Bugs vorzubeugen durch ein strenges "Rezept" für Erstellung von Subklassen
"""

# Erstellung einer abstrakten Klasse:

class AbstractFileClass(metaclass=ABCMeta):
    """
    Es ist nicht möglich, ein Objekt von einer abstrakten Klasse zu instanziieren:
    TypeError: Can't instantiate abstract class AbstactClassCSV with abstract methods display_file_info, file_name, path
    """

    def __init__(self, path, file_name):
        self._path = path
        self._file_name = file_name

        @property  # getter-Decorator
        @abstractmethod  # Decorator zwingt alle Unterklassen, dieses Getter zu implementieren. Sonst wird ein Fehler aufgerufen
        def path(self):
            pass

        @path.setter
        @abstractmethod
        def path(self, new_value):
            pass

        @property
        @abstractmethod
        def file_name(self):
            return

        @file_name.setter
        @abstractmethod
        def file_name(self, new_value):
            return

    @abstractmethod   # Decorator zwingt alle Unterklassen, diese Methode zu implementieren. Sonst wird ein Fehler aufgerufen
    def display_file_info(self):
        pass


# Erstellung einer echten Klasse auf der Basis der absrakten:

class FileGetInfo(AbstractFileClass, ABC):  # AbstractFileClass ist eine direkte Überklassem ABC ist eine SUPERKlasse

    """ Die Klasse stellt eine Zusamenfassung einer Datei dar """

    @property
    def path(self):
        """
        Getter for accessing a value of a file object's path

        :return:
            a value of a protected variable for the file path
        """
        print("Es wird auf den Pfad der Datei zugegriffen...")
        return self._path

    """ 
    Bei Versuch, ein Objekt dieser Klasse nur mit dem obigen Getter zu instanziieren, wird ein Fehler ausgelöst:
    TypeError: Can't instantiate abstract class CSVGetInfo with abstract methods display_summary, file_name
    
    Also, alle weitere Members der AbstractFileClass Klasse müssen implementiert werden:
    """

    @path.setter
    def path(self, new_value):
        """ Setter for defining a new path to a file under a protected variable

        Checks if the received value for a path is valid

        :param new_value:
            a new path to a file object
        :return:
            nothing is returned
        """
        if '/' in new_value:
            self._path = new_value
            print("Der neue Pfad wird gesetzt: {}...".format(new_value))
        else:
            print("Warnung: {} ist kein gültiger Pfad".format(new_value))

    @property
    def file_name(self):
        """
        Getter for accessing a value of a file object's name

        :return:
            a value of a protected variable for the file name
        """
        print("Es wird auf den Namen der Datei zugegriffen...")
        return self._file_name

    @file_name.setter
    def file_name(self, new_value):
        """ Setter for defining a new file name+extension under a protected variable

        Checks if the received value for a name+extension is valid

        :param new_value:
            a new name+extension for a file object

        :return:
            nothing is returned
                """
        if '.' in new_value:
            self._file_name = new_value
            print("Der neue Name wird gesetzt: {}...".format(new_value))
        else:
            print("Warnung: {} ist kein gültiger Name".format(new_value))


def display_summary(self):
    data = pd.read_csv(self._path + self._file_name)
    print(self._file_name)
    print(data.info())


data_scv = FileGetInfo("C://Users/niil02/Documents/github/smsdigital/Azubirepo-Ilia/Aufgabensammlung_Python_0921/Aufgabe5_pandas_und_numpy/data", "data.csv")