"""
Das Skript enthält maßgeschneiderte Ausnahmen für die Anwendung.
Mehr zu Custom-Exceptions: Mehr dazu @ https://www.programiz.com/python-programming/user-defined-exception

Es ist ein gutes Muster, maßgeschneiderte Ausnahmen in ein separates Skript dem Projekt hinzufügen!
"""

# A custom exception class has to be derived, either directly or indirectly, from the built-in Exception Class!
# User-defined exception class can implement everything a normal class can do, but we generally make them simple and
# concise. Most implementations declare a custom base class and derive others exception classes from this base class


class OptionNumberNotDefinedError(Exception):
    """
    Die Ausnahme wird im Projekt dann eingesetzt, wenn der Benutzer eine Zahl als input eingegeben hat, aber es gibt
    keine Option in einem Optionen-Dictionary mit dieser Nummer
    """
    pass

# This new exception, like other exceptions, can now be raised in code using the RAISE statement with an optional
# error message. Without the message text
