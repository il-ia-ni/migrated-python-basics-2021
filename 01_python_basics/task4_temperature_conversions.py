"""
This script contains functions that convert each of three SI temperature units to other 2
"""


def convert_celsius(operation_id: int, temperature_from: float):
    """This function converts initial temperature in Celsius either to Kelvin or to Fahrenheit according to users choices received

    Prints an error into console if the received credentials cannot be calculated

    :param
        operation_id: an int number for a temperature conversion option received from the user

    :param
        temperature_from: a float number for a temperature to be converted received from the user

    :return:
        a full integer number for a final (converted) temperature in either Kelvin or Fahrenheit
    """
    temperature_to = 0
    if operation_id == 1:
        temperature_to = temperature_from + 273.15
    elif operation_id == 2:
        temperature_to = temperature_from * 9 / 5 + 32
    else:
        print(
            "Oops, etwas ist falsch gelaufen. Der Vorgang konnte nicht abgeschlossen werden."
        )
    return temperature_to


def convert_kelvin(operation_id: int, temperature_from: float):
    """This function converts initial temperature in Kelvin either to Celsius or to Fahrenheit according to users choices received

    Prints an error into console if the received credentials cannot be calculated

    :param
        operation_id: an int number for a temperature conversion option received from the user

    :param
        temperature_from: a float number for a temperature to be converted received from the user

    :return:
        a full integer number for a final (converted) temperature in either Celsius or Fahrenheit
    """
    temperature_to = 0
    if operation_id == 3:
        temperature_to = temperature_from - 273.15
    elif operation_id == 4:
        temperature_to = (temperature_from - 273.15) * 9 / 5 + 32
    else:
        print(
            "Oops, etwas ist falsch gelaufen. Der Vorgang konnte nicht abgeschlossen werden."
        )
    return temperature_to


def convert_fahrenheit(operation_id: int, temperature_from: float):
    """This function converts initial temperature in Fahrenheit either to Celsius or to Kelvin according to users choices received

    Prints an error into console if the received credentials cannot be calculated

    :param
        operation_id: an int number for a temperature conversion option received from the user

    :param
        temperature_from: a float number for a temperature to be converted received from the user

    :return:
        a full integer number for a final (converted) temperature in either Celsius or in Kelvin
    """
    temperature_to = ""
    if operation_id == 5:
        temperature_to = 5 / 9 * (temperature_from - 32)
    elif operation_id == 6:
        temperature_to = 5 / 9 * (temperature_from - 32) + 273.15
    else:
        print(
            "Oops, etwas ist falsch gelaufen. Der Vorgang konnte nicht abgeschlossen werden."
        )
    return temperature_to
