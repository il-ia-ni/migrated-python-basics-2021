"""This script contains solutions to the tasks found @
https://www.w3resource.com/python-exercises/project/covid-19/index.php about working with statistics of coronavirus
cases read from .cvs-files published @ https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master
/csse_covid_19_data/csse_covid_19_daily_reports /csse_covid_19_daily_reports """

from datetime import date  # eine Klasse für Operationen mit dem Datum (datetime.now() gibt das Datum UND Zeit wieder)
import requests as reqs  # https://docs.python-requests.org/en/master/ - wird für HTTP-Anfragen benutzt
import pandas as pd
import options_formulas as formulas
from custom_exceptions import OptionNumberNotDefinedError

""" Global variables """

covid_stats_source = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports"


def main():
    """ creates a URL address for the latest corona-stats .csv report available

    creates a Pandas DataFrame from the .csv file on the server

    prints 5 rows of the DF and its dataset info (Task 1) in console

    :return:
        nothing is returned
    """

    keep_working = True

    analysis_options_dict = {
        1: "Die registrierten neuen Fälle, Sterbefälle, Genesene, Gesamtfälle nach Ländern",  # Aufgabe 2
        2: "Die registrierten neuen Fälle, Sterbefälle nach Provinzen / Staaten eines Landes / Regions",  # Aufgabe 3
        3: "Die registrierten Gesamtfälle, Sterbefälle, Genesene nach Provinzen Chinas",  # Aufgabe 4
        4: "Die absteigend sortierten registrierten Sterbefälle nach Ländern",  # Aufgabe 5
        5: "Die Liste von Ländern ohne bis dato registrierte Corona Fälle",  # Aufgabe 6
        6: "Die Liste von Ländern mit allen registrierten Fällen gestorben",  # Aufgabe 7
        7: "Die Liste von Ländern mit allen registrierten Fällen genesen",  # Aufgabe 8
        8: "Die absteigend sortierte Liste von Statistiken über Top-10 Ländern nach Gesamtfällen",  # Aufgabe 9
        9: "Eine Grafik für Corona-Entwicklung in Ländern mit registrierten Sterbefällen über 100.000",  # Aufgabe 10
        10: "Eine Grafik für registrierte Sterbefälle nach den Staaten der USA",  # Aufgabe 11
        11: "Eine Grafik für registrierte laufende (aktive) Fälle nach den Staaten der USA",  # Aufgabe 12
        12: "Eine Grafik für Corona-Entwicklung für die Staaten der USA",  # Aufgabe 13
        13: "Eine Grafik für zeitliche Entwicklung der weltweit registrierten Corona-Fälle",  # Aufgabe 14
    }

    user_choice = 0

    latest_stats_csv_url = get_latest_stats()

    print("Creating a DataFrame from a .csv file at:", latest_stats_csv_url)
    latest_stats_df = pd.read_csv(latest_stats_csv_url, sep=',', quotechar='"', skipinitialspace=True, parse_dates=True)
    # Attribut parse_dates=True (funktioniert nur bei gleichen Timezonen in einer Reihe)
    # != .read_csv().to_datetime() - ermöglicht ein non-standardes DateTime-Parsing, z.B, mit einem date_parser=func, wo
    # utc=True fürs Parsing einer Reihe mit gemischten Timezonen. Siehe https://pandas.pydata.org/docs/user_guide/io.html#io-csv-mixed-timezones

    print("Ein DataFrame wurde erstellt:", latest_stats_df)
    print("Die Dataset-Informationen zu dem DF:", latest_stats_df.info())

    while keep_working:

        user_choice = get_user_choices(analysis_options_dict)
        print(user_choice)

        if user_choice in analysis_options_dict:
            print(f"Sie haben Option {user_choice} gewählt: {analysis_options_dict[user_choice]}")
            formulas.choose_stats_analysis(latest_stats_df, user_choice)

        decision = input(f"Möchten Sie einen weiteren Report erstellen? [y / n] \n")
        if decision == "y" or decision == "Y":
            keep_working = True
        else:
            keep_working = False


def get_latest_stats():
    """ gets the name of the latest corona stats .csv file available on a server

    combines the string for the global variable of the stats servers URL with the string for the name of the latest
    stats file

    :return:
        a string with a full URL-path to the latest .csv file

    """

    today_ts = pd.Timestamp.now()

    full_csv_url = covid_stats_source + "/" + today_ts.strftime("%m-%d-%Y") + ".csv"

    does_csv_exist = False

    while not does_csv_exist:
        does_csv_exist = check_csv_availability(full_csv_url)  # prüft jeweils die neue Version des URLs auf dem Server
        iterator = 0
        print("Checking availability of the csv file:", full_csv_url)
        print("Checking if file exists:", does_csv_exist)

        if does_csv_exist:  # beendet die Schleife falls die Datei auf dem Server gefunden wurde
            break
        else:  # erstellt eine neue Version des URL Strings mit jeweils absteigendem Datum
            iterator += 1

            past_date_ts = today_ts - pd.Timedelta(days=iterator)

            full_csv_url = covid_stats_source + "/" + past_date_ts.strftime("%m-%d-%Y") + ".csv"

            """ OLD CODE: KEPT FOR PRACTICE WITH STRINGS SLICING PURPOSES
            today_date = date.today().strftime("%m-%d-%Y")  # y == XX, Y == XXXX für das Jahr; m == 03, B == March
            # Sowohl date.today() als auch datetime.now() Methoden geben ein OBJEKT wieder. Um diese in ein String in einem
            # bestimmten Format umzuwandeln, wird die .strftime(FORMAT) benutzt
            
            previous_day = date.today().day - iterator  # mit jedem Vorgang der Schleife substrahiert den steigenden
            # Iterator aus dem HEUTIGEN Tag

            # es wäre möglich mit dem .zfill() hier zu arbeiten, um den 1-Stelligen Zahlen die 0 vorne hinzuzufügen

            if previous_day >= 10:  # Für die zweistelligen Tagesnummer - einfach dem URL String hinzugefügt
                full_csv_url = full_csv_url[:-11] + "{prev_day}" + full_csv_url[-9:]

            elif 1 <= previous_day >= 9:  # Die einstellige Tagesnummer sind auf
                # dem Server im mm-0d-YYYY Format aufgelistet, d.h. z.B. int=3 muss ins str=03 umgewandelt werden
                full_csv_url = full_csv_url[:-11] + "0{prev_day}" + full_csv_url[-9:]
            # OPEN: numpyarray oder eine Liste für Prüfung der Bedienung verwenden (Zeilen 106-111)

                # a = [4,2,3,1,5,6]
              #  if 4 in a:
            # OPEN: TimeStamps wären besser für die Arbeit mit Tagen und Monatenwechsel

            full_csv_url = full_csv_url.format(prev_day=previous_day)  # fügt die immer sinkende Tagesnummer dem
            # String hinzu, bis die letzte existierende Datei auf dem Server gefunden wird (am Anfang eines nächsten
            # Vorgangs der Schleife)
            """

    print("The last existing csvs url found:", full_csv_url)

    return full_csv_url


def check_csv_availability(csv_url: str) -> bool:  # -> defines that output type is supposed to be boolean!
    # The arrow symbol here is NOT a lambda expression! It is an extended part of the function annotations in Python
    # used for output typing along with inputs typing as Python moves towards stricter typing. More @
    # https://stackoverflow.com/questions/14379753/what-does-mean-in-python-function-definitions

    # alternatively we import Union from class "typing", than we can specify the output in the function annotation as
    # -> Union[False, True]. Union type is coming from statically typed languages (like C, Java). Since Python is an
    # OOP language, where objects return what they can return based on their methods logic, this is not a default
    # functionality and the Union type needs to be imported first, even though it comes preinstalled.

    """ Checks availability of a .csv-file under a received URL-address

    :param
        csv_url: a full URL-address to the .csv-file on the server

    :return:
        True if the server returned positive answer (the URL is valid)

        False if the server returned any other answer (the URL is not valid)
    """
    header_request = reqs.get(csv_url)
    if header_request.status_code == 200:
        return True
    else:
        return False


def get_user_choices(options_dict: dict):
    """ lists each description of the corona stats analysis options in a separate line of the terminal

    requests from a user an analysis options number

    checks if the received option number is valid

    :param options_dict:
        a predefined main dictionary of numbered analysis options as keys and their string descriptions as values

    :return:
        an integer value of the valid user choice for the stats analysis option
    """
    display_dictionary_options_values(options_dict)

    try:
        user_response_int = int(input(f"Bitte geben Sie eine Nummer der gewünschten Option zur Analyse von "
                                      f"Statistiken aus dem DataFrame: \n"))

        # Prüfen, ob der int-Wert im options_Dictionary vorhanden ist:
        if user_response_int in options_dict:  # CASE 1: correct number input, is in dictionary
            return user_response_int
        elif isinstance(user_response_int, int):  # CASE 2: correct number input, not is in dictionary
            # hier verwende ich eine Custom-Exception, die in einem separaten Skript erstellt wurde.
            # Mehr dazu @ https://www.programiz.com/python-programming/user-defined-exception
            raise OptionNumberNotDefinedError(
                "Die gewählte Option existiert nicht. Bitte geben Sie die Nummer der Option erneut.")

    except Exception as e:
        # Exception as VAR ist ein besserer Weg, ohne ein Fehlertyp einzugeben allen Fehlern einzugehen. "as VAR"
        # eignet sich außerdem gut für flexibleres Weiterarbeiten mit jeweiligem Fehler. Mehr dazu: 8.5. Exception
        # Chaining @ https://docs.python.org/3/tutorial/errors.html#exception-chaining

        if isinstance(e, OptionNumberNotDefinedError):  # falls die Custom-Exception stattfindet
            print(e)

        # CASE 3: incorrect letter/symbol input
        else:  # falls alle anderen Exception Typen passieren (z.B, ValueError findet im Fall int(letter) stattfinden)
            print(
                "Die gewählte Option ist nicht gültig. Bitte versuchen Sie erneut und wählen die Option aus der Liste.")


def display_dictionary_options_values(options_dict: dict):
    """ prints in console every option and its description from a predefined corona stats analysis options dictionary
    in a separate line for improved readability

    :param options_dict:
        a dictionary consisting of an int number for an option and a string for its description

    :return:
        nothing is returned

    """

    for option in options_dict:
        print(f"{option}: {options_dict[option]}")


main()
