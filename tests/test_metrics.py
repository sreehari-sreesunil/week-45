from src.metrics import evaluate

def test_evaluate():
    x = [1,2,3]
    y = [1,2,3]
    assert evaluate(x, y) == 0