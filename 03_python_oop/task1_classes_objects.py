"""
Dieses Skript enthält Informationen zu Grundlagen des OOPs in Python: Klassen und Objekten
"""

# Vorteile von Klassen: Bug-Prävention, lassen nur einen Test je Klasse schreiben
# Bessere Übersichtlichkeit des Codes => Lesbarkeit & Verständlichkeit
# Vereinfachte Änderung des Codes

import turtle  # turtle ist eine pre-installierte Bibliothek für grafische Darstellung von Daten als Formen / Bilder
                # Siehe https://realpython.com/beginners-guide-python-turtle/


class Figure:  # Klassendefinierung ist immer großgeschrieben
    def __init__(self, sides, name, side_size=100, color='black'):
        # Alle Klassen haben __init__(self, args) Funktion. Sie wird aufgeführt sobald die
        # Klasse initialisiert ist und wird jedes Mal gerufen, wenn ein Objekt der Klasse erstellt wird (aber sie ist
        # KEIN Konstruktor: siehe https://pythonbuch.com/objekte.html#id9 ) und initialisiert die Attribute eines Objekts.
        # SELF ähnelt sich dem THIS in JS / C# und übernimmt alle Eigenschaften der Klasse, sodass ein Objekt vollständig
        # seinen Methoden übergeben wird, ohne die Funktion mit sämtlichen Argumenten schreiben zu müssen
        # Args sind Eigenschaften von Objekten der Klasse, die innerhalb der __init__ bestimmt werden
        # Args können standarde Werte haben (side_size=100)

        self.sides = sides  # die Eigenschaften werden immer so in der __init__ deklariert
        self.name = name
        self.side_size = side_size
        self.color = color
        self.interior_angles_sum = (self.sides - 2) * 180  # Eine Eigenschaft kann auch bei Initialisierung berechnet
        # werden. Solche Eigenschaften gehören nicht in Argumente der __init__ !!!
        self.each_angle = self.interior_angles_sum / self.sides

    def draw_figure(self):  # Deklarierung einer Methode der Klasse (enthält keine Argumente)
        turtle.color(self.color)
        for i in range(self.sides):
            turtle.forward(self.side_size)  # Länge einer Linie
            turtle.right(180 - self.each_angle)  # Ein ÄUßERER Winkel für Abbiegen des Zeichners. (n-2) * 180* / n ist
            # eine Formel für einen INNEREN Winkel eines gleichstelligen Polygons.
        turtle.done()


square = Figure(4, "Square", 70)  # Erstellung (INSTANZIERUNG) eines Objekts der Klasse Figure mit Eigenschaften sides=4 und name=Square
pentagon = Figure(5, "Pentagon", color='red')  # falls nicht alle Argumente eingegeben werden, müssen die Eingenschaften
# mit Namenangaben angegeben werden (color='red')!
hexagon = Figure(6, "Pentagon", 130, color='green')
octagon = Figure(8, "Pentagon", color='blue')

print("A figure", square.name, "has", square.sides, "sides.")  # die Eigenschaften eines Objekts können direkt angesprochen werden
print("A figure", pentagon.name, "has", pentagon.sides, "sides.")

octagon.draw_figure()  # Methoden mit SELF brauchen keine Argumente!!