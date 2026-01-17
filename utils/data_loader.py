import pandas as pd
import os

def load_data():
    """
    Load the sample prediction market dataset
    """
    file_path = os.path.join("data", "sample_data.csv")

    if not os.path.exists(file_path):
        raise FileNotFoundError("Dataset not found: data/sample_data.csv")

    df = pd.read_csv(file_path)
    return df
