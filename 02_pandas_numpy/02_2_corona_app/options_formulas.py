""" This script contains functions that form corresponding Pandas Series / DataFrames / Matplot charts from a
received DataFrame according to a received option value """

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerTuple

report_df = pd.DataFrame

rows_labels_list = []
cols_labels_list = []


def choose_stats_analysis(stats_df: pd.DataFrame, option_nr: int):  # hier gibt int bei Mismatch nur die Warnung zurück
    """ calls a corresponding function for creating a report on the basis of a received DataFrame

    :param
        stats_df: a DataFrame with latest corona stats

        option_nr: a user defined analysis options number

    :return:
        nothing is returned

    """

    # OPEN: Besser lesbar wäre zuerst eine Prüfung/Fehlermeldung schreiben. + Steigert Effiktivität (es wird zuerst
    # auf Fehler geprüft) UND Sicherheit (z.B., um Schadbefehle aus der DB vermeiden)

    # OPEN 2: Ob man "if isinstance()" oder "if not type(x) is int: raise Error("Fehlermeldung")" hier verwendet ist
    # nicht wichtig, jedoch bei "not type" können die 13 Bedingungen einfach auf derselbe Ebene nachfolgen. Bei
    # "isinsctance" werden die 13 Varianten als Unterbedingungen eingegeben + "else: print" muss noch verwendet werden.

    if isinstance(option_nr, int):  # hier gibt int bei Mismatch ein FALSE (Ergebnis) zurück
        if option_nr == 1:
            stats_analysis_opt1(stats_df)
        elif option_nr == 2:
            stats_analysis_opt2(stats_df)
        elif option_nr == 3:
            stats_analysis_opt3(stats_df)
        elif option_nr == 4:
            stats_analysis_opt4(stats_df)
        elif option_nr == 5:
            stats_analysis_opt5(stats_df)
        elif option_nr == 6:
            stats_analysis_opt6(stats_df)
        elif option_nr == 7:
            stats_analysis_opt7(stats_df)
        elif option_nr == 8:
            stats_analysis_opt8(stats_df)
        elif option_nr == 9:
            stats_analysis_opt9(stats_df)
        elif option_nr == 10:
            stats_analysis_opt10(stats_df)
        elif option_nr == 11:
            stats_analysis_opt11(stats_df)
        elif option_nr == 12:
            stats_analysis_opt12(stats_df)
        elif option_nr == 13:
            stats_analysis_opt13()  # in der Aufgabe handelt es sich um einer anderen .csv-Datei, siehe Funktion
    else:
        print("Der Report kann nicht gebaut werden")


def stats_analysis_opt1(stats_df: pd.DataFrame):  # task 2
    """ contains logic for building a report on newest stats of corona cases COUNTRY(REGION) wise

    :param stats_df: a received DataFrame with original corona stats

    :return:
        nothing is returned
    """

    global report_df

    report_df = stats_df[["Country_Region", "Confirmed", "Deaths", "Recovered", "Active"]].groupby(
        "Country_Region").sum()
    # hier wird Gebrauch von dem Split-Apply-Combine Muster gemacht:

    # stats_df[["Country_Region", "Confirmed", "Deaths", "Recovered", "Active"]] - splittet die Daten von ausgewählten
    # Spalten in eine Group. OHNE [Spaltennamen] wird das Muster auf ALLE Spalten des DFs mit NUMERISCHEN Inhalten angewendet

    # Apply & Combine Schritte werden in der Regel in Pandas zugleich ausgeführt:

    # .groupby("Country_Region") - kombiniert die Daten nach einem eingegebenen Parameter in eine Datenstruktur. Man
    # kann auch mehrere Parameter für Groupieren eingeben (siehe Funktion 2), muss dann aber ein Apply-Parameter definieren:
    # .groupby(["Country_Region", "Province_State"])["Confirmed"]

    # .sum() - wendet eine bestimmte Funktion an jede Datenstruktur der Datengroup an

    # !!!!!! .groupby().sum() != .value_counts() or .groupby().count() - listen den Zähler von Einträgen, nicht die Summe von Werten
    # Dabei .groupby().count() schließt die NaNs aus, .groupby().size() zählt auch die NaNs (also gibt einfach die Anzahl von Reihen)

    # !!!!!! .groupby().sum() == .pivot_table(values="Confirmed", index="Country_Region", aggfunc="sum")

    print("Report für Statistiken nach Ländern: \n", report_df)
    print("Reports Ausnahme für Deutschland & Russland: \n", report_df.loc[("Germany", "Russia"), :])


def stats_analysis_opt2(stats_df: pd.DataFrame):  # task 3
    """ contains logic for building a report on newest stats of dead / recovered cases COUNTRY(REGION)-PROVINCE(STATE) wise

    :param stats_df: a received DataFrame with original corona stats

    :return:
        nothing is returned
    """

    global report_df
    global rows_labels_list
    global cols_labels_list

    rows_labels_list = ["Country_Region", "Province_State"]
    cols_labels_list = ["Deaths", "Recovered"]
    # lists are declared because of the .groupby()-warning: FutureWarning: Indexing with multiple keys (implicitly
    # converted to a tuple of keys) will be deprecated, use a list instead.

    report_df = stats_df.groupby(rows_labels_list)[cols_labels_list].sum()
    # .groupby(["Country_Region", "Province_State"]) - eine Liste von Parameter für das multi-Spalten-Sortieren,
    # [("Deaths", "Recovered")] - eine Liste mit Apply-Parametern, deren Werte groupiert werden

    print("Report für Statistiken nach Ländern und deren Provinzen: \n", report_df)

    print("Reports Ausnahme für die deutschen Bundesländer: \n", report_df.loc["Germany"])


def stats_analysis_opt3(stats_df: pd.DataFrame):  # task 4
    """ contains logic for building a report on newest stats of confirmed / dead / recovered cases CHINESE PROVINCE(STATE) wise

    :param stats_df: a received DataFrame with original corona stats

    :return:
        nothing is returned
    """

    global report_df

    global cols_labels_list

    cols_labels_list = ["Confirmed", "Deaths", "Recovered"]

    report_df = stats_df[stats_df["Country_Region"] == "China"].groupby("Province_State")[cols_labels_list].sum()

    print("Report für Statistiken nach Provinzen Chinas: \n", report_df)


def stats_analysis_opt4(stats_df: pd.DataFrame):  # task 5
    """ contains logic for building a report on the LATEST death cases COUNTRY wise

    :param stats_df: a received DataFrame with original corona stats

    :return:
        nothing is returned
    """

    global report_df

    global rows_labels_list

    rows_labels_list = ["Country_Region", "Last_Update"]

    report_df = stats_df.groupby(rows_labels_list)["Deaths"].sum().sort_values(
        ascending=False)  # Gibt eine Serie zurück!
    #  pls advise: sollte der 2. Reihenindex ("Last Update") hier weggelassen werden? Manche Länder haben 2 Werten in der
    #  "Deaths" Spalte wegen unterschieldicher TimeStamps von Provinzen/Staaten

    print("Report für die aktuellsten Statistiken von Sterberaten nach Ländern: \n", report_df)


def stats_analysis_opt5(stats_df: pd.DataFrame):  # task 6
    """ contains logic for building a report on countries with no cases of corona registered

    :param stats_df: a received DataFrame with original corona stats

    :return:
        nothing is returned
    """

    global report_df

    report_df = stats_df.groupby("Country_Region")["Confirmed"].sum()  # Gibt eine Serie zurück!
    report_df = report_df.loc[report_df[:] <= 0].sort_values()  # Es wird eine Serie mit 0 Fällen aussortiert
    df_dimension = report_df.shape  # Ein Tuple mit Dimensionen eines Arrays und Anzahl der Werte in jeder Dimension.
    # Im Fall einer Serie ohne Reihen mit Werten wird (0, ) zurückgegeben

    increment = 0

    if df_dimension[0] != 0:  # Falls die ursprüngliche Serie die Reihen mit Inhalten hatte (df_dimension = (x, ) )
        print(f"Report für die Länder mit weniger als {increment} registrierten Corona Fällen: \n", report_df)

    else:  # Falls die ursprüngliche Serie keine Reihen mit Inhalten hatte (df_dimension = (0, ) )

        while df_dimension[0] == 0:
            report_df = stats_df.groupby("Country_Region")["Confirmed"].sum()  # DF wird erneut komplett erstellt
            report_df = report_df.loc[
                report_df[:] <= increment].sort_values()  # Diesmal wird die Serie mit größerem Schritt aussortiert
            df_dimension = report_df.shape  # Ein Tuple mit Dimensionen eines Arrays und Anzahl der Werte in jeder Dimension wird erneut erstellt

            print(f"Prüfe, ob es Länder mit weniger als {increment} registrierten Corona Fällen gibt...")

            if df_dimension[0] != 0:  # Falls die neueste Serie mit größerem Sorttierungsschritt Reihen mit Werten hatte
                print(f"Report für die Länder mit weniger als {increment} registrierten Corona Fällen: \n",
                      report_df)
            # Der nächste Vorgang der while-Schleife beginnt und beendet zugleich die Schleife.

            else:  # Falls die neueste Serie mit größerem Sorttierungsschritt auch keine Reihen mit Werten hatte
                print(f"Keine Länder mit bis dato weniger als {increment} registrierten Corona Fälle gefunden.")
                increment += 50
            # Der nächste Vorgang der while-Schleife beginnt mit der Suche auf Werten mit dem erhöhtem Schritt.


def stats_analysis_opt6(stats_df: pd.DataFrame):  # task 7
    """ contains logic for building a report on countries with all confirmed cases dead

    :param stats_df: a received DataFrame with original corona stats

    :return:
        nothing is returned
    """

    global report_df

    global cols_labels_list

    cols_labels_list = ["Confirmed", "Deaths"]

    report_df = stats_df.groupby("Country_Region")[cols_labels_list].sum()
    report_df = report_df[report_df["Confirmed"] == report_df["Deaths"]]

    df_dimension = report_df.shape

    if df_dimension[0] == 0:
        print("Stand heute gibt es keine Länder, wo alle registrierten Corona-Erkrankte gestorben sind")
    else:
        print(f"Report für die Länder mit allen registrierten Fällen gestorben: \n", report_df)


def stats_analysis_opt7(stats_df: pd.DataFrame):  # task 8
    """ contains logic for building a report on countries with all confirmed cases recovered

    :param stats_df: a received DataFrame with original corona stats

    :return:
        nothing is returned
    """

    global report_df

    global cols_labels_list

    cols_labels_list = ["Confirmed", "Recovered"]

    report_df = stats_df.groupby("Country_Region")[cols_labels_list].sum()
    report_df = report_df[report_df["Confirmed"] == report_df["Recovered"]]

    df_dimension = report_df.shape

    if df_dimension[0] == 0:
        print("Stand heute gibt es keine Länder, wo alle registrierten Corona-Erkrankte genesen sind")
    else:
        print(f"Report für die Länder mit allen registrierten Fällen genesen: \n", report_df)


def stats_analysis_opt8(stats_df: pd.DataFrame):  # task 9
    """ contains logic for building a report on newest stats of corona cases for TOP 10 COUNTRIES

    :param stats_df: a received DataFrame with original corona stats

    :return:
        nothing is returned
    """

    global report_df

    global rows_labels_list

    global cols_labels_list

    cols_labels_list = ["Confirmed", "Deaths", "Recovered"]

    rows_labels_list = ["Country_Region", "Last_Update"]

    stats_df["Last_Update"] = pd.to_datetime(stats_df["Last_Update"])  # irgendwie setzt pd.read_csv() in Main() trotz
    # parse_dates=True dieser Spalte ein String-Format ein. Für weiteres Resamplen von DFs braucht man unbedingt
    # DateTime-Indexen aus der "Last_Update"-Spalte zu erstellen

    stats_df.set_index(["Country_Region", "Last_Update"], inplace=True, append=False, drop=True)  # Das habe ich hier
    # gemacht, weil beim einfachen .sortby(["Country_Region", "Last_Update"])[...] lassen sich die level=1 Sub-Indexen
    # ("Last_Update") nicht im Multiindex einem level=0 Index ("Country_Region") unterordnen, obwohl die .sortby-Methode
    # standardmäßig Gruppen-Labels als Reihenindexe (Attribut: as_index=True default) des DFs setzt.

    # 3 Wege, einem bestehenden DF Multi-Indexe hinzufügen: https://www.geeksforgeeks.org/pandas-multi-index-and-groupbys/
    # Mehr zum .set_index(): https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html
    # inplace=True - Attribut ändert Indexen im bestehenden DF, anstatt ein neues zurückzugeben
    # append=False - Attribut ersetzt bereits bestehenden Indexe des DFs
    # drop=True - Attribut löscht die Spalten im DF, aus denen die neuen Indexe erstellt werden

    report_df = stats_df.groupby(by=rows_labels_list)[cols_labels_list].sum()

    # report_df_2 = stats_df.groupby(by=rows_labels_list)[cols_labels_list].sum().sort_values(by=["Confirmed"], ascending=False)
    # Die kalend.Daten werden wegen Sortiereung nach "Confirmed" gelöscht

    # report_df_3 = report_df.resample("D", level="Last_Update").sum()  - hilft nicht, die Länder werden weggelassen
    # .resample() is a time-based .groupby(), followed by a reduction method on each of its groups.

    # report_df_4 = report_df.groupby(level=report_df.index.names.difference(["Last_Update"])).sum().sort_values(by="Confirmed", ascending=False)
    # Die kalend.Daten werden gelöscht. Für Multi-Index DFs gruppiert nach allen außer der eingegebenen Spalte,
    # siehe https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html

    report_df_fin = stats_df.groupby(by=rows_labels_list)[cols_labels_list].sum().sort_values(by=["Confirmed"],
                                                                                              ascending=False)[:10]

    print(report_df.to_string())  # the problem with combining indexes level=1 is here!!!
    print(f"Report für absteigend sortierte Statistiken über Top-10 Ländern nach Gesamtfällen: \n", report_df_fin)
    # In diesem Report hat z.B. die USA nicht alle Werten aus allen "Last_Update" addiert!!! Nur der größte Wert wird aufgelistet


def stats_analysis_opt9(stats_df: pd.DataFrame):  # task 10
    """ contains logic for building a graph with newest stats for countries with deaths greater than 100.000

    :param stats_df: a received DataFrame with original corona stats

    :return:
        nothing is returned
    """

    global report_df

    global cols_labels_list

    cols_labels_list = ["Confirmed", "Deaths", "Active"]

    report_df = stats_df.groupby("Country_Region")[cols_labels_list].sum()  # Einfaches Gruppieren nach Ländern

    report_df = report_df.loc[report_df.loc[:, "Deaths"] > 100000, :].sort_values(by="Confirmed",
                                                                                  ascending=False).reset_index()
    # Auschnitt des DFs nach der Bedingung von Sterbefällen und Neuerstellung des Hauptindexes aus Zahlen

    report_df["Active"] = report_df["Confirmed"] - report_df["Deaths"]  # Da es in neueren .csv-Dateien offenbar ein
    # Fehler für die Spalten Genesene und Aktive gibt (es wird keine Statistiken veroffentlicht), wird die Spalte
    # Aktive neu gerechnet

    # Plotting

    colors = ("Blue", "Red", "Green")

    report_df.plot.bar(x='Country_Region', y=cols_labels_list, stacked=False, subplots=True, color=colors,
                       edgecolor='k', alpha=.55)  # Ein Bar-Plot wird direkt aus dem DataFrame erstellt, das Backend der
    # .plot-Methode wendet sich implizit auf Matplotlib (standardmäßig) zu

    # Subplot-Attribut wurde auf True gesetzt, da die Spalte Gestorbene wesentlich geringere Werte als die anderen
    # enthält -> Bars sind zu klein auf einer Multidata-Grafik. Stacking von Bars bringt in diesem Fall auch nichts

    # Mehr zu DF.plot: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html
    # Mehr zu DF.plot.bar: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html

    # report_df.plot.yticks(ticks=(report_df.min(axis=1), report_df.mean(axis=1), report_df.max(axis=1)))
    # Die Frage wäre: ist es möglich, für diese Grafiken die y-Ticks manuell zu ändern? .yticks() funktioniert für
    # Pandas Plot nicht...
    # https://stackoverflow.com/questions/12608788/changing-the-tick-frequency-on-x-or-y-axis-in-matplotlib
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html
    # https://newbedev.com/pandas-plot-x-axis-tick-frequency-how-can-i-show-more-ticks

    plt.tight_layout()
    plt.show()  # Matplotlib wird explizit angesprochen, um das aus dem DF erstellte Plot anzuzeigen


def stats_analysis_opt10(stats_df: pd.DataFrame):  # task 11
    """ contains logic for building a graph with newest stats for Death-Cases in the States of the USA

    :param stats_df: a received DataFrame with original corona stats

    :return:
        nothing is returned
    """

    global report_df

    report_df = stats_df.loc[stats_df.loc[:, "Country_Region"] == "US"].groupby("Province_State")[
        "Deaths"].sum().sort_values(ascending=False)

    print(report_df)

    # Plotting

    bars_colors = "Red"

    wedges_explosion = []

    fill_pie_explosion_list(report_df, wedges_explosion)  # Ist es besser, die Helferfunktion mit einem return-Parameter
    # der Variable wedges_explosion einfach zu verweisen? Aka wedges_explosion = fill_pie_explosion_list(report_df)

    report_df.plot.pie(y='Active', rotatelabels=True, labeldistance=1.2, explode=wedges_explosion)
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html

    plt.tight_layout()
    plt.show()


def stats_analysis_opt11(stats_df: pd.DataFrame):  # task 12
    """ contains logic for building a graph with newest stats for active Corona-Cases in the States of the USA

    :param stats_df: a received DataFrame with original corona stats

    :return:
        nothing is returned
    """

    global report_df

    global cols_labels_list

    cols_labels_list = ("Confirmed", "Deaths", "Active")

    report_df = stats_df.loc[stats_df.loc[:, "Country_Region"] == "US"].groupby("Province_State")[
        cols_labels_list].sum()

    report_df["Active"] = report_df["Confirmed"] - report_df["Deaths"]

    report_df = report_df.loc[:, "Active"].sort_values(ascending=False)

    print(report_df)

    # Plotting

    wedges_explosion = []

    fill_pie_explosion_list(report_df, wedges_explosion)

    report_df.plot.pie(y='Active', rotatelabels=True, labeldistance=1.2, explode=wedges_explosion)
    # https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.pie.html

    plt.tight_layout()
    plt.show()


def stats_analysis_opt12(stats_df: pd.DataFrame):  # task 13
    """ contains logic for building a graph with the newest stats of Corona-Cases in the States of the USA

    :param stats_df: a received DataFrame with original corona stats

    :return:
        nothing is returned
    """

    global report_df

    global cols_labels_list

    cols_labels_list = ("Confirmed", "Deaths", "Active")

    report_df = stats_df.loc[stats_df.loc[:, "Country_Region"] == "US"].groupby("Province_State")[
        cols_labels_list].sum()

    report_df["Active"] = report_df["Confirmed"] - report_df["Deaths"]

    report_df = report_df.sort_values(by="Confirmed", ascending=True)

    # plotting
    # Die Idee wurde hier gefunden: https://stackoverflow.com/questions/24183101/pandas-bar-plot-with-two-bars-and-two-y-axis

    bars_width = .3

    plotting_figure = plt.figure(figsize=(20, 6))  # Erstellen einer matplotlib-Figur, default: figsize=[6.4, 4.8]

    axes_object_1 = plotting_figure.add_subplot()  # Erstellen eines Axes-Wesens, das in sich Figuren-Elemente (wie
    # Axis, Tick, Linie, Text) und das Koordinatensystem enthält. Mehr dazu: https://matplotlib.org/stable/api/axes_api.html

    axes_object_2 = axes_object_1.twinx()  # Erstellen eines zweiten Axes-Wesens, das mit dem ersten die X-Achse teilt

    confirmed_bars = report_df.Confirmed.plot(kind='bar', color='grey', ax=axes_object_1, width=bars_width, position=2, label="Registrierte Fälle")
    active_bars = report_df.Active.plot(kind='bar', color='blue', ax=axes_object_1, width=bars_width, position=1, label="Aktive Fälle")
    deaths_bars = report_df.Deaths.plot(kind='bar', color='red', ax=axes_object_2, width=bars_width, position=0, label="Gestorbene")
    # position=0.5 ist ein Attribut, das standardmäßig die Bars überschneiden lässt

    axes_object_1.set_ylabel('Confirmed & Active')
    axes_object_2.set_ylabel('Deaths')

    axes_object_1.tick_params(axis='x', labelrotation=35)
    axes_object_2.tick_params(axis='x', labelrotation=35)

    axes_object_1.legend(loc='upper left')  # hier übernimmt Labels aus der Grafik-Variable, die können aber auch hier
                            # eingegeben werden: ax.legend([gr1, gr2, ...], [lbl1, lbl2, ...])
    axes_object_2.legend(loc=9)  # loc Atributen haben auch Ziffer-Codes: 9 = 'upper center'
                                            # https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.legend.html

    # legend = axes_object_1.legend([(confirmed_bars, active_bars), deaths_bars], ['Confirmed Active', 'Deaths'], scatterpoints=1,
    #         numpoints=1, handler_map={tuple: HandlerTuple(ndivide=None)}, loc="upper left")
    # Problem hier: die komplexe Legende funktioniert nicht. 2 einfachen Legenden überschneiden sich
    # Beispiel gefunden hier: https://matplotlib.org/stable/gallery/text_labels_and_annotations/legend_demo.html

    axes_object_1.set_title("Aktuellste Corona-Statistiken nach den Staaten der USA")

    plt.tight_layout()
    plt.show()


def fill_pie_explosion_list(df: pd.DataFrame, explosions_list: list):
    """ this helper function fills a list with the same integers that are used for explosion of axes of massive pie
    charts in Tasks 11 & 12

    estimates the amount of integers based on the length of a received DataFrame

    :param df:
        a plotting-ready DataFrame filtered and sorted within a task function

    :param explosions_list:
        an empty list from a task function to be filled with integers

    :return:
        nothing is returned

    """

    df_length = len(df.index)  # df.index gibt ein Tuple von Indexen eines DataFrames wieder, len() gibt die Länge
    # eines Array-ähnlichen Objekts wieder
    print(f"Das DataFrame enthält {df_length} Elemente")
    iterator = 0

    while iterator < df_length:
        explosions_list.append(.1)
        iterator += 1


def stats_analysis_opt13():  # task 14
    """ creates 3 DataFrames from TimeSeries .csv-files for Confirmed / Deaths / Recovered global cases found @
    https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series

    groups statistics of each country within each DataFrame into monthly values to reflect the change of the
    worldwide statistic over time

    builds a Multidata-Line Graph to represent a change of Corona Statistic over time

    :return:
        nothing is returned
    """

    confirmed_stats_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master'
                                     '/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')

    deaths_stats_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master'
                                  '/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')

    # recovered_stats_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master'
    #                                 '/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    # Recovered-Statistiken sind auf dem Server fehlerhaft, deren Rechnung ist hier deaktiviert

    confirmed_stats_df = create_total_df(confirmed_stats_df)

    deaths_stats_df = create_total_df(deaths_stats_df)

    # recovered_stats_df = create_total_df(recovered_stats_df)
    # Recovered-Statistiken sind auf dem Server fehlerhaft, deren Rechnung ist hier deaktiviert

    # Plotting

    figure = plt.figure(figsize=(12, 6))

    axes_1 = figure.add_subplot()

    confirmed_line = confirmed_stats_df.plot.line(x="Date", ax=axes_1, color="blue", lw=2, label='Registrierte Fälle', linestyle='dashed')
    deaths_line = deaths_stats_df.plot.line(x="Date", ax=axes_1, color="red", lw=1, label='Gestorbene', linestyle='dashdot')
    # Mehr zu Line-2D Eigenschaften: https://matplotlib.org/2.0.2/users/pyplot_tutorial.html

    axes_1.set_title("Entwicklung der weltweit registrierten Corona-Fälle")

    axes_1.legend()

    axes_1.grid(True)

    plt.tight_layout()
    plt.show()


def create_total_df(timeseries_df: pd.DataFrame):
    """ this helper function transforms DataFrames to the format used for global over-time dynamics of corona stats
    in task 14

    :param timeseries_df:
        a DataFrame created from a time-series .csv file on a server

    :return:
        a ready for plotting DataFrame
    """

    result_df = timeseries_df.iloc[:, 5:].transpose()  # alle .csv time-series Dateien haben das älteste Datum in
    # der Spalte 5, das neueste - in der letzten Spalte

    result_df.index.name = "Date"  # ? ähnlich dem .index.set_name() ?

    result_df = result_df.sum(axis=1)  # axis=1 bezieht sich auf Spalten, d.h. addiert den Reihen (Indexen) nach

    print(result_df)

    return result_df
