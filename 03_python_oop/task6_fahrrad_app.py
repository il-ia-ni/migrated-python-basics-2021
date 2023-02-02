"""
Das Skript enthält die Logik der Anwendung für die Aufgabe Fahrrad
"""

from task7_fahren_spiel_data.transport_classes import Fahrrad
from task7_fahren_spiel_data import custom_exceptions


def main():
    """ creates an object of a bike based on the external class rad_kl

    displays a list of actions options to perform with the bike object

    gets users choices of bike actions options as long as the user wants to keep the app running

    makes corresponding changes to the bike object based on the user choice

    :return:
    nothing is returned
    """

    fahrrad_options_dict = {
        1: "Einen Zahnkranz hochschalten",
        2: "Einen Zahnkranz herunterschalten",
        3: "Ein Ritzel hochschalten",
        4: "Ein Ritzel herunterschalten",
        5: "Den Zustand des Fahrrads wieder anzeigen",
        6: "Die Marke des Fahrrads ändern",
        7: "Die Anzahl der Zahnkränze ändern",
        8: "Die Anzahl der Ritzel ändern"
    }

    fahrrad = Fahrrad()
    fahrrad.print_zustand()

    fahrrad_konfigurieren(fahrrad)

    keep_working = True

    while keep_working:
        user_choice = get_user_choices(fahrrad_options_dict)

        if user_choice in fahrrad_options_dict:
            print(f"Sie haben Option {user_choice} gewählt: {fahrrad_options_dict[user_choice]}")

        fahrrad_aendern(fahrrad, user_choice)

        decision = input(f"Möchten Sie etwas noch mit Ihrem Fahrrad machen? [y / n] \n")
        if decision == "y" or decision == "Y":
            keep_working = True
        else:
            keep_working = False


def fahrrad_konfigurieren(fahrrad: object):
    """ Performs initial configuration of a newly created bike objekt

    Gets user choices for the basic attributes of the bike object

    calls the setters of the bike object to safely set the private attributes

    :param fahrrad:
        an object of a bike containing members from the external class rad_kl

    :return:
        nothing is returned
    """

    fahrrad.typ = "Fahrzeug"

    print("Bitte geben Sie eine Marke Ihres Fahrrads ein: \n")
    fahrrad.marke = input()  # SCHREIBWEISE DES BEFEHLS SICH MERKEN!!!

    print("Bitte geben Sie eine gültige Anzahl von Zahnkränzen Ihres Fahrrads zwischen 1 und 20 ein: \n")
    fahrrad.anz_zahnkraenze = input()

    print("Bitte geben Sie eine gültige Anzahl von Ritzeln Ihres Fahrrads zwischen 1 und 10 ein: \n")
    fahrrad.anz_ritzel = input()

    fahrrad.print_zustand()


def display_dictionary_options_values(options_dict: dict):
    """ prints in console every option and its description from a predefined bike actions operations dictionary
    in a separate line for improved readability
    :param options_dict:
        a dictionary consisting of an int number for an action option and a string for its description
    :return:
        nothing is returned
    """

    for option in options_dict:
        print(f"{option}: {options_dict[option]}")


def get_user_choices(options_dict: dict):
    """ lists each description of the bike actions options in a separate line of the terminal

    requests from a user a bike action option's number

    checks if the received option number is valid

    :param options_dict:
        a predefined main dictionary of numbered bike actions options as keys and their string descriptions as values

    :return:
        an integer value of the valid user choice for the stats analysis option
    """

    display_dictionary_options_values(options_dict)

    try:
        user_response_int = int(input("Was möchten Sie mit Ihrem Fahrrad jetzt machen? \n"))
        if user_response_int in options_dict:
            return user_response_int
        else:
            print("Die gewählte Option existiert nicht. Bitte geben Sie die Nummer der Option erneut.")
    except Exception as e:
        print("Die gewählte Option ist nicht gültig. Bitte versuchen Sie erneut und wählen die Option aus der Liste.")


def fahrrad_aendern(fahrrad: object, user_choice: int):
    """ Performs a certain action with a bike object based on the user choice received

    Displays an updated condition of the bike object

    :param fahrrad:
        an object of a bike containing members from the external class rad_kl

    :param user_choice:
        an integer received from the user choice

    :return:
        nothing is returned
    """

    if user_choice == 1:
        fahrrad.up_zahnkranz()
    elif user_choice == 2:
        fahrrad.down_zahnkranz()
    elif user_choice == 3:
        fahrrad.up_ritzel()
    elif user_choice == 4:
        fahrrad.down_ritzel()
    elif user_choice == 5:
        pass
    elif user_choice == 6:
        print("Bitte geben Sie eine Marke Ihres Fahrrads ein: \n")
        fahrrad.marke = input()
    elif user_choice == 7:
        print("Bitte geben Sie eine gültige Anzahl von Zahnkränzen Ihres Fahrrads zwischen 1 und 20 ein: \n")
        fahrrad.anz_zahnkraenze = input()
    elif user_choice == 8:
        print("Bitte geben Sie eine gültige Anzahl von Ritzeln Ihres Fahrrads zwischen 1 und 10 ein: \n")
        fahrrad.anz_ritzel = input()
    fahrrad.print_zustand()


main()
