import pytest


@pytest.fixture()
def setup2(request):
    print("Starting Test by conftest::setup")

    def fin():
        print("Ending the test from contest::setup")

    request.addfinalizer(fin)


@pytest.fixture()
def setup1(request):

    module_name = getattr(request.module, "module_name", "default_module_name")
    print("Starting Test by for module = {}".format(module_name))

    def fin1():
        print("teardown smtp_connection")

    request.addfinalizer(fin1)

