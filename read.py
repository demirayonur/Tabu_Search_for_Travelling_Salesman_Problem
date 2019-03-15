import pandas as pd


def read_tsp_data():
    """
    This function reads the STSP data by using
    pandas and returns the data Numpy array
    format.

    :return: 2D Numpy Array
    """
    return pd.read_csv('INDR568_HW2_STSP_instance.csv').values[:, 1:]
