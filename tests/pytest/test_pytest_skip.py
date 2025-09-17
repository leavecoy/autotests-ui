import pytest

@pytest.mark.skip(reason="фича в разработке")
def test_feature_in_development():
    pass

@pytest.mark.skip(reason="фича в разработке")
class TestSuiteSkip:
    def test_feature_in_development1(self):
        pass

    def test_feature_in_development2(self):
        pass