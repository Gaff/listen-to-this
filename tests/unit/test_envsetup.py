import pytest
from listentothis import env


def test_noop():
    assert True

def test_env():
    env.setup_json("tests/jsonfile.json")

    assert(env.get("testkey") == "testvalue")
