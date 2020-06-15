import pytest
from listentothis.environment import Env


def test_noop():
    assert True


def test_nosetup():
    env = Env()
    with pytest.raises(Exception) as xception:
        env.get("notsetupyet")
    assert "Env not setup" in str(xception.value)


def test_env():
    env = Env()
    env.setup_json("tests/jsonfile.json")

    assert env.get("testkey") == "testvalue"
