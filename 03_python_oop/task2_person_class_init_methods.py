"""
Das Skript enthält Lösungen zu Aufgaben 2-4
"""


class Person:
    people_counter = 0  # ein algemeines Property der KLASSE

    def __init__(self, name="Anonym", lastname="n/a"):
        Person.people_counter += 1  # Für jedes Objekt wird auf eine allgemeine Eigenschaft DER KLASSE zugegriffin.
        # Die Objekte teilen solches Attribut
        self.name = name  # Attribute mit self gehören NUR EINEM Objekt, die werden zwischen Objekten nicht geteilt!
        self.lastname = lastname

    def introduce_myself(self):
        print("Hallo, ich bin", self.name, self.lastname)

    def ask_name(self):
        print("Wie heißt du?")


ilia = Person("Ilia", "Nikolaenko")

samuel = Person("Samuel", "Regier")

phillip = Person("Phillip", "Hänisch")

ilia.introduce_myself()
ilia.ask_name()
samuel.introduce_myself()
samuel.ask_name()
phillip.introduce_myself()