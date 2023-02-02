# Docstrings immer am Anfang des Scripts hinzufügen!

"""
This script request personal data from user and returns selected information as a message
"""

name = input("Bitte geben Sie Ihren Vornamen ein")
lastName = input("Bitte geben Sie Ihren Nachnamen ein")
birthDate = input("Bitte geben Sie Ihr Geburtsdatum ein")
telephone = input("Bitte geben Sie Ihre Telefonnummer ein")
address = input("Bitte geben Sie Ihre Wohnadresse ein")

# This line prints your result
print(f"Hallo, {name} \n {birthDate}")
