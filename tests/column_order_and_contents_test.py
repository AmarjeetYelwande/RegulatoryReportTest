from xmlrpc.client import boolean

import pandas as pd
import os as os
import numpy as np
import string
import pytest

COLUMN_NAME_TO_COMPARE = "Column Code"
COLUMN_NAME_WITH_TYPE = "Type"

df = pd.DataFrame({'float': [1.00],
                   'int': [1],
                   'datetime': [pd.Timestamp('20180310')],
                   'string': ['foo']})

# Template file product owned composes as part of specification.
# When you upload them make sure to add their name in data file.
def first_file(file_name):
    data_folder = os.path.join("files", "datafieldstemplates")
    return os.path.join(data_folder, file_name)

# Generated report files.
# When you upload them make sure to add their name in data file
def second_file(file_name):
    data_folder = os.path.join("files", "generatedreports")
    return os.path.join(data_folder, file_name)

# Ideally product owner should hand report and template files to a test engineer
# He should upload the files in respective folders and update below file.
# This is useful when you have hundreds of report and template files to run as part of regression testing
def data_file(file_name):
    data_folder = os.path.join("files")
    return os.path.join(data_folder, file_name)

# Parameterised test accepts arrays. So converting dataframe to array
testData = pd.read_csv(data_file("test_run_data.csv")).to_numpy()

# Use data read from datafile and use for parameterised tests
@pytest.mark.parametrize("template_file,file_to_be_compared_with_template,are_columns_equal",
                        testData)
def test_compare_columns(template_file,file_to_be_compared_with_template,are_columns_equal):
    first_data_frame = pd.read_csv(first_file(template_file))
    # Need to insert another column as report file does not have headers.
    # Pandas is not able to read file correctly when there is no header column.
    # Tried various techniques but failed. So using this workaround which works
    column_names = np.random.choice(list(string.ascii_lowercase), size=len(first_data_frame.columns) + 1, replace=False)
    second_data_frame = pd.read_csv(second_file(file_to_be_compared_with_template), names=column_names, header=None)
    first_column_template = first_data_frame[COLUMN_NAME_TO_COMPARE].to_numpy()
    second_column_template = first_data_frame[COLUMN_NAME_WITH_TYPE].to_numpy()
    print(first_column_template)
    print(second_column_template)
    # Even though it is index 0 it actually reads values in second column.
    # First column is headers inserted manually by test for workaround implemented
    second_column_report = second_data_frame.iloc[0].to_numpy()
    assert np.array_equal(first_column_template, second_column_report) == are_columns_equal