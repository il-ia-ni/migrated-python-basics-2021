"""
This script converts a radian angle unit into a degree angle unit returns selected information as a message
"""

from math import pi as pi

pi_const = pi  # In Python, all variables that are created outside a function are considered to be in the “global”
# space. GLOBAL VARIABLES are defined outside any function and will exist until they are deleted or the program ends.
# !!! To modify a global variable within a function in must be imported within the function using "global" keyword!!!
# Otherwise, a reference to the global variable creates a LOCAL COPY of it within the function.

DEGREE_SYMBOL = "\N{DEGREE SIGN}"


def main():
    """contains a logical structure of the script

    call functions that request a degree value and convert it to another format

    prints a message into console containing an original angle unit in Radians and a converted angle unit in degrees

    :return:
       nothing is returned

    """

    global DEGREE_SYMBOL  # an example of importing a global variable in a function (even though no change to * value)

    rad_angle = get_radians()
    degree_angle = convert_rads_todegrees(rad_angle)

    print(
        f"Der eingegebene Winkel von {rad_angle} Radiant beträgt {round(degree_angle, 2)} {DEGREE_SYMBOL}"
    )


def get_radians():
    """requests a user to give in a radian angle value

    proves if the entered value can be used for further mathematical operations

    returns a failure message if the received value is not a number

    :return:

       radian value in a full float format

    """

    # Instead of try-except-finally also custom-based exceptions can be built in Python using custom exception classes:
    # https://towardsdatascience.com/how-to-define-custom-exception-classes-in-python-bfa346629bca

    try:
        rad_angle = float(
            input(
                f"Bitte geben Sie den beliebigen Winkel im Bogenmaß ein, um ihn in den Gradmaß umzurechnen: \n "
            )
        )
    except ValueError:
        print(f"Bitte geben Sie nur eine Zahl ein!")

    return rad_angle


def convert_rads_todegrees(rad: float = 1):
    # Man kann den Parametern einer Funktion einen festen Datentyp durch X:int UND einen standarden Wert durch X=1 geben

    """calculates a corresponding degree angle value from a received radian value using a mathematical formula

    :param
        rad: a radian angle value received from a user in full float format. Default value is set to 1 Radian

    :return:
        a degree angle value in a full float format

    """

    global pi_const  # an example of importing a global variable in a function (even though no change to pi value)

    degree = rad * 180 / pi_const

    return degree


main()
