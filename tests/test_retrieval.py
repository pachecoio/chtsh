from chtsh.retrieval import coding_query, query_with_serpapi

def test_query_with_serpapi():
    response = query_with_serpapi("What is the capital of France?")
    assert "Paris" in response["output"], "Capital of France is Paris"


def test_coding_query():
    res = coding_query("How to reverse a list in Python?")
    assert "reversed" in res["output"], "Reversing a list in Python"
