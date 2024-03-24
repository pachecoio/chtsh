from chtsh.main import query


def test_query():
    res = query("What is the capital of France?")
    assert res == "The capital of France is Paris."

