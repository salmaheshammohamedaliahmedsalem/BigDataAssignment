import sys
import pandas as pd

def load_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    return data

if __name__ == "__main__":
    file_path = sys.argv[1]
    data = load_data(file_path)
    data.to_csv('/home/doc-bd-a1/loaded_data.csv', index=False)
    print("Data loaded and saved to loaded_data.csv")
