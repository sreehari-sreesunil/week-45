from src.data import load_data, clean_data
from src.model import train_model
from src.metrics import evaluate 

def run(path):
    df = load_data(path)
    df = clean_data(df)

    x = df[['Hours']]
    y = df['Scores']

    model = train_model(x,y)
    preds = model.pred(x)

    mse = evaluate(y, preds)
    print("MSE :", mse)
