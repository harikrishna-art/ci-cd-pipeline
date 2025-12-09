from src.main import add

def test_add_func():
    assert add(10,20) == 30
    assert add(21,19) == 40
    assert add(1,-1) == 0