import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize('number', [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0

@pytest.mark.parametrize('number, expected', [(1, 1), (2, 4), (3, 9)] )
def test_several_numbers(number, expected: int):
    number ** 2 == expected


@pytest.mark.parametrize('os', ['windows', 'macos', 'linux', 'debian'])
@pytest.mark.parametrize('browser', ['chromium', 'webkit', 'firefox'])
def test_multiplication_of_numbers(os: str, browser: str):
    assert len(os + browser) > 0

@pytest.fixture(params=['chromium', 'webkit', 'firefox'])
def browser(request):
    return request.param

def test_open_browser(browser: str):
    print(f"Running test on browser: {browser}")



@pytest.mark.parametrize('user', ['Alice', 'Zara'])
class TestOperations:
    @pytest.mark.parametrize('account', ['Credit card', 'Debit cart'])
    def test_user_with_operations(self, user: str, account: str):
        pass

    def test_user_without_operations(self, user: str):
        pass

users = {
'89281111111' : 'User 1',
'89282222222' : 'User 2',
'89283333333' : 'User 3'
}

@pytest.mark.parametrize(
    'phone_number',
    users.keys(),
    ids=lambda phone_number: f'{phone_number} : {users[phone_number]}'
)
def test_identifies(phone_number: str):
    pass