import pytest

@pytest.mark.xfail(reason="Найден баг")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason="Был баг")
def test_without_bug():
    pass