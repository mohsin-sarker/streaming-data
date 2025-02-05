import pytest



@pytest.mark.it('Unit test: This a simple test for testing environment')
def test_simple():
    string = "This is simple test"
    assert type(string) == str