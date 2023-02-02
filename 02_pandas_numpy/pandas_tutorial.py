"""
This script is dedicated to the Pandas library for Python, DataFrames and TimeStamps
"""

import pandas as pd  # Pandas is usually imported under the pd alias.
import os
import pathlib
from datetime import date, time

# Pandas is used for working with data sets to analyze data. It has functions for analyzing,
# cleaning, exploring, and manipulating data. The name has a reference to both "Panel Data" and "Python Data
# Analysis" and was created by Wes McKinney in 2008.
# Allows analysis of big data and make conclusions based on statistical theories.
# Can clean messy data sets, make them readable and relevant, delete not relevant rows / with wrong values (null etc).
# Typical questions Pandas can answer: correlation between columns? average value? max / min value?

def series_and_labels():
    """
  contains tutorial to Pandas Series and their labels
  :return: nothing
  """

    # A Pandas Series is like a COLUMN in a table. It is a one-dimensional array containing elements (data) of any
    # type (i.e. potentially heterogeneous). In the next case is created from from a list (Items MUST NOT REPEAT!!!).
    subjects_list = ["EVP", "SWD", "ITD"]

    my_subjects_series = pd.Series(subjects_list)

    print(my_subjects_series)

    # Labels: if nothing else is specified, the values are LABELED with their index number (by default):
    # First value has index 0, second value has index 1 etc. This label can be used to access a specified value.
    print(my_subjects_series[0])

    # creating custom labels using 'INDEX'-argument of the Series() Method
    my_subjects_series_index = pd.Series(subjects_list, index=["LF1", "LF2", "LF3"])

    # Creating a Series from a dictionary (Key/Value Object) selecting only specified keys
    subjects_dict = {"LF1": "EVP", "LF2": "SWD", "LF3": "ITD"}

    my_subjects_series_dict = pd.Series(subjects_dict, index=["LF1", "LF2"])


def dataframes_basics():
    """
    contains tutorial to Pandas DataFrames basic operations
    :return: nothing
    """
    # A Pandas DataFrames is like a WHOLE table with rows and columns. It is a multi-dimensional (2-dimensional)
    # array containing elements (data) of any type (i.e. potentially heterogeneous) with labeled axes (rows and columns)

    # In the real world a DataFrame is created by loading the datasets from existing storage: an SQL Database,
    # a CSV / Excel file, etc. DataFrames can also be created from Python lists, dictionaries, lists of dictionaries etc

    # In the next case a DataFrame is created from from a dictionary of 2 lists (arrays).

    data_dict = {
        "calories": [420, 380, 390],
        "duration": [50, 40, 45]
    }

    data_frame = pd.DataFrame(data_dict)

    print("A DataFrame made from a dictionary:", data_frame)  # ! By default printing a DataFrame displays only a
    # reduced sample with the FIRST 5 rows AND the LAST 5 rows

    # .LOC-attribute of the .DataFrame method is used to get or set a specific ROW (group of elements) of a DataFrame
    # through referring to INDEX(es) (LABEL(s)) of the row(s):
    print("LOC: row 1 (index 0) of the DF:", data_frame.loc[0])  # returns a SERIES: "calories 420, duration 50" + name
    # (here: 0) + dtype (here: int64)
    print("LOC: rows 2 and 3 (indexes 1 & 2) of the DF:", data_frame.loc[[1, 2]])  # returns a DataFrame "calories,
    # duration" as column names and "0, 1" as NEW indexes

    # .ILOC-attribute gets or sets the values of a group of elements in their specified positions using both ROW- and
    # COLUMN indexes of each specific element to be returned:
    print("ILOC: element from row 2 (index 1) AND column 1 (index 0) of the DF:", data_frame.iloc[1, 0])

    # Creating a DataFrame with a list of custom indexes + using LOC to return a specified row(s):
    data_frame_daily = pd.DataFrame(data_dict, index=["day1", "day2", "day3"])

    print("LOC: addressing element through a custom index of DF:", data_frame_daily.loc["day2"])

    # More ways of viewing the data from DateFrames + removing null values + data analysis basics

    # df.HEAD() method: a quick overview returning the HEADERS and a specified number of ROWS, starting from the TOP.
    # If the amount of rows is not specified, returns the first 5 rows only
    print("displaying first 2 elements of the DF using .head():", data_frame_daily.head(2))

    # df.TAIL() method: a quick overview returning the HEADERS and a specified number of ROWS, starting from the BOTTOM.
    # If the amount of rows is not specified, returns the first 5 rows only
    print("displaying last 2 elements of the DF using .tail():", data_frame_daily.tail(2))

    # df.INFO() method returns information about elements (data) within a DataFrame, such as RangeIndex,
    # Memory usage, amount of entries, ttl columns, Dtypes, Non-Null Count: Empty (Null) values are bad for data
    # analysis. Removing rows with null values is a first step to CLEANING THE DATA: .dropna(inplace=True)
    print("Printing detailed information about DF using .info():", data_frame_daily.info())

    # df.DESCRIBE() method is used to view some basic statistical details like percentile, mean (average),
    # std (standarde Abweichung) etc. of a DF or a series of NUMERIC values.
    # When applied to a series of STRINGS returns a count of values, unique values, top and frequency of occurrence
    """
    Parameters of .describe() (for NUMERIC values only):
        percentile: list like data type of numbers between 0-1 to return the respective percentile
        include: List of data types to be included while describing dataframe. Default is None
        exclude: List of data types to be Excluded while describing dataframe. Default is None
    Returns: 
        Statistical summary of a data frame.
    """
    print("Printing description about DF contents using .describe():", data_frame_daily.describe())

    # Loading a file into a DataFrame

    # Creating variables for a relative path to the data files
    root_path = os.path.join(pathlib.Path(__file__).parent.joinpath('data'))
    csv_file_name = 'data.csv'
    json_file_name = 'data.json'
    joined_csv_path = os.path.join(root_path, csv_file_name)
    joined_json_path = os.path.join(root_path, json_file_name)

    # Reading a CSV-file (contains plain text and is a simple way to store big data sets):
    data_frame_csv = pd.read_csv(joined_csv_path)
    # "data.csv"-string is a file name and a path to the file

    # Reading a JSON-file (contains plain text in a format of an object and is a simple way to store big data sets):
    data_frame_json = pd.read_json(joined_json_path)
    # ! Python Dictionaries with a JSON-structure can be loaded into a DataFrame using a simple pd.DataFrame(dict_var)

    print("DF extracted from a CSV file:", data_frame_csv.to_string())  # to_string() method is used to print the
    # entire DataFrame in console. By default printing a DataFrame displays only a reduced sample with the FIRST 5
    # rows AND the LAST 5 rows
    # print("DF extracted from a JSON file:", data_frame_json.to_string())  # Deactivated: long file!


def dataframe_timestamps():
    """
        contains tutorial to Pandas Timestamps and their attributes and methods
        :return: nothing
        """
    # Good examples with TimeStamps (Daten addieren / substrahieren, vergleichen, Tagesnamen bekommen, Formattieren etc)
    # @ https://towardsdatascience.com/mastering-dates-and-timestamps-in-pandas-and-python-in-general-5b8c6edcc50c

    # More about pd.Timedelta() used for adding/substracting Timestamps:
    # @ https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html

    # Timestamp is the equivalent of python’s Datetime. It’s the type used for the entries that make up a
    # DatetimeIndex, and other timeseries-oriented data structures in pandas.

    # Method 1: Creating a Timestamp using a corresponding Class constructor:
    datetimelike_string = "1992-01-28"
    my_bd_timeStamp = pd.Timestamp(datetimelike_string)
    print("Printing a Timestamp formed from a datetime-like string", my_bd_timeStamp)

    unixepoch_insecs_float = 696594600
    print("Printing a Timestamp formed from a unix-epoch int in units of seconds \n and for a particular timezone ("
          "GMT-3)", pd.Timestamp(unixepoch_insecs_float, unit="s", tz='Etc/GMT-3'))

    # Method 2: Creating a Timestamp by addressing (mimicking) the API for datetime.datetime method using positional
    # OR keyword arguments (cannot be combined):
    print("Printing a Timestamp from following parameters: year, month, day, hour, minute: \n",
          pd.Timestamp(1992, 1, 28, 14, 30), "\n", pd.Timestamp(year=2021, month=9, day=1))

    # Attributes for TimeStamps:
    print("Index of the day of the week for my birthday TimeStamp: \n", my_bd_timeStamp.dayofweek)  # Monday = 0,
    # Sunday = 6
    print("Day of the year for my birthday TimeStamp: \n", my_bd_timeStamp.day_of_year)  # or also .dayofyear
    print("Amount of days in the month of my birthday TimeStamp: \n", my_bd_timeStamp.daysinmonth)  # or also .freqstr
    print("Week number of my birthday TimeStamp: \n", my_bd_timeStamp.weekofyear)  # or also .week

    # Methods for TimeStamps:
    print("Combining both a date and a time objects using TimeStamp .combine() method: \n",
          pd.Timestamp.combine(date(2021, 9, 1), time(7, 30, 00)))
    print("Month I was born in from my birthday TimeStamp using .month-name() method: \n",
          my_bd_timeStamp.month_name())
    print("Day I was born from my birthday TimeStamp using .weekday() method: \n",
          my_bd_timeStamp.weekday())  # == attributes .dayofweek / .day-of-week


def dataframe_join_combine_merge_append_concat():
    """
        contains tutorial to Pandas DataFrames extended functionality for combining DataFrames together
        :return: nothing
        """
    # See DataFrame APIs Reference 1: https://www.w3schools.com/python/pandas/pandas_ref_dataframe.asp
    # See DataFrame APIs Reference 2: https://pandas.pydata.org/docs/reference/api/pandas.concat.html

    bku_subjects = {
        "fach": ["EVP", "SWD", "D"],
        "ttl_stunden": [30, 20, 10]
    }

    kms_subjects = {
        "fach": ["ITD", "P", "R"],
        "ttl_stunden": [10, 10, 10]
    }

    is_mint_subject_bku = {
        "is_mint": [True, True, False]
    }

    is_mint_subject_kms = {
        "is_mint": [True, False, False]
    }

    df_bku = pd.DataFrame(bku_subjects)
    df_kms = pd.DataFrame(kms_subjects)
    df_ismint_bku = pd.DataFrame(is_mint_subject_bku)
    df_ismint_kms = pd.DataFrame(is_mint_subject_kms)
    print("DataFrame of subjects and hours from BKU: \n", df_bku)
    print("DataFrame of subjects and hours from KMS: \n", df_kms)

    # df1.JOIN(obj2, on, how, lsuffix, rsuffix, sort) - Add the content to a DataFrame from another DataFrame or Series
    # Does not change the original DataFrame!!! Returns a new DataFrame!
    # Optional keyword args:
    # on - Specifies in what level to do the joining (string / list Value)
    # how - default: left / right / outer / inner - specify which index to use
    # lsuffix / rsuffix (string value, Default: '' ) - specifies a string to add for overlapping columns
    # sort (boolean value, Default: False) - specify whether to sort the DataFrame by the join key or not

    joined_df_bku = df_bku.join(df_ismint_bku)
    print("Result of .join of is-mint values to subjects of bku: \n", joined_df_bku)

    joined_df_kms = df_kms.join(df_ismint_kms)
    print("Result of .join of is-mint values to subjects of bku: \n", joined_df_kms)

    # df1.APPEND(obj2, ignore_index, verify_integrity, sort) - appends a DataFrame-like object (DF, Series, Dict, List)
    # at the end of the current DataFrame. Returns a new DataFrame object, no changes are done to the original DataFrame
    # Optional keyword args:
    # ignore_index (bool value, Default: False) - if set to True, original indexes are ignored and will be replaced by
    # new listing of 0, 1, 2 etc
    # verify_itegrity (bool value, Default: False) - if set to True, returns an error in case of two or more rows with
    # the same index
    # sort (boolean value, Default: False) - specify whether to sort the DataFrame by the join key or not

    df_colleges_appended = df_bku.append(df_kms, ignore_index=False, verify_integrity=False)
    df_ismint_appended = df_ismint_bku.append(df_ismint_kms, ignore_index=True, verify_integrity=True)
    print("Results of .append of colleges-DFs and of IsMint-DFs: \n", df_colleges_appended, "\n", df_ismint_appended)

    # df1.COMBINE(df2, FUNC, fill_value, overwrite) - combine two DataFrames columnwise and return (keep) ONE column
    # in a new DF from columns with the same index of the original DFs according to a specified FUNCTION
    # Optional keyword args:
    # fill_value (Number / NONE value, Default: None) - a value to fill empty cells with.
    # overwrite (bool value, Default: True) - specify whether columns that do not exists in the second DataFrame will
    # be overwritten (with NaN) or not

    df1 = pd.DataFrame([[10, 2], [7, 1]])  # Column 0: 10, 7. Column 1: 2, 1
    df2 = pd.DataFrame([[5, 9], [3, 0]])  # Column 0: 5, 3. Column 1: 9, 0

    def return_biggest_value(a, b):
        """
        Compares sums of contents of a column with the same index from 2 recieved DFs
        :param a: Column with index i from a DF1
        :param b: Column with index i from a DF2
        :return: Column with index i from a DF1 or DF2 with the BIGGEST sum of contents
        """
        if a.sum() > b.sum():
            return a
        else:
            return b

    print("DF1: ", df1)
    print("DF2: ", df2)
    print("Printing a result of .combine of 2 DF with Lists of numbers using a function to choose a column with the "
          "biggest sum of its contents: \n", df1.combine(df2, return_biggest_value))

    # df1.MERGE(obj2, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False,
    # sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None) - merge DataFrame or named Series
    # objects with a database-style join syntax.
    # The join is done on columns or indexes. If joining columns on columns, the DataFrame indexes will be ignored.
    # If joining indexes on indexes or indexes on a column / columns, the index will be passed on.
    # Optional keyword args:
    # on - Column or index level names to join DFs on. These must be found in both DFs.
    # left_on / right_on: Column or index level names to join on in the left DataFrame / in the right DataFrame.
    # left_index / right_index: Use the index from the left / right DataFrame as the join key(s). If it is a MultiIndex,
    # the number / keys in the other DataFrame (either the index or a number of columns) must match the number of levels
    # suffixes - A length-2 sequence where each element is optionally a string indicating the suffix to add to
    # overlapping column names in left and right respectively. At least one of the values must not be None.

    df_sam = pd.DataFrame({'sam_key': ['EN', 'DE', 'RU', 'SV'],
                        'value': [4, 5, 2, 0]})
    df_ili = pd.DataFrame({'ili_key': ['EN', 'DE', 'RU', 'SV'],
                        'value': [4, 4, 5, 1]})
    df_our_languages_merged = df_sam.merge(df_ili, left_on='sam_key', right_on='ili_key', suffixes=('_niveau_sam', '_niveau_ili'))
    print("DF mit Sprachen von Sam: \n", df_sam)
    print("DF mit Sprachen von Ili: \n", df_ili)
    print("Die merged languages DFs using .merge with DFs languages column key to join: \n", df_our_languages_merged)

    # pd.CONCAT([obj1, obj2], axis=0, join='outer', ignore_index=False, keys=None, levels=None, names=None,
    # verify_integrity=False, sort=False, copy=True) - concatenate pandas objects along a particular axis with
    # optional set logic along the other axes. Can also add a layer of hierarchical indexing on the concatenation
    # axis, which may be useful if the labels are the same (or overlapping) on the passed axis number.
    # axis (default 0) - the axis to concatenate along:
    # When concatenating all Series along their index (axis=0), a Series is returned.
    # When objs contain at least one DataFrame, a DataFrame is returned.
    # When concatenating along the columns (axis=1), a DataFrame is returned.

    s1 = pd.Series(['S1Elem1', 'S1Elem2'])
    s2 = pd.Series(['S2Elem1', 'S2Elem2'])
    print("S1: \n", s1, "S2: \n", s2)

    print("Simple concatenation of 2 series: \n", pd.concat([s1, s2]))  # here == .append with ignore_index=False
    print("Simple concatenation of 2 series with index reset: \n", pd.concat([s1, s2], ignore_index=True))  # here == .append with ignore_index=True

    labeled_hierarch_index_concat = pd.concat([s1, s2], keys=['Series 1', 'Series 2'], names=['Series name', 'Row ID'])
    print("2 series concatenated along index (axis=0) with hiererchical index names for their unresetted indexes and "
          "also with labeled index keys for the hierarchical index and usual indexes: \n", labeled_hierarch_index_concat)

    labeled_hierarch_index_concat_y = pd.concat([s1, s2], keys=['Series 1', 'Series 2'], axis=1)
    print("2 series concatenated along the columns (axis=1): \n", labeled_hierarch_index_concat_y)


series_and_labels()
input("Information above refers to Pandas Series and their labels. Press Enter to continue...")
dataframes_basics()
input("Information above refers to basics of Pandas DataFrames. Press Enter to continue...")
dataframe_timestamps()
input("Information above refers to Pandas Timestamps. Press Enter to continue...")
dataframe_join_combine_merge_append_concat()
input("Information above refers to DataFrames combining methods. Press Enter to continue...")
