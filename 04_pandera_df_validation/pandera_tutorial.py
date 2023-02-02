"""
Dieses Skript enthält Informationen zu Datenvalidierung mithilfe vom Objekt-basierten API sowie Grundlagen der Pandera
Bibliothek für Definierung von Schemata Modelen

Siehe @ https://towardsdatascience.com/how-automated-data-validation-made-me-more-productive-7d6b396776
"""

import pandera as pa
import pandas as pd


def main():
    """Normale vs Strenge Validierung"""

    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/12-20-2021.csv"
    corona_cases_df = pd.read_csv(url, parse_dates=[4])

    print("The data set contains following columns:\b")
    print(corona_cases_df.info())

    # Initializing an object (instance) of the schema of the data we expect (object-based API).
    # See more @ https://pandera.readthedocs.io/en/stable/reference/generated/pandera.schemas.DataFrameSchema.html#pandera.schemas.DataFrameSchema

    # In case the schema cannot be initialized with set params raises a SchemaInitError
    # In case of unsuccessful validation (using method schema.validate(dataset) of a data set raises a SchemaError
    # In case of succeeded validation returns the data set itself (DF or Series)
    strict_schema = pa.DataFrameSchema(
        columns={
            # 'columns='-named property can be dispensed (see next schemas)
            # All .Column params are available @ https://pandera.readthedocs.io/en/v0.3.2/generated/pandera.Column.html
            "FIPS": pa.Column(float, nullable=True),
            # datatypes can be declared as native python ones OR pandas legal dtypes as str ("float64") OR as a pa.Float etc
            # nullable=True if we expect/allow NaN values for this column, else - False (default value!)
            "Admin2": pa.Column(pa.Object, nullable=True),
            "Province_State": pa.Column(pa.Object, nullable=True),
            "Country_Region": pa.Column(
                pa.String, nullable=False
            ),  # String and Object are interchangeable?
            "Last_Update": pa.Column(pa.DateTime, nullable=False),
            "Lat": pa.Column(pa.Float, nullable=True),
            "Long_": pa.Column(pa.Float, nullable=True),
            "Confirmed": pa.Column(
                pa.Int, nullable=False
            ),  # nullable=False is the default value, doesn't have to be declared
            "Vaccinated": pa.Column(
                pa.Int, nullable=True, required=False
            ),  # requiered=False makes column optional
            "Deaths": pa.Column(
                pa.Int, nullable=False, required=True
            ),  # requiered=True makes column obligatory (default value)
            "Recovered": pa.Column(pa.Float, nullable=True),
            "Active": pa.Column(pa.Float, nullable=True),
            "Combined_Key": pa.Column(pa.Object, nullable=False),
            "Incident_Rate": pa.Column(
                pa.String, nullable=True, coerce=True
            ),  # coerce=True forces conversion of the
            # datatype to the one in scheme if the one received is not the same, otherwise error! (Here - Float gets converted to String)
            "Case_Fatality_Ratio": pa.Column(pa.Float, nullable=True),
        },
        strict=True,  # strict=True doesn't allow any other columns be added to a DF if not registered in the schema
        ordered=False,  # ordered=False allows columns to be in a different order in a data set than in a schema
        name="strict_initial_schema",  # an optional name of a schema
        coerce=False,  # a forced conversion of datatypes can be done globally instead of single props of each Column
    )

    not_strict_schema = pa.DataFrameSchema(
        {
            "FIPS": pa.Column(pa.Float, nullable=True),
            "Admin2": pa.Column(pa.Object, nullable=True),
            "Province_State": pa.Column(pa.Object, nullable=True),
            "Country_Region": pa.Column(pa.String, nullable=False),
            "Last_Update": pa.Column(pa.DateTime, nullable=False),
            "Lat": pa.Column(pa.Float, nullable=True),
            "Long_": pa.Column(pa.Float, nullable=True),
            "Confirmed": pa.Column(pa.Int, nullable=False),
            "Vaccinated": pa.Column(pa.Int, nullable=True, required=False),
            "Deaths": pa.Column(pa.Int, nullable=False, required=True),
            "Recovered": pa.Column(pa.Float, nullable=True),
            "Active": pa.Column(pa.Float, nullable=True),
            "Combined_Key": pa.Column(pa.Object, nullable=False),
            "Incident_Rate": pa.Column(pa.String, nullable=True, coerce=True),
            "Case_Fatality_Ratio": pa.Column(pa.Float, nullable=True),
        },
        strict=False,
    )  # strict=False allows any other columns added to a DF that are not registered in the scheme

    # Strenge Datenvalidierung
    # Es gibt 2 Wege, mit dem objekt-basierten API von pandera die Validierung durchzuführen: siehe Zeilen 103 & 108
    print("A strict validation schema has been created:\n", strict_schema)

    corona_cases_df["Total_cases"] = (
            corona_cases_df["Confirmed"] + corona_cases_df["Deaths"]
    )
    print(
        "The DF has been extended with a new column: {}".format(
            corona_cases_df.columns[-1]
        )
    )

    input("Press any key to strictly validate the DF without updating the schema...")

    try:
        validation_result = strict_schema.validate(  # Validation WAY 1: calling a .validate Schemainstance method
            corona_cases_df, lazy=True
        )  # lazy=True gives a more detailed report
        # on a failed validation with tips for errors

        # Validation WAY 2: In case a DF is created by a function there are 3 pandera Decorators( @ check_input,
        # @check_output, @check_io) that are based on the object-based API Schemas instances of the DataFrameSchema,
        # but allow to check the callback function's DF-arguments or returned DFs in an existing Pipeline Integration
        # (https://www.dataquest.io/blog/data-pipelines-tutorial/) in the same manner the class-based API does. See
        # @ https://pandera.readthedocs.io/en/stable/decorators.html.
        print(
            "Strict validation succeeded, returning an object:",
            type(validation_result),
            "with following columns:",
        )
        print(corona_cases_df.info())

    except Exception as e:
        print(
            f"Validation error for the strict validation: \n{e}\nPlease try a non-strict validation!\n"
        )

    # Normale Datenvalidierung

    input("Press any key to non-strictly validate the DF...")

    try:
        validation_result2 = not_strict_schema.validate(corona_cases_df, lazy=True)
        print(
            "Not strict validation succeeded, returning an object:",
            type(validation_result2),
            "with following columns:",
        )
        print(corona_cases_df.info())

    except Exception as e:
        print(
            f"Validation error {e} for the non-strict validation! Please check the data set.\b"
        )

    """ Validierung von Indexen """

    idx_schema = pa.DataFrameSchema(
        {
            "FIPS": pa.Column(pa.Float, nullable=True),
            "Admin2": pa.Column(pa.Object, nullable=True),
            "Province_State": pa.Column(pa.Object, nullable=True),
            "Country_Region": pa.Column(pa.String, nullable=False),
            "Last_Update": pa.Column(pa.DateTime, nullable=False),
            "Lat": pa.Column(pa.Float, nullable=True),
            "Long_": pa.Column(pa.Float, nullable=True),
            "Confirmed": pa.Column(pa.Int, nullable=False),
            "Vaccinated": pa.Column(pa.Int, nullable=True, required=False),
            "Deaths": pa.Column(pa.Int, nullable=False, required=True),
            "Recovered": pa.Column(pa.Float, nullable=True),
            "Active": pa.Column(pa.Float, nullable=True),
            "Combined_Key": pa.Column(pa.Object, nullable=False),
            "Incident_Rate": pa.Column(pa.String, nullable=True, coerce=True),
            "Case_Fatality_Ratio": pa.Column(pa.Float, nullable=True),
            "Total_cases": pa.Column(pa.Int, nullable=False, required=True),
        },
        index=pa.Index(
            # Index can be validated, f.e. for any specific pattern or if it is of any special importance in a dataset
            pa.String, pa.Check(lambda x: x.str.startswith("index_0"))
        ),
        strict=True,
    )

    idx_corona_cases_df = corona_cases_df.copy()
    idx_corona_cases_df["idx"] = idx_corona_cases_df["Combined_Key"].apply(
        lambda x: "index_" + str(x)
    )
    idx_corona_cases_df.set_index("idx", inplace=True)
    idx_corona_cases_df.index.name = None

    # Index Validierung
    input("Press any key to validate the indexed DF...")
    print(idx_corona_cases_df)
    print(idx_schema)

    try:
        validation_result3 = not_strict_schema.validate(idx_corona_cases_df, lazy=True)
        print(
            "Index validation succeeded, returning an object:",
            type(validation_result3),
            "with following columns:",
        )
        print(idx_corona_cases_df.info())

    except Exception as e:
        print(
            f"Validation error {e} for the index validation! Please check the data set."
        )

    """ Transformation von DataSchema Instanzen """

    # Neue Spalten hinzugefügt
    corona_cases_df["Virus_mutation"] = "Not reported"
    input(
        "New column {} has been added to the DF! \nPress any key to extend the non-strict schema and validate the "
        "DF...".format(corona_cases_df.columns[-1])
    )

    extended_schema = not_strict_schema.add_columns(
        {  # Params of the added cols have to be specified in the schema
            "Virus_mutation": pa.Column(pa.String, nullable=False, required=True)
        }
    )

    try:
        print("The schema was extended: \b", extended_schema)
        validation_result4 = extended_schema.validate(corona_cases_df, lazy=False)
        print(
            "Non-strict validation using the extended schema succeeded, returning an object:",
            type(validation_result4),
            "with following columns:",
        )
        print(corona_cases_df.info())

    except Exception as e:
        print(
            f"Validation error {e} for the extended validation! Please check the data set."
        )

    # Spalten entfernt
    to_remove_list = ["FIPS", "Admin2", "Lat", "Long_"]
    light_corona_cases_df = corona_cases_df.drop(columns=to_remove_list)

    input(
        f"Following columns were removed from the DF: {to_remove_list}! \n Press any button to shrink the non-strict "
        f"schema and validate the light DF...."
    )

    shrunk_schema = extended_schema.remove_columns(
        to_remove_list
    )  # cols just have to be removed from the schema

    try:
        print("The schema was shrunk: \b", shrunk_schema)
        validation_result5 = shrunk_schema.validate(light_corona_cases_df, lazy=False)
        print(
            "Non-strict validation using the shrunk schema succeeded, returning an object:",
            type(validation_result5),
            "with following columns:",
        )
        print(light_corona_cases_df.info())

    except Exception as e:
        print(f"Validation error {e} of the shrunk DF! Please check the data set.")

    """ Validierung von Werten einer Spalte mit .Check-Eigenschaft """

    # Check-Objekt-Leitfaden: @ https://pandera.readthedocs.io/en/stable/checks.html#checks inkl. Handling Null Values,
    # Column Check Groups, Wide Checks and Raising UserWarnings on Check Failure

    # Alle standarden Check-Methoden der Pandera (eq/ge/gt/in_range/isin/le/ne/str_contains/str_length etc) sind hier:
    # @ https://pandera.readthedocs.io/en/stable/reference/generated/pandera.checks.Check.html#pandera.checks.Check

    # Siehe auch Great Expectations Bibliothek für Daten-validating, -documenting, -profiling
    # @ https://docs.greatexpectations.io/docs/

    mutations_list = ["Not reported", "British", "South African", "Delta", "Omicron"]

    # By default pa.Check applies a rule on a SERIES of data (faster way). element_wise=True needs to be set otherwise
    # NULL values are EXCLUDED from the check! ignore_na=False needs to be set if Nulls are important

    # Any failures of a values check raise a Validation error with all failure cases from a SchemaError exception
    # To change this behavior and continue execution of code, raise_warning=True needs to be set for Check / Hypothesis.
    # See @ https://pandera.readthedocs.io/en/stable/checks.html#raise-userwarning-on-check-failure
    values_check_schema = pa.DataFrameSchema(
        {
            "FIPS": pa.Column(pa.Float, nullable=True),
            "Admin2": pa.Column(pa.Object, nullable=True),
            "Province_State": pa.Column(
                # !!! Im Unterschied zu statischen Klassenmethoden des class-basierten API für Checks, die Check-
                # Methoden im objekt-basierten API sind Methoden der Instanz -> sie können die Instanz des Schemas ändern
                # Siehe Skript 'pandera_tutorial_class-based.py' zu statischen Checks der SchemaModel-Klasse.
                pa.Object, pa.Check.str_matches(r"^[A-Za-z- .*,\'()]+$"), nullable=True
            ),  # use Regex to validate the symbols in a str
            "Country_Region": pa.Column(
                pa.String,
                checks=pa.Check.str_length(
                    min_value=4, max_value=30, raise_warning=True
                ),
            ),  # checks the str length
            # 'checks=' named-property is not obligatory for single checks, can also take lists of pa.Check.xyz-s for
            # complex checks of values validity !
            "Last_Update": pa.Column(
                pa.DateTime,
                pa.Check.greater_than_or_equal_to(
                    min_value="2021-12-01 00:00:00", raise_warning=True
                ),
                nullable=False,
            ),  # checks if the dates are newer than
            "Lat": pa.Column(pa.Float, nullable=True),
            "Long_": pa.Column(pa.Float, nullable=True),
            "Confirmed": pa.Column(
                pa.Int, pa.Check.greater_than_or_equal_to(0), nullable=False
            ),
            "Vaccinated": pa.Column(pa.Int, nullable=True, required=False),
            "Deaths": pa.Column(pa.Int, nullable=False, required=True),
            "Recovered": pa.Column(pa.Float, nullable=True),
            "Active": pa.Column(pa.Float, nullable=True),
            "Combined_Key": pa.Column(pa.Object, nullable=False),
            "Incident_Rate": pa.Column(pa.String, nullable=True, coerce=True),
            "Case_Fatality_Ratio": pa.Column(pa.Float, nullable=True),
            "Total_cases": pa.Column(
                pa.Int,
                pa.Check(
                    lambda x: (isinstance(x, int) and x >= 0),
                    error="ttl cases must be a positive integer",
                    raise_warning=False,
                    ignore_na=False,
                ),
            ),
            # custom labmda functions for Check allow extra params and complex grouping of a DF/creating new cols at the end
            # of a succeeded validation. See @ https://pandera.readthedocs.io/en/stable/checks.html#column-check-groups
            # error=""-parameter takes custom error message for a not passed check result
            # raise_warning=False (default) stops the code execution and raises Error. If True - code is executed further
            # ignore_na=False (def. True) parameter doesn't exclude null values of a DF before the validation
            "Virus_mutation": pa.Column(
                pa.String, pa.Check.isin(mutations_list)
            ),  # checks if value is allowed
        },
        strict=False,
    )

    try:
        input("Press any key to validate the DF with also checking data values...")
        validation_result6 = values_check_schema.validate(corona_cases_df, lazy=True)
        print(
            "validation using the values check schema succeeded, returning an object:",
            type(validation_result6),
            "with following columns:",
        )
        print(corona_cases_df.info())

    except Exception as e:
        print(f"Validation error {e} of the values check! Please check the data set.")


main()
