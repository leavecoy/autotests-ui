import pytest
from tools.allure.environment import create_allure_environment

@pytest.fixture(scope="session", autouse=True)
def save_environment_file():
    yield
    create_allure_environment()
