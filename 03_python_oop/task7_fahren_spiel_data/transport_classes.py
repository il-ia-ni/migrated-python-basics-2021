"""
Das Skript enthält die abstrakte Klasse für alle Fahrzeuge sowie die echten Klassen Fahrrad und Auto für Instanziierung
von Objekten
"""
import random
from abc import ABCMeta, abstractmethod, ABC
import turtle
from custom_exceptions import ValidInputError
import custom_exceptions


class AbstractTransport(metaclass=ABCMeta):
    """ Die abstrakte Klasse definiert Hauptparameter und -Methoden für die Transport-Oberklasse """

    def __init__(self, typ, marke, geschwindigkeit_kmh):
        self.__typ = typ
        self.__marke = marke
        self._geschwindigkeit_kmh = geschwindigkeit_kmh

        @property
        @abstractmethod
        def typ(self):
            pass

        @typ.setter
        @abstractmethod
        def typ(self, new_value):
            pass

        @property
        @abstractmethod
        def marke(self):
            pass

        @typ.setter
        @abstractmethod
        def marke(self, new_value):
            pass

        @property
        @abstractmethod
        def geschwindigkeit_kmh(self):
            pass

        @geschwindigkeit_kmh.setter
        @abstractmethod
        def geschwindigkeit_kmh(self, new_value):
            pass

    @abstractmethod
    def print_zustand(self):  # Es ist gewöhnlich, solche info-Methoden als __str__(self) Methode
            # zu definieren (Grundobjekt-Klasse in Python verfügt über diese standardmäßig). Dann gibt print(obj)
            # dieselbe Info zurück statt einfach die Cash-Info des Objekts im Arbeitsspeicher aufzulisten.
            # SIEHE BEISPIEL HUMAN / DRIVER Klassen
        pass


class Transport(AbstractTransport, ABC):
    """
    Die echte Klasse für alle Transportmittel mit Hauptparameter und -Methoden
    """

    def __init__(self, typ, marke, geschwindigkeit_kmh):
        self.__typ = typ
        self.__marke = marke
        self._geschwindigkeit_kmh = geschwindigkeit_kmh

        """ 
        Getters
        """

        @property
        def typ(self):
            return self.__typ

        @property
        def marke(self):
            return self.__marke

        @property
        def geschwindigkeit_kmh(self):
            return self._geschwindigkeit_kmh

        """ 
        Setters
        """

        @typ.setter
        def typ(self, neuer_typ):
            if isinstance(neuer_typ, str):
                self.__typ = neuer_typ
                print("Der Typ des Transportmittels wurde erfolgreich auf", self.__typ, "gesetzt")
            else:
                raise ValueError("Der Typ Ihres Transportmittels kann nur ein Text sein. Bitte versuchen Sie es erneut")

        @marke.setter
        def marke(self, neue_marke):
            if isinstance(neue_marke, str):
                self.__marke = neue_marke
                print(f"Die Marke des {self.typ}s wurde erfolgreich auf", self.__marke, "gesetzt")
            else:
                raise ValueError("Die Marke Ihres Fahrrads kann nur ein Text sein. Bitte versuchen Sie es erneut")

        @geschwindigkeit_kmh.setter
        def geschwindigkeit_kmh(self, neue_geschwindigkeit):
            if isinstance(neue_geschwindigkeit, int) and 0 > neue_geschwindigkeit < 88:  # PferdGW
                self._geschwindigkeit_kmh = neue_geschwindigkeit
                print(f"Die Geschwindigkeit des {self.typ}s wurde erfolgreich auf", self._geschwindigkeit_kmh, "gesetzt")
            else:
                raise ValidInputError(
                    f"Die Geschwindigkeit Ihres {self.typ}s kann nur eine positive gerade Zahl bis 88 kmh sein. "
                    "Bitte versuchen Sie es erneut")

    def print_zustand(self):  # Es ist gewöhnlich, solche info-Methoden als __str__(self) Methode
        # zu definieren (Grundobjekt-Klasse in Python verfügt über diese standardmäßig). Dann gibt print(obj)
        # dieselbe Info zurück statt einfach die Cash-Info des Objekts im Arbeitsspeicher aufzulisten
        # SIEHE BEISPIEL HUMAN / DRIVER Klassen

        print("Das", self.typ, self.marke, "ist im folgenden Zustand: \n", "gefahrene Geschwindigkeit:",
              self._geschwindigkeit_kmh, "Stundenkilometer \n" )


class Fahrrad(Transport):
    """ Die echte Klasse definiert Parameter und Methoden für Fahrräder-Instanzen """

    def __init__(self, typ="Fahrrad", marke="keine Angabe", geschwindigkeit_kmh=20, anz_zahnkraenze=0, anz_ritzel=0, zahnkranz=1, ritzel=1):
        super().__init__(typ, marke, geschwindigkeit_kmh)

        self._geschwindigkeit_kmh = geschwindigkeit_kmh
        self.__anz_zahnkraenze = anz_zahnkraenze  # Anzahl der Zahnkränze des Fahrrads, positive ganze Zahl
        self.__anz_ritzel = anz_ritzel  # Anzahl der Zahnkränze des Fahrrads, positive ganze Zahl
        self._zahnkranz = zahnkranz  # gegenwärtige Zahnkranz des Fahrrads, positive ganze Zahl
        self._ritzel = ritzel  # gegenwärtiges Ritzel des Fahrrads, positive ganze Zahl

    """ Getters """

    @property  # Wenn wir die vererbten Setter umschreiben wollen, müssen auch die Getter wiederholt werden!
    def geschwindigkeit_kmh(self):
        return self._geschwindigkeit_kmh

    @property
    def anz_zahnkraenze(self):
        return self.__anz_zahnkraenze

    @property
    def anz_ritzel(self):
        return self.__anz_ritzel

    @property
    def zahnkranz(self):
        return self._zahnkranz

    @property
    def ritzel(self):
        return self._ritzel

    """ Setters """

    @geschwindigkeit_kmh.setter  # Das vererbte Setter wird hier für Fahrräder-Objekte umgeschrieben
    def geschwindigkeit_kmh(self, neue_geschwindigkeit):
        if isinstance(neue_geschwindigkeit, int) and 0 > neue_geschwindigkeit < 30:
            self._geschwindigkeit_kmh = neue_geschwindigkeit
            print("Die Geschwindigkeit des Fahrrads wurde erfolgreich auf", self._geschwindigkeit_kmh, "gesetzt")
        else:
            raise ValidInputError("Die Geschwindigkeit Ihres Fahrrads kann nur eine positive gerade Zahl bis 30 kmh sein. "
                             "Bitte versuchen Sie es erneut")

    @anz_zahnkraenze.setter
    def anz_zahnkraenze(self, neue_anzahl):
        try:
            neue_anzahl = int(neue_anzahl)

            if 0 < neue_anzahl <= 20:
                self.__anz_zahnkraenze = neue_anzahl
                print("Die Anzahl der Zahnkränze wurde erfolgreich auf", self.__anz_zahnkraenze, "gesetzt")

            else:  # wird nur bei erfolgreicher Umwandlung von str ins int erreicht
                raise ValidInputError("Die Anzahl der Zahnkränze kann nur zwischen 1 und 20 sein")

        except Exception as e:
            if ValidInputError:
                print(e)
            else:  # für alle Fehler außerthalb der if-Bedingung oben (d.h., unerfolgreiche Umwandlung von str ins int)
                print("Die Anzahl der Ritzel kann nur eine positive ganze Zahl sein")

    @anz_ritzel.setter
    def anz_ritzel(self, neue_anzahl):
        try:
            neue_anzahl = int(neue_anzahl)

            if 0 < neue_anzahl <= 10:
                self.__anz_ritzel = neue_anzahl
                print("Die Anzahl der Ritzel wurde erfolgreich auf", self.__anz_ritzel, "gesetzt")

            else:  # wird nur bei erfolgreicher Umwandlung von str ins int erreicht
                raise ValidInputError("Die Anzahl der Ritzel kann nur zwischen 1 und 10 sein")

        except Exception as e:
            if ValidInputError:
                print(e)
            else:  # für alle Fehler außerthalb der if-Bedingung oben (d.h., unerfolgreiche Umwandlung von str ins int)
                print("Die Anzahl der Ritzel kann nur eine positive ganze Zahl sein")

    @zahnkranz.setter
    def zahnkranz(self, neue_position):
        try:
            neue_position = int(neue_position)

            if 0 < neue_position <= self.__anz_zahnkraenze:
                self._zahnkranz = neue_position
                print("Es wurde der Zahnkranz", self._zahnkranz, "eingelegt")

            elif neue_position <= 0:
                print(f"Es ist bereits der niedrigste Zahnkranz eingelegt")
            elif neue_position > self.__anz_zahnkraenze:
                print(f"Es ist bereits der höchste Zahnkranz eingelegt")

        except TypeError:
            print("Die Position des Zahnkranzes kann nur eine positive ganze Zahl sein")

    @ritzel.setter
    def ritzel(self, neue_position):
        try:
            neue_position = int(neue_position)

            if 0 < neue_position <= self.__anz_ritzel:
                self._ritzel = neue_position
                print("Es wurde das Ritzel", self._ritzel, "eingelegt")

            elif neue_position <= 0:
                print(f"Es ist bereits das niedrigste Ritzel eingelegt")
            elif neue_position > self.__anz_ritzel:
                print(f"Es ist bereits das höchste Ritzel eingelegt")

        except TypeError:
            print("Die Position des Ritzels kann nur eine positive ganze Zahl sein")

    """ Methoden """

    def up_zahnkranz(self):
        print("Es wird versucht, die Kette über den nächsten Zahnkratz zu verschieben...")
        self.zahnkranz += 1

    def down_zahnkranz(self):
        print("Es wird versucht, die Kette über den vorherigen Zahnkratz zu verschieben...")
        self.zahnkranz -= 1

    def up_ritzel(self):
        print("Es wird versucht, die Kette über das nächste Ritzel zu verschieben...")
        self.ritzel += 1

    def down_ritzel(self):
        print("Es wird versucht, die Kette über das vorherige Ritzel zu verschieben...")
        self.ritzel -= 1

    def print_zustand(self):  # die vererbte Methode wird hier umgeschrieben
        zahnkraenze = "o" * self.anz_zahnkraenze
        zahnkraenze_aktiv = zahnkraenze[:(self.zahnkranz - 1)] + "*" + zahnkraenze[self.zahnkranz:]

        ritzel = "o" * self.anz_ritzel
        ritzel_aktiv = ritzel[:(self.ritzel - 1)] + "*" + ritzel[self.ritzel:]

        print("Das", self.typ, self.marke, "ist im folgenden Zustand: \n", zahnkraenze_aktiv, "----", ritzel_aktiv)


class Auto(Transport):
    """ Die echte Klasse definiert Parameter und Methoden für Autos-Instanzen """

    def __init__(self, typ="Auto", marke="keine Angabe", geschwindigkeit_kmh=50, tankinhalt=50, verbrauch_liter_100km=4):
        super().__init__(typ, marke, geschwindigkeit_kmh)

        self._geschwindigkeit_kmh = geschwindigkeit_kmh
        self.__tankinhalt = tankinhalt
        self.__verbrauch_liter_100km = verbrauch_liter_100km

        """ Getters """

        @property  # Wenn wir die vererbten Setter umschreiben wollen, müssen auch die Getter wiederholt werden!
        def geschwindigkeit_kmh(self):
            return self._geschwindigkeit_kmh

        @property
        def tankinhalt(self):
            return self.__tankinhalt

        @property
        def verbrauch_liter_100km(self):
            return self.__verbrauch_liter_100km

        """ Setters """

        @geschwindigkeit_kmh.setter  # Das vererbte Setter wird hier für Fahrräder-Objekte umgeschrieben
        def geschwindigkeit_kmh(self, neue_geschwindigkeit):
            if isinstance(neue_geschwindigkeit, int) and 0 > neue_geschwindigkeit < 120:
                self._geschwindigkeit_kmh = neue_geschwindigkeit
                print("Die Geschwindigkeit des Autos wurde erfolgreich auf", self._geschwindigkeit_kmh, "gesetzt")
            else:
                raise ValidInputError(
                    "Die Geschwindigkeit Ihres Autos kann nur eine positive gerade Zahl bis 120 kmh sein. "
                    "Bitte versuchen Sie es erneut")

        @tankinhalt.setter
        def tankinhalt(self, neuer_tankinhalt):
            if isinstance(neuer_tankinhalt, int) and 30 > neuer_tankinhalt < 100:
                self.__tankinhalt = neuer_tankinhalt
                print("Der Tankinhalt des Autos wurde erfolgreich auf", self.__tankinhalt, "Liter gesetzt")
            else:
                raise ValidInputError(
                    "Der Tankinhalt Ihres Autos kann nur eine positive gerade Zahl zwischen 30 und 100 Liter sein. "
                    "Bitte versuchen Sie es erneut")

        @verbrauch_liter_100km.setter
        def verbrauch_liter_100km(self, neuer_verbrauch):
            if isinstance(neuer_verbrauch, int) and 3 > neuer_verbrauch < 12:
                self.__verbrauch_liter_100km = neuer_verbrauch
                print("Der Verbrauch des Autos wurde erfolgreich auf", self.__verbrauch_liter_100km, " Liter pro 100 km gesetzt")
            else:
                raise ValidInputError(
                    "Der Verbrauch des Autos kann nur eine positive gerade Zahl zwischen 3 und 12 Liter pro 100 km sein. "
                    "Bitte versuchen Sie es erneut")

    def print_zustand(self):  # Die vererbte Methode wird hier umgeschrieben
        print("Das", self.typ, self.marke, "ist im folgenden Zustand: \n", "gefahrene Geschwindigkeit:",
              self._geschwindigkeit_kmh, "Stundenkilometer \n", "aktueller Tankinhalt:", self.__tankinhalt, "Liter \n",
              "aktueller Verbrauch:", self.__verbrauch_liter_100km, "Liter pro 100 km")

