
import pytest

"""
import argparse
parser = argparse.ArgumentParser(usage="use as per swapan")
parser.add_argument("name", help="provide a name")
parser.add_argument("--title", help="provide title", action="store_false")
# parser.add_argument("--title", help="provide title", action="store_true")
args = parser.parse_args()

print(args.name)
if args.title:
    print(args.title)
else:
    print("No title")

"""
"""
@pytest.fixture()
def input_method():
    return "input_method_value"


def test_receiver_method(input_method):
    print("we got {} as input method".format(input_method))

"""

def test_receiver_method(setup):
    print("This is test method")


def test_argument(get_browser):
    print("\nBrowser name provided in command line is {}".format(get_browser))


