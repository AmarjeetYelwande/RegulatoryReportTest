import pandas as pd
import os as os
import numpy as np
import string
import pytest

testdata = [
    ("y_01.01.csv", "y_01.01.t.csv", True),
    ("y_01.01.csv", "y_01.01.f.csv", False),
]

def first_file(file_name):
    data_folder = os.path.join("files", "datafieldstemplates")
    return os.path.join(data_folder, file_name)

def second_file(file_name):
    data_folder = os.path.join("files", "generatedreports")
    return os.path.join(data_folder, file_name)

@pytest.mark.parametrize("first,second,are_equal", testdata)
def test_compare_columns(first,second,are_equal):
    df1 = pd.read_csv(first_file(first))
    column_names = np.random.choice(list(string.ascii_lowercase), size=len(df1.columns) + 1)
    df2 = pd.read_csv(second_file(second), names=column_names, header=None)
    first_column = df1['Column Code'].to_numpy()
    second_column = df2.iloc[0].to_numpy()
    assert np.array_equal(first_column, second_column) == are_equal