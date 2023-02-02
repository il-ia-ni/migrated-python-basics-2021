"""
Das Skript enthält Lösungen zu Aufgabe 6
"""

# Parent class == Oberklasse, Superklasse oder Basisklasse

# Child class == Unterklasse, abgeleitete Klasse oder Subklasse


class Fahrzeug:
    def __init__(self, marke : str, hubraum: float = 'Nicht bekannt', leistung: int = 'Nicht bekannt'):
        self.marke = marke
        self.hubraum = hubraum
        self.leistung = leistung

    def get_infos(self):
        return "Marke: " + self.marke + ", Hubraum: " + str(self.hubraum) + ", Leistung: " + str(self.leistung)


class Lastwagen(Fahrzeug):  # Für Erstellung einer Unterklasse wird der Name der Unterklasse als Parameter eingegeben
    pass
    # Das Keyword PASS muss immer eingegeben werden, falls keine weitere neue Members der Unterklasse
    # hinzugefügt werden (alles wird aus der Superklasse so wie es ist übernommen ("vererbt") ). In diesem
    # Fall die __init__() function wird auch von der Oberklasse übernommen!

    """ Alternative zum PASS für Vererbung der __init__() von der Oberklasse:
        def __init__(self, marke, hubraum="n/a", leistung="n/a"):
            Fahrzeug.__init__(marke, hubraum, leistung)
            
        OR 
        
        def __init__(self, marke, hubraum="n/a", leistung="n/a"):
            super().__init__(marke, hubraum, leistung)  
            
        mehr zu SUPER(): siehe unten
    """


class Personenwagen(Fahrzeug):
    def __init__(self, marke: str, hubraum: float = "n/a", leistung: int = "n/a", anz_plaetze: int = 5):
        super().__init__(marke, hubraum, leistung)  # Um Code Dublizität zu vermeiden, können alle
        # Methoden & Eigenschaften der Oberklasse, ohne deren Namen erwähnen zu müssen, mithilfe der SUPER() Funktion
        # aufgerufen werden.
        #
        # Man MUSS NICHT die __init__() der Oberklasse vererben! Dann müssen aber alle Eigenschaften aus der Superklasse
        # in der __init__() der Unterklasse wiederholt eingegeben werden

        self.anz_plaetze = anz_plaetze  # zusätzlicher Parameter der Unterklasse

    def beep(self):  # zusätzliche Methode der Unterklasse
        print(self.marke, "PKW hupt: BEEP!")

    def get_infos(self):  # Methode der Unterklasse, die die durch SUPER()-Funktion vererbte Methode mit gleichem Namen
        # der Superklasse ÜBERSCHRIEBEN HAT
        return "Marke: " + self.marke + ", Hubraum: " + str(self.hubraum) + ", Leistung: " + str(self.leistung) + \
               ", Anzahl von Sitzplätzen: " + str(self.anz_plaetze)


auto = Fahrzeug("Fiat")  # Objekt der Basisklasse instanziiert
print("Daten des Fahrzeugs:", auto.get_infos())

lkw = Lastwagen("Fiat Ducato", 2.2, 100)  # Objekt der Unterklasse mit allen Eigenschaften vererbt instanziiert
print("Daten des LKW:", lkw.get_infos())

pkw = Personenwagen("Fiat", 1.1, 65)  # Objekt der Unterklasse instanziiert
pkw.beep()
print("Daten des PKW:", pkw.get_infos())
