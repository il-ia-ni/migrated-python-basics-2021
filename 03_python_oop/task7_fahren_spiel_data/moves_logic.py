""" Das Skript steuert die Logik des Fahrens von Fahrer und ihren Fahrzeugen mithilfe von Turtle Package und dessen
Objekten """

import random
import turtle

players_colors_set = {'red', 'green', 'blue', 'cyan', 'magenta', 'black', 'yellow', 'pink', 'brown'}  # Ich verwende
# hier ein Set (unindexierten, ungeordneten Werte), da die für eine turtle Figur random gewählte Farbe wird danach
# aus dem Set entfernt, damit weitere Figuren diese Farbe nicht mehr bekommen. Das Löschen der Farbe im Set erfolgt
# durch das String anstatt die Indexnummer bei Tuples oder Lists (siehe Methode prepare_figures())!

drivers_shapes_list = []


def begin_moving_game(drivers_objs_list: list):
    """ Gets an int from the player(s) for the distance to be driven

    calls a function that lets player(s) choose the transport they start the drive and sets their initial location and speeds

    creates a turtle space (plot) in accordance with the distance to be driven

    calls a function that creates turtle objects from the drivers objects list received + fills the global turtles objects list

    calls a function that makes all turtles objects in the global turtles objects list move in the turtle space

    quits the turtle space on user click

    :param drivers_objs_list:
        a list with objects of the Driver class that already have their transports objectsas attributes

    :return:
        nothing is returned

    """

    print("\nSpieler und Fahrzeuge sind nun für das Spiel bereit!\n")

    print("Welche Strecke sollen die Fahrer nun befahren? Bitte in Metern eingeben:")
    x_distance = int(input())

    prepare_players(drivers_objs_list)

    # TODO: Umsteigen-Funktionalität noch vorgesehen
    # print("Wo hast der Fahrer {} sein anderes Fahrzeug {} eingeparkt? Bitte Eingabe in Meter eingeben:")

    game_window = turtle.Screen()
    game_window.title("Fahren Spiel")
    game_window.setup(.90, 500)  # floats = % von Displaygröße, ints = Größe in Pixeln
    game_window.setworldcoordinates(0, 0, (x_distance + 10), 100)  # y-Achse enthält derzeit max. 4 Spieler mit 20px Abständen

    prepare_figures(drivers_objs_list)

    start_moving_figures(drivers_shapes_list, x_distance)

    turtle.exitonclick()


def prepare_players(drivers_objs_list: list):
    """ Gives every Driver Object initial X-asis starting value (0)

    Gives every Driver Object an always increasing Y-asis starting value (prev+20)

    Asks player(s) to choose one of their configured transport objects to begin the drive with

    Gives each player a current_speed attribute in accordance with the selected transport

    :param drivers_objs_list:
        a list with objects of the Driver class that already have their transports objectsas attributes

    :return:
        nothing is returned
    """

    align_over_y = 20

    for driver_obj in drivers_objs_list:

        driver_obj.location_x = 0  # gibt dem Spieler-Objekt Position auf der x-Achse (alle fangen auf 0 an)
        driver_obj.location_y = align_over_y  # gibt dem Spieler-Objekt Position auf der y-Achse

        print("Mit welchem Fahrzeug beginnt Fahrer(in) {} seine Fahrt?\n".format(driver_obj.name))
        for option in driver_obj.vehicles_dict:
            print(f"{option}: {driver_obj.vehicles_dict[option]}")
        try:
            choice = int(input())

            if choice == 1:
                transport_selected = driver_obj.vehicles_dict[1]
            elif choice == 2:
                transport_selected = driver_obj.vehicles_dict[2]

            transport_obj = getattr(driver_obj, transport_selected)  # gibt ein bestimmtes Fahrzeugsobjekt zurück
            speed = transport_obj._geschwindigkeit_kmh  # HELP NEEDED: Wenn ein Objekt mithilfe von getattr
            # zurückgegeben wird, kann mann seine getters nicht mehr verwenden! Man bekommt Fehlermeldung "Objekt
            # Auto hat kein Attribut "geschwindigkeit_kmh".
            # Im Debugger sieht man aber, dass die Attribute immer noch
            # drin sind... Ich konnte nichts dazu finden :(

            driver_obj.current_speed = speed

            # FRAGE: Kann man hier noch eine ELIF für z.B. ESC Taste gedrückt machen (Spiel beendet bzw. Spieler
            # fährt nicht)?

            align_over_y += 20  # Nächster Spieler wird 20 Pixel höher auf der y-Achse untergebracht

        except Exception as e:
            print(e)
            print("Du hast die Option falsch eingegeben! Versuche es noch einmal!\n")
            prepare_players(drivers_objs_list)  # Ich habe mich hier auf Rekursion entschieden, da es hier nicht fair
            # wäre, das Spiel zu beenden.


def prepare_figures(drivers_objs_list: list):
    """ For each fully prepared driver object in the list creates corresponding turtle objects

    adds each created turtle object into the global turtle objects list

    :param drivers_objs_list:
        a list with objects of the Driver class that already have their transports objectsas attributes

    :return:
        nothing is returned
    """

    global drivers_shapes_list

    for driver_obj in drivers_objs_list:

        global players_colors_set
        colors_list = list(players_colors_set)

        random_color_str = random.choice(colors_list)
        players_colors_set.remove(random_color_str)

        # Alles ist hier zu finden @ https://docs.python.org/3/library/turtle.html
        driver_shape = turtle.Turtle()
        driver_shape.sety(driver_obj.location_y)  # Platziert das Shape jeweiliges Fahrers entlang der y-Achse
        driver_shape.showturtle()
        driver_shape.pendown()  # draws when moving
        driver_shape.shape("circle")
        driver_shape.color(random_color_str)
        driver_shape.pencolor(random_color_str)

        # TODO: Geschwindigkeiten von Transporten eingeben zu können (Bei Transporten Konfiguration?) + Turtle Animation
        #  Speed entsprechend anzupassen (muss aber immer zw 1 und 10 liegen!)
        if driver_obj.current_speed <= 30:  # Fahrrad Bereich
            driver_shape.speed(2)  # definiert nur Draw-Animation GW!!!

        elif 30 > driver_obj.current_speed <= 50:  # Auto:innerorts Bereich :)
            driver_shape.speed(3)
        elif 80 > driver_obj.current_speed <= 120:  # Auto:außerorts Bereich :)
            driver_shape.speed(4)

        drivers_shapes_list.append(driver_shape)  # TODO: ALTERNATIVE: place delayed move functions here?


def start_moving_figures(shapes_list: list, distance_2_go: int):
    """

    :param shapes_list:
        global list of created turtle objects for each of the driver objects

    :param distance_2_go:
        a user-defined int for the distance to be driven by all turtle objekts aka drivers objects

    :return:
        nothing is returned
    """

    for shape in shapes_list:
        shape.forward(distance_2_go)

        # TODO: As for now, I couldn't do the simultaneous move of Figures, since "for in" contents are being called one
        #  after the other. Turtle package does have a function .ontimer(func(), delay_ms), but I couldn't make it work yet
        # More @ https://stackoverflow.com/questions/32414431/python-move-turtles-simultaneously
        # @ https://stackoverflow.com/questions/39879410/how-do-you-make-two-turtles-draw-at-once-in-python
