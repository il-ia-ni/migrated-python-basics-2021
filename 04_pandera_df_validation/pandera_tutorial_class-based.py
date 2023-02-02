"""
Dieses Skript enthält Informationen zu Datenvalidierung mithilfe vom Klassen-basierten API (inspiriert durch Pydantic
@ https://pydantic-docs.helpmanual.io/ sowie durch Datenklassen @ https://docs.python.org/3/library/dataclasses.html)
für Definierung von Schemata Modelen

Siehe @ https://pandera.readthedocs.io/en/stable/schema_models.html#schema-models
"""

import pandas as pd
import pandera as pa
from pandera.typing import (
    DataFrame,
    Series,
)  # are used in SchemaModel-classes for type annotation validation of DFs
from typing import (
    Optional,
    Dict,
)  # By default all columns specified in the schema are required,

# BSP1: direkte Validierung eines DataFrames mithilfe einer Schemaklasse

df1 = pd.DataFrame(
    {
        "column1": [1, 4, 0, 10, 9],
        "column2": [-1.3, -1.4, -2.9, -10.1, -20.4],
        "column3": ["value_1", "value_2", "value_3", "value_2", "value_1"],
    }
)


# Models can be explicitly converted to a DataFrameSchema Instance (object-based API) using Schema.to_schema()
# or used to validate a DataFrame directly, either with a class method .validate or by referring to the schema in type
# annotations of a callable function wrapped with a pandera decorator (see BSP2).
class Schema(pa.SchemaModel):
    # !!! Class attributes which begin with an _underscore will be automatically excluded from the model. 'Config' is
    # also a reserved name. However, aliases can be used to circumvent these limitations (see BSP4).
    column1: Series[int] = pa.Field(
        le=10
    )  # column/index fields are defined as class attributes in Class-based API.
    # They must receive TYPES (a: Series[pd.StringDtype]) and not INSTANCES
    # (a: Series[pd.StringDtype()])
    column2: Series[float] = pa.Field(
        lt=-1.2
    )  # pa.Fields apply to BOTH Column AND Index objects of a DF. The built-in
    # pandera Checks are based on key-word arguments (Schema class attributes' names,
    # they have to correspond to either cols or idxs of a DF)
    column3: Optional[Series[str]] = pa.Field(
        str_startswith="value_"
    )  # Optional[] annotation makes a column optional

    @pa.check("column3")
    def column_3_check(cls, series: Series[str]) -> Series[bool]:
        """Check that column3 values have two elements after being split with '_'"""
        return series.str.split("_", expand=True).shape[1] == 2


Schema.validate(
    df1
)  # you can also use the SchemaModel() class directly to validate dataframes, which is syntactic


# sugar that simply delegates to the validate() method: Schema(df)


# BSP2: Erstellung eines Validierungsdekorators für eine mit einem DF interagierende 'callable' Funktion

# Models can be explicitly converted to a DataFrameSchema Instance (object-based API) using InputSchema.to_schema()
# # or used to validate a DataFrame directly, either with a class method .validate or by referring to the schema in type
# # annotations of a callable function wrapped with a pandera decorator.

# Schema Models are annotated with the pandera.typing (See @https://pandera.readthedocs.io/en/stable/reference/generated/pandera.typing.html#module-pandera.typing)
# module using the standard typing syntax.
#
# STATIC VS DYNAMIC TYPE CHECK
# Due to pandas limitations, pandera annotations are only used for RUNTIME VALIDATION (dynamic type check) and cannot be
# leveraged by static-type checkers like mypy. More on STATIC vs DYNAMIC type check
# @ https://thecodeboss.dev/2015/11/programming-concepts-static-vs-dynamic-type-checking/.

# != the difference between Types and Classes @ https://www.python.org/dev/peps/pep-0483/#types-vs-classes (Class is a
# dynamic, runtime concept. Type is a set of values and a set of functions that one can apply to these values, can
# however be either validated at compile time (i.e. statically) or at runtime (i.e. dynamically))

# != strongly-typed language (variables are bound to specific data types, these are explicitly defined when initializing
# a variable) vs weakly-typed language. Even Python, JS are STRONGLY TYPED, even without verbose type definition of a var:
# they receive a type implicitly, based on a var's value (TYPE INFERENCE).
# PHP (dynamic language) or C (static language) are weakly-typed, "2" + 4 = 6, no type error is raised.
class InputSchema(pa.SchemaModel):
    # year: Index[int] = pa.Field(gt=2000, coerce=True)
    # month: Index[int] = pa.Field(ge=1, le=12, coerce=True)  # Multiple Index annotations are automatically converted
    # into a MultiIndex. MultiIndex options are given in the Config subclass.
    year: Series[int] = pa.Field(gt=2000, coerce=True)
    month: Series[int] = pa.Field(ge=1, le=12, coerce=True)
    day: Series[int] = pa.Field(ge=0, le=365, coerce=True)
    weather: Optional[Series[str]] = pa.Field(
        str_startswith="Weather_"
    )  # Optional[] annotation makes a column optional

    class Config:  # Schema-wide options can be controlled via the Config subclass of a SchemaModel class. Must always
        # be named ‘Config’! All options are @ https://pandera.readthedocs.io/en/stable/reference/generated/pandera.model.BaseConfig.html#pandera.model.BaseConfig
        name = "BaseSchema"
        strict = True
        coerce = False
        #foo = "bar"  # Interpreted as a registered dataframe check. See @ https://pandera.readthedocs.io/en/stable/extensions.html#class-based-api-dataframe-checks
        # provide multi index options in the config:
        # multiindex_name = "time"
        # multiindex_strict = False
        # multiindex_coerce = True

    @pa.check("year", name="foobar", raise_warning=True)  # Unlike the object-based API (https://pandera.readthedocs.io/en/stable/checks.html), custom checks can be
    # specified as CLASS methods for DataSchema. Similarly to pydantic, classmethod() decorator is added behind the
    # scenes, if omitted.
    # Since @checks are class methods, the first argument value they receive is a SchemaModel SUBCLASS, NOT an INSTANCE
    # of a model of the subclass -> static class methods never have an access to instances and cannot change their attributes!
    # Keyword argument RAISE_WARNING calls a UserWarning instead of raising an exception, validation is succeeded! See @ https://pandera.readthedocs.io/en/stable/reference/generated/pandera.checks.Check.html#pandera.checks.Check
    def custom_check(cls, year: Series[int]) -> Series[bool]:
        return year > 2000

    # @pa.check(
    #     "value", groupby="group", regex=True, name="check_means"
    # )  # key-word arguments of the Check class
    # # initializer can be provided to get the flexibility of groupby checks
    # def check_groupby(cls, grouped_value: Dict[str, Series[int]]) -> bool:
    #     return grouped_value["A"].mean() < grouped_value["B"].mean()


class OutputSchema(InputSchema):  # Durch die Vererbung über die InputSchema erweiterte Validierungschema
    revenue: Series[float]


""" Validating a DF using a Schema Class"""
@pa.check_types  # Validate a callable function's inputs AND output based on TYPE ANNOTATIONS (See @ https://docs.python.org/3.9/library/typing.html#typing.overload
# and @ https://www.python.org/dev/peps/pep-0483/) on RUNTIME (DYNAMIC type check, increases overhead for the callable function).

# On the other hand there are 3 pandera Decorators (@check_input, @check_output, @check_io) that are based on the
# object-based API Schemas instances of the DataFrameSchema class. They allow to check a callback function's DF-arguments
# or returned DFs in an existing Pipeline Integration (https://www.dataquest.io/blog/data-pipelines-tutorial/)
# in the same manner the class-based API's @check_type does. See @ https://pandera.readthedocs.io/en/stable/decorators.html.
def transform(
    df: DataFrame[InputSchema],
) -> DataFrame[OutputSchema]:  # the callable function, InputSchema and OutputSchema
    # are used in type annotations of args and output accordingly
    return df.assign(revenue=100.0)


df2 = pd.DataFrame(
    {
        "year": ["2001", "2002", "2003"],
        "month": ["3", "6", "12"],
        "day": ["200", "156", "365"],
    }
)

transform(df2)  # Valideierung ist erfolgreich

invalid_df = pd.DataFrame(
    {
        "year": ["2001", "2002", "1999"],
        "month": ["3", "6", "12"],
        "day": ["200", "156", "365"],
    }
)
#transform(invalid_df)  # gibt ein Fehler zurück, ein Jahr 1999 passt nicht zur Schema

InputSchema.year  # calling a Schema class attribute returns just a string ("year"). Is useful for DF reading:
print(f"Reading a DF by cols names {InputSchema.year} and {InputSchema.day}\n")
print(df2.loc[:, [InputSchema.year, InputSchema.day]])


# BSP3 - Validate a pandas DF on its' initialization using panderas typing module type annotation DataFrame([data, index, columns, dtype, copy])

class Schema2(pa.SchemaModel):
    state: Series[str]
    city: Series[str]
    price: Series[int] = pa.Field(in_range={"min_value": 5, "max_value": 20})


pa_df = DataFrame[Schema2](  # Initializes a DF with its' direct validation.
    # API for validating DFs on their initialization uses the pandera.typing.pandas.DataFrame
    # generic type DataFrame, not of pandas! Can also work with datasets of other libraries, see
    # @ https://pandera.readthedocs.io/en/stable/supported_libraries.html#supported-dataframe-libraries
    {
        "state": ["NY", "FL", "GA", "CA"],
        "city": ["New York", "Miami", "Atlanta", "San Francisco"],
        "price": [8, 12, 10, 16],
    }
)
print(pa_df)


# BSP4: Aliases für nicht unterstützte Namen von Spalten / Indexen

class SchemaWithAlias(pa.SchemaModel):
    col_2020: pa.typing.Series[int] = pa.Field(
        alias=2020
    )  # int cannot be a var annotation in SchemaModels. In this
    # example 'col_2020' is alias of 2020
    idx: pa.typing.Index[int] = pa.Field(
        alias="_idx", check_name=True
    )  # # !!! Class attributes which begin with an

    # _underscore are automatically excluded from the model. In
    # this example 'idx' is alias of '_idx'

    @pa.check(2020)  # == @pa.check(col_2020)
    def int_column_lt_100(cls, series):
        return series < 100


underscore_idx_df = pd.DataFrame({2020: [99]}, index=[0])
underscore_idx_df.index.name = "_idx"

print(SchemaWithAlias.validate(underscore_idx_df))

SchemaWithAlias.col_2020  # Returns not "col_2020" but 2020!!! (Beginning with pandera v.0.6.2)
