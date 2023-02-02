"""
This script converts a temperature value from one unit system to the other according to a user's options selection
"""

import task4_temperature_conversions as temperature_formulas


def main():
    """Stores all available temperature conversion options within a dictionary

    Calls all logic-defining functions of the programme to fill user-defined variables and perform conversions

    Stores user choices (conversion option; initial temperature) within a dictionary

    Stores an initial and final (converted) temperatures within two integers

    Loops temperature conversions until the user makes the decision to stop the programme

    Resets all user-defined variables upon receiving a choice of the user to perform a next loop

    :return:
        nothing is returned
    """
    keep_working = True

    temp_conversions_dict = {
        1: "Umrechnung von Celsius nach Kelvin",
        2: "Umrechnung von Celsius nach Fahrenheit",
        3: "Umrechnung von Kelvin nach Celsius",
        4: "Umrechnung von Kelvin nach Fahrenheit",
        5: "Umrechnung von Fahrenheit nach Celsius",
        6: "Umrechnung von Fahrenheit nach Kelvin",
    }

    user_preferences_dict = {
        "operation_id": 0,
        "temperature": 0,
        "unit_convert_from": "",
        "unit_convert_to": "",
        "temperature_converted": 0,
    }

    while (
            keep_working
    ):  # auch in Python gilt: (!keep_working) == (keep_working == False)
        get_user_choices(temp_conversions_dict, user_preferences_dict)

        select_converting_method_and_display(user_preferences_dict)

        decision = input(
            f"Möchten Sie eine weitere Umwandlung durchzuführen? [y / n] \n"
        )
        if decision == "y" or decision == "Y":
            keep_working = True
            user_preferences_dict = (
                {  # für den nächsten Vorgang setzt die Benutzer-definirten Werte zurück
                    "operation_id": 0,
                    "temperature": 0,
                    "unit_convert_from": "",
                    "unit_convert_to": "",
                    "temperature_converted": 0,
                }
            )
        else:
            keep_working = False


def get_user_choices(options_dict: dict, choices_dict: dict):
    """lists each description of the temperature conversion options in a separate line of the terminal

    requests from a user a conversion options number and a temperature amount to be converted

    fills the values for the keys of the user-defined dictionary based on the received choices of the user

    :param options_dict:
        a predefined main dictionary of numbered conversion options as keys and their string
    descriptions as values

    :param choices_dict:
        a user-defined dictionary with keys: a conversion options number, a temperature amount to be
    converted and temperature units, final (converted) temperature, all with empty values

    :return:
        nothing is returned

    """
    display_dictionary_options_values(options_dict)

    keys_list = list(
        choices_dict.keys()
    )  # In Python 3 dict.keys() returns an iterable but not indexable object =>
    # must be converted to a list to avoid an error "TypeError: 'dict_keys' object is not subscribable"

    try:
        choices_dict[keys_list[0]] = int(
            input(
                f"Bitte geben Sie die Nummer (1-6) der gewünschten Temperaturumwandlung aus der Liste ein: \n"
            )
        )
        choices_dict[keys_list[1]] = float(
            input("Bitte geben Sie eine gewünschte Temperatur zur Umwandlung ein: \n")
        )
        choices_dict[keys_list[2]], choices_dict[keys_list[3]] = assign_initial_units(
            options_dict, choices_dict
        )
    except ValueError:
        print(
            "Die gewählte Option ist nicht gültig. Bitte versuchen Sie erneut und wählen die Option aus der Liste."
        )
    except TypeError:
        print(
            "Die gewählte Option ist nicht gültig. Bitte versuchen Sie erneut und wählen die Option aus der Liste."
        )
    except UnboundLocalError:
        print(
            "Die gewählte Option ist nicht gültig. Bitte versuchen Sie erneut und wählen die Option aus der Liste."
        )


def assign_initial_units(options_dict: dict, choices_dict: dict):
    """extracts temperature units strings from the predefined options dictionary according to the option stored in
    the user choice dictionary

    handles KeyError that appears if user has provided a false input as a conversion options number returning a message

    fills temperature units keys of the user-defined dictionary with values

    :param options_dict:
        a predefined dictionary containing conversion options numbers and their string
    descriptions

    :param choices_dict:
        a user-defined dictionary with keys: a conversion options number, a temperature amount to be
    converted with filled values and with keys: temperature units, final (converted) temperature with empty values

    :return:
        a string for an initial temperature unit

        a string for a temperature unit to be converted to
    """
    try:
        unit_convert_from = options_dict[choices_dict["operation_id"]].split()[2]
        unit_convert_to = options_dict[choices_dict["operation_id"]].split()[-1]
    except KeyError:
        print(
            "Die gewählte Option ist nicht gültig. Bitte versuchen Sie erneut und wählen die Option aus der Liste."
        )
    return unit_convert_from, unit_convert_to


def display_dictionary_options_values(options_dict: dict):
    """prints in console every option and its description from a predefined temperature conversion options dictionary

    :param
        options_dict: a dictionary consisting of an int number for an option and a string for its description

    :return:
        nothing
    """
    for option in options_dict:
        print(f"{option}: {options_dict[option]}")


def select_converting_method_and_display(choices_dict: dict):
    """calls a corresponding external temperature conversion function in accordance with received user defined
    option number and temperature from the user-defined dictionary

    rounds a final (converted) temperature reeived from the temp conversion function to a float number with 2 numbers
    after comma

    fills the value of the final (converted) temperature key of the user-defined dictionary based on the received
    choices of the user

    prints a final message containing both original and final temperatures and their units accordingly

    :param choices_dict:
        a user-defined dictionary with keys: a conversion options number, a temperature amount to be
    converted, temperature units with filled values and with the key: final (converted) temperature with empty value

    :return:
        nothing is returned
    """

    keys_list = list(
        choices_dict.keys()
    )  # In Python 3 dict.keys() returns an iterable but not indexable object =>
    # must be converted to a list to avoid an error "TypeError: 'dict_keys' object is not subscribable"

    if choices_dict[keys_list[0]] == 1 or choices_dict[keys_list[0]] == 2:

        choices_dict[keys_list[4]] = round(
            temperature_formulas.convert_celsius(
                choices_dict[keys_list[0]], choices_dict[keys_list[1]]
            ),
            2,
        )
        print(
            "Die Temperatur von",
            choices_dict[keys_list[1]],
            f"{choices_dict[keys_list[2]]} ist {choices_dict[keys_list[4]]} {choices_dict[keys_list[3]]}",
        )

    elif choices_dict[keys_list[0]] == 3 or choices_dict[keys_list[0]] == 4:

        choices_dict[keys_list[4]] = round(
            temperature_formulas.convert_kelvin(
                choices_dict[keys_list[0]], choices_dict[keys_list[1]]
            ),
            2,
        )
        print(
            "Die Temperatur von",
            choices_dict[keys_list[1]],
            f"{choices_dict[keys_list[2]]} ist {choices_dict[keys_list[4]]} {choices_dict[keys_list[3]]}",
        )

    elif choices_dict[keys_list[0]] == 5 or choices_dict[keys_list[0]] == 6:

        choices_dict[keys_list[4]] = round(
            temperature_formulas.convert_fahrenheit(
                choices_dict[keys_list[0]], choices_dict[keys_list[1]]
            ),
            2,
        )
        print(
            "Die Temperatur von",
            choices_dict[keys_list[1]],
            f"{choices_dict[keys_list[2]]} ist {choices_dict[keys_list[4]]} {choices_dict[keys_list[3]]}",
        )


main()
