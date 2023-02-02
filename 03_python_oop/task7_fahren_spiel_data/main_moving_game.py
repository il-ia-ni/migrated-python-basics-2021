"""
Das Skript für das Fahren Spiel: Einstellungen für das Spiel, die Spieler und ihre Fahrzeuge
"""

from driver_class import Driver
from transport_classes import Fahrrad, Auto, AbstractTransport as Verkehrsmittel
from moves_logic import begin_moving_game as play_move
from custom_exceptions import ValidInputError


def main():
    """ Lets user(s) select the game mode

    Creates driver(s) instance(s) based on valid player(s) inputs for name and amount of vehicles

    Adds each created driver object into a list of players

    Calls driver object info-method to display information about the player in console

    calls a function to configure the vehicles of each player

    calls a function with the logic of moving based on Turtle instances from the external script

    :return:
        nothing is returned
    """

    spiel_modus_dict = {
        1: "Single Player",
        2: "Multiplayer"
    }

    fahrzeug_typen = {
        1: "Auto",
        2: "Fahrrad"
    }

    fahrer_props_dict = {
        "name": "",
        "vehicles_amount": 0
    }

    transport_props_dict = {
        "typ": "",
        "marke": ""
    }

    fahrer_objs_list = []

    print("Wähle dir nun das Spielmode: ")
    display_dictionary_options_values(spiel_modus_dict)

    # Bereich für korrekte Eingabe des Spielmodus
    try:
        user_choice = int(input())

        # Bereich für das Singlespieler Modus
        if user_choice == 1:
            areChoicesCorrect = []
            print("Du spielst allein. Konfiguriere nun deinen Fahrer. \n")

            get_user_choices(fahrer_props_dict, areChoicesCorrect)

            if False in areChoicesCorrect:
                raise ValidInputError("Falsche Eingaben. Das Spiel wird beendet.")
            else:
                driver = create_driver(fahrer_props_dict)
                fahrer_objs_list.append(driver)
                print(driver)  # SIEHE __str__ der Klasse Driver! Ändert das Verhalten von print(obj)

                configure_drivers_vehicles(fahrzeug_typen, fahrer_objs_list, transport_props_dict,
                                           areChoicesCorrect)
                if False in areChoicesCorrect:
                    raise ValidInputError("Falsche Eingaben. Das Spiel wird beendet.")
                else:
                    play_move(fahrer_objs_list)


        # Bereich für das Multispieler Modus
        elif user_choice == 2:
            drivers_amount = 0
            print("Du spielst im Multimode (max. 4 Spieler!). Wähle nun, wie viele Fahrer spielen werden. ")

            try:
                drivers_amount = int(input())

                # Bereich für korrekte Eingabe der Spieleranzahl
                if 0 < drivers_amount <= 4:
                    iterator = 0
                    areChoicesCorrect = []

                    print("Konfiguriere nun {} Fahrer und Ihre Fahrzeuge: \n".format(drivers_amount))
                    while iterator < drivers_amount:

                        get_user_choices(fahrer_props_dict, areChoicesCorrect)

                        if False in areChoicesCorrect:
                            break
                        else:
                            driver = create_driver(fahrer_props_dict)
                            fahrer_objs_list.append(driver)

                            print(driver)  # SIEHE __str__ der Klasse Driver! Ändert das Verhalten von print(obj)
                            iterator += 1

                    if False in areChoicesCorrect:
                        raise ValidInputError("Falsche Eingaben sind gefunden. Das Spiel wird beendet.")
                    else:
                        print("Es nehmen folgende Fahrer am Spiel teil: \n")
                        for driver in fahrer_objs_list:
                            print(driver.name, "mit", driver.vehicles_amount, "Fahrzeugen")

                        configure_drivers_vehicles(fahrzeug_typen, fahrer_objs_list, transport_props_dict,
                                                   areChoicesCorrect)

                        if False in areChoicesCorrect:
                            raise ValidInputError("Falsche Eingaben. Das Spiel wird beendet.")
                        else:
                            play_move(fahrer_objs_list)


                # Bereich für inkorrekte Eingaben der Spieleranzahl
                elif isinstance(drivers_amount, int):  # wird nur bei erfolgreicher Umwandlung von str ins int erreicht
                    raise ValidInputError("Inkorrekte Anzahl von Spielern gewählt. Das Spiel wird nun beendet.")

            except Exception as e2:
                if isinstance(e2, ValidInputError):
                    print(e2)
                else:  # für alle andere Fehler (inkl. unerfolgreicher Umwandlung von str ins int)
                    print("Nur gerade positive Zahlen sind erlaubt. Das Spiel wird nun beendet.")

        # Bereich für inkorrekte Eingaben des Spielmodus
        else:  # wird nur bei erfolgreicher Umwandlung von str ins int erreicht
            raise ValidInputError("Bitte nur Option aus der Liste wählen! Das Spiel wird nun beendet.")
    except Exception as e:
        if isinstance(e, ValidInputError):
            print(e)
        else:  # für alle andere Fehler (inkl. unerfolgreiche Umwandlung von str ins int
            print("Nur gerade positive Zahlen für Spielmodus sind erlaubt! Das Spiel wird nun beendet.")


def create_driver(driver_dict: dict):
    """ Creates an object of a driver class from received attributes values within a dictionary

    :param driver_dict:
        a user filled dictionary with driver attributes names as keys and their values

    :return:
        a new driver object
    """

    driver_obj = Driver()  # FRAGE: Warum funktioniert es nicht, wenn die Atribute name und vehicles_amount einfach in
    # Klammern auf Werte aus dem Dictionary angewiesen werden?

    driver_obj.name = driver_dict["name"]  # so funktioniert es aber!
    driver_obj.vehicles_amount = driver_dict["vehicles_amount"]

    return driver_obj


def configure_drivers_vehicles(transport_types_list: list, driver_objs_list: list, vehicle_params_list: list,
                               areChoicesCorrect: bool):
    """ Gets choices of each player for the specs of each of his transports

    Checks if players inputs are correct or stops the game otherwise

    Enters the transport specs received from the player into a list

    Creates a corresponding transport object of either the Class Auto or of the Class Fahrrad

    Calls a method of the player object to add the just-created transport object as player's object's instanced attribute

    In the end displays a summary of all instanced attributes with transport objects for each player

    :param transport_types_list:
        a list of program-defined transport types (Currently only 2: Car & Bike
    :param driver_objs_list:
        a list previously filled by players with their objects of the Driver Class
    :param vehicle_params_list:
        a list to be filled with user choices for parameters of each of his transports
    :param areChoicesCorrect:
        a predefined dictionary to be filled woth bool values to check if any of user inputs are wrong

    :return:
        nothing is returned
    """

    iterator1 = 0

    while iterator1 < len(driver_objs_list) and False not in areChoicesCorrect:
        driver = driver_objs_list[iterator1]
        print(f"\nNun konfiguriert {driver.name} {driver.vehicles_amount} Fahrzeug(e):")

        iterator2 = 1

        while iterator2 <= driver.vehicles_amount:
            print(f"\nBitte wähle nun den Typ deines Fahrzeugs {iterator2} aus der Liste:")
            display_dictionary_options_values(transport_types_list)

            try:
                user_input = int(input())
                if user_input in transport_types_list:
                    areChoicesCorrect.append(True)
                    vehicle_params_list["typ"] = user_input
                else:
                    raise ValidInputError("Falsche Eingabe. Das Fahrzeug konnte nicht erstellt werden")
            except Exception as e:
                print(e)
                areChoicesCorrect.append(False)
                break

            print("Bitte trage nun die Marke deines {}s ein:".format(transport_types_list[vehicle_params_list["typ"]]))
            vehicle_params_list["marke"] = input()

            if vehicle_params_list["typ"] == 1:
                transport = Auto()
                transport.typ = "Auto"
                transport.marke = vehicle_params_list["marke"]
            elif vehicle_params_list["typ"] == 2:
                transport = Fahrrad()
                transport.typ = "Fahrrad"
                transport.marke = vehicle_params_list["marke"]

            driver.set_transport(transport, transport.typ)
            iterator2 += 1

        iterator1 += 1

    for driver in driver_objs_list:
        search_options_list = ("transportAuto1", "transportAuto2", "transportFahrrad1", "transportFahrrad2")
        print("\nInformationen zu Fahrzeug(en) von", driver.name, ":")

        for search_option in search_options_list:
            try:
                getattr(driver, search_option).print_zustand()  # Falls das search_option-Attribut ist nicht im
                # Objekt vorhanden, löst gettatr() ein Exception aus!!!
            except Exception as e:
                pass  # Das Exception wird einfach übersprungen


def get_user_choices(options_dict: dict, areChoicesCorrect: list):
    """ requests from a user a value for each attribute of an object to be created

    fills the dictionary with values

    :param options_dict:
        a predefined dictionary with parameters of a driver object
    :param areChoicesCorrect:
        a predefined dictionary to be filled woth bool values to check if any of user inputs are wrong

    :return:
        nothing is returned
    """

    print(f"Gib den Namen von Fahrer(in) {(Driver.drivers_amount + 1)} ein:")
    options_dict["name"] = input()

    print(
        f"Wie viele Fahrzeuge hat Fahrer(in) {(Driver.drivers_amount + 1)}? \nNur eine positive gerade Zahl (max. 2!):")
    try:
        vehicles_amount = int(input())
        if 0 < vehicles_amount <= 2:
            options_dict["vehicles_amount"] = vehicles_amount
            areChoicesCorrect.append(True)
        elif isinstance(vehicles_amount, int):  # Wird nur bei erfolgreicher Umwandlung von str ins int erreicht
            raise ValidInputError("Es sind maximal 2 Fahrzeuge pro Fahrer erlaubt!")

    except Exception as e:
        areChoicesCorrect.append(False)
        if isinstance(e, ValidInputError):
            print(e)
        else:  # für alle andere Fehler (inkl. unerfolgreicher Umwandlung von str ins int)
            print("Nur gerade positive Zahlen erlaubt!")


def display_dictionary_options_values(options_dict: dict):
    """ prints in console every option from a predefined dictionary in a separate line for improved readability
    :param options_dict:
        a dictionary consisting of an int number for an option and a string for its description
    :return:
        nothing is returned
    """

    for option in options_dict:
        print(f"{option}: {options_dict[option]}")


main()
