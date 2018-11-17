import pytest


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def get_browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def input_method(get_browser):
    print("input_method_value is {}".format(get_browser))
