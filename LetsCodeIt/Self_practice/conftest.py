import pytest


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session")
def get_browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(get_browser):
    print("\nSetup : We got from command line argument = {}".format(get_browser))
