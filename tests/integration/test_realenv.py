import pytest
from listentothis import env


def test_noop():
    assert True


def test_env():
    env.setup_gcloud_json("allsecretsjson")
    assert env.get("id") == "allsecretsjson"
