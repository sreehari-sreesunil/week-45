import pandas as pd
from src.data import clean_data 

def test_clean_data():
    df = pd.DataFrame({
        "Hours" : [1, 2, None],
        "Scores": [10, 20, 30]
    })
    cleaned = clean_data(df)
    assert len(cleaned) == 2

    