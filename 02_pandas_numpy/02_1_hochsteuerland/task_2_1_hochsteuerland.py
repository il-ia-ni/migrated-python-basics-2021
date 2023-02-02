import os
import pathlib
from datetime import date, time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# .apply(func)-Methode https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html
# .loc()-Methode https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html
# .where()-Methode https://stackoverflow.com/questions/21702342/creating-a-new-column-based-on-if-elif-else-condition
# Essential DF functionality:
# https://pandas.pydata.org/pandas-docs/stable/user_guide/basics.html#essential-basic-functionality und
# https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
# was scalar data ist: https://softwareengineering.stackexchange.com/questions/238033/what-does-it-mean-when-data-is-scalar

# ML Grundlagen: https://www.w3schools.com/python/python_ml_percentile.asp
# Matplotlib & Histogramms: https://www.w3schools.com/python/matplotlib_histograms.asp

attempts_counter = 0

en_tuple = ("EN", "en", "En", "English", "english", "Englisch", "englisch", "englische")
de_tuple = ("DE", "de", "De", "German", "german", "Deutsch", "deutsch", "deutsche")


def main():
    """ reads an excel-file from a received relative path

    creates a Pandas DataFrame from the excel file

    proves if the generated DataFrame contains all obligatory keys for creation of a report

    fills the valid DataFrame with 2 extra columns for tax amount and for an applied tax rate

    generates necessary statistical parameters with Numpy or Pandas based on the user choice

    generates and displays 2 histograms for incomes and for applied interest rates including their statistical
    parameters Mean, Median and normal distribution line of the standard deviation

    :return:
        nothing to return
    """

    # Zugriff auf eine .xlsx-Datei
    root_path = os.path.join(pathlib.Path(__file__).parent.joinpath('data'))
    excel_file_name = 'einkommen.xlsx'
    excel_joined_path = os.path.join(root_path, excel_file_name)

    # Erstellung eines DFs aus der .xlsx-Datei
    df_taxpayers_income = pd.read_excel(excel_joined_path)
    print("DataFrame aus den eingelesenen Daten: \n", df_taxpayers_income)

    # Validierung des DFs (der .xlsx-Datei)
    print("\nIhre .xlsx Datei wird auf die Möglichkeit geprüft, einen Report zu erstellen.")
    inspection_result = validate_df_cols(df_taxpayers_income)  # entweder ein dictionary mit DF labels oder bool False

    if not inspection_result:  # falls False => das DF passt nicht für Reportserstellung
        print("Die Anwendung wird nun beendet.")

    else:  # falls es Dictionary gibt (True) => das DF passt für Reportserstellung

        # Erweiterung eines DFs mit erforderlichen Spalten Steuersumme, Steuersatz
        add_rates_and_tax(df_taxpayers_income, inspection_result)
        print("Das DataFrame wurde erfolgreich erweitert:\n", df_taxpayers_income)

        # Erstellung von Plots für Einkommen und Steuersätze
        build_histograms(df_taxpayers_income, inspection_result)


"""
Operational functions: perform certain tasks in main()
"""


def validate_df_cols(df: pd.DataFrame):
    """ generates a list of column labels of the DataFrame received for validation

    asks user for a language of the column labels to begin validation

    proves if each of column labels in the list is matching a predefined tuple of strings for EN and GE languages

    sets each found column label as a value for a corresponding key in a predefined dictionary

    raises error if one of the obligatory keys of the dictionary has no match in the list of columns labels

    :param df: a DataFrame created from a .xlsx-file

    :return:
        a dictionary filled with column labels of the validated DataFrame OR boolean False if any
    obligatory key of the dictionary was not found in the list of columns labels
    """

    input1_list = ["Steuerzahler", "steuerzahler", "Taxpayer", "taxpayer"]
    input2_list = ["Einkommen", "einkommen", "Income", "income"]

    validated_cols_labels_dict = {
        "taxpayer_col_label": False,
        "income_col_label": False,
        "output_col_label1": "",
        "output_col_label2": ""
    }

    df_cols_labels_list = list(df.columns)

    print("Bitte geben Sie die Sprache ein, in welcher Ihre .xlsx Datei erfasst ist:")

    language_choice = input()  # df.columns gibt ein Array von column Labels-strings zurück
    # Es beugt Probleme bei Labeländerung in der .cvs-Datei bei weiterem Ablauf des Programms vor!

    try:
        if language_choice in en_tuple:
            validated_cols_labels_dict["output_col_label1"] = "Tax Amount"
            validated_cols_labels_dict["output_col_label2"] = "Tax Rate"
        elif language_choice in de_tuple:
            validated_cols_labels_dict["output_col_label1"] = "Steuersumme"
            validated_cols_labels_dict["output_col_label2"] = "Steuersatz"
        else:
            raise ValueError("Die eingegebene Sprache ist falsch. Bitte versuchen Sie es erneut!")

        for label in df_cols_labels_list:
            if label in input1_list:
                validated_cols_labels_dict["taxpayer_col_label"] = label
            elif label in input2_list:
                validated_cols_labels_dict["income_col_label"] = label
            else:
                print("Spalte {} kann nicht für Erstellung des Reports verwendet werden...\n".format(label))

        if not validated_cols_labels_dict["taxpayer_col_label"] or not validated_cols_labels_dict["income_col_label"]:
            raise TypeError("Es wurde erforderliche Spalten nicht gefunden. Der Report kann nicht erstellt werden!")
        else:
            return validated_cols_labels_dict

    except Exception as e:
        print(e)
        if ValueError:
            validate_df_cols(df)
        elif TypeError:
            return False


def add_rates_and_tax(df: pd.DataFrame, inspected_dict: dict):
    """ Cleans a received DataFrame of lines with empty values

    Adds a new column for a calculated tax amount according to an applicable condition

    Adds a new column for an applied tax rate according to an applicable condition

    :param df:
        a valid DataFrame with columns tax payer and income

    :param inspected_dict:
        a dictionary filled with column labels of the validated DataFrame

    :return:
        a valid DataFrame cleaned of rows with missing values and extended with new columns for tax amount and tax rate
    """

    tax_payer_column = inspected_dict["taxpayer_col_label"]
    income_column = inspected_dict["income_col_label"]
    tax_amount_column = inspected_dict["output_col_label1"]
    tax_rate_column = inspected_dict["output_col_label2"]

    df.dropna(inplace=True)  # Remove missing values and keep the DataFrame with valid entries in the same variable

    df.loc[df.loc[:, income_column] <= 10000, tax_amount_column] = df.loc[:, income_column] * 0.2
    df.loc[df.loc[:, income_column] <= 10000, tax_rate_column] = 20

    df.loc[(df.loc[:, income_column] > 10000) & (df.loc[:, income_column] <= 30000), tax_amount_column] = df.loc[:, income_column] * 0.4
    df.loc[(df.loc[:, income_column] > 10000) & (df.loc[:, income_column] <= 30000), tax_rate_column] = 40

    df.loc[(df.loc[:, income_column] > 30000) & (df.loc[:, income_column] <= 70000), tax_amount_column] = df.loc[:, income_column] * 0.55
    df.loc[(df.loc[:, income_column] > 30000) & (df.loc[:, income_column] <= 70000), tax_rate_column] = 55

    df.loc[df.loc[:, income_column] > 70000, tax_amount_column] = df.loc[:, income_column] * 0.75
    df.loc[df.loc[:, income_column] > 70000, tax_rate_column] = 75

    return df


def build_histograms(df_ext: pd.DataFrame, inspected_dict: dict):
    """ requests a user choice int for further statistics calculation

    generates 2 datasets for income and tax rates and 3 dictionaries filled with corresponding statistical params

    builds a histogram incl. statistical params lines for the income data set

    builds a histogram incl. statistical params lines for the tax rate data set

    prints (shows) a plot consisting of both histograms and their normal distribution lines subplots

    :param df_ext:
        an extended, valid DataFrame with columns tax payer, income, tax amount and tax rate

    :param inspected_dict:
        an integer for the user choice received

    :return:
        nothing is returned

    """

    user_choice = get_validated_user_choice()

    try:
        # Erfrage von statistischen Werten sowie 1-Dimensionalen Arrays für Plotting erfolgt anhand von Numpy oder Pandas
        incomes_dataset, tax_rates_dataset, means, medians, deviations = set_statistic_values(df_ext, user_choice, inspected_dict)

        """
        subplot 1 - Einkommen Statistik
        """
        plt.subplot(2, 1, 1)

        plt.hist(incomes_dataset, density=True, color="green", edgecolor='k', alpha=0.55,
                 label='Einkommen')  # builds a histogram

        # density parameter normalizes bin heights so that the integral of the histogram is 1. The resulting histogram is
        # an approximation of the probability density function. If True, draw and return a probability density: each bin
        # will display the bin's raw count / by the total number of counts * the bin width

        # Selecting different bin counts and sizes can significantly affect the shape of a histogram:
        # https://docs.astropy.org/en/stable/visualization/histogram.html
        # with 2 bins, the fine structure of the data distribution is lost, while with 2000 bins, heights of individual bins
        # are affected by sampling error. The tried-and-true method employed by most scientists is a trial and error
        # approach that attempts to find a suitable midpoint between these.

        plt.axvline(means["income_mean"], color='red', linestyle='dashed', linewidth=1.5,
                    label='Mean')  # builds a mean line
        plt.axvline(medians["income_median"], color='violet', linestyle='dotted', linewidth=2,
                    label='Median')  # builds a median line

        build_normal_distribution_line(means, deviations, "income")  # builds a normal distribution line for

        plt.title("Einkommen")
        plt.xlabel("Jährliches Einkommen, td. Euro")
        plt.ylabel("Häufigkeit")
        plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05))
        # bbox_to_ancher läßt die Legendenkiste etwas aus dem Plot wegschieben:
        # https://stackoverflow.com/questions/4700614/how-to-put-the-legend-out-of-the-plot

        """
        subplot 2 - Steuersätze Statistik
        """
        plt.subplot(2, 1, 2)

        # Erstellen einer maßgeschneiderten X-Achse für die Steuersätze
        plt.xticks(np.concatenate([np.arange(0, 60, 20), np.arange(55, 95, 20)]))  # Wir brauchen Ticks 20, 40, 55, 75
        # plt.xticks läßt Ticks (sowie deren Labels) entlang der X-Achse flexibel bestimmen
        # np.arrange gibt ein ndarray zurück, das mit gleichmäßig verteilten Werten von A (inkl.) bis B (nicht inkl.) mit
        # Abstand C befüllt wurde
        # np.concatenate nimmt eine FOLGE (Liste, Tuple...) von ndarrays an, die geflattet (oder entlang bestimmter
        # Achse) zusammengefügt werden

        plt.hist(tax_rates_dataset, density=True, color="blue", edgecolor='k', alpha=0.55, label="Steuersätze")
        plt.axvline(means["tax_rate_mean"], color='red', linestyle='dashed', linewidth=1.5, label='Mean')
        plt.axvline(medians["tax_rate_median"], color='violet', linestyle='dotted', linewidth=2, label='Median')

        build_normal_distribution_line(means, deviations, "tax_rate")

        plt.title("Steuersätze")
        plt.xlabel("Steuersatz, %")
        plt.ylabel("Häufigkeit")
        plt.legend(loc='upper right', bbox_to_anchor=(1.1, 1.05))

        """
        plot Einstellungen
        """
        if user_choice == 1:
            plottitle_type = "(Numpy)"
        elif user_choice == 2:
            plottitle_type = "(Pandas)"
        plt.suptitle("Statistiken für private Personen {}".format(plottitle_type))
        plt.tight_layout()  # automatically adjusts subplot params so that the subplot(s) fits in to the figure area.
        # This is an experimental feature and may not work for some cases. It only checks the extents of ticklabels,
        # axis labels, and titles. Will also adjust spacing between subplots to minimize the overlaps. Works even if the
        # sizes of subplots are different provided grid specification is compatible (f.e., 2 1x1 subplots, 1 2x1 subplot).
        # More @ https://matplotlib.org/stable/tutorials/intermediate/tight_layout_guide.html
        plt.show()

        print("\nDer grafische Report wurde anhand von {} erfolgreich erstellt!".format(plottitle_type))

    except Exception as e:
        print("Statistische Werte konnten nicht gesetzt werden. Die Anwendung wird nun beendet.")


"""
Helper Functions: are used in operational functions to separate their extended functionality
"""


def get_validated_user_choice():
    """ Gets input from the user

    Proves the validity of the input towards condition, if invalid:

    Recursively requests another user input until a certain amount of input attempts gets exceeded

    :return:
        an integer for the correct user input OR a boolean False if couldn't get a correct input after all attempts
    """
    global attempts_counter

    print("\nMöchten Sie statistische Parameter (Mean, Median, Standardabweichung) mithilfe von Numpy (1) oder Pandas "
          "(2) berechnen?")

    try:
        choice = int(input())

        if choice == 1 or choice == 2:
            return choice

        elif isinstance(choice, int):
            raise ValueError("Falsche Eingabe!")

    except Exception as e:
        if ValueError:
            print("Bitte nur 1 für Numpy oder 2 für Pandas oder eingeben!")
        else:
            print(e)

        attempts_counter += 1

        if attempts_counter < 5:
            print("Versuchen Sie es erneut!")
            get_validated_user_choice()
        else:
            print("\nZu viele Falsche Eingaben!")
            return False


def set_statistic_values(df_ext: pd.DataFrame, user_choice: int, inspected_dict: dict):
    """ Creates 2 Numpy arrays or 2 Pandas Series for incomes and tax rates according to the user choice received

    Calculates MEAN value for income and tax rates data sets

    Calculates MEDIAN value for income and tax rates data sets

    Calculates STANDARD DEVIATION value for income and tax rates data sets

    :param df_ext:
        an extended, valid DataFrame with columns tax payer, income, tax amount and tax rate

    :param user_choice:
        an integer for the user choice received

    :param inspected_dict:
        a dictionary filled with column labels of the validated DataFrame

    :return:
        2 Datasets for income and tax rate, either as a Numpy Array or as a Panda Series

        a dictionary for the calculated MEAN values for keys "income" and "tax_rate"

        a dictionary for the calculated MEDIAN values for keys "income" and "tax_rate"

        a dictionary for the calculated STANDARD DEVIATION values for keys "income" and "tax_rate"
    """
    means_dict = {
        'income_mean': 0,
        'tax_rate_mean': 0
    }
    medians_dict = {
        'income_median': 0,
        'tax_rate_median': 0
    }
    deviations_dict = {
        'income_deviation': 0,
        'tax_rate_deviation': 0
    }

    tax_payer_column = inspected_dict["taxpayer_col_label"]
    income_column = inspected_dict["income_col_label"]
    tax_amount_column = inspected_dict["output_col_label1"]
    tax_rate_column = inspected_dict["output_col_label2"]

    # Berechnung von statistischen Werten mit Numpy
    if user_choice == 1:
        incomes_np_arr = df_ext.loc[:, income_column].to_numpy()
        tax_rates_np_arr = df_ext.loc[:, tax_rate_column].to_numpy()

        means_dict['income_mean'] = np.mean(incomes_np_arr)
        means_dict['tax_rate_mean'] = np.mean(tax_rates_np_arr)

        medians_dict['income_median'] = np.median(incomes_np_arr)
        medians_dict['tax_rate_median'] = np.median(tax_rates_np_arr)

        deviations_dict['income_deviation'] = np.std(incomes_np_arr)
        deviations_dict['tax_rate_deviation'] = np.std(tax_rates_np_arr)

        print("Statistische Werte anhand von Numpy: \b")
        print(means_dict)
        print(medians_dict)
        print(deviations_dict)

        return incomes_np_arr, tax_rates_np_arr, means_dict, medians_dict, deviations_dict

    # Berechnung von statistischen Werten mit Pandas
    elif user_choice == 2:
        incomes_pd_series = df_ext.loc[:, income_column]
        tax_rates_pd_series = df_ext.loc[:, tax_rate_column]

        means_dict['income_mean'] = incomes_pd_series.mean()
        means_dict['tax_rate_mean'] = tax_rates_pd_series.mean()

        medians_dict['income_median'] = incomes_pd_series.median()
        medians_dict['tax_rate_median'] = tax_rates_pd_series.median()

        deviations_dict['income_deviation'] = incomes_pd_series.std()
        deviations_dict['tax_rate_deviation'] = tax_rates_pd_series.std()

        print("Statistische Werte anhand von Pandas: \b")
        print(means_dict)
        print(medians_dict)
        print(deviations_dict)

        return incomes_pd_series, tax_rates_pd_series, means_dict, medians_dict, deviations_dict


def build_normal_distribution_line(means_dict: dict, stand_devs_dict: dict, dict_key_name: str):
    """ Builds a plot for a normal distribution line on x-axis with an even interval using received statistical values

    :param
        means_dict: a dictionary for mean values for the keys "income" and "tax rate"

    :param
        stand_devs_dict: a dictionary for standard deviations values for the keys "income" and "tax rate"

    :param
        dict_key_name: a string extension for either "income" or "tax_rate" keys used to extract a corresponding value

    :return:
        nothing is returned

    """
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, means_dict[dict_key_name + "_mean"], stand_devs_dict[dict_key_name + "_deviation"])
    plt.plot(x, p, color='green', linewidth=2, label='Normalverteilung')


main()
