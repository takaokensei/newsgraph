import pandas as pd
from src.config import DATA_PATH

def load_data(filepath=DATA_PATH):
    """
    Load the CSV data, handling potential encoding issues and expanding functionality.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"✅ Data loaded successfully from {filepath}")
        print(f"📊 Shape: {df.shape}")
        print(f"📝 Columns: {df.columns.tolist()}")
        return df
    except FileNotFoundError:
        print(f"❌ Error: File not found at {filepath}")
        return None
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return None

if __name__ == "__main__":
    df = load_data()
    if df is not None:
        print(df.head())
