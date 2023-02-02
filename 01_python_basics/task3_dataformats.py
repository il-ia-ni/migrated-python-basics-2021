"""
This script contains basic information about Python data formats and -structures as well as examples of their operations
"""
import math
import random


def main():
    """ contains examples of variables with different data types

    contains applicable operations with the declared variables

    :return:
        nothing is returned

    """

    # Python has no command for declaring a variable. A variable is created the moment you first assign a value to it.
    # Variables do not need to be declared with any particular type and can change type after they have been set.

    # Variable names are case-sensitive in Python. Names must not begin with numbers or symbols and can only contain
    # letters, numbers and "_". Common naming conventions: snake_case and camelCase

    # To explicitly specify the data type of a variable, CASTING of data type objects (constructor) must be implemented:
    expl_string = str(1992)  # "1992"
    expl_int = int(1992)  # 1992
    expl_float = float(1992)  # 1992.0
    expl_tuple = tuple(("HTML", "CSS", "JS", "TypeScript", "C#", "Python"))

    # Getting a type of the variable may be useful for logical conditions:
    print(f"The type of expl_int variable = {expl_int} ist:", type(expl_int))

    choice = input("Möchten Sie über einfachen Datentypen wissen (int, float, bool, str)? Geben Sie 1 ein. \n Geben "
                   "Sie 2 ein, wenn Sie über Datenstrukturen (lists, tuples, dicts) wissen möchten. \n")
    if choice == "1":
        simple_variables()
        input("Beispiele für einfache Variablen sind aufgelistet. Drücken Sie Enter um fortzufahren.")
    elif choice == "2":
        data_structures()
        input("Beispiele für data-structure Variablen sind aufgelistet. Drücken Sie Enter um fortzufahren.")
    else:
        "Bitte geben Sie nur 1 oder 2 ein. Die Anwendung wird nun beendet."


def simple_variables():
    """ contains examples of variables with simple data types

    prints into console applicable operations with the simple data types functions and methods

    :return:
        nothing is returned

    """

    """
    Zahlen
    """
    # int - ein Numeric Type fur die ganzen, sowohl positiven als auch negativen Zahlen ohne Längenbeschränkung und
    # ohne Dezimalstellen
    input("Drücken Sie Enter, um Beispiele für INTEGERS zu zeigen.")

    int_var = 1992
    int_neg_var = -35

    # Umwandlung von integers:
    int_tofloat_var = float(int_var)
    int_tocompl_var = complex(int_var)

    print(f"Umgewandelte int-Zahl {int_var} in: \n eine float Zahl: {int_tofloat_var} \n eine complexe Zahl:"
          f" {int_tocompl_var}")

    # float - ein Numeric Type für die sowohl positiven als auch negativen Zahlen mit einer oder mehreren
    # Dezimalstellen. Kann auch wissenschaftliche dezimale Exponentenzahlen darstellen mit E = Hoch*10x
    input("Drücken Sie Enter, um Beispiele für FLOATS zu zeigen.")

    float_var = 36.65
    float_exp_var = -87.7e100

    # Umwandlung von floats:
    float_toint_var = int(float_var)
    float_tocompl_var = complex(float_var)

    print(f"Umgewandelte float-Zahl {float_var} in: \n eine integer Zahl: {float_toint_var} \n eine complexe Zahl:"
          f" {float_tocompl_var}")

    # Aufrunden von Dezimallstellen kann ab- (math.floor()) / aufgerundet (math.ceil()) werden
    # oder mit nativem .round(Zahl, Stellen) matematisch auf bestimmte Dezimalstellen begränzt werden
    float_floored_var = math.floor(float_var)
    float_ceiled_var = math.ceil(float_var)
    float_rounded_var = round(float_var, 1)

    print(
        f"Für die float var = {float_var} folgende Aufrunden-Methoden sind verfügbar: \n .floor(): {float_floored_var}"
        f" \n .ceil(): {float_ceiled_var} \n .round(1 Stelle): {float_rounded_var}")

    # complex - ein Numeric Type für komplexe Zahlen mit J-Zeichen für einen Imaginärteil
    # Können nicht in andere Zahltypen umgewandelt werden!!!
    input("Drücken Sie Enter, um Beispiele für COMPLEXes zu zeigen.")

    compl_var = 1j

    print("Ein Beispiel einer komplexen Zahl: ", compl_var)

    # Eine zufällige Zahl kann in Python nur durch das Importieren vom 'random' Moduls erstellt werden, es gibt keine
    # native .random()-Funktion!
    input("Drücken Sie Enter, um Beispiel für eine zufällige Zahl zu zeigen.")

    print("Eine zufällige Zahl im Raum von 1 bis 100 ist: ", random.randrange(1, 100))

    """
    Booleans
    """
    # boolean - ein logischer Datentyp, der nur 2 Werte auf sich nimmt: True oder False (Wahrheitswert). Werden in
    # Vergleichsoperationen und in If-Elif_Else Bedingungen verwendet
    input("Drücken Sie Enter, um Beispiele für BOOLEANS zu zeigen.")

    keep_working = True
    while keep_working:
        a = random.randrange(1, 100)
        b = random.randrange(1, 100)
        print(f"Das Ergebnis der Bedingung A > B für 2 zufälligen Zahlen A = {a} und B = {b} ist: {a > b}")
        keep = input("Möchten Sie noch 2 zufälligen Zahlen auf diese Bedingung prüfen? Geben sie y/Y ein falls JA")
        if keep == "y" or keep == "Y":
            keep_working = True
        else:
            keep_working = False

    """
    Strings
    """
    # str - eine Text-Type Unicode Symbole-Zeichenkette innerhalb von "." oder mit '.'. Ein String ist ein ARRAY von
    # Bytes-Werten der Unicode-Symbolen !!! => Symbole dürfen willkürlich platziert werden (== einen beliebigen
    # Index bekommen)!
    input("Drücken Sie Enter, um Beispiele für STRINGS zu zeigen.")

    short_str_var = "Ilia Nikolaenko"

    # Escape Zeichen in Python werden mit einem Backslash eingeführt:
    some_escape_chars_tuple = ("\' Anführungszeichen ", "\\ Backslash", "\n Zeilenbruch", "\r Wortbruch", "\t tab")

    # Ein langes String kann auch mithilfe von """.""" deklariert werden. Dann dürfen die Zeilenbrüche genauso wie im
    # Code gemacht werden (einfach mit Enter, ohne Verwendung des Escape-Zeichens "\n"
    long_str_var = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua. 
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua.
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut 
    labore et dolore magna aliqua."""

    print(short_str_var, "sagt: \n", long_str_var)  # .print()-Funktion zeigt eine String-Variable in der Konsole

    # Strings Methoden Leitfaden: https://www.w3schools.com/python/python_strings_methods.asp
    # Alle Strings-Metoden geben einen NEUEN Wert wieder und ändern das ursprüngliche String nicht!!!

    # Strings Können concatenated (addiert) werden (str1 + str2 + "text") ODER separiert werden ( str[indA : inxZ] oder
    # .split(Trennungszeichen, Anzahl von Trennungen) )

    vorname_str_var = short_str_var.split()[0]  # .split() ohne ein Argument hat ein Leerzeichen als Trennungszeichen
    nachname_str_var = short_str_var[5:]  # schneidet ein String ab dem 5. Index bis dessen Ende
    rus_name_str_var = nachname_str_var + " " + vorname_str_var
    print(f"Splitted den Vornamen aus dem str {short_str_var}: {vorname_str_var}")
    print(f"Extrahiert den Nachnamen aus dem str {short_str_var}: {nachname_str_var}")
    print(f"Russischer Name durch Addieren von 2 str: {rus_name_str_var}")

    # Eine Zahl kann einem String durch .format()-Methode hinzugefügt werden:
    hello_str = "Ich heiße Ilia, ich bin {} Jahre alt"
    age = 29
    hello_str = short_str_var.format(age)
    print(hello_str)

    # Die Zahl im Stringformat kann mit beliebiger Anzahl von Nullen befüllt werden, dafür wird .zfill() verwendet:
    # @ https: www.w3schools.com/python/ref_string_zfill.asp
    day = "7"
    day = day.zfill(1)  # print(day): 07

    # native .len() Funktion gibt die Länge des Strings wieder.
    print(f"Die Länge eines {rus_name_str_var} Strings: {len(rus_name_str_var)} Zeichen")


def data_structures():
    """ contains examples of variables with sequence or mapping types (data structures)

    prints into console applicable operations with data structures functions and methods

    :return:
        nothing is returned

    """
    # Data Structures-Typen in Python haben keine strengen Datentyp- oder Längeneinschränkungen

    """ List """
    # ein Sequence Type mit EINGEORDNETEN (indexierten) und ÄNDERNBAREN Inhalten. Wiederholte Werte sind ERLAUBT
    input("Drücken Sie Enter, um Beispiele für ein List Type zu zeigen.")

    list_var = ["apple", "banana", "cherry", "apple", "cherry"]
    print("Ein List wird gezeigt:", list_var, "\n Wiederholter Wert: ", list_var[0], "\n Zwischen ihnen liegen: ",
          list_var[1:3], "\n Der letzte Wert ist: ", list_var[-1])

    # Leitfaden für alle Lists-Methoden: https://www.w3schools.com/python/python_lists_methods.asp

    """ Einfügen / Ersetzen von Elementen """
    # einfaches Einfügen vom neuen Wert AM ENDE des Lists - .append(Wert)-Methode:
    extended_list_var = list_var.append("coconut")

    # einfügen von Element(en) ins List OHNE Ersetzung von bestehenden Elementen - .insert(start_ind, Wert)-Methode:
    extended_list_var = list_var.insert(3, "papaja")

    # einfügen von Element(en) ins List MIT Ersetzung von bestehenden Elementen
    list_var[3] = ["papaja"]  # ersetzt Element 4 mit einem Wert

    list_var[3] = ["papaja", "avocado"]  # ersetzt Element 4 mit 2 neuen Elementen, die weitere VERSCHIEBEN sich

    list_var[3:4] = ["papaja"]  # ersetzt Elemente 4 & 5 mit einem Wert

    # Einfügen von Elementen eines ANDEREN OBJEKTS (List / Tuple / Set / Dict / etc.) ins List - list.extend(obj)-Metode
    list2_var = ["dog", "cat"]
    list_var.extend(list2_var)

    # Concatination von 2 Lists in einem neuem List
    list3_var = list_var + list2_var

    """ Löschen von Elementen """
    # Löschen eines spezifischen Werts - .remove(Wert)-Methode
    list_var.remove("cherry")

    # Löschen eines LETZTEN Indexes - .pop()-Methode
    list_var.pop()

    # Löschen eines spezifischen Indexes / des ganzen Lists - del-Keyword
    del list_var[-2]  # Löscht das vorletzte Element
    del extended_list_var  # Löscht das ganze List!

    # Leeren eines Lists ohne seine Löschung - .clear()-Methode:
    list2_var.clear()

    """ Sortieren eines Lists .sort() + .reverse() """
    # .sort(revese = False, key = func/method)-Methode sortiert Elemente von Lists alphabetisch (für Strings),
    # numerisch (nur für int / floats).

    # Standardmäßig werden die Elemente AUFSTEIGEND sortiert. Das Argument "reverse" muss auf "True" gesetzt
    # werden für ABSTEIGENDES Sortieren
    num_list_var = [1, 30, 14, 20, -20, 7, 0, -5]
    print("Sortiertes numerisches List: ", num_list_var.sort())
    print("Absteigend sortiertes numerisches List: ", num_list_var.sort(reverse=True))

    # .sort(key = any_func) kann eine individuelle Funktion als Argument für flexibles Sortieren beinhalten, z.B:
    def sort_closest_to_5(n):
        return abs(n - 5)  # gibt eine absolute (positive) Zahl wieder

    print("Sortiertes numerisches List mit 5 als das Mean: ", num_list_var.sort(key=sort_closest_to_5))

    letters_list_var = ["a", "B", "F", "d", "o", "L", "K"]
    print("Sortiertes alphabetisches List MIT Case-Sensitivität: ", letters_list_var.sort())
    print("Sortiertes alphabetisches List OHNE Case-Sensitivität: ", letters_list_var.sort(key=str.lower))
    print("Umgekehrt sortiertes alphabetisches List OHNE Case-Sensitivität: ", letters_list_var.reverse())

    """ Kopieren eines Lists in ein neues List """
    # Data Structure-Typen sind Link-Typen, d.h. einfache =-Operation erstellt einen Link auf die ursprüngliche
    # Variable. Das Kopieren von Werten ist mit .copy()-Methode möglich
    new_letters_list_var = letters_list_var.copy()  # Erstellt & befüllt das neue List mit Werten aus dem alten List
    # anstatt eine einfachen Link zu erstellen

    """ Tuple """
    # ein Sequence Type mit EINGEORDNETEN (indexierten) und UNÄNDERNBAREN Inhalten. Wiederholte Werte sind ERLAUBT
    input("Drücken Sie Enter, um ein Beispiel für ein Tuple Type zu zeigen.")

    pr_langs_tuple_var = ("HTML", "CSS", "JS", "C#", "Python")
    print("Ein Tuple wird gezeigt: \n", pr_langs_tuple_var)

    # Leitfaden für Tuples-Methoden: https://www.w3schools.com/python/python_tuples_methods.asp

    """ Range """
    # ein Sequence Type array generiert eine Reihe von Zahlen durch einen range(start_int, stop_int [, step_int]) Konstruktor
    # Wird oft als ein Argument von FOR-Schleifen verwendet. Nur "stop_int" ist ein obligatorisches Argument!
    # Mehr dazu: https://linuxize.com/post/python-range/
    input("Drücken Sie Enter, um ein Beispiel für ein Range Type zu zeigen.")

    print("Ein Range von Zahlen ab 0 bis 30 mit dem Increment von 2 wird aufgelistet: \n")
    for i in range(0, 30, 2):  # Range beinhaltet jede 2te. Zahl beginnend mit einschl. 0 bis 29. 2 ist ein Increment
        print(i)

    """ Set """
    # ein Set Type mit UNEINGEORDNETEN (NICHT indexierten) und UNÄNDERNBAREN (ABER ERGÄNZBAREN !!!) Inhalten.
    # Wiederholte Werte sind NICHT ERLAUBT
    # Die Werte werden immer in neuem Order dargestellt und können nicht per ihren Index zugegriffen werden
    input("Drücken Sie Enter, um ein Beispiel für ein Set Type zu zeigen.")

    countries_set_var = {"USA", "EU", "China", "Russland", "Australia"}
    print("Ein Set wird gezeigt: \n", countries_set_var)
    print("Ein Set wird gezeigt: \n", countries_set_var)
    print("Ein Set wird gezeigt: \n", countries_set_var)

    # Leitfaden für Sets-Methoden: https://www.w3schools.com/python/python_sets_methods.asp

    """ Dict """
    # Ein Mapping Type mit EINGEORDNETEN (AB PYTHON v.3.7!!!) und ÄNDERNBAREN Inhalten. Wiederholte KEYS sind NICHT ERLAUBT
    # Ein Verzeichnis / Wörterbuch mit dem Namen, dem die Key/Value Paaren ".": "." eingegeben werden können.
    input("Drücken Sie Enter, um Beispiele für ein Dictionary Type zu zeigen.")

    car_dict_var = {
        "brand": "Ford",
        "model": "Mondeo",
        "year": 1970
    }

    car_dict_var["model"] = "Mustang"  # Einen neuen Wert dem Key eingeben
    car_dict_var["price"] = 100000  # Ein neues Key:Value Paar dem Dictionary hinzufügen

    print("Ein Dictionary wird gezeigt: \n", car_dict_var)
    print("Ein Brand-Key Wert aus dem Dictionary wird gezeigt: \n", car_dict_var["brand"])

    # Leitfaden für Dictionaries-Methoden: https://www.w3schools.com/python/python_dictionaries_methods.asp

    """ Spezifische Versionen von Data Structures-Typen: """
    # frozen (immutable) set - ein Set, dass auch nicht ergänzt werden darf

    # bytes - ein Binary Type - ein Objekt-Reihenfolge von Integers von 0 bis 256

    # byte array - ein Binary Type Array mit Elementen von integers von 0 bis 256 (Unicode Chars)


main()
