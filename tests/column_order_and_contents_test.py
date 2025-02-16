import pandas as pd
import os as os
import numpy as np
import string
import pytest
import sys

# Import all types from respective classes
sys.path.insert(0, '')
from tests.types.CustomTypes import Alphanumeric, Date, Country, ClosedSetOfOptions, Lei, BinaryOptions

COLUMN_NAME_TO_COMPARE = "Column Code"
COLUMN_NAME_OF_EXPECTED_TYPES = "Type"

# Template file product owner composes as part of specification.
# When you upload them make sure to add their name in test_run_data.csv file.
def get_path_of_template_file(file_name):
    data_folder = os.path.join("files", "datafieldstemplates")
    return os.path.join(data_folder, file_name)

# Generated report files.
# When you upload them make sure to add their name in data file
def get_path_of_reports_file(file_name):
    data_folder = os.path.join("files", "generatedreports")
    return os.path.join(data_folder, file_name)

# Ideally product owner should hand report and template files to a test engineer
# He should upload the files in respective folders and update test_run_data.csv file.
# This is useful when you have hundreds of report and template files to run as part of regression testing
def get_test_data_files_list(file_name):
    data_folder = os.path.join("files")
    return os.path.join(data_folder, file_name)

# Parameterised test accepts arrays. So converting dataframe to array
test_data_files_list = pd.read_csv(get_test_data_files_list("test_run_data.csv")).to_numpy()

# Use data read from datafile and use for parameterised tests
@pytest.mark.parametrize("template_file,report_file_to_be_compared_with_template,expected_outcome_column_test,expected_outcome_types_test",
                         test_data_files_list)
def test_compare_columns(template_file,report_file_to_be_compared_with_template,expected_outcome_column_test,expected_outcome_types_test):
    data_frame_of_template = pd.read_csv(get_path_of_template_file(template_file))
    # Need to insert another column as report file does not have headers.
    # Pandas is not able to read file correctly when there is no header column.
    # Tried various techniques but failed. So using this workaround which works
    column_names_from_template = np.random.choice(list(string.ascii_lowercase), size=len(data_frame_of_template.columns) + 1, replace=False)
    data_frame_of_reports = pd.read_csv(get_path_of_reports_file(report_file_to_be_compared_with_template), names=column_names_from_template, header=None)

    first_column_of_template = data_frame_of_template[COLUMN_NAME_TO_COMPARE].to_numpy()
    second_column_of_template = data_frame_of_template[COLUMN_NAME_OF_EXPECTED_TYPES].to_numpy()

    # Even though it is index 0 it actually reads values in second column.
    # First column is headers inserted manually by test for workaround implemented
    # This column contains column names reported e.g. c0010, c0020 etc
    second_column_report = data_frame_of_reports.iloc[0].to_numpy()
    assert np.array_equal(first_column_of_template, second_column_report) == expected_outcome_column_test ,\
        f"Expected columns : {first_column_of_template} , but actually received : {second_column_report}"
    # This column contains actual values of respective columns e.g. 1-1-2025 ( date ) , United Kingdom ( country name )
    third_column_report = data_frame_of_reports.iloc[1].to_numpy()
    index_of_received_value = 0

    for expected_datatype in second_column_of_template:
        received_data = third_column_report[index_of_received_value]
        # Expected datatype is nothing but name of the class to be called for verification
        # Skipping test when there is empty / null value for received data in report.
        if received_data == object:
            is_datatype_correct = globals()[str(expected_datatype)](received_data)
            assert str(is_datatype_correct) == str(expected_outcome_types_test),\
                f"Expected datatype : {expected_datatype} does not match for received data : {received_data}"
        index_of_received_value += 1