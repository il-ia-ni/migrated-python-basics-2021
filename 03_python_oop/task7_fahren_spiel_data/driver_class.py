"""
Das Skript enthält die abstrakte Klasse für alle mennschliche Wesen sowie die echte Klasse Driver für Instanziierung von
mennschlichen Objekten
"""

from abc import ABCMeta, abstractmethod, ABC


class AbstractHuman(metaclass=ABCMeta):  # Human ist nicht ganz richtig als abstrakt zu bezeichnen, aber ich habe es
    # für Wiederholung des Themas so gemacht
    """ Die abstrakte Klasse definiert Hauptparameter für menschliche Unterklassen """

    def __init__(self, name):
        self.__name = name

        @property
        @abstractmethod
        def name(self):
            pass

        @name.setter
        @abstractmethod
        def name(self, new_name):
            pass

    @abstractmethod
    def __str__(self):  # Definiert das Verhalten von print(obj) neu! Anstatt einfach die Cash-Info des Objekts im
        # Arbeitsspeicher aufzulisten, zeigt print() eine individuelle Nachricht an.
        pass


class Driver(AbstractHuman, ABC):
    """ Die echte Klasse definiert Parameter für Spieler(Fahrer)-Instanzen """

    drivers_amount = 0  # FRAGE: SOLLTE man allgemeine Klassenattribute auch in ihren abstrakten Klassen definieren?

    def __init__(self, name="Anonym", vehicles_amount=0, location_x=0, location_y=0, current_speed=0):
        Driver.drivers_amount += 1
        self.vehicles_counter = 0
        self.vehicles_dict = {}
        self.__name = name
        self.__vehicles_amount = vehicles_amount
        self.__location_x = location_x
        self.__location_y = location_y
        self.__current_speed = current_speed

        """ Getters """
        @property
        def name(self):
            return self.__name

        @property
        def vehicles_amount(self):
            return self.__vehicles_amount

        @property
        def location_x(self):
            return self.__location_x

        @property
        def location_y(self):
            return self.__location_y

        @property
        def current_speed(self):
            return self.__current_speed

        """ Setters """
        @name.setter
        def name(self, new_name):
            if isinstance(new_name, str):
                self.__name = new_name
                print("Der Name von Fahrer(in) is erfolgreich auf {} gesetzt".format(self.name))

        @vehicles_amount.setter
        def vehicles_amount(self, new_value):
            if isinstance(new_value, int) and 0 < new_value <= 2:
                self.__vehicles_amount = vehicles_amount
                print("Fahrer(in) {1} hat nun {2} Fahrzeuge".format(self.name, self.vehicles_amount))

        @location_x.setter
        def location_x(self, new_location):
            if isinstance(new_location, int):
                self.__location_x = new_location
                print("Fahrer(in) {1} befindet sich jetzt auf {2} Metern".format(self.name, self.location_x))

        @location_y.setter
        def location_y(self, new_location):
            if isinstance(new_location, int):
                self.__location_y = new_location

        @current_speed.setter
        def current_speed(self, new_speed):
            if isinstance(new_speed, int):
                self.__current_speed = new_speed
                print("Fahrer(in) {1} bewegt sich jetzt mit {2} Kilometer pro Stunde".format(self.name, self.current_speed))

    def set_transport(self, new_transport_obj: object, new_transport_type: str):
        """ Checks if a parameter recieved is indeed an object

        increases a personal counter of a transport number of a driver object

        creates a custom string for a name of an instanced attribute to be created

        sets a new instanced attribute for a driver object with a previously user-configured transport object as value

        adds a name of the newly created object into a dictionary of the drivers vehicles

        :param new_transport_obj:
            A previously user-configured transport object of either Auto or Fahrrad-class
        :param new_transport_type:
            A string value of an attribut "typ" of a "new_transport_obj-object

        :return:
            nothing is returned
        """

        if isinstance(new_transport_obj, object):

            self.vehicles_counter += 1
            transport_obj_name = "transport" + new_transport_type + str(self.vehicles_counter)  # Solche Namengebung
            # von Instanzattributen vorbeugt, dass Objekte bei der Wahl von 2 Autos / 2 Fahrräder überschrieben werden

            setattr(self, transport_obj_name, new_transport_obj)  # erstellt ein Instanzattribut mit vorgegebenem Namen
            # aus einem Transport-Objekt für ein Fahrer-Objekt
            # See: https://stackoverflow.com/questions/2900821/in-python-can-an-object-have-another-object-as-an-attribute

            self.vehicles_dict[self.vehicles_counter] = transport_obj_name

        else:
            raise TypeError("Nur Objekte können dem Fahrer zugewiesen werden")

    def __str__(self):  # Definiert das Verhalten von print(obj) neu! Anstatt einfach die Cash-Info des Objekts im
        # Arbeitsspeicher aufzulisten, zeigt print() eine individuelle Nachricht an.
        return f"Fahrer(in) {self.name} hat dem Spiel mit {self.vehicles_amount} Fahrzeugen beigetreten. \n"

