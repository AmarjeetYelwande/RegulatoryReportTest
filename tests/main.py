import pandas as pd
import os as os
import numpy as np
import string

pd.DataFrame({'float': [1.00],
                    'integer': [1],
                    'datetime': [pd.Timestamp('20180310')],
                    'string': ['foo'],
                    'bool': [True]})

# Load the CSV files
df1 = pd.read_csv(os.path.join('files', 'first_file.csv'))
df2 = pd.read_csv(os.path.join('files', 'second_file.csv'))

def compare_schema(first_file, second_file):
    # Compare column names
    if set(df1.columns) != set(df2.columns):
        print("Column names differ.")
        print("Columns in file1 but not in file2:", set(df1.columns) - set(df2.columns))
        print("Columns in file2 but not in file1:", set(df2.columns) - set(df1.columns))
        return False

    # Compare column order
    if list(df1.columns) != list(df2.columns):
        print("Column order differs.")
        return False

    # Compare data types
    if not df1.dtypes.equals(df2.dtypes):
        print("Data types differ.")
        print("Data types in file1:\n", df1.dtypes)
        print("Data types in file2:\n", df2.dtypes)
        return False

    # Compare number of columns
    if len(df1.columns) != len(df2.columns):
        print("Number of columns differs.")
        return False

    print("Schemas are identical.")
    return True

# Usage

def compare_columns( first_file, second_file):
    if set(df1.columns) == set(df2.columns):
        print("Column names are the same.")
    else:
        print("Column names differ.")
        print("Columns in file1 but not in file2:", set(df1.columns) - set(df2.columns))
        print("Columns in file2 but not in file1:", set(df2.columns) - set(df1.columns))

def compare_csv(first_file, second_file):
    df1 = pd.read_csv(first_file)
    first_column = df1['Column Code'].to_numpy()
    colnames = np.random.choice(list(string.ascii_lowercase),  size=len(df1.columns) + 1)
    df2 = pd.read_csv(second_file, names= colnames, header=None)
    second_column = df2.iloc[0].to_numpy()
    if np.array_equal(first_column,second_column):
        print("Both columns are equal")
    else:
        print("Both arrays are not equal")



#compare_schema(df1, df2)
#compare_columns(df1, df2)
compare_csv(os.path.join('files','datafieldstemplates', 'y_01.01.csv'),
            os.path.join('files','generatedreports', 'y_01.01.csv'))