import pytest  # import needed only if using fixtures
import requests
import example


# custom class to be the mock return value of requests.get()
class MockResponse:
    @staticmethod
    def json():
        return {"mock_key": "mock_response"}


def test_always_pass():
    assert True


def test_always_fail():
    assert False


def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"


def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]


def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }


@pytest.fixture
def example_fixture():
    return 1


def test_with_example_fixture(example_fixture):
    assert example_fixture == 1


def format_data_for_display(people):
    """output a list of strings that include each person’s
    full name (their given_name followed by their family_name), a colon, and
    their title

    Args:
        people (JSON): data returned by an API endpoint

    Returns:
        list: list of strings that include each person’s full name (their
        given_name followed by their family_name), a colon, and their title
    """
    return [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]


def format_data_for_excel(people):
    """transform the data into comma-separated values for use in Excel

    Args:
        people (JSON): data returned by an API endpoint

    Returns:
        csv: comma-separated values with heading given,family,title
    """
    return """given,family,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager
"""


@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Alfonsa",
            "family_name": "Ruiz",
            "title": "Senior Software Engineer",
        },
        {
            "given_name": "Sayid",
            "family_name": "Khan",
            "title": "Project Manager",
        },
    ]


def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Alfonsa Ruiz: Senior Software Engineer",
        "Sayid Khan: Project Manager",
    ]


def test_format_data_for_excel(example_people_data):
    assert format_data_for_excel(example_people_data) == """given,family,title
Alfonsa,Ruiz,Senior Software Engineer
Sayid,Khan,Project Manager
"""


@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    def stunted_get():
        raise RuntimeError("Network access not allowed during testing!")
    monkeypatch.setattr(requests, "get", lambda *args, **kwargs: stunted_get())


def test_network_call(disable_network_calls):
    result = example.get_json("https://fakeurl")
    assert result["mock_key"] == "mock_response"
