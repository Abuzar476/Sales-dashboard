import os
import pandas as pd
def load_csv(filepath):
    if not os.path.exists(filepath):
        print("Error: File not found")
        return None
    name, extension = os.path.splitext(filepath)
    if extension != '.csv':
        print("Error: file is not a csv")
        return None
    df = pd.read_csv(filepath, low_memory=False)
    return df


